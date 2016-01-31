#!/usr/bin/python

import json
import sys
import time
import shutil

# Conf file with constants
from config import *

def json_read(filename, skip_check=0):
    try:
        json_file = open(filename)
        json_parsed = json.loads(json_file.read())
    except IOError:
        sys.stderr.write("Could not open json file")
        sys.exit()
    if skip_check == 1:
        pass
    else:
        if int(json_parsed["state"]["lastchange"]) < (int(time.time()) - TIME_DELTA):
            update_status(JSON_FILENAME, EMERG_MSG, False)
    return json_parsed

def json_value(filename, tag, tag2=None, tag3=None):
    json_parsed = json_read(filename)
    try:
        if tag2 and tag3:
            result = json_parsed[tag][tag2][tag3]
        elif tag2:
            result = json_parsed[tag][tag2]
        else:
            result = json_parsed[tag]
    except KeyError as err:
        return None
    except TypeError as err:
        return None
    else:
        return str(result)

def update_status(filename, status, open_closed):
    json_parsed = json_read(filename, skip_check=1)
    json_parsed["state"]["open"] = open_closed
    json_parsed["state"]["message"] = status
    json_parsed["state"]["lastchange"] = int(time.time())
    try:
        json_file = open(filename, "w")
        json_file.write(
            json.dumps(
                json_parsed,
                sort_keys=True,
                indent=4,
                separators=(
                    ",",
                    ": ")))
    except IOError:
        sys.stderr.write("Could not write json file")
        sys.exit()
    if open_closed:
        shutil.copy(LOGO_OPEN,LOGO_DYN_1)
        shutil.copy(LOGO_OPEN,LOGO_DYN_2)
        shutil.copy(LOGO_OPEN_SMALL,LOGO_DYN_SMALL)
    else:
        shutil.copy(LOGO_NORMAL,LOGO_DYN_1)
        shutil.copy(LOGO_CLOSED,LOGO_DYN_2)
        shutil.copy(LOGO_CLOSED_SMALL,LOGO_DYN_SMALL)
    return True
