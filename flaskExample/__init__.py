#!/usr/bin/env python

import os
from flask import Flask
import uuid


app = Flask(__name__)
app.secret_key = str(uuid.uuid4())

app_root = os.path.dirname(os.path.abspath(__file__))
app_configuration_path = os.path.join(app_root, 'static', 'configurations')

from flaskExample import program
program.main()

from flaskExample import views