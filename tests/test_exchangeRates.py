#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from exchangeRates import BankOfTaiwan

expectedBoTRates = {'USD': 29.325, 'AUD': 22.83, 'CHF': 31.29, 'SEK': 3.6, 'THB': 0.9555, 'JPY': 0.2789, 'GBP': 40.53, 'NZD': 21.38, 'CNY': 4.635, 'EUR': 36.1, 'ZAR': 2.5, 'SGD': 22.26, 'HKD': 3.769, 'CAD': 22.92}

def test_parse():
    bot = BankOfTaiwan()
    f = open('./sample.exchange.rates.2018.03.02.16.01.txt', 'r')
    bot.parse(f)
    rates = bot.exchangeRates

    for currency in expectedBoTRates.keys():
        assert currency in rates
        expectedRate = expectedBoTRates[currency]
        rate = rates[currency]
        assert expectedRate == rate
