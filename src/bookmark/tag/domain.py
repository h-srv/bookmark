from ..infrastructure import db
from ..shared.domain import Model


# Pocket model
class Tag(Model):
    __tablename__ = 'tags'
    __table_args__ = (db.UniqueConstraint('id', 'user_rel', name='uniq_tags_id_user_rel'), )

    user_rel = db.Column(db.String(64), nullable=True)  # may be bigint or some other hash
    title = db.Column(db.String(1024), nullable=False)


class TagRepository:
    pass
