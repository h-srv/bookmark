from cerberus import Validator
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
validator = Validator()


def validate_or_fail(data, schema, code=422) -> bool:
    """generic data validation checker"""
    if not validator.validate(data, schema):
        raise ValueError(validator.errors, code)

    return True


def exception_handler(ex):
    """generic exception handler"""
    from sqlalchemy.exc import IntegrityError

    msg, code = {}, 500

    if type(ex) is ValueError:  # if validation error
        (message, c) = ex.args
        msg, code = dict(ok=0, message=message), c

    elif type(ex) is IntegrityError:  # if db error
        if 'Duplicate entry' in str(ex):
            msg, code = dict(ok=0, message='Duplicate entry found'), 400

    if len(msg) == 0:  # if empty msg then throw generic msg
        msg = dict(ok=0, message='Unknown system exception')

    # add traceback if debug
    from flask import current_app
    if current_app.testing:
        import traceback
        msg = msg | dict(traceback=traceback.format_exc())

    return msg, code
