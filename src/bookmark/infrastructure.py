from cerberus import Validator
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
validator = Validator()


def exception_handler(ex):
    (message, code) = ex.args
    msg = dict(message=message)

    from flask import current_app
    if current_app.testing:
        import traceback
        msg = msg | dict(traceback=traceback.format_exc())

    return msg, code
