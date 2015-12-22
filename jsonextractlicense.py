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
print("version:%s"%dict['version'])
print("requestUUID:%s"%dict['requestUUID'])
print("created:%s"%dict['created'])
print("sourceIP:%s"%dict['sourceIP'])
payload=dict['payload']
for item in payload:
	print(item)
sys.exit(0)
