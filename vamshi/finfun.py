import os, signal
pid=os.getpid()
with open("pid2.txt", "w") as text_file:
   text_file.write(str(pid))
import serial
import RPi.GPIO as GPIO
import time

def rssi_pi():
	import subprocess
	import time
	import argparse
	k =0
	link_avg = 0
	rssi_avg = 0
	kp = [None] * 100
	f  = [None] * 100
	c  = [None] * 100
	parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
	parser.add_argument(dest='interface', nargs='?', default='wlan0',
	                    help='wlan interface (default: wlan0)')
	args = parser.parse_args()
	#print '\n---Press CTRL+Z or CTRL+C to stop.---\n'
	while k < 10:
	    cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
	                           stdout=subprocess.PIPE)
	    for line in cmd.stdout:
	        if 'Link Quality' in line:
	            kp = line.lstrip(' '),
	        elif 'Not-Associated' in line:
	            print 'No signal'
	    time.sleep(0.1)
	    h = kp[0]
	    #print(h)
	    d =int(h[13])
	    e =int(h[14])
	    f[k] =10*d+e  
	    #print 'link',f[k]
	    link_avg = link_avg+f[k] 
	    a = int(h[34])
	    b = int (h[35])
	    c[k] = 10*a+b
	    rssi_avg = rssi_avg + c[k]
	    #print 'rssi', c[k]
	    k = k+1
	    if k is 10:
	    	link_avg = float(float(link_avg)/float(10.0000))
	    	rssi_avg = float(float(rssi_avg)/10.00000)
	print 'link avg', link_avg
	print 'rssi_Avg', rssi_avg    
	return link_avg,rssi_avg
count=0
while 1 :
	a,b=rssi_pi()
	if (a==70):
		count = count +1		
		if (count==3):
			ff = open("pid.txt")
			k=( int(ff.read()) )
			#import os, signal
			print "stopping in few seconds"
			time.sleep(1)
			print "stopped"
			os.kill(k, signal.SIGKILL)	
			print "after os.kill"
			os.system("python stop.py")
			print "after stop.py"
			time.sleep(4)
			os.system("python vstart.py")
			print "after start.py"
			break
			break
count=0
while 1 :
	a,b=rssi_pi()
	if (b<=29):#check thi svalue out
		count = count +1		
		if (count==2):
			ff = open("pid1.txt")
			k=( int(ff.read()) )
			#import os, signal
			print "stopping in few seconds"
			time.sleep(2)
			print "stopped"
			os.kill(k, signal.SIGKILL)	
			print "after os.kill"
			os.system("python stop.py")
			print "after stop.py"
			## #KILLING MYSELF	####
			ff = open("pid2.txt")
			k=( int(ff.read()) )
			#import os, signal
			print "stopping my self"
			os.kill(k, signal.SIGKILL)
			break
			break

