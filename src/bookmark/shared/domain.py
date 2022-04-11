from ..infrastructure import db


# Pocket model
class Model(db.Model):
    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime,
                           nullable=True,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           nullable=True,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
