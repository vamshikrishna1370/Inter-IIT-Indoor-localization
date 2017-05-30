import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
kk = [None] * 200
count1=100
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
for i in range(0,199):
	kk[i]=int(s.readline())
	print 'value',kk[i]
        GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.HIGH)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
        time.sleep(0.05)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	if(count1>kk[i]):
		count1=kk[i]         
print "completed searching "
while 1:
	k=int(s.readline())
 	if(count1==k or  count1 > k):
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)	
		time.sleep(3)
	else:
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)      
	        

