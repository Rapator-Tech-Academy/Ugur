from flask import render_template
from app import app

@app.route("/")
def mainPage():
    user = {
        "name" : "Ugur",
        "surname" : "Guliyev",
        "age" : 18
    }
    return render_template("index.html", user=user)

@app.route("/contact")
def contactPage():
    address = {
        "building" : "Elektron hökümət (E-gov)",
        "floor" : "1-ci mərtəbə",
        "street" : "19 Atatürk prospekti",
        "postal_adress" : "Bakı 1069"
    }
    return render_template("contact_page.html", adress = address)