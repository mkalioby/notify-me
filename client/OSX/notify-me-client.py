#! /usr/bin/python
import platform
if not platform.system() == 'Darwin':
	print "This is script is for Mac OS X 10.8 or higher"
	exit(-1)


import urllib,simplejson,time,os,TerminalNotifier

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
					TerminalNotifier.Notify(message["Topic"]+": "+message["Message"],title="Notify-me")
					time.sleep(5)
	except: 
		pass
	open(os.path.dirname(__file__)+"lastIDs","w").write(simplejson.dumps(ids))
	time.sleep(30)
