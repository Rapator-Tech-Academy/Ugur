from flask import render_template, flash, redirect
from app import app

from app.forms import AddUserForms
from app.actions import CreateUser
from app.repository import Repository

repo = Repository()

@app.route("/")
def mainPage():
    all_users = repo.get_all_user()

    return render_template("home.html", users=all_users)


@app.route("/createuser", methods=["GET", "POST"])
def userCreationPage():
    add_user = CreateUser()
    add_user.repo = repo
    form = AddUserForms()

    if form.validate_on_submit():
        result = add_user.create(
            name = form.name.data,
            surname = form.surname.data,
            age = form.age.data, 
            address = form.address.data
        )
        flash(f"User created {result}")
        return redirect("/")

    return render_template("forms.html", form=form)
