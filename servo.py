import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.OUT)

p = GPIO.PWM(29, 50)

p.start(7.5)

try:
        while True:
		
		for i in range(0,180):
			p.ChangeDutyCycle(float(float(i)/float(18))+2.5)
			print (float(float(i)/float(18))+2.5000)
			time.sleep(0.015) 
		for i in range(0,180):
			p.ChangeDutyCycle(float(float((180-i))/float(18))+2.5)
			time.sleep(0.015) 
			print (float(float((180-i))/float(18))+2.5)

		#p.ChangeDutyCycle(2.5)  # turn towards 90 degree
		#time.sleep(1) # sleep 1 second
		#p.ChangeDutyCycle(2.5)  # turn towards 0 degree
		#time.sleep(1) # sleep 1 second
		#p.ChangeDutyCycle(12.5) # turn towards 180 degree
                #time.sleep(1) # sleep 1 second 
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
