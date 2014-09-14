# Interface bottle app with Apache / modwsgi

import sys
import os
import bottle

ROOT_FOLDER = '/data/www_app/status/'

sys.path = [ROOT_FOLDER] + sys.path
os.chdir(os.path.dirname(__file__))

import status_api  # Loads application

application = bottle.default_app()

###DEUG OPTION###
# bottle.debug(True)

## Expetions in apache log (but not in browser) ###
#bottle.app().catchall = False
