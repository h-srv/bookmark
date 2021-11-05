# ----------------------------------
# flask application and middleware
# ----------------------------------
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CORS
CORS(app)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = '{DB_DRVR}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(**os.environ)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# ----------------------------------
# setup routes
# ----------------------------------
from health_check.api import check
from pocket.api import store

app.add_url_rule(
    '/health',
    view_func=check,
    methods=['GET'])

app.add_url_rule(
    '/pockets',
    view_func=store,
    methods=['POST'])
