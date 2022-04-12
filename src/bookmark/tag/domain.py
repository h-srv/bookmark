from ..infrastructure import db
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
    pass


class TagDTO:
    """DTO for tag"""
    @staticmethod
    def to_tag(tag) -> Tag:
        return Tag(
            title=tag.get('title'),
            user_rel=tag.get('user_rel')
        )
