from flask import render_template, request
from forms import SearchForm

import flask.views
import version
import sys

sys.path.append('API/python')  # for importing modules in other folders

import disce

class Search(flask.views.MethodView):  # Class for searching

    def post(self, searchQuery): # The page for the results

        return render_template('results.html',
                                searchQuery = disce.getResults(searchQuery),
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)

    def get(self):

        form = SearchForm()

        searchQuery = request.args.get('searchQuery')

        return render_template('results.html',
                                form = form,
                                searchQuery = disce.getResults(searchQuery),
                                imageresultsPlace1 = disce.apiList[0],
                                resultsPlace1 = 'Definition: ' +  disce.apiList[1],
                                resultsPlace2 = 'Wikipedia article summary: ' + disce.apiList[2],
                                version = version.version)