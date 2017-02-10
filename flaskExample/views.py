"""
Routes and views for the flask application.
"""

from datetime import datetime
import os
from flaskExample import app
from flaskExample import app_configuration_path
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from oauth2client import client


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    """Renders the home page."""
    return render_template("home.html", title="Home", year=datetime.now().year)


@app.route('/login', methods=['GET'])
def login():
    try:
        if 'credentials' not in session:
            return redirect(url_for('google_oauth2callback'))
        credentials = client.OAuth2Credentials.from_json(session['credentials'])
        if credentials.access_token_expired:
            return redirect(url_for('google_oauth2callback'))
        return render_template("login.html", title="Login", year=datetime.now().year)
    except Exception as ex:
        print(ex)
        raise


@app.route('/google/oauth2callback')
def google_oauth2callback():
    flow = client.flow_from_clientsecrets(
        os.path.join(app_configuration_path, 'client_secret_local.json'),
        scope='https://www.googleapis.com/auth/gmail.readonly',
        redirect_uri=url_for('google_oauth2callback', _external=True)
    )
    if 'code' not in request.args:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)

    auth_code = request.args.get('code')
    credentials = flow.step2_exchange(auth_code)
    session['credentials'] = credentials.to_json()
    return redirect(url_for('home'))


@app.route('/logout', methods=['GET'])
def logout():
    return "logout"


@app.errorhandler(500)
def handle_internal_error_page(error):
    return render_template('page_internal_error.html', error=error)