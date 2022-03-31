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

    post = db.relationship('Post', backref='users')

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    first_name = db.Column(db.String(50),
                    nullable=False)
    last_name = db.Column(db.String(50),
                    nullable=False)
    img_url= db.Column(db.Text, nullable=True)

class Post(db.Model):
    """Creating Post class w/ title, content, created at timestamp, and a foreign key to User table"""
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                  primary_key=True,
                  autoincrement=True)
    title = db.Column(db.String(50),
                    nullable=False)
    content = db.Column(db.Text,
                    nullable=False)
    created_at = db.Column(db.Timestamp,
                    nullable=False)

    user_id = db.Column(db.Integer, 
                    db.ForeignKey('users.id') )