"""
Bookmark flask application and middleware
"""
import os
import pymysql

from flask import Flask, current_app

from .bookmark.infrastructure import db, cors, migrate, exception_handler
from .bookmark.tag import blueprint_tag

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
    app.config['TESTING'] = True

    db.init_app(app)  # setup db
    cors.init_app(app)  # setup cors
    migrate.init_app(app, db)  # setup migrate

    app.register_blueprint(blueprint_tag, url_prefix='/api/v1/tags')

    app.register_error_handler(Exception, exception_handler)

    return app

