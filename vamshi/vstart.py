import os, signal 

pid=os.getpid()
with open("pid1.txt", "w") as text_file:
    text_file.write(str(pid))
vs=[None] *(181)
import serial
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
p = GPIO.PWM(29, 50)
p.start(7.5)
print "                                  Congrats....."
print "                                  hello i have entered into two stage "
s = serial.Serial('/dev/ttyUSB0', 115200)
sp = serial.Serial('/dev/ttyACM0', 9600)
vs=[None] *200
count12=200
p.ChangeDutyCycle(7.5)
time.sleep(1)
def servo_write(angle):#function for setting the the servo to a particular angle 
	p.ChangeDutyCycle(float(float(angle)/float(18))+2.5)

def servo_oscillate(angle1,angle2,delay): #function to oscillate servo from angle1 to angle2 with given time delay between every degree
	for i in range(angle1,angle2):
			p.ChangeDutyCycle(float(float(i)/float(18))+2.5)
			time.sleep(delay) 
	for i in range(angle1,angle2):
			p.ChangeDutyCycle(float(float((180-i))/float(18))+2.5)
			time.sleep(delay) 
def searchwithservo(timedelay):
	val=[None] *(181)
	count1=999
	for i in range(0,180):
		print '    ',i
		s.flushInput()
		s.readline()
	        ap = s.readline()
		k = int(ap[0])*10 + int(ap[1])
		vs[i]=k
		sp.flushInput()
		sp.readline()
		yo = sp.readline()
		f = float(yo)
		print 'current magn = ',f
		if(count1>vs[i]):
			count1=vs[i]
        		pos=i
			magni=float(yo)
		p.ChangeDutyCycle(float(float(i)/float(18))+2.5)
		#servo_write(i)
		time.sleep(timedelay)
		
#	for i in range(0,180):
#		print '  ',i
#		s.flushInput()
#		s.readline()
#	        ap = s.readline()
#		k = int(ap[0])*10 + int(ap[1])
#		vs[i]=k
#		sp.flushInput()
#		sp.readline()
#		yo = sp.readline()
#		f = float(yo)
#		print 'current magn = ',f
#		#val[i]=getrssival(usb)
#		if(count1>vs[i]):
#			count1=vs[i]
#        		pos=180-i
#			magni=float(yo)
#		p.ChangeDutyCycle(float(float(180-i)/float(18))+2.5)
#		#servo_write(180-i)
#		time.sleep(timedelay)
		
	print' least value ',count1
	print 'value of i', pos
	servo_write(pos)
	time.sleep(2)
	return count1,pos,magni


	
for j in range(0,1):

	count,pos,magn=searchwithservo(0.001)
	servo_write(85)
	time.sleep(2)
	while 1:
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		#time.sleep(0.15)
		print 'where as i have to go to ',magn
		sp.flushInput()
		sp.readline()
		yo = sp.readline()
		mag = float(yo)
		print 'magn is ',mag
		if( abs((magn) - (mag))< 2.0000 ):
			print "enetered if loop in while"
			GPIO.output(37,GPIO.LOW)
			GPIO.output(31,GPIO.LOW)
			GPIO.output(33,GPIO.LOW)
			GPIO.output(35,GPIO.LOW)
			time.sleep(0.15)
			break
			break
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(5)
	print "hasdifhnia"
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	time.sleep(0.15)
	print "reached last line of big while" 
		
print "program terminated"