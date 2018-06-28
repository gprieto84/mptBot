import os
from flask import Flask

application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])

from app import routes