from app import db

# Pocket model
class Pocket(db.Model):
    __tablename__ = 'pockets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
