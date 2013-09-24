space_API_status-update
=======================

Interface web pour modifier du fichier JSON space API.

## What is the SpaceAPI?

Check the official site:  spaceapi.net
Also: http://hackerspaces.nl/spaceapi/

## What is this project?

A simple web interface to update part of the SpaceAPI Json file. 
The project is written in python and uses the small web framework bottle.

* Bottle web framework:  http://bottlepy.org

## Current feature

Currently using SpaceAPI v0.12. Upcoming version 0.13 not tested.

* A main page "change_status" which can update if the Hackerspace is open/closed and the status message.
* Can optionally send the status update to twitter using the CLI client twidge (still need work / testing)

* Will serve the json spaceAPI file

## File structure

* ptl_space.py (main file)
* ptl_json.py (provides json functionality)
* ptl_twitter.py (provides twitter functionality)

* api_keys (list of allowed API key)

* change_status.html
* form_styles.css

* adapter.wsgi (needed for use with wsgi capable web server)

The status.json (space API compliant json file). You will need to provide this.
For PTL, reference file is "status.json.reference" in git.

* status.json 

## Installing (WIP)

* Copy all files into a folder where you want the web app to reside (exemple: /var/www_app/api/)
* Modify the "ROOT_FOLDER" constant in ptl_space.py accordingly

If you're using an external web server with wsgi:

* Change sys.path in adapter.wsgi to relect the installation folder
* Configure you webserver

If you want to use the python built in web server (useful for testing)
* Uncomment the relevent lines a the end of "ptl_space"
* Execute "ptl_space.py"
* You should have a local web server running on port 8080

### Sample apache configuration

Note: you will need "mod_wsgi" installed


>     ServerName mypage.com

>     WSGIDaemonProcess api user=www-data group=www-data processes=1 threads=5
>     WSGIScriptAlias /api /var/www_app/api/adapter.wsgi

>     <Directory /var/www_app/api>
>         WSGIProcessGroup api
>         WSGIApplicationGroup %{GLOBAL}
>         Order deny,allow
>         Allow from all
>     </Directory>

