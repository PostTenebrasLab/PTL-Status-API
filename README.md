PTL-Status-API
=======================

Used for updating the Hackerspace Space API Json file and more.

The project is written in python and uses the web framework bottle.
* Bottle framework:  http://bottlepy.org

**Please see http://www.posttenebraslab.ch/status for more information about the use at Post Tenebras Lab**

## What is the SpaceAPI?

Check the official site: http://spaceapi.net/

>What is the Space API?
>
>The purpose of the Space API is to define a unified specification across the hackerspaces that can be used to expose information to web apps or any other application. The specification is based on the JSON data interchange format.

## What is this project?

- A simple webapp/"API" to update the Space API Json file.
- Update can be done from a simple web page
- Or simply send a POST request from any device
- Can return different hackerspace logo depending on status
- Retrive info from Json using HTTP URL

**Please see http://www.posttenebraslab.ch/status for more information**

Note: This project is mainly intended for use at the PTL Hackerspace.

## Future feature / improvement

## File structure

## Installing

* Install the bottle web framework (tested on debian7. Packaged version is 0.10)
* Copy all files into a folder where you want the web app to reside (exemple: /var/www_app/status/ or /data/www_app/status)
* Modify the "ROOT_FOLDER" constant in adapter.wsgi
* Modify the constants in config.py (configuratin file)
* Add a key in api_keys (one key per line, length must match what is set in config.py)

If using in another Hackerspace, you will likely want to modify the doc, json file, and python script to suit your usercase.

If you're using an external web server with wsgi:

* Configure you webserver to serve the bottle web app

If you want to use the python built in web server (useful for testing)
* Uncomment the relevent lines a the end of "status_api.py"
* Execute "status_api.py"
* You should now have a local web server running on port 8080

### Sample apache configuration

* You will need to install "mod_wsgi"

On debian, you can add a file to your /etc/apache2/conf.d folder with this configuration:

* Adapt location as needed

````
## PTL-Status-API ##
## Uses bottle python web framework ##
## https://github.com/PostTenebrasLab/PTL-Status-API

WSGIDaemonProcess status user=www-data group=www-data processes=1 threads=5
WSGIScriptAlias /status /data/www_app/status/adapter.wsgi

<Directory /data/www_app/status>
    WSGIProcessGroup status
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
##### END BOTTLE #######
````

