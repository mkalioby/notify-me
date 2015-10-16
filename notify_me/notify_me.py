#!/usr/bin/env python
print "Running"
import Config
import sys
import Common
import smail
import pushNotification

__author__ = 'mohamed'

to_emails = []
subject = Config.default_subject
push = False
success = Config.OK_MESSAGE
failure = Config.ERR_MESSAGE
send_output_by_email=True
topic = Config.default_topic
cmd=""

if sys.argv[1]=="--help" or sys.argv[1]=="-h":
    print """
 This program runs a program and notify you be SMTP email and/or push notification.

 notify-me OPTIONS Command

 Options
    --notify-to=mail1,mail2    send an email when done to the following mails
    --notify-push              send a push notification
    --notify-OK=               send this message after success
    --notify-ERR=              send this message after failure
    --notify-topic=            the topic to send on if different than default queue
    --notify-name=             name of the job, to put it subject or push notifications
    --no-notify-send-out       don't send the stderr and stdout in the email.

 Example

 notify-me  --notify-to=someone@example.com,someone2@example.com --notify-push --notify-OK="System Updated" --notify-ERR="System Update Failed" --notify-name="System Update" --notify-topic="Admin" sudo apt-get upgrade
"""
    exit(0)
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
        cmd += arg + " "
print "Running:",cmd
res = Common.run(cmd,True)
if res[0] == 0:
    if push:
        pushNotification.push(subject+ " " + success,topic,Config.notification_key)
    if to_emails != []:
        subject+=" " + success
        if send_output_by_email:
            msg="<pre>"+res[1]+"</pre>"
        else:
            msg=success

        for mail in to_emails:
            smail.send(mail,subject,msg,Config.default_from)
else:
    if push:
        pushNotification.push(subject + " " +failure,topic,Config.notification_key)
    if to_emails!=[]:
        subject+=" " + failure
        if send_output_by_email:
            msg="<pre>"+res[1]+"</pre>"
        else:
            msg=failure
        for mail in to_emails:
            smail.send(mail,subject,msg,Config.default_from)