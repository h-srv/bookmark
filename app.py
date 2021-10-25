# flask application and middleware
# -------------
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


# setup routes
# -------------
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
