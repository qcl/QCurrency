# -*- coding: utf-8 -*-

import webapp2
import json

from google.appengine.api import memcache

from updateExchangeRates import fetchFromBoT, fetchFromGoogle

def fetchToUpdateBoT():
    bot = fetchFromBoT()
    if bot is not None:
        memcache.set('exchange-rates', '%s' % (json.dumps(bot.exchangeRates)))
        memcache.set('latest-fetch-time', '%s' % (bot.updateTime.isoformat()))
        memcache.set('latest-bot', bot)
    else:
        print 'Fetch to update fail'

def fetchToUpdateGoogle():
    result = fetchFromGoogle()
    if result is not None:
        memcache.set('latest-google', result)
    else:
        print 'Fetch to update fail'

def fetchToUpdateAll():
    fetchFromGoogle()
    fetchToUpdateBoT()

class Fetch(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Trigger fetch latest exchange rates.')
        #print self.request.headers

        fetchToUpdateAll()

class FetchFromGoogle(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Trigger fetch latest exchange rates.')

        fetchToUpdateGoogle()

class FetchFromBoT(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Trigger fetch latest exchange rates.')
    
        fetchToUpdateBoT()


routes = [
    webapp2.Route('/', Fetch),
    webapp2.Route('/google', FetchFromGoogle),
    webapp2.Route('/bot', FetchFromBoT),
]
