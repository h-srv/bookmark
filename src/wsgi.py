# ----------------------------------
# flask application and middleware
# ----------------------------------
import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # load db config and init db
    from .bookmark.infrastructure import db

    app.config['SQLALCHEMY_DATABASE_URI'] = '{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(**os.environ)
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)

    return app


# # CORS
# CORS(app)

# Migration
# migrate = Migrate(app, db)

# from .bookmark.tag.domain import Pocket

# ----------------------------------
# setup routes
# ----------------------------------
from .bookmark.health_check import api as health_check_api
from .bookmark.tag.api import store as tag_store

app = create_app()

app.add_url_rule('/health', view_func=health_check_api, methods=['GET'])
app.add_url_rule('/pockets', view_func=tag_store, methods=['POST'])
