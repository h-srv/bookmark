from dataclasses import dataclass
from datetime import datetime
from typing import Union

from ..infrastructure import db
from ..shared.domain import Model, Repository


@dataclass
class Tag(Model):
    """
    Tag model
    """
    __tablename__ = 'tags'
    __table_args__ = (db.UniqueConstraint('title', 'user_rel', name='uniq_title_user_rel'), )

    id: int
    created_at: datetime
    updated_at: datetime
    user_rel: str = db.Column(db.String(64), nullable=True)  # may be bigint or some other hash
    title: str = db.Column(db.String(128), nullable=False)


class TagRepository(Repository):
    """
    Tag repo
    """

    @staticmethod
    def get_where(conditions: dict) -> Union[list[Tag], None]:
        return Tag.query.filter_by(**conditions).all()
