#!/usr/bin/python

from bottle import get, post, request, static_file, route, error, run

import sys

import ptl_json
import ptl_twitter

### MODIFY DEPENDING ON APP LOCATION 
ROOT_FOLDER = '/var/www_app/api/'
###

# Other file locations
JSON_FILENAME= ROOT_FOLDER  + 'status.json'
API_KEYS= ROOT_FOLDER + 'api_keys'

#API_KEYS must be a fixed lenght, one per line
KEY_LENGTH=20

@get('/change_status')
def change_status():
    return static_file('change_status.html', root=ROOT_FOLDER )

@get('/form_styles.css')
def form_styles_css():
    return static_file('form_styles.css', root=ROOT_FOLDER )

@post('/change_status')
def change_status_post():
    api_key 	= request.forms.get('api_key')
    status 	= request.forms.get('status')
    open_closed	= request.forms.get('open_closed')
    twitter 	= request.forms.get('twitter')

    if len(status) <= 140 and open_closed in ("open", "closed"):
        if open_closed == "open":
             open_closed = True
        else:
	        open_closed = False
    else:
		return "Missing some information or status is longer than 140char"

    if API_KEYS:
        if valid_api_key(api_key, API_KEYS):
            ptl_json.update_status(JSON_FILENAME, status, open_closed)
            msg = "Did not tweet status"
            if twitter and twitter == "tweet":
			    msg = "Will NOT send to Twitter: Tweet is less than 3 char long"
			    if status and len(status) > 2:
				    msg = format_twitter_rtrn_value(ptl_twitter.update(status))
            return "Information updated" + "<br>" + msg
        else:
            return "The API Key is invalid"

def format_twitter_rtrn_value(twitter_rtrn_value):
	if twitter_rtrn_value == 0:
		return "Status has been sent to Twitter"
	else:
		return "<strong>ERROR while sending to Twitter</strong>. Return value is: " + str(twitter_rtrn_value)

@get('/info/:tag#[a-z]+#')
@get('/info/:tag#[a-z]+#/')
def return_info(tag):
    return ptl_json.json_value(JSON_FILENAME, tag)
    
@get('/info/:tag#[a-z]+#/:tag_sec#[a-z]+#')
def return_info(tag, tag_sec):
    return ptl_json.json_value(JSON_FILENAME, tag, tag_sec)

#Serve json file
@get('/status.json')
@get('/json/')
@get('/json')
def return_json():
    return static_file('status.json', root=ROOT_FOLDER)

#Error page
@error(404)
def error404(error):
    return '404 - Nothing here, sorry'

### Functions ###
def valid_api_key(api_key, file_keys):
    if len(api_key) == KEY_LENGTH:
        key_list = open(file_keys)
        for key in key_list.readlines():
            if api_key == key.rstrip():
                return True
    return False

#Uncomment to use python built-in webserver
#Should be commented when using another web server
#run(host='localhost', port=8080)
