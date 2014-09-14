#!/usr/bin/python

import json
import sys
import time


def json_read(filename):
    try:
        json_file = open(filename)
        json_parsed = json.loads(json_file.read())
    except IOError:
        sys.stderr.write("Could not open json file")
        sys.exit()
    else:
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
    json_parsed = json_read(filename)
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
    else:
        return True
