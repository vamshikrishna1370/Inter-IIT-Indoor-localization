def rssi_mag():
	import serial
	usb = "0"
	s = serial.Serial('/dev/ttyUSB'+ usb, 115200)
	s.flushInput()
	s.readline()
	ap = s.readline()
	k = int(ap[0])*10 + int(ap[1])
	f = float(ap[3:])
	print k
	print 'Magnetic',f
        return k,f
while 1:
    rssi_mag()        
        