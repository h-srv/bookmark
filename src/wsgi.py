"""
Bookmark flask application and middleware
"""
import os
import pymysql

from .bookmark.infrastructure import db, cors, migrate, api, ma
from .bookmark.tag.api import tag_ns
from flask import Flask

pymysql.install_as_MySQLdb()


def create_app() -> Flask:
    """
    Create app
    :return:
    """
    app = Flask(__name__, static_folder=None)

    # load db config and init db
    app.config['SQLALCHEMY_DATABASE_URI'] = '{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(**os.environ)
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)  # setup db
    cors.init_app(app)  # setup cors
    migrate.init_app(app, db)  # setup migrate
    api.init_app(app)  # setup api
    ma.init_app(app)  # setup marshmallow

    load_api_ns(api)

    return app


def load_api_ns(api):
    api.add_namespace(tag_ns)
