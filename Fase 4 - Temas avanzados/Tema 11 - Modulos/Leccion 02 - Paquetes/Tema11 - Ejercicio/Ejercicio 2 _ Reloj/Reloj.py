import datetime
import time
import os

def clock():
	os.system("cls")
	while True:
		current_time=datetime.datetime.now()
		print ("{}:{}:{}".format(current_time.hour, current_time.minute, current_time.second))
		time.sleep (1)
		os.system("cls")
		