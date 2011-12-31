__author__ = 'rbastian'

from game import app

from flask import render_template, flash, url_for, redirect

from google.appengine.api import users

@app.route('/')
def hello_world():
    return 'hello world'
