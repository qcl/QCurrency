# -*- coding: utf-8 -*-

import webapp2
from webapp2_extras import routes
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('QCurrency is working.')

class LatestExchangeRates(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(rates))

app = webapp2.WSGIApplication([
        routes.PathPrefixRoute('/api', [
            webapp2.Route('/latest', LatestExchangeRates),
        ]), 
        ('/', MainPage),
    ], debug=True)
