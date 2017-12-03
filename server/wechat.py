# -*- coding:utf-8 -*-
import werobot 
import database
import time 
robot = werobot.WeRoBot(token="cfuture")


@robot.text
def handle(message):
	format = '%Y-%m-%d %H:%M:%S'
	content = message.content
	if type(content).__name__ == 'unicode':
		content = content.encode('utf-8')
	if content.count('温度'):
		
		#将UNIX时间戳转为正常时间
		value = time.localtime(message.time)
		dt = time.strftime(format, value)
		#将命令插入数据库
		db = database.database('database.db')
		db.insert('weixin',['TIME','USERID','CONTENT'],[dt,message.source,message.content])
		command = 'SELECT TEMP,HUM,TIME FROM data  ORDER BY ID DESC LIMIT 0,1;'
		result = db.getData(command)
		db.database.close()
		word = u'现在是北京时间：'+str(dt)+u'。现在室内的温度是：'+str(result[0][0])+u'摄氏度。现在室内的湿度是：'+str(result[0][1])+u'%'
		return word
	elif content.count('监控'):
		return[
		[
			"监控",
			"这是一条测试",
			"http://ooiaw5slt.bkt.clouddn.com/%E9%95%9C%E5%A4%B4.png",
			"https://github.com/TioWang"
		]]
	elif content.count('浇水'):
		#将UNIX时间戳转为正常时间
		value = time.localtime(message.time)
		dt = time.strftime(format, value)
		#将命令插入数据库
		db = database.database('database.db')
		db.insert('weixin',['TIME','USERID','CONTENT'],[dt,message.source,message.content])
		return '开始浇水~~~'
	elif content.count('湿度'):
		#将UNIX时间戳转为正常时间
		value = time.localtime(message.time)
		dt = time.strftime(format, value)
		#将命令插入数据库
		db = database.database('database.db')
		db.insert('weixin',['TIME','USERID','CONTENT'],[dt,message.source,message.content])
		command = 'SELECT DATA FROM water  ORDER BY ID DESC LIMIT 0,1;'
		result = db.getData(command)
		db.database.close()
		return '当前土壤湿度为:'+str(result[0][0])
	return message.content
	

@robot.voice
def voiceHandle(message):
	format = '%Y-%m-%d %H:%M:%S'
	content = message.recognition
	if type(content).__name__ == 'unicode':
		content = content.encode('utf-8')
	if content.count('温度'):
		#打开数据库
		db = database.database('database.db')
		#将UNIX时间戳转为正常时间
		value = time.localtime(message.time)
		dt = time.strftime(format, value)
		#将命令插入数据库
		db.insert('weixin',['TIME','USERID','CONTENT'],[dt,message.source,message.recognition])
		command = 'SELECT TEMP FROM data  ORDER BY ID DESC LIMIT 0,1;'
		result = db.getData(command)
		db.database.close()
		return str(result[0])
	elif content.count('监控'):
		return[
		[
			"监控",
			"这是一条测试",
			"http://ooiaw5slt.bkt.clouddn.com/%E9%95%9C%E5%A4%B4.png",
			"https://github.com/TioWang"
		]]
	elif content.count('浇水'):
		#将UNIX时间戳转为正常时间
		value = time.localtime(message.time)
		dt = time.strftime(format, value)
		#将命令插入数据库
		db = database.database('database.db')
		db.insert('weixin',['TIME','USERID','CONTENT'],[dt,message.source,message.recognition])
		return '开始浇水~~~'
	return message.recognition
robot.run(server = 'gunicorn',port = 8000)