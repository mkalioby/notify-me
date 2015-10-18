#! /usr/bin/python
import urllib,simplejson,time,os,platform

if "Linux" in platform.platform():
	OS="Linux"
	if os.environ["DESKTOP_SESSION"]=="ubuntu" or os.environ["DESKTOP_SESSION"]=="gnome":
		from gi.repository import Notify
	else:
		import dbus
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
	try:
		for topic in topics:
			if topic not in ids:
				ids[topic]=0
			server=notification_server+"/get?topic=%s&id=%s"%(topic,ids[topic])
		#	print server
			url=urllib.urlopen(server)
			messages=simplejson.loads(url.read())
			
			if len(messages)>0:	
				if  messages[0]["id"]>ids[topic]:
					ids[topic]=messages[0]["id"]
			for message in messages:
				if os.environ["DESKTOP_SESSION"]=="ubuntu" or os.environ["DESKTOP_SESSION"]=="gnome":
					Notify.init ("Notify-me")
					diag=Notify.Notification.new ("Notify-me", message["Topic"]+": "+message["Message"],"dialog-information")
					diag.show ()
				#	time.sleep(5)
				else:
					knotify = dbus.SessionBus().get_object("org.kde.knotify", "/Notify")
					knotify.event("info", "kde", [], "Notify-me", message["Topic"]+": "+message["Message"], [], [], 0, 0, dbus_interface="org.kde.KNotify")
	except: 
		pass
	open(os.path.dirname(__file__)+"lastIDs","w").write(simplejson.dumps(ids))
	time.sleep(30)
