import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
s1 = serial.Serial('/dev/ttyUSB1', 115200)
kk = [None] * 100
kl = [None] * 100
count1=0
count2=0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
#while 1:
#	k1=int(s.readline())
#	print 'first=',k1
#	k2=int(s1.readline())
#	print 'second = ' ,k2
#	print 'first + second=',k1+k2
while 1:		
	for i in range(0,99):
		kk[i]=int(s.readline())
		kl[i]=int(s1.readline())
		#print i
		count1=count1+kk[i]
		count2=count2+kl[i]	
	count1=float(count1/100)
	count2=float(count2/100)
	print 'count1',count1
	print 'count2',count2
	if abs(count1-count2)<1:
                GPIO.output(37,GPIO.HIGH)
                GPIO.output(33,GPIO.HIGH)
                GPIO.output(31,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
        if count1 < count2:
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
        if count1>count2:
                GPIO.output(37,GPIO.HIGH)
                GPIO.output(31,GPIO.HIGH)
                GPIO.output(33,GPIO.LOW)
                GPIO.output(35,GPIO.LOW)
	#time.sleep(1)
	#GPIO.cleanup()

