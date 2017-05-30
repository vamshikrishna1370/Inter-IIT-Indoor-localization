import serial
usb = "0"
sp = serial.Serial('/dev/ttyACM'+ usb, 9600)
while 1:
	sp.flushInput()
	sp.readline()
	yo = sp.readline()
	p = float(yo)
	print p