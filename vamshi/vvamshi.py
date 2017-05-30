import os
pid=os.getpid()
with open("pid.txt", "w") as text_file:
    text_file.write(str(pid))
import serial
import RPi.GPIO as GPIO
import time
s = serial.Serial('/dev/ttyUSB0', 115200)
sp = serial.Serial('/dev/ttyACM0', 9600)
vs=[None] *16
count1=200
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
#GPIO.setup(29, GPIO.OUT)
#p = GPIO.PWM(29, 50)
#p.start(7.5)


#p.ChangeDutyCycle(float(float(90)/float(18))+2.5)
#time.sleep(1)
while 1:
	#p.ChangeDutyCycle(float(float(90)/float(18))+2.5)
	#time.sleep(0.15)

	#s.flushInput()
	#s = serial.Serial('/dev/ttyUSB0', 115200)
        #s.readline()
        #s.readline()
        #s.readline()
        #s.readline()
        #ss=int(s.readline())
	if(count1<=27):
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		time.sleep(1)
		break
	count1=200
	for i in range(0,16):
	        s.flushInput()
		s = serial.Serial('/dev/ttyUSB0', 115200)
	        s.readline()
	        ap = s.readline()
		k = int(ap[0])*10 + int(ap[1])
		vs[i]=k
		sp.flushInput()
		sp.readline()
		yo = sp.readline()
		f = float(yo)
		#print 'Magnetic',f
        	#print 'values' ,vs[i]
        	if(count1>vs[i]):
            		count1=vs[i]
            		pos=i
			mag=f
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
	print 'direct is at ',mag
	#tc=(2+((count1-40)*9)/15)/2
	if(count1<=27):
        	GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		time.sleep(1)
        	break

	#GPIO.output(37,GPIO.HIGH)
	#GPIO.output(31,GPIO.HIGH)
	#GPIO.output(33,GPIO.LOW)
	#GPIO.output(35,GPIO.LOW)
	#time.sleep(4-(pos)*0.25)
	sp.flushInput()
	sp.readline()
	yo = sp.readline()
	magn = float(yo)
	print 'current magn = ',magn
	
	while 1:
		GPIO.output(37,GPIO.HIGH)
		GPIO.output(31,GPIO.HIGH)
		GPIO.output(33,GPIO.LOW)
		GPIO.output(35,GPIO.LOW)
		#time.sleep(0.15)
		print 'where as i have to go to ',mag
		if( abs((magn) - (mag))< 6.0000 ):
			print "enetered if loop in while"
			GPIO.output(37,GPIO.LOW)
			GPIO.output(31,GPIO.LOW)
			GPIO.output(33,GPIO.LOW)
			GPIO.output(35,GPIO.LOW)
			time.sleep(0.15)
			break		
		sp.flushInput()
		sp.readline()
		yo = sp.readline()
		magn = float(yo)
		print 'magn is ',magn
		

	GPIO.output(37,GPIO.HIGH)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(4)
	


