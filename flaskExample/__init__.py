#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

from flaskExample import program
program.main()

from flaskExample import views