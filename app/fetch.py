# -*- coding: utf-8 -*-

import webapp2
import json

from google.appengine.api import memcache

from updateExchangeRates import fetchFromBoT

class Fetch(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Trigger fetch latest exchange rates.')
        #print self.request.headers

        bot = fetchFromBoT()
        if bot is not None:
            memcache.set('exchange-rates', '%s' % (json.dumps(bot.exchangeRates)))
            memcache.set('latest-fetch-time', '%s' % (bot.updateTime.isoformat()))
            memcache.set('latest-bot', bot)
        else:
            print 'Fetch to update fail'

routes = [
    webapp2.Route('/', Fetch),
]
