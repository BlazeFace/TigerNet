from flask.ext.login import LoginManager, UserMixin
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager(app)
from TigerNet.static import views, models

