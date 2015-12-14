## Citrix Licencing Web Service - How To

#### Introduction
------
This document describe how to use the Citrix Licencing Web Service (LWS), specified in: "Citrix Licencing Web Service Specification"

#### References
------
* [AWS](https://aws.amazon.com/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS DynamoDB](https://aws.amazon.com/dynamodb/)


#### Implementation
------
Because of its tight constraints on availability and performance at scale, LWS is implemented on the Amazon Web Service infrastructure (AWS).

More precisely, LWS uses AWS Lambda and AWS DynamoDB as backend.

The service has been succesfully tested to handle up to 100 simultaneous request for 100 licenses.

#### Access to LWS
------
Access is by posting a json with an HTTP 'POST' method to the service endpoint url.

##### File description:
* [`jsonextractlicense.py`](jsonextractlicense.py) Sample Python code to decode the json response sent back by LWS
* [`testkey.pub.asc`](testkey.pub.asc) is the test public key, matching the test private key used with LWS at the moment
* [`Makefile`](Makefile)
  * check:  Checks that the request.json file has the correct syntax
  * import: Import the test public key in the gpg keyring for signing
  * post: send the request.json to LWS
  * extract: decode the received response.json
  * verify: Verify the gpg signature of the response
	
#### Invocation:
------
You first need to get a valid url.txt, which the Makefile needs to access LWS
You need a valid request.json file.
This should have been sent to you along with this document.
Then invoke `make`

#### Limits
------
tested working up to 100 simultaneous request
beyond that, requests start to fail with: `{"Type":"User","message":"Rate Exceeded."}`


