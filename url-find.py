#!/usr/bin/env python
# Written by Ivan Avilla - http://ivanavilla.com
# import required modules
import itertools
from itertools import product
import string
import urllib2
import time
import requests
import ssl
from requests.exceptions import HTTPError
# Ignore certificate errors
context = ssl._create_unverified_context()
# Set characters to be used in URL finder
# May use available Character sets in strings or custom
#chars = string.lowercase + string.digits + string.punctuation + string.whitespace
chars = string.lowercase
# Configure starting URL - include trailing slash if starting at domain name
website = "http://ivanavilla.com/"
# Configure min length to try
minurl = 1
# Configure max length to try
maxurl = 20
# Configure time between attempts in seconds
delay = 0.1
# Configure output files
foundurls = "urls.txt"
non404errors = "non404.txt"
# Uncomment print statements to debug
for increment in range(minurl,maxurl):
    #print increment
    time.sleep(delay)
    for guess in itertools.product((chars), repeat=increment):
        i = ''.join(guess)
        #print i
        try:
            sitetry = urllib2.urlopen(website + i, context=context)
            print "\nURL found - " + website + i
            f = open(foundurls,"a+")
            f.write(website + i + "\n")
            f.close()
        except urllib2.HTTPError as e:
            #print e.code
            #print "\nInvalid URL - " + website + i
            if e.code != 404:
                 print "\n" + str(e.code) + " - " + website + i
                 f2 = open(non404errors,"a+")
                 f2.write(website + i + " - Error " + str(e.code) + "\n")
                 f2.close()
            continue
