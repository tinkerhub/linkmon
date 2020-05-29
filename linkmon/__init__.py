import os
from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(os.environ['APP_SETTINGS'])
from linkmon.config import *
from linkmon.service import *
