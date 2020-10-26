from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app

from app.forms import LoginForm, RegisterForm
from app.actions import CreateUser
from app.models import UserModel



@app.route("/")
def home():
    return "Welcome to home page!"


@app.route('/login', methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('account'))
    

    form = LoginForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()
        if user is None and user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('account'))
    return render_template('login.html', form=form)



@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    user_create = CreateUser()

    if form.validate_on_submit():
        result = user_create.create(
            name = form.name.data,
            surname = form.surname.data,
            username = form.username.data,
            mail = form.mail.data,
            password = form.password.data
        )

        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route("/account")
@login_required
def account():
    return f"Hello {current_user.username}!"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
