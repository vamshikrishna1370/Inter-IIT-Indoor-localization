import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
vs=[None] *16
count1=200
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
while 1:
	count1=200
	for i in range(0,15):
        	s.flushInput()
		GPIO.output(33,GPIO.HIGH)
	        GPIO.output(35,GPIO.HIGH)
	        GPIO.output(37,GPIO.LOW)
	        GPIO.output(31,GPIO.LOW)
	        time.sleep(0.5)
#	        GPIO.output(33,GPIO.LOW)
#	        GPIO.output(35,GPIO.LOW)
#	        GPIO.output(37,GPIO.LOW)
#		GPIO.output(31,GPIO.LOW)
#		time.sleep(0.5)
		s = serial.Serial('/dev/ttyUSB0', 115200)
		s.readline()
		s.readline()
		s.readline()
		s.readline()
		vs[i]=int(s.readline())
		print 'values' ,vs[i]
		if(count1>vs[i]):
			count1=vs[i]
			pos=i
	print' least value ',count1
	print 'value of i', pos
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(31,GPIO.HIGH)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	time.sleep(8-(pos+1)*0.5)
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(12)
	
