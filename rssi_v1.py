import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
s1 = serial.Serial('/dev/ttyUSB2', 115200)
kk = [None] * 2
kl = [None] * 2
count1=0
count2=0
flag1=0
flag2=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
while 1:
	k1=int(s.readline())
	print 'first=',k1
	k2=int(s1.readline())
	print 'second = ' ,k2
	print 'first + second=',k1+k2
while 1:		
	for i in range(0,1):
		kk[i]=int(s.readline())
		kl[i]=int(s1.readline())
		#print i
		count1=kk[i]
		count2=count2+kl[i]	
	count1=(count1/2)
	count2=(count2/2)
	print 'count1',count1
	print 'count2',count2
        if count1 > count2+10:
               flag1=1
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		time.sleep(0.1)
        if count1<count2+10:
                flag2=1
                GPIO.output(37,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
		time.sleep(0.1)
	if (flag1==1 & flag2==1):
                GPIO.output(37,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
                time.sleep(0.9)
                flag1=0
                flag2=0
