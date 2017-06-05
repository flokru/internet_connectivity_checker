#!/usr/bin/env python3

import time
from datetime import datetime
import sys
import subprocess

TEST_HOSTS = ["www.google.com", "www.facebook.com", "www.amazon.com"]
TIMEOUT = 2
WAIT_TIME = 15
file_num = 1
results = []

def check_ping(hostname):
	try:
		output = subprocess.check_output(['ping', '-c 1', hostname], stderr=subprocess.PIPE, timeout=TIMEOUT)
		return True
	except Exception:
		return False

def fetch_any_site():
	for host in TEST_HOSTS:
		result_ping = check_ping(host)
		if result_ping is True:
			return True
	return False

def check_internet():
	global results

	is_connected = fetch_any_site()
	timestamp = str(datetime.now())
	status = "connected" if is_connected else "disconnected"
	
	result_str = status + "," + timestamp
	print(result_str)
	sys.stdout.flush()

def loop():
	check_internet()
	time.sleep(WAIT_TIME)

if __name__ == "__main__":
	while True:
		loop()
		
