from flask import render_template, request, redirect, flash, session, url_for
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods = ["POST"])
def create():
    if not user.User.validate_user(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user_id = user.User.create_user(data)
        user_in_db = user.User.get_one(user_id)
        session["logged_in_id"] = user_in_db.id
        session["logged_in_name"] = user_in_db.first_name
        return redirect (url_for("dashboard"))

@app.route("/login", methods = ["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = user.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid login.", "login")
        return redirect(url_for("index"))
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid login.", "login")
        return redirect(url_for("index"))
    session["logged_in_id"] = user_in_db.id
    session["logged_in_name"] = user_in_db.first_name
    return redirect (url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))