from flask import Flask
import newrelic.agent
import datetime

app = Flask(__name__)
newrelic.agent.initialize('./newrelic.ini')

# Apparently doesn't work for non-web transactions:
# newrelic.agent.record_custom_event('testEventType', {'id': '123'}, application)
# DOCS for non-web trnasactions:
# https://docs.newrelic.com/docs/agents/python-agent/supported-features/python-background-tasks

@app.route("/")
def hello():
    time=str(datetime.datetime.now())
    return call(time)

@newrelic.agent.background_task()
def call(task_name):
    # with newrelic.agent.BackgroundTask(name=task_name, group='My Time'):
    # This will throw
    # raise RuntimeError('transaction already active')
    return task_name