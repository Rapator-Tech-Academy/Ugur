from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

from app.actions import CreateStudent


create_student = CreateStudent()


@app.route("/")
def mainPage():
    user = {
        "name" : "Ugur",
        "surname" : "Guliyev",
        "age" : 18
    }
    return render_template("index.html", user=user)

@app.route('/forms', methods=["GET", "POST"])
def formPage():
    form = LoginForm()
    if form.validate_on_submit():
        msg = f"Name: {form.name.data}, Surname: {form.surname.data}, Age: {form.age.data}, Number: {form.number.data}"
        flash(msg)
        create_student.run(
                name = form.name.data,
                surname = form.surname.data,
                age = form.age.data,
                number = form.number.data
            )
    return render_template("forms.html", form=form)