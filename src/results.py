from flask import render_template, request, Request
from forms import SearchForm

import flask.views
import version
import sys

sys.path.append('API/python')  # for importing modules in other folders

import disce

class Search(flask.views.MethodView):  # Class for searching

    def searchDisce(self,searchQueryURL):

        searchqueryProcessed = searchQueryURL

        searchqueryProcessed = searchqueryProcessed.replace(" ", "%20")

        disce.getResults(searchqueryProcessed)

        searchqueryProcessed = searchqueryProcessed.replace("%20", " ")

        return searchqueryProcessed

    def post(self): # The page for the results

        searchQuery = request.form['searchQuery']

        searchqueryProcessed = self.searchDisce(searchQuery)

        print "test"

        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                imageResults =  disce.apiList[0],
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)

    def get(self):

        print "test"

        form = SearchForm()

        searchQuery = request.args.get('searchQuery')

        searchqueryProcessed = self.searchDisce(searchQuery)

        searchqueryProcessed = searchqueryProcessed.replace("?", "")

        return render_template('results.html',
                                form = form,
                                searchQuery = searchqueryProcessed,
                                imageResults =  disce.apiList[0],
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)