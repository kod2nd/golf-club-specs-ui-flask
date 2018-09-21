from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from golf_spec_ui import views

app.config.from_object('config')