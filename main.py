import os
import sys
import wsgiref.handlers

from google.appengine.ext import webapp

import gaeo
from gaeo.dispatch import router

def initRoutes():
    r = router.Router()
    
    #TODO: add routes here

    r.connect('/:controller/:action/:id')

def main():
    # add the project's directory to the import path list.
    sys.path.append(os.path.dirname(__file__))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'application'))

    # get the gaeo's config (singleton)
    config = gaeo.Config()
    # setup the templates' location
    config.template_dir = os.path.join(
        os.path.dirname(__file__), 'application', 'templates')

    initRoutes()

    app = webapp.WSGIApplication([
                (r'.*', gaeo.MainHandler),
            ], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
