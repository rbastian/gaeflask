__author__ = 'rbastian'

from flask import Flask
import settings

app = Flask('game')
app.config.from_object('game.settings')

import views