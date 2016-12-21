Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/python

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
