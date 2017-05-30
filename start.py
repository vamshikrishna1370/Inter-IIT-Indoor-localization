import os
import time
pid=os.getpid()
with open("pid.txt", "w") as text_file:
    text_file.write(str(pid))

while 1:
	print "Congrats....."
	print " hello i have entered into two stage "
	time.sleep(2)
