import RPi.GPIO as GPIO
import time
import serial
s = serial.Serial('/dev/ttyUSB0', 115200)
(s.readline())
(s.readline())
(s.readline())
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
count=200
GPIO.output(3,GPIO.LOW)
for i in range(0,1499):
	s.flushInput()
	s = serial.Serial('/dev/ttyUSB0', 115200)
        s.readline()
        s.readline()
        s.readline()
        s.readline()
        vs=int(s.readline())
        print 'values',i ,vs
	#k=int(s.readline())
	#print 'values is ',k
	if (count>vs):
		count=vs
print 'min detected',count

while 1:
	s.flushInput()
        s = serial.Serial('/dev/ttyUSB0', 115200)
        s.readline()
        s.readline()
        s.readline()
        s.readline()
        vs=int(s.readline())
        print 'values' ,vs
	if (count==vs or (count-1) == vs or (count+1) ==vs):
		GPIO.output(3,GPIO.HIGH)
