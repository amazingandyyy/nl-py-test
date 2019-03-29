flask: . ./bin/activate
	pip install -r ./app/requirements.txt
	FLASK_APP=./app/start.py flask run

newrelic: FLASK_APP=start.py NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program flask run