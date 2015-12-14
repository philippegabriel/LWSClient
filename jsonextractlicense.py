#!/usr/bin/python
from __future__ import print_function # Python 2/3 compatibility
import json
import sys
try:
	input=str(sys.argv[1])
except:
	print("Missing json file name\nusage: upload.py <json input file>\n")
	sys.exit(1)
fd=open(input)
input=fd.read()
decoder=json.JSONDecoder(strict=False)
dict=decoder.decode(input)
if('errorMessage' in dict):
	print("############################### LWS returned an ERROR ######################################")
	for k, v in dict.iteritems():
    		print(k, v)
	print("############################################################################################")
	sys.exit(1)
print("RequestUUID:%s"%dict['RequestUUID'])
print("Created:%s"%dict['Created'])
print("from IP address:%s"%dict['Source IP'])
payload=dict['Payload']
for item in payload:
	print(item)
sys.exit(0)
