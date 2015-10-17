import MySQLdb
import simplejson
dbServer="localhost"
dbPort=3306
dbUsername="root"
dbPassword="password"
dbSchema="notify"

def connect():
	db = MySQLdb.connect(host=dbServer,  port=dbPort, user=dbUsername, passwd=dbPassword,db=dbSchema,charset="utf8")
	return db
	
def execute(statement):
	db=connect()
	cursor=db.cursor()
	try:
		cursor.execute(statement)
		db.commit()
		return cursor.lastrowid
		cursor.close ()
		db.close()
		return "OK"
	except Exception as exp:
		raise Exception (exp)

def select(query):
	db=connect()
	try:
		db.query(query)
		r=db.store_result()
		rows=r.fetch_row(maxrows=0,how=1)
		db.close()
		return rows
	except Exception  as exp:
		raise Exception (exp)


