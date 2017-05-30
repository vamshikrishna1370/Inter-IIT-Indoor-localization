import serial
s1 = serial.Serial('/dev/ttyUSB0', 115200)
s2 = serial.Serial('/dev/ttyUSB1', 115200)

while 1:
     k1 = int(s1.readline())
     print 'first',k
     