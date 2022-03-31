"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'test'

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Creating User class w/ first_name, last_name, img"""
    __tablename__ = "users"

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False)
    last_name = db.Column(db.String(50),
                    nullable=False)
    img_url= db.Column(db.Text, nullable=True)

