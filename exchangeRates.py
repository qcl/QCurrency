#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from datetime import datetime

class BankExchangeRates:
    """An Abstract class of bank object which in charge of parsing bank exchange rates raw data"""
    def __init__(self):
        raise Exception('Please subclass')

    def parse(self, fileDescriptor):
        raise Exception('Please implement it in subclass')

    @property
    def exchangeRates(self):
        return {}

    @property
    def updateTime(self):
        return datetime.fromtimestamp(0) 


class BankOfTaiwan(BankExchangeRates):
    """Bank of Taiwan"""

    def __init__(self):
        pass

    def parse(self, fileDescriptor):
        ln = 0
        rates = []
        for line in fileDescriptor:
            if ln == 0:
                ln += 1
                continue
            
            rateLine = line.split()
            if len(rateLine) > 13:
                rates.append((rateLine[0], rateLine[13]))
            ln += 1

        self.exchangeRates = dict(filter(lambda x: x[1] > 0.0 ,map(lambda x: (x[0], float(x[1])), rates)))

if __name__ == '__main__':
    # simple test
    x = BankOfTaiwan()
    f = open('./sample.exchange.rates.2018.03.02.16.01.txt', 'r')
    x.parse(f)
    print x.exchangeRates
