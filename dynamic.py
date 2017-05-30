import serial
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
p = GPIO.PWM(29, 50)
p.start(7.5)

def servo_write(angle):#function for setting the the servo to a particular angle 
	p.ChangeDutyCycle(float(float(angle)/float(18))+2.5)

def servo_oscillate(angle1,angle2,delay): #function to oscillate servo from angle1 to angle2 with given time delay between every degree
	for i in range(angle1,angle2):
			p.ChangeDutyCycle(float(float(i)/float(18))+2.5)
			time.sleep(delay) 
	for i in range(angle1,angle2):
			p.ChangeDutyCycle(float(float((180-i))/float(18))+2.5)
			time.sleep(delay) 
def robot_foreward(timetotravel):
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(timetotravel)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
def robot_backward(timetotravel):
	GPIO.output(37,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.HIGH)
	GPIO.output(31,GPIO.HIGH)
	time.sleep(timetotravel)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
def robot_stop():
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
def robot_right(timetotravel):
	GPIO.output(33,GPIO.HIGH)
	GPIO.output(35,GPIO.HIGH)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
	time.sleep(timetotravel)
def robot_left(timetotravel):
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(31,GPIO.HIGH)
	time.sleep(timetotravel)
def getrssival(usb="0"):
	s = serial.Serial('/dev/ttyUSB'+ usb, 115200)
	s.flushInput()
	s = serial.Serial('/dev/ttyUSB'+ usb, 115200)
	s.readline()
	s.readline()
	s.readline()
	s.readline()
	k= int(s.readline())
	print k
	return k
def robot_slow_right(dc):#time to rotate and dutycycle == pwm frequency (directly PWM applied to signal pins)
	p1=GPIO.PWM(31, 100)
	p2=GPIO.PWM(33, 100)
	p3=GPIO.PWM(35, 100)
	p4=GPIO.PWM(37, 100)
	p1.start(0)
	p2.start(0)
	p3.start(0)
	p4.start(0)
	p2.ChangeDutyCycle(dc)
	p3.ChangeDutyCycle(dc)
	#time.sleep(timetotravel)
def robot_slow_left(dc):#time to rotate and dutycycle == pwm frequency (directly PWM applied to signal pins)
	p1=GPIO.PWM(31, 100)
	p2=GPIO.PWM(33, 100)
	p3=GPIO.PWM(35, 100)
	p4=GPIO.PWM(37, 100)
	p1.start(0)
	p2.start(0)
	p3.start(0)
	p4.start(0)
	p1.ChangeDutyCycle(dc)
	p4.ChangeDutyCycle(dc)
	#time.sleep(timetotravel)
	

def searchwithrobot(numbofitter,time4itt,time2halt,usb="0"):
	val=[None] *(numbofitter+1)
	count1=999
	for i in range(0,numbofitter):
		val[i]=getrssival(usb)
		if(count1>val[i]):
			count1=val[i]
        		pos=i
		#robot_slow_right(time4itt,dc)	
		GPIO.output(33,GPIO.HIGH)
		GPIO.output(35,GPIO.HIGH)
		GPIO.output(37,GPIO.LOW)
		GPIO.output(31,GPIO.LOW)
		time.sleep(time4itt)
		print 'time it has rotated',(time4itt + time4itt * i)
		#GPIO.output(33,GPIO.LOW)
		#GPIO.output(35,GPIO.LOW)
		#GPIO.output(37,GPIO.LOW)
		#GPIO.output(31,GPIO.LOW)
		#time.sleep(time2halt)
	print' least value ',count1
	print 'value of i', pos
	return count1,pos
def alignit2min(pos,time4itt,numbofitter):
#	robot_slow_left(( ((numbofitter) * time4itt) - ((pos)*time4itt)),dc)
	GPIO.output(37,GPIO.HIGH)
	GPIO.output(31,GPIO.HIGH)
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	print 'time to rotate is ', ( ((numbofitter ) * time4itt) - ((pos)*time4itt))
	time.sleep(( ((numbofitter) * time4itt) - ((pos)*time4itt)))
	GPIO.output(33,GPIO.LOW)
	GPIO.output(35,GPIO.LOW)
	GPIO.output(37,GPIO.LOW)
	GPIO.output(31,GPIO.LOW)
#count1, pos=searchwithrobot(15,0.25,0,"0")
#alignit2min(0,0.25,15)
def searchwithservo(timedelay,usb="0"):
	val=[None] *(181)
	count1=999
	for i in range(0,180):
		print '    ',i
		val[i]=getrssival(usb)
		if(count1>val[i]):
			count1=val[i]
        		pos=i
		servo_write(i)
		time.sleep(timedelay)
	for i in range(0,180):
		print '  ',i
		val[i]=getrssival(usb)
		if(count1>val[i]):
			count1=val[i]
        		pos=180-i
		servo_write(180-i)
		time.sleep(timedelay)
		
	print' least value ',count1
	print 'value of i', pos
	servo_write(pos)
	return count1,pos
#print 'final write after search', b







#____________________________________________________________________________________________________________________



while 1:

	#s.flushInput()

	#s = serial.Serial('/dev/ttyUSB0', 115200)

        #s.readline()

        #s.readline()

        #s.readline()

        #s.readline()

        #ss=int(s.readline())
	
	command = raw_input()

	if(command=='g'):

		while 1:

			command = raw_input()
		
			if(command=='w'):
				GPIO.output(37,GPIO.HIGH)

				GPIO.output(35,GPIO.LOW)
				GPIO.output(33,GPIO.HIGH)

				GPIO.output(31,GPIO.LOW)		

				

			if(command=='s'):

				GPIO.output(37,GPIO.LOW)
				GPIO.output(35,GPIO.HIGH)

				GPIO.output(33,GPIO.LOW)

				GPIO.output(31,GPIO.HIGH)		

				

			if(command=='a'):	
				GPIO.output(37,GPIO.LOW)

				GPIO.output(35,GPIO.HIGH)
				GPIO.output(33,GPIO.HIGH)

				GPIO.output(31,GPIO.LOW)		

				

			if(command=='d'):
				GPIO.output(37,GPIO.HIGH)

				GPIO.output(35,GPIO.LOW)

				GPIO.output(33,GPIO.LOW)

				GPIO.output(31,GPIO.HIGH)

				

			if(command=='b'):
				
				GPIO.output(37,GPIO.LOW)

				GPIO.output(35,GPIO.LOW)
				GPIO.output(33,GPIO.LOW)

				GPIO.output(31,GPIO.LOW)		

				
				

		

				
