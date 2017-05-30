import os
pid=os.getpid()
with open("pid.txt", "w") as text_file:
    text_file.write(str(pid))
import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
vs=[None] *16
count1=200
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

while 1:
	#s.flushInput()
	#s = serial.Serial('/dev/ttyUSB0', 115200)
        #s.readline()
        #s.readline()
        #s.readline()
        #s.readline()
        #ss=int(s.readline())
	if(count1<=30):
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		time.sleep(1)
		break
	count1=200
	for i in range(0,12):
        	s.flushInput()
		s = serial.Serial('/dev/ttyUSB0', 115200)
                s.readline()
                '''s.readline()
                s.readline()
                s.readline()'''
		ap = s.readline()
		k = int(ap[0])*10 + int(ap[1])
		f = float(ap[3:])
                vs[i]=k
		print 'Magnetic',f
                print 'values' ,vs[i]
                if(count1>vs[i]):
                        count1=vs[i]
                        pos=i
		
		
		GPIO.output(33,GPIO.HIGH)
	        GPIO.output(35,GPIO.HIGH)
	        GPIO.output(37,GPIO.LOW)
	        GPIO.output(31,GPIO.LOW)
	        time.sleep(0.25)
	        GPIO.output(33,GPIO.LOW)
	        GPIO.output(35,GPIO.LOW)
	        GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		time.sleep(0.15)
	print' least value ',count1
	print 'value of i', pos
	#tc=(2+((count1-40)*9)/15)/2
	if(count1<=30):
                GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		time.sleep(1)
                break

	GPIO.output(37,GPIO.HIGH)
	GPIO.output(31,GPIO.HIGH)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	time.sleep(3.25-(pos)*0.25)
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(4)
	

