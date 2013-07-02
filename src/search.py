from flask import render_template, request

import flask.views
import wordnikbase
import version
import urllib2
import simplejson
import time

class Search(flask.views.MethodView):  # Class for searching

    def get(self): # The main search page

        return render_template('index.html', version = version.version)

    def post(self): # The page for the results

        searchQuery = request.form['searchQuery']

        searchqueryProcessed = searchQuery

        definitionSearch = wordnikbase.wordApi.getDefinitions(searchqueryProcessed,
                                                        partOfSpeech='',
                                                        sourceDictionaries='all',
                                                        limit=200)


        searchqueryProcessedreplaced = searchqueryProcessed

        searchqueryProcessedreplaced = searchqueryProcessedreplaced.replace(" ", "%20")

        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
              'v=1.0&q=' + searchqueryProcessedreplaced + '&imgsz=small|medium|large')

        imageRequest = urllib2.Request(url, None, {'Referer': 'localhost'})

        imageResponse = urllib2.urlopen(imageRequest)

        imageResults = simplejson.load(imageResponse)

        data = imageResults['responseData']

        imagehits = data['results']

        for h in imagehits:

            urllist = []

            test = h['url']

            urllist.append(test) # TODO: Get more than one image


        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                definitionResults =  definitionSearch[0].text,
                                imageResults = urllist[0])
