#! /usr/bin/python
import urllib,simplejson,time,os,platform

import dbus,gobject

def sendKDENotification(title,message):
	knotify = dbus.SessionBus().get_object("org.kde.knotify", "/Notify")
	knotify.event("warning", "kde", [], title, message, [], [], 0, 0, dbus_interface="org.kde.KNotify")

ids={}
try:
	ids=simplejson.loads(open(os.path.dirname(__file__)+"lastIDs").read())
except:
	pass


if not "NOTIFY_TOPICS" in os.environ or os.environ["NOTIFY_TOPICS"]=="":
	print "No Topic to check, set NOTIFY_TOPICS env with comma seprated list for multiple topics"
	exit(-1)
if  "NOTIFY_SERVER" not in os.environ or os.environ["NOTIFY_SERVER"]=="" :
	print "The notification server isn't set, set NOTIFY_SERVER env."
	exit(-2)

notification_server=os.environ["NOTIFY_SERVER"]

while True:
	topics=os.environ["NOTIFY_TOPICS"].split(",")
	#print topics
#	try:
	for topic in topics:
		if topic not in ids:
			ids[topic]=0
		server=notification_server+"/get?topic=%s&id=%s"%(topic,ids[topic])
		print server
		url=urllib.urlopen(server)
		messages=simplejson.loads(url.read())
		
		if len(messages)>0:	
			if  messages[0]["id"]>ids[topic]:
				ids[topic]=messages[0]["id"]
		for message in messages:
			print message["Message"]
			sendKDENotification("Notify-me",topic+": "+message["Message"])
#	except Exception as exp: 
#		print exp
	open(os.path.dirname(__file__)+"lastIDs","w").write(simplejson.dumps(ids))
	time.sleep(30)
