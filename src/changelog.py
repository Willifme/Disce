from flask import render_template

import flask.views
import version

class Changelog(flask.views.MethodView): # Class for changelog

    def get(self):
        return render_template('changelog.html',
                                version = version.version)