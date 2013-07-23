from flask import render_template, request, Request

import flask.views
import version
import sys

sys.path.append('API/python')  # for importing modules in other folders

import disce

class Search(flask.views.MethodView):  # Class for searching

    def searchDisce(self,searchQueryURL):

        searchqueryProcessed = searchQueryURL

        searchqueryProcessed = searchqueryProcessed.replace(" ", "%20")

        disce.getResults("http://127.0.0.1:4000/api/v1.0/", searchqueryProcessed)

        searchqueryProcessed = searchqueryProcessed.replace("%20", " ")

        print searchqueryProcessed

        return searchqueryProcessed

    def post(self, searchQuery): # The page for the results

        searchqueryProcessed = self.searchDisce(searchQuery)

        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                imageResults =  disce.apiList[0],
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)

    def get(self, searchQuery):

        searchqueryProcessed = self.searchDisce(searchQuery)

        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                imageResults =  disce.apiList[0],
                                definitionResults = disce.apiList[1],
                                wikipediaResults = disce.apiList[2],
                                version = version.version)