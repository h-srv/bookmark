from typing import Union

from ..infrastructure import db, ma
from ..shared.domain import Model, Repository


class Tag(Model):
    """
    Tag model
    """
    __tablename__ = 'tags'
    __table_args__ = (db.UniqueConstraint('id', 'user_rel', name='uniq_tags_id_user_rel'),)

    user_rel = db.Column(db.String(64), nullable=True)  # may be bigint or some other hash
    title = db.Column(db.String(1024), nullable=False)


class TagRepository(Repository):
    """
    Tag repo
    """

    @staticmethod
    def get_where(conditions: dict) -> Union[list[Tag], None]:
        return Tag.query.filter_by(**conditions).all()


class TagSchema(ma.SQLAlchemySchema):
    """DTO for tag"""
    class Meta:
        model=Tag

    id = ma.auto_field()
    title = ma.auto_field()
    user_rel = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()