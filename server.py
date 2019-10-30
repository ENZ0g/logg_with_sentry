from bottle import route, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
import os


sentry_sdk.init(
    dsn="https://d06396132ee848b3a833516f1e2534cf@sentry.io/1802010",
    integrations=[BottleIntegration()]
)


@route('/success')
def success():
    return 'Request is ok'


@route('/fail')
def fail():
    raise RuntimeError


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost',
        port=8080)
