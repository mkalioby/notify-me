import db,datetime,simplejson
def push(topic,message):
	now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	try:
		return simplejson.dumps({"message":db.execute("insert into notification (Message,Topic,Datetime) Values('%s','%s','%s')"%(message,topic,now))})
	except Exception as exp:
		return simplejson({"err": exp})
	
def get(topic,id=0, datetime=None):
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
	return simplejson.dumps(rows)
	
	
