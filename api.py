# -*- coding: utf-8 -*-

import webapp2
import json

from datetime import datetime
from google.appengine.api import memcache

class APIEndpoint(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('QCurrency API Endpoint')

class LatestExchangeRates(webapp2.RequestHandler):
    def get(self):
        response = {
                    'source': 'Bank of Taiwan',
                    'update': datetime.fromtimestamp(0).isoformat(),
                    'rates': {}
                }
        self.response.headers['Content-Type'] = 'application/json'

        bot = memcache.get('latest-bot')
        if bot is not None:
            response['update'] = bot.updateTime.isoformat()
            response['rates'] = bot.exchangeRates

        self.response.write(json.dumps(response))

routes = [
    webapp2.Route('/latest', LatestExchangeRates),
    webapp2.Route('/', APIEndpoint),
]
