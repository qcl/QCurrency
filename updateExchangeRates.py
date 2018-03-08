# -*- coding: utf-8 -*-

from exchangeRates import BankOfTaiwan
from datetime import datetime, tzinfo, timedelta

import urllib2

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


def update():
    print 'Start update'
    fetchFromBoT()
    print 'End update'


if __name__ == '__main__':
    update()
