import sys
print(sys.path)


# ----------------------------------
# flask application and middleware
# ----------------------------------
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# CORS
CORS(app)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = '{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(**os.environ)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Migration
migrate = Migrate(app, db)

# from .bookmark.tag.domain import Pocket

# ----------------------------------
# setup routes
# ----------------------------------
from .bookmark.health_check import api as health_check_api
from .bookmark.tag.api import store as tag_store

app.add_url_rule('/health', view_func=health_check_api, methods=['GET'])
app.add_url_rule('/pockets', view_func=tag_store, methods=['POST'])
