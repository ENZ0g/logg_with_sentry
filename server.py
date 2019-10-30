from bottle import route, run
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
import os


sentry_sdk.init(
    dsn=os.environ.get('DSN'),
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
