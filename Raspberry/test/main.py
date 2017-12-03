#!/usr/bin/python
import RPi.GPIO
import time
import smbus
import urllib2
import urllib
def http_post(v):  
    url = "http://YOUR_SERVER_IP/sensor/"  
    postdata = 'data=' + str(v) 
    req = urllib2.Request(url,postdata)   
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')  
    response = urllib2.urlopen(req)  
    result = response.read() 
    print result
    if result == 0:
	print("fail")
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(25,RPi.GPIO.IN)
address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
while 1:
        bus.write_byte(address,A0)
        value = bus.read_byte(address)
        time.sleep(0.1)
        print("AOUT:%d" %(value))
        time.sleep(10)
        http_post(value)
RPi.GPIO.cleanup()
