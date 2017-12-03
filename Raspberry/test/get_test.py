# -*-coding: utf-8 -*-
import urllib2
import urllib
import RPi.GPIO as GPIO
import time
history = ''
channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
GPIO.output(channel,GPIO.LOW)
def access_token():  
    local_url = 'http://YOUR_SERVER_IP/sensor/?userid=oBFMQxJfEAXKYN0Fwz1rfIC1Q2h8'  
    response = urllib2.urlopen(local_url).read()  
    resp = response.split(';')
    
    content = resp[0]
    Time = resp[1]
    
    global history
    if  history != Time and content.count('浇水'):
        history = Time

	GPIO.setup(channel,GPIO.OUT)
	GPIO.output(channel,GPIO.HIGH)
	time.sleep(0.5)
	print 1
	GPIO.output(channel,GPIO.LOW)
    
while 1:
    time.sleep(0.1)
    access_token()
