flask: . ./bin/activate
	pip install -r ./app/requirements.txt
	FLASK_APP=./app/start.py flask run