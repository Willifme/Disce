# -*- coding: utf-8 -*-

from flask import render_template

import flask.views
import version

class Homework(flask.views.MethodView): # Class for homework

    def get(self):
        return render_template('homework.html',
                                version = version.version)