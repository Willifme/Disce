from flask import render_template, request

import flask.views
import version

class Index(flask.views.MethodView): # Class for index

    def get(self):

        return render_template('index.html',
                                version = version.version)

    def post(self):
        return render_template('index.html',
                                version = version.version)

