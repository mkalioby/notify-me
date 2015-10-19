import db,datetime,simplejson
import datetime
import PyRSS2Gen

def genRss(notifications,req):
	rss = PyRSS2Gen.RSS2(
	title = "Notify-me feed",
	link = req.HOST,
	description = "The latest notification on notify-me server. ",

	lastBuildDate = datetime.datetime.now())
	items=[]
	for notification in notifications:
		items.append(PyRSS2Gen.RSSItem(
		title = notification["Message"],
		link = "",
		description = notification["Message"],
		guid = PyRSS2Gen.Guid(""),
		pubDate = notification["Datetime"]))
	rss.items=items

	return rss.to_xml()

def push(topic,message):
	now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	try:
		return simplejson.dumps({"message":db.execute("insert into notification (Message,Topic,Datetime) Values('%s','%s','%s')"%(message,topic,now))})
	except Exception as exp:
		return simplejson({"err": exp})
	
def get(topic,req,id=0, datetime=None,format="json"):
	query="select * from notification where topic='%s'"%topic
	if id != 0 and id != "0":
		query+= " and id > %s"%id
	if datetime != None:
		query += " and datetime >'%s'"%datetime
	query+=" order by id desc"
	#res=[]
	rows=db.select(query)
	for row in rows:
		#res.append(row)
		row["Datetime"]=row["Datetime"].strftime("%Y-%m-%d %H:%M:%S")
	if format.lower()=="json":
		return simplejson.dumps(rows)
	elif format.lower()=="rss":
		return genRss(rows,req)
	
	
