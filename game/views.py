__author__ = 'rbastian'

from game import app
from json import dumps

from flask import render_template, flash, url_for, redirect

from google.appengine.api import users

@app.route('/')
def hello_world():

    json_str = dumps({ 'name':'Rob', 'age':42})
    return json_str
