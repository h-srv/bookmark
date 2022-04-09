"""
Bookmark flask application and middleware
"""
import os
import pymysql

from .bookmark.health_check import api as health_check_api
from .bookmark.infrastructure import db, cors, migrate
from .bookmark.tag.api import store as tag_store
from flask import Flask, g

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

    routes(app)  # load routes

    with app.app_context():
        g.db = db

    return app


def routes(app: Flask) -> None:
    """
    setup routes
    :param app:
    :return:
    """
    app.add_url_rule('/api/v1/health', view_func=health_check_api, methods=['GET'])
    app.add_url_rule('/api/v1/pockets', view_func=tag_store, methods=['POST'])
