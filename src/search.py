from flask import render_template, request

import flask.views
import version
import sys

sys.path.append('API/python')  # for importing modules in other folders

import disce

class Search(flask.views.MethodView):  # Class for searching

    def get(self): # The main search page

        return render_template('index.html', version = version.version)

    def post(self): # The page for the results

        searchQuery = request.form['searchQuery']

        searchqueryProcessed = searchQuery

        searchqueryProcessed = searchqueryProcessed.replace(" ", "%20")

        disce.getResults("http://127.0.0.1:4000/api/v1.0/", searchqueryProcessed)

        searchqueryProcessed = searchqueryProcessed.replace("%20", " ")

        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                imageResults =  disce.apiList[0],
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)