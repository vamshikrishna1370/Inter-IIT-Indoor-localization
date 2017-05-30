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
	return k
	print k
def robot_slow_right(timetotravel,dc):#time to rotate and dutycycle == pwm frequency (directly PWM applied to signal pins)
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
	time.sleep(timetotravel)
def robot_slow_left(timetotravel,dc):#time to rotate and dutycycle == pwm frequency (directly PWM applied to signal pins)
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
	time.sleep(timetotravel)
	

