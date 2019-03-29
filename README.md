# nl-py-test

newrelic python agent testing

## Preparation

follow [docs](https://docs.newrelic.com/docs/agents/python-agent/installation/standard-python-agent-install) to create your `app/newrelic.ini`

```console
$ cd app
app $ newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
```

## Development

```console
$ pip install virtualenv
$ virtualenv .
$ . ./bin/activate
(nl-py-test) pip install -r ./app/requirements.txt
(nl-py-test) cd app
(nl-py-test) FLASK_APP=./start.py flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Snippets

```python
from flask import Flask
import newrelic.agent
import datetime

app = Flask(__name__)
newrelic.agent.initialize('./newrelic.ini')

# DOCS for non-web trnasactions:
# https://docs.newrelic.com/docs/agents/python-agent/supported-features/python-background-tasks

@app.route("/")
def hello():
    time=str(datetime.datetime.now())
    return call(time)

@newrelic.agent.background_task()
def call(task_name):
    return task_name
```

## Screenshots

Non-web tx works!

![image](https://i.imgur.com/dyZ7mQa.png)

## Links

New relic: https://rpm.newrelic.com/accounts/2291348/applications/268470687