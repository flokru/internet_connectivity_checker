This is a simple utility for testing internet connectivity over time. To be very specific, I've been experiencing crappy internet outages at home lately, and I wanted some data to back me up when contacting my ISP.

You can modify the constants in the Python script to adjust the test URI, the delay between polling attempts, and how often the results get flushed to output files.

Pre-requisites: Python 3.

Execute the script with `python internet_test.py`. It will run indefinitely unless you halt it (e.g., with Ctrl + C).

Outputs a CSV-compatible line with connection status each 15 seconds (roughly).
