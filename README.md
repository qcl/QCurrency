# QCurrency 
A simple NTD foreign exchange rates API

[![Build Status](https://travis-ci.org/qcl/QCurrency.svg?branch=master)](https://travis-ci.org/qcl/QCurrency)

QCurrency is a API for getting almost realtime NTD (New Taiwan Dollar, NT$, ISO-4217 currency cocde TWD) foreign exchange rates that [published](http://rate.bot.com.tw/) by [Bank of Taiwan](http://www.bot.com.tw/)

## Usage

To be designed.

## APIs

### Get latest exchange rates

```http
GET /latest
```

Reponse:

```json
{
	"update": 1520199621,
	"source": "Bank of Taiwan",
	"rates": {
		"USD": 29.325,
		"EUR": 36.1,
		"JPY": 0.2789
	}
}
```

## How does it work?

Basically, it's a Google App Engine instance that fetchs data and parses it from Bank of Taiwan every few minutes. 
