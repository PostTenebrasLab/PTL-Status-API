#!/usr/bin/python                                                                                                                                                                                     

JSON_FILENAME = '/data/www_app/status/json/ptl_space_api.json'
JSON_FILE_REL = '/json/ptl_space_api.json'
ROOT_FOLDER = '/data/www_app/status/'

# API_KEYS must be a fixed lenght, one per line
KEY_LENGTH = 20
API_KEYS = '/data/www_app/status/api_keys'

# Emmergency shutdown option
# If no update where made within the last TIME_DELTA second, EMERG_MSG message is set
TIME_DELTA=1800
EMERG_MSG="Lab status unknown: emmergency shutdown ! [No update from PTL control panel in last 30m]"

# Images
LOGO_OPEN="img/static/open_logo.png"
LOGO_CLOSED="img/static/closed_logo.png"
LOGO_OPEN_SMALL="img/static/open_small.png"
LOGO_CLOSED_SMALL="img/static/closed_small.png"
LOGO_NORMAL="img/static/normal_logo.png"
LOGO_DYN_1="img/dyn/logo.png"
LOGO_DYN_2="img/dyn/logo_status.png"
LOGO_DYN_SMALL="img/dyn/status_small.png"
