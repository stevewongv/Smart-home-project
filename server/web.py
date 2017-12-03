# -*- coding:utf-8 -*-
from flask import Flask , jsonify as flask_jsonify, request, g , make_response
import database
import time
app = Flask(__name__)
app.debug = True

@app.route('/spy/',methods=['GET','POST'])
def spy():
	if request.method =='POST':
		data = request.form['data']
		format = '%Y-%m-%d %H:%M:%S'
		value = time.localtime(time.time())
		dt = time.strftime(format, value)
		db = database.database('database.db')
		db.insert('COMMAND',['USERID','TIME','COMMAND'],['oBFMQxJfEAXKYN0Fwz1rfIC1Q2h8',dt,data])
		db.database.close()
	else:
		if request.args.get('userid'):
			userid = request.args['userid']
			db = database.database('database.db')
			command = 'SELECT max(COMMAND.ID),TIME,USERID , COMMAND'+ \
					  ' FROM COMMAND'+ \
					  ' GROUP BY COMMAND.USERID'
			result = db.getData(command)

			for user in result:
				if userid in user:
					content = user[3]
					TIME = user[1]
					return content+','+TIME
	return '1'


@app.route('/sensor/',methods=['GET','POST'])
def sensor():
	if request.method == 'POST':
		if len(request.form) == 1:
			GroundHumidity = eval(request.form['data'])
			format = '%Y-%m-%d %H:%M:%S'
			value = time.localtime(time.time())
			dt = time.strftime(format, value)
			db = database.database('database.db')
			db.insert('WATER',['USERID','TIME','DATA'],['oBFMQxJfEAXKYN0Fwz1rfIC1Q2h8',dt,GroundHumidity])
			db.database.close()
			return "1"
		elif len(request.form) == 2:
			Temp = eval(request.form['tem'])
			Humidity = eval(request.form['hum'])
			format = '%Y-%m-%d %H:%M:%S'
			value = time.localtime(time.time())
			dt = time.strftime(format, value)
			db = database.database('database.db')
			db.insert('data',['USERID','TEMP','HUM','TIME'],['oBFMQxJfEAXKYN0Fwz1rfIC1Q2h8',Temp,Humidity,dt])
			db.database.close()
			return '1'
		else:
			return '0'
	elif request.method == 'GET':
		if  request.args.get('userid'):
			userid = request.args['userid']
			db = database.database('database.db')
			command = 'SELECT max(weixin.ID),weixin.TIME,weixin.USERID , weixin.CONTENT'+ \
					  ' FROM weixin'+ \
					  ' GROUP BY weixin.USERID'
			result = db.getData(command)
			for user in result:
				if userid in user:
					content = user[3]
					TIME = user[1]
					if content.count(u'浇水'):
						return u"浇水" + ';' + TIME
					else:
						return content + ';' + TIME

		return '0'
	return 'error'
if __name__ == '__main__':
	app.run()
