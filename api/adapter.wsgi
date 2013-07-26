import sys, os, bottle

sys.path = ['/var/www_app/api/'] + sys.path
os.chdir(os.path.dirname(__file__))

import ptl_space # This loads your application

application = bottle.default_app()

###DEUG OPTION###
bottle.debug(True)

## Expetions in apache log (but not in browser) ###
#bottle.app().catchall = False
