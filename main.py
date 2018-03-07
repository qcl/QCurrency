#-*- coding: utf-8 -*-

import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('QCurrency is working.')

class LatestExchangeRates(webapp2.RequestHandler):
    def get(self):
        rates = {}
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(rates))

app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/api/latest', LatestExchangeRates),
    ], debug=True)
