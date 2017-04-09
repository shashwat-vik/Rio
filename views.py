from app import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("first_page.html")

@app.route("/a")
def all_rounds():
    return render_template("all_rounds.html")

@app.route("/1")
def round_1():
    return render_template("round_1.html")

@app.route("/2")
def round_2():
    return render_template("round_2.html")
