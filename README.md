# QCurrency 
A simple NTD foreign exchange rates API

[![Build Status](https://travis-ci.org/qcl/QCurrency.svg?branch=master)](https://travis-ci.org/qcl/QCurrency)

QCurrency is a API for getting almost realtime NTD (New Taiwan Dollar, NT$, ISO-4217 currency cocde TWD) foreign exchange rates that [published](http://rate.bot.com.tw/) by [Bank of Taiwan](http://www.bot.com.tw/)

## Usage

To be designed.

## APIs

API end point: `https://qcurrency-excahnge-rates.appspot.com/api`. You can also use this repository to build your own API server.

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

Dou to Google App Engine Python Standard Enviroment use `python2.7` as its python version. If the default `python` command in your computer (e.g. Using homebrew python on a Mac) is Python 3, then you may need use `virtualenv` to create a enviroment which using `python2.7` as default `python` command for developing and testing.

```
$ virtualenv -p PATH_TO_YOUR_PYTHON27 ENV_PATH
```

Then enter enviroment:

```
$ source ENV_PATH/bin/active
```

Use following command to leave virtual enviroment.

```
$ deactive
```

### Run local app engine 

```
$ dev_appserver.py app.yaml
```

Then it will start a local app engine server for developing and testing.

### Depoly

```
$ gcloud app depoly --project=APP_ENGINE_PROJECT_NAME
```