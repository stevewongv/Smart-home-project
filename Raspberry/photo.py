# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import subprocess
import people
import urllib2
import urllib

class photo():
 	def __init__(self):
 		self.GPIOID =37
 		GPIO.setmode(GPIO.BOARD)
 		time.sleep(1)
 		GPIO.setup(self.GPIOID,GPIO.IN)
 		GPIO.setup(3,GPIO.OUT)
 		self.history = 0
 		self.content = ''
 		self.c = False

 	def up(self):
 		url = 'http://YOUR_SERVER_IP/spy/'
 		postdata = 'data='+self.content
 		req = urllib2.Request(url,postdata)
 		req.add_header('Content-Type','application/x-www-form-urlencoded')
 		response = urllib2.urlopen(req)
 
 	def press(self):
 		signal = GPIO.input(self.GPIOID)
 		if signal:
 			print 1
 		if signal :
 			self.history = signal
 			P = subprocess.Popen('./script.sh', shell=True, stdout=subprocess.PIPE)
 			time.sleep(2)
 			p = people.people()
 			con = p.compare() #相似度
 			if con == False:
 				self.content = '姿势'
 				self.up()
 				print '请调整姿势！'
 			elif con > 60:
 				self.c = True
 				self.content = '开门'
 				self.up()
 				print '解锁'
 				GPIO.output(3,GPIO.HIGH)
 				time.sleep(3)
 				GPIO.output(3,GPIO.LOW)
 			else:
 				self.content = '允许'
 				print "请获得主人允许！"
 			
 		elif not signal and self.c == True:
 			self.history = signal
 			self.c = False
 			self.content = '关闭'
 			self.up()
 			print '锁住'
 			#GPIO.output(3,GPIO.HIGH)
 		GPIO.cleanup()
 		GPIO.setmode(GPIO.BOARD)
 		time.sleep(1)
 		GPIO.setup(self.GPIOID,GPIO.IN)
 		GPIO.setup(3,GPIO.OUT)
if __name__ == '__main__':
	p = photo()
	while True:
		p.press()
		
