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

        googleRates = memcache.get('latest-google')
        print googleRates
        if googleRates is not None and bot is not None and googleRates['update'] > bot.updateTime:
            response['source'] = googleRates['source']
            response['update'] = googleRates['update'].isoformat()
            response['rates'] = googleRates['rates']
        #print googleRates['update']
        
        #print bot.updateTime
        #print bot.updateTime > googleRates['update']

        self.response.write(json.dumps(response))

# TODO: different source api
routes = [
    webapp2.Route('/latest', LatestExchangeRates),
    webapp2.Route('/', APIEndpoint),
]
