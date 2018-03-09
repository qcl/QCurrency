PROJECT_NAME = 'qcurrency-exchange-rates'


run_dev_server:
	# force to use system's default python rather than homebrew's
	export PATH=/usr/bin:$(PATH); dev_appserver.py app.yaml;

deploy:
	gcloud app deploy --project=$(PROJECT_NAME)

deploy_cron:
	gcloud app deploy cron.yaml --project=${PROJECT_NAME}

test:
	python2.7 -m pytest tests

clean:
	rm -f *.pyc
	rm -f app/*.pyc
