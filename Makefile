#!/usr/bin/make -f
.PHONY: import check post extract verify clean
all: check import post extract verify
#Check that the json request file is correct syntax
check:
	ls request.json
	ls url.txt
	cat request.json | python -mjson.tool
import:
	gpg --import testkey.pub.asc
#Post the request to the Licence Web Service
post:
	time wget -O response.json --header "Content-Type: application/json" --post-file=request.json `cat url.txt`
#Extract the json encoded request
extract:
	./jsonextractlicense.py response.json | tee license.asc
#Verify the signature of the license
verify:
	gpg  --allow-multiple-messages --verify license.asc
clean:
	rm -f license.asc response.json
