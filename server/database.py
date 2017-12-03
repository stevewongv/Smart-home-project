import sqlite3

class database(object):
	"""docstring for database"""

	def __init__(self,database):
		self.connect = sqlite3.connect(database)
		self.database = self.connect.cursor()
	
	def show(self):
		self.database.execute("SELECT CONTENT FROM weixin;")
		result = self.database.fetchall()
		for r in result:
			print r[0]
	
	def insert(self,table,attributes,values):
		a = ''
		v = ''
		for attribute in attributes:
			a += attribute + ','
		for value in values:
			if isinstance(value,str) or isinstance(value,unicode):
				v+='\'' + value + '\''+','
			else:
				print type(value)
				v+= str(value) + ','
		command = 'INSERT '+ 'INTO ' + \
				  table + ' (' + a[:-1] + ') ' + \
				  'VALUES (' + v[:-1] + ');'
		self.database.execute(command)
		self.connect.commit()

	def getData(self,command):
		self.database.execute(command)
		result = self.database.fetchall()
		return result

# if __name__ == '__main__':
# 	db = database('database.db')
# 	command='SELECT max(weixin.ID),weixin.TIME,weixin.USERID , weixin.CONTENT'+ \
# 			' FROM weixin'+ \
# 			' GROUP BY weixin.USERID'
# 	result = db.getData(command)
# 	for i in result:
# 		if u'oBFMQxJfEAXKYN0Fwz1rfIC1Q2h8' in i:
# 			print i[3]
# 	print result