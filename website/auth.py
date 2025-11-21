from flask import Blueprint, render_template, flash, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route("/")
@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("routes.dashboard"))
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        existing_user = User.query.filter_by(email=email).first()
        existing_username = User.query.filter_by(username=username).first()

        errors = False

        if existing_user:
            flash("Email already exists. Please sign in instead.", category="error")
            return redirect(url_for("auth.signup"))

        if existing_username:
            flash("Username already exists. Try a different one.", category="error")
            return redirect(url_for("auth.signup"))

        if len(username) < 4:
            flash("Username must be greater than 4 characters", category="error")
            errors = True

        if len(email) < 6:
            flash("Email must be greater than 6 characters", category="error")
            errors = True

        if password1 != password2:
            flash("Sorry your passwords don't match, try again", category="error")
            errors = True

        if len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
            errors = True

        if errors:
            return redirect(url_for("auth.signup"))

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password1, method="pbkdf2:sha256"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)

        flash(
            "Congrats, your account has been created successfully", category="success"
        )
        return redirect(url_for("routes.products"))

    return render_template("sign_up.html", title="Sign Up")


@auth.route("/sign-in", methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("routes.products"))
    if request.method == "POST":
        identifier = request.form.get("identifier")
        password = request.form.get("password")

        user = User.query.filter(
            (User.username == identifier) | (User.email == identifier)
        ).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Logged in successfully!", category="success")
                return redirect(url_for("routes.products"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("User not found.", category="error")

    return render_template("sign_in.html", title="Sign In")


@auth.route("/sign-out")
@login_required
def signout():
    logout_user()
    return redirect(url_for("auth.signin"))
