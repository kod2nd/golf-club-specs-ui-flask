from flask import Flask
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__, instance_relative_config=True)
Bootstrap(app)

from golf_spec_ui import views

app.config.from_object('config')
app.config['API_URL'] = os.getenv('API_URL')