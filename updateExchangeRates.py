# -*- coding: utf-8 -*-

from exchangeRates import BankOfTaiwan
from datetime import datetime, tzinfo, timedelta

import urllib, urllib2

latestBoTExchangeRatesURL = 'http://rate.bot.com.tw/xrt/fltxt/0/day'

class TaipeiTime(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=8)
    def dst(self, dt):
        return timedelta(0)
    def tzname(self, dt):
        return 'Asia/Taipei'

def fetchFromBoT():
    print 'Fetch from %s' % (latestBoTExchangeRatesURL)

    bot = None
    try:
        request = urllib2.Request(latestBoTExchangeRatesURL)
        response = urllib2.urlopen(request)

        # try to get update time, filename format from BoT: ExchangeRate@201803081600.txt
        # ExchangeRates@YYYYMMDDHHMM.txt
        updateTime = None
        contentDisposition = response.headers.get('Content-Disposition', '')
        if 'ExchangeRate@' in contentDisposition:
            filenameStr = contentDisposition.split('ExchangeRate@')[1]
            if '.txt' in filenameStr :
                filenameStr = filenameStr.split('.txt')[0]
            if len(filenameStr) is 12:
                year = int(filenameStr[:4])
                month = int(filenameStr[4:6])
                day = int(filenameStr[6:8])
                hour = int(filenameStr[8:10])
                minute = int(filenameStr[10:12])

                updateTime = datetime(year=year, month=month, day=day, hour=hour, minute=minute, tzinfo=TaipeiTime())

        if updateTime is None:
            print 'Cannot resolve exchange rates update time.'

        bot = BankOfTaiwan()
        bot.parse(response)
        bot.updateTime = updateTime

        print bot.exchangeRates
    except:
        print 'Fetch fail.'
    
    return bot

def fetchFromGoogle():
    print 'Fetch from Google Currency Converter'
    
    #'https://finance.google.com/finance/converter?a=1&from=TWD&to=EUR'
    googleConverterURL = 'https://finance.google.com/finance/converter'

    currencies = ['USD', 'AUD', 'CHF', 'ZAR', 'CNY', 'JPY', 'GBP', 'NZD', 'SGD', 'CAD', 'SEK', 'THB', 'HKD', 'EUR']
    rates = {}

    try:
        for currency in currencies:
            query = {
                'a': 1,
                'to': 'TWD',
                'from': currency
            }

            requestURL = googleConverterURL + '?' + urllib.urlencode(query)
            request = urllib2.Request(requestURL)
            response = urllib2.urlopen(request)

            for line in response:
                if 'currency_converter_result' in line:
                    if '<span class=bld>' in line:
                        resultStr = line.split('<span class=bld>')[1]
                        resultStr = resultStr.split()[0]
                        rates[currency] = float(resultStr)
                    break

        if len(rates.keys()) == len(currencies):
            result = {
                'rates': rates,
                'update': datetime.now(tz=TaipeiTime()),
                'source': 'Google Currency Converter'
            }
            print result
            return result
    except:
        print 'Fetch fail.'

    return None


def update():
    print 'Start update'
    fetchFromBoT()
    fetchFromGoogle()
    print 'End update'


if __name__ == '__main__':
    update()
