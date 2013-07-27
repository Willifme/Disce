from flask import render_template, request

import flask.views
import version
import sys

sys.path.append('API/python')  # for importing modules in other folders

import disce

class DirectURLInput(flask.views.MethodView):

    def get(self, searchQuery):

        return render_template('results.html',
                                searchQuery = disce.getResults(searchQuery),
                                resultsPlace1 = disce.apiList[0],
                                resultsPlace2 = 'Definition: ' + disce.apiList[1],
                                resultsPlace3 = 'Wikipedia article summary: ' + disce.apiList[2],
                                resultsPlace4 = 'Google Images results: ',
                                version = version.version)

class MainResults(flask.views.MethodView):  # Class for searching

    def post(self): # The page for the results

        searchQuery = request.form['searchQuery']

        return render_template('results.html',
                                searchQuery = disce.getResults(searchQuery),
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)

    def get(self):

        try:

            searchQuery = request.args.get('searchQuery')

            return render_template('results.html',
                                    searchQuery = disce.getResults(searchQuery),
                                    resultsPlace1 = disce.apiList[0],
                                    resultsPlace2 = 'Definition: ' +  disce.apiList[1],
                                    resultsPlace3 = 'Wikipedia article summary: ' + disce.apiList[2],
                                    resultsPlace4 = 'Google Images results: ',
                                    cleanURL = 'http://0.0.0.0:5000/search/' + searchQuery,
                                    version = version.version)

        except AttributeError:

            return render_template('search.html')