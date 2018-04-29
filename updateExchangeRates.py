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
    print 'Fetch from Google Search'
    
    #'http://www.google.com/search?q=EUR+TWD'
    googleConverterURL = 'http://www.google.com/search'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}

    currencies = ['USD', 'AUD', 'CHF', 'ZAR', 'CNY', 'JPY', 'GBP', 'NZD', 'SGD', 'CAD', 'SEK', 'THB', 'HKD', 'EUR']
    rates = {}

    try:
        for currency in currencies:
            query = {
                'hl': 'zh-TW',
                'q': '%s TWD' % (currency)
            }

            requestURL = googleConverterURL + '?' + urllib.urlencode(query)
            request = urllib2.Request(requestURL, None, headers)
            response = urllib2.urlopen(request)

            for line in response:
                if ' 台幣</div>' in line:
                    if ' =</div>' in line:
                        resultStr = line.split(' =</div>')[1]
                        resultStr = resultStr.split(' 台幣</div>')[0]
                        resultStr = resultStr.split('>')[1]
                        rates[currency] = float(resultStr)
                    break

        if len(rates.keys()) == len(currencies):
            result = {
                'rates': rates,
                'update': datetime.now(tz=TaipeiTime()),
                'source': 'Google Search'
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
