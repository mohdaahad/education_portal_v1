import lambda_wsgi
from mysite.wsgi import application as app
import sys


def lambda_handler(event, context):
    print(f'Invoked with Payload:: {event}')
    print(f"Available Paths:: {sys.path}")
    return lambda_wsgi.response(app, event, context)
