# nl-py-test

> newrelic python agent testing

## Preparation

change your own license key in `app/newrelic.ini`

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