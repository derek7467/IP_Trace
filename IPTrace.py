#!/usr/bin/python

import pygeoip
import socket

hostip = raw_input('What is the IP or Hostname to trace? ') target = socket.gethostbyname(hostip)
query = pygeoip.GeoIP("GeoLiteCity.dat") results = query.record_by_addr(target)

with open(hostip + "_Trace.txt", "w") as file:
	file.write("[*] Query Results: \n\n")
	for key, val in results.items():
		file.write(str(key) + ": " + str(val) + "\n")
	file.write("IP Address: " + target)
	file.write("\n[*] End of Results\n")
