#!/usr/bin/python
import RPi.GPIO
import time
import smbus
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(25,RPi.GPIO.IN)
address = 0x48
A0 = 0x40

bus = smbus.SMBus(1)
for i in range(0,2):
    for i in range(0,4):
        bus.write_byte(address,A0)
        value = bus.read_byte(address)
        time.sleep(0.1)
        print("AOUT:%1.3f" %(value*3.3/255))
        time.sleep(1)
RPi.GPIO.cleanup()
