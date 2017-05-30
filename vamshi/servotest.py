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

servo_oscillate(0,180,0.005)
