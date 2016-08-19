This is a simple utility for testing internet connectivity over time. To be very specific, I've been experiencing crappy internet outages at home lately, and I wanted some data to back me up when contacting my ISP.

You can modify the constants in the Python script to adjust the test URI, the delay between polling attempts, and how often the results get flushed to output files.

Pre-requisites: Python 2.7.

Execute the script with `python internet_test.py`. It will run indefinitely unless you halt it (e.g., with Ctrl + C).

The results can be found as CSV files. Each line represents the result of a test, with the status (connected or disconnected) followed by a timestamp (in local time). By default, the script attempts to connect to google.com every 30 seconds or so (timing is approximate) with a 2-second timeout, flushing the results to a file whenever 100z results are collected. If it cannot connect, we consider the state to be disconnected.
