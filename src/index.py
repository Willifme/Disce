from flask import render_template, request
from forms import SearchForm

import flask.views
import version

class Index(flask.views.MethodView): # Class for index

    def get(self):

        form = SearchForm()

        return render_template('index.html',
                                form = form,
                                version = version.version)

    def post(self):

        form = SearchForm()

        return render_template('index.html',
                                form = form,
                                version = version.version)

