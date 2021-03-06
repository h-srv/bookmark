from abc import ABC, abstractmethod

from ..infrastructure import db


class Model(db.Model):
    """
    Base model
    """
    __abstract__ = True

    id = db.Column(db.BigInteger, primary_key=True)
    created_at = db.Column(db.DateTime,
                           nullable=True,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime,
                           nullable=True,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())


class Repository(ABC):
    """
    Base repository
    """
    @staticmethod
    def create_or_fail(mdlCls, data_dict) -> Model:
        mdl = mdlCls(**data_dict)
        db.session.add(mdl)
        db.session.commit()
        return mdl

    @staticmethod
    @abstractmethod
    def get_where(conditions): pass
