# QCurrency 
A simple NTD foreign exchange rates API

[![Build Status](https://travis-ci.org/qcl/QCurrency.svg?branch=master)](https://travis-ci.org/qcl/QCurrency)

QCurrency is a API for getting almost realtime NTD (New Taiwan Dollar, NT$, ISO-4217 currency cocde TWD) foreign exchange rates that [published](http://rate.bot.com.tw/) by [Bank of Taiwan](http://www.bot.com.tw/)

## Usage

### Directly use HTTP GET
```HTTP
GET API_ENDPOINT/latest
```

Then you will get the exchange rates response JSON object. See [APIs](#apis) for more infromation and excample.

## APIs

API endpoint: `https://qcurrency-exchange-rates.appspot.com/api`. You can also use this repository to build your own API server.

### Get latest exchange rates

```http
GET /latest
```

#### Response

- update: string, update time in ISO 8601 format.
- source: string, name of soure.
- rates: dictionary, currency name string in ISO 4217 to as key, and exchange rate in float as value.

#### Sample response

```json
{
	"update": "2018-03-09T16:15:00+08:00",
	"source": "Bank of Taiwan",
	"rates": {
		"THB": 0.9586,
		"ZAR": 2.5,
		"GBP": 40.73,
		"NZD": 21.42,
		"CHF": 30.92,
		"CNY": 4.647,
		"JPY": 0.2765,
		"USD": 29.34,
		"SGD": 22.32,
		"HKD": 3.766,
		"SEK": 3.6,
		"CAD": 22.86,
		"AUD": 22.97,
		"EUR": 36.27
	}
}
```

## How does it work?

Basically, it's a Google App Engine instance that fetchs data and parses it from Bank of Taiwan every few minutes. 

## Develop

### Google Cloud SDK

Install [Google Cloud SDK](https://cloud.google.com/sdk/downloads), so that you can start use `gcloud` commands.

After installation, [install app engine component](https://cloud.google.com/appengine/docs/standard/python/download).

```
$ gcloud components install app-engine-python
```

If you already have `gcloud`, you can also update it.

```
$ gcloud components update
```

### Python2.7

Dou to Google App Engine Python Standard Enviroment use `python2.7` as its python version. If the default `python` command in your computer (e.g. Using homebrew python on a Mac) is Python 3, please modify enviroment variable or `$PATH` to make `pathon2.7` as default one to make sure it will use `python2.7` to execute scroipt like `dev_appserver.py`.

You can also check `Makefile` for some useful command to help you developing.

### Run local app engine 

```
$ dev_appserver.py app.yaml
```

Then it will start a local app engine server for developing and testing.

### Run test cases
```
$ python2.7 -m pytest tests/
```

### Depoly

```
$ gcloud app depoly --project=APP_ENGINE_PROJECT_NAME
```

### Deploy cron job
```
$ gcloud app depoly cron.yaml --project=APP_ENGINE_PROJECT_NAME 
```
