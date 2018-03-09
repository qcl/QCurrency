# -*- coding: utf-8 -*-

import webapp2
from webapp2_extras import routes
import json

from api import routes as apiRoutes
from fetch import routes as fetchRoutes

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('QCurrency is working.')

app = webapp2.WSGIApplication([
        routes.PathPrefixRoute('/api', apiRoutes),
        routes.PathPrefixRoute('/fetch', fetchRoutes),
        ('/', MainPage),
    ], debug=True)
