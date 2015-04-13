#!/usr/bin/python

from bottle import get, post, request, static_file, route, error, run, response, abort

import sys
import status_json

# Conf file with constants
from config import *

######## Start of status image section ####################

# Return small open / closed logo


@get('/img/small_status.png')
def open_closed_img():
    response.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.set_header('max age', '0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')
    if status_json.json_value(JSON_FILENAME, "state", "open") == "True":
        return static_file(
            'img/open_small.png',
            root=ROOT_FOLDER,
            mimetype='image/png')
    else:
        return static_file(
            'img/closed_small.png',
            root=ROOT_FOLDER,
            mimetype='image/png')


@get('/img/static/open_small.png')
def open_closed_img():
    return static_file(
        'img/open_small.png',
        root=ROOT_FOLDER,
        mimetype='image/png')


@get('/img/static/closed_small.png')
def open_closed_img():
    return static_file(
        'img/closed_small.png',
        root=ROOT_FOLDER,
        mimetype='image/png')

# Return PTL logo with red / green text for "lab"


@get('/img/logo_status.png')
def open_closed_img():
    response.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.set_header('max age', '0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')
    if status_json.json_value(JSON_FILENAME, "state", "open") == "True":
        return static_file(
            'img/open_logo.png',
            root=ROOT_FOLDER,
            mimetype='image/png')
    else:
        return static_file(
            'img/closed_logo.png',
            root=ROOT_FOLDER,
            mimetype='image/png')


@get('/img/static/open_logo.png')
def open_closed_img():
    return static_file(
        'img/open_logo.png',
        root=ROOT_FOLDER,
        mimetype='image/png')


@get('/img/static/closed_logo.png')
def open_closed_img():
    return static_file(
        'img/closed_logo.png',
        root=ROOT_FOLDER,
        mimetype='image/png')

# Return normal PTL logo when closed and with open logo (green "lab" text)
# when open


@get('/img/logo.png')
def open_closed_img():
    response.set_header('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.set_header('max age', '0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')
    if status_json.json_value(JSON_FILENAME, "state", "open") == "True":
        return static_file(
            'img/open_logo.png',
            root=ROOT_FOLDER,
            mimetype='image/png')
    else:
        return static_file(
            'img/normal_logo.png',
            root=ROOT_FOLDER,
            mimetype='image/png')


@get('/img/static/normal_logo.png')
def open_closed_img():
    return static_file(
        'img/normal_logo.png',
        root=ROOT_FOLDER,
        mimetype='image/png')

# HTML page showing the different logo
@get('/img/')
def img_info_page():
    return static_file('html/info_img.html', root=ROOT_FOLDER)

@get('/img/ptl_control_panel.jpg')
def img_info_page():
    return static_file('img/ptl_control_panel.jpg', root=ROOT_FOLDER)

######## End of status image section ####################

######## Start of status update section ####################


@get('/change')
@get('/change_status')
def change_status():
    return static_file('html/change_status.html', root=ROOT_FOLDER)


@get('/form_styles.css')
def form_styles_css():
    return static_file('html/form_styles.css', root=ROOT_FOLDER)


@post('/change')
@post('/change_status')
def change_status_post():
    api_key = request.forms.get('api_key')
    status = request.forms.get('status')
    open_closed = request.forms.get('open_closed')

    if len(status) <= 140 and open_closed in ("open", "closed"):
        if open_closed == "open":
            open_closed = True
        else:
            open_closed = False
    else:
        return "Missing information or status is longer than 140char"

    if API_KEYS:
        if valid_api_key(api_key, API_KEYS):
            status_json.update_status(JSON_FILENAME, status, open_closed)
            return "Information updated"
        else:
            abort(401, "Sorry, the API Key is invalid")

######## End of status image section ####################

######## Start of simple JSON info retriever ####################


@get('/')
@get('/info')
@get('/info/')
def info_ptl_status_api_page():
    return static_file('html/info_ptl_status_api.html', root=ROOT_FOLDER)


@get('/info/:tag#[a-z]+#')
@get('/info/:tag#[a-z]+#/')
def return_info(tag):
    response = status_json.json_value(JSON_FILENAME, tag)
    if response:
        return response
    else:
        abort(404, "")


@get('/info/:tag#[a-z]+#/:tag2#[a-z]+#')
@get('/info/:tag#[a-z]+#/:tag2#[a-z]+#/')
def return_info(tag, tag2):
    response = status_json.json_value(JSON_FILENAME, tag, tag2)
    if response:
        return response
    else:
        abort(404, "")


@get('/info/:tag#[a-z]+#/:tag2#[a-z]+#/:tag3#[a-z]+#')
@get('/info/:tag#[a-z]+#/:tag2#[a-z]+#/:tag3#[a-z]+#/')
def return_info(tag, tag2, tag3):
    response = status_json.json_value(JSON_FILENAME, tag, tag2, tag3)
    if response:
        return response
    else:
        abort(404, "")

######## End of simple JSON info retriever ####################

######## Start of return Json ####################
# Serve json file


@get('/status.json')
@get('/json/')
@get('/json')
def return_json():
    status_json.json_read(JSON_FILENAME, skip_check=0)
    response.set_header('Cache-Control', 'no-cache')
    response.set_header('max age', '0')
    response.set_header('Pragma', 'no-cache')
    response.set_header('Expires', '0')
    response.set_header('Access-Control-Allow-Origin', '*')
    return static_file(JSON_FILE_REL, root=ROOT_FOLDER)

######## End of return Json ####################

######## Start of error page def ####################
# Return blank page on 404


@error(404)
def error404(error):
    return ''
######## End of error page def ####################

### Functions ###


def valid_api_key(api_key, file_keys):
    if len(api_key) == KEY_LENGTH:
        key_list = open(file_keys)
        for key in key_list.readlines():
            if api_key == key.rstrip():
                return True
    return False

# Uncommend to use python built-in webserver (development only)
# Should be commented when using Apache / modwsgi
#run(host='localhost', port=8080)
