#!/usr/bin/python
#Uses twidge to udpate tiwitter status

#Create config beforehand with "twidge setup" and make sure it is 
#readable by the user bottlepy is running as (typically www-data)
TWIDGE_CONFIG_FILE="/var/www_app/.twidgerc"

from subprocess import call

def update(status):
	return call(["twidge", "-c", TWIDGE_CONFIG_FILE, "update", status])

#print update("sc ript runn  ing ok")
