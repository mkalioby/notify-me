#!/usr/bin/env python
__author__ = 'mohamed'
import Config
import sys
import Common
import smail
import pushNotification

to_emails = []
subject = Config.default_subject
push = False
success = Config.OK_MESSAGE
failure = Config.ERR_MESSAGE
send_output_by_email=True
topic = Config.default_topic
cmd=""
for arg in sys.argv[1:]:
    if "--notify-to=" in arg:
        to_emails = arg.split("=")[1].split(",")
    elif "--notify-push" in arg:
        push=True
    elif "--notify-OK=" in arg:
        success=arg.split("=")[1]
    elif "--notify-ERR=" in arg:
        failure=arg.split("=")[1]
    elif "--notify-topic=" in arg:
        topic=arg.split("=")[1]
    elif "--notify-name=" in arg:
        subject=arg.split("=")[1]
    elif "--no-notify-send-out" in arg:
        send_output_by_email=arg.split("=")[1]
    else:
        cmd+=arg + " "
print "Running:",cmd
res = Common.run(cmd,True)
if res[0] == 0:
    if push:
        pushNotification.push(subject+ " " + success,topic,Config.notification_key)
    if to_emails!=[]:
        subject+=" " + success
        if send_output_by_email:
            msg="<pre>"+"\n===========================================\n".join(res[1:])+"</pre>"
        else:
            msg=success

        for mail in to_emails:
            smail.send(mail,subject,msg,Config.default_from)
else:
    if push:
        pushNotification.push(subject + " " +failure,topic,Config.notification_key)
    if to_emails!=[]:
        subject+=" " failure
        if send_output_by_email:
            msg="<pre>"+"===========================================".join(res[1:])+"</pre>"
        else:
            msg=failure
        for mail in to_emails:
            smail.send(mail,subject,msg,Config.default_from)
