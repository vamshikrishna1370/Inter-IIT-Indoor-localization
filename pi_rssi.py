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
while k < 5:
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
    print 'link',f[k]
    link_avg = link_avg+f[k] 
    a = int(h[34])
    b = int (h[35])
    c[k] = 10*a+b
    rssi_avg = rssi_avg + c[k]
    print 'rssi', c[k]
    k = k+1
    if k is 5:
    	link_avg = link_avg/5
    	rssi_avg = rssi_avg/5
print 'link avg', link_avg
print 'rssi_Avg', rssi_avg    