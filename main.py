import os
from data import get_users_data

from flask import Flask, render_template

view_dir = os.path.abspath("./views/")
app = Flask(__name__, template_folder=view_dir)

@app.route("/")
def root():
    return render_template("index.html", username="'Ainur Rofiq")

@app.route("/users")
def users():
    users = get_users_data(15)
    print(users)
    return render_template("users.html", users=users)