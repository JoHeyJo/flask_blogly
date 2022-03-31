"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.get("/")
def show_home():
    """display all users"""
    users = User.query.all()
    return render_template("index.html", users=users)

@app.get("/users")
def show_users():
    """render index page"""
    users = User.query.all()
    return render_template("index.html", users=users)

@app.get("/users/new")
def show_new_user_form():
    """render new user form"""
    return render_template("new_user_form.html")


@app.post("/users/new")
def add_user():
    """grab user form data, cerate user instance and commit instance to db, redirect back to /users"""
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    img_url = request.form["img-url"]

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect("/users")

@app.get("/users/<int:user_id>")
def show_user(user_id):
    """ render user """
    user = User.query.get_or_404(user_id)
    return render_template("user_detail.html", user=user)

@app.get("/users/<int:user_id>/edit")
def show_edit_user(user_id):
    """show edit user form for specific user"""
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)

@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):
    """grab data from user form, update user, commmit changes to db. render updated user"""
    
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    img_url = request.form["img-url"]
        
    user = User.query.get_or_404(user_id)

    if first_name == "":
        first_name = user.first_name
    else:
        user.first_name = first_name

    if last_name == "":
        last_name = user.last_name
    else:
        user.last_name = last_name

    if img_url == "":
        img_url = user.img_url
    else:
        user.img_url = img_url

    db.session.commit()

    return redirect('/users')


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """fetch them delete them redirect them """
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/')
    # users = User.query.all()
    # return render_template("index.html", users=users)
