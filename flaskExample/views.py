"""
Routes and views for the flask application.
"""

from datetime import datetime
from flaskExample import app
from flask import render_template

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    """Renders the home page."""
    return render_template("home.html", title="Home", year=datetime.now().year)


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html", title="Login", year=datetime.now().year)


@app.route('/logout', methods=['GET'])
def logout():
    return "logout"
