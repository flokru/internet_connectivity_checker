#!/usr/bin/env python3

from urllib import request
#from socket import timeout
import time
from datetime import datetime
import sys

TEST_URIS = ["http://www.google.com", "http://www.facebook.com", "http://www.amazon.com"]
TIMEOUT = 2
MAX_BUFFER_LEN = 100
WAIT_TIME = 15
file_num = 1
results = []

def fetch_any_site():
	for uri in TEST_URIS:
		#try:
			print 'probing', uri, TIMEOUT
			response = request.urlopen(uri, timeout = TIMEOUT)
			return True
		#except (urllib2.URLError, timeout) as err: pass
	return False

def flush_results():
	global file_num
	global results
	
	filename = "internet_status_" + str(file_num) + ".csv"
	file_num = file_num + 1
	file_handle = open(filename, "w")
	for line in results:
		file_handle.write(line + "\n")
	file_handle.close()
	results = []

def check_internet():
	global results

	is_connected = fetch_any_site()
	timestamp = str(datetime.now())
	status = "connected" if is_connected else "disconnected"
	
	result_str = status + "," + timestamp
	print result_str
	sys.stdout.flush()
	#results.append(result_str)

	#if len(results) >= MAX_BUFFER_LEN:
	#	flush_results()

def loop():
	check_internet()
	time.sleep(WAIT_TIME)

if __name__ == "__main__":
	loop()
		
