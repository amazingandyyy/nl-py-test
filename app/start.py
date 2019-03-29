from flask import Flask
import newrelic.agent
app = Flask(__name__)

@app.route("/")
def hello():
    newrelic.agent.initialize('./newrelic.ini')
    TEST_EVENT_TYPE = 'testEventType'
    application = newrelic.agent.application()
    newrelic.agent.record_custom_event(TEST_EVENT_TYPE, {'id': '123'}, application)
    return "Hello World!"