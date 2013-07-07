from flask import render_template, request
from flask.ext import restful

import flask.views
import wordnikbase
import version
import urllib2
import simplejson
import sys

sys.path.append('API')  # for importing modules in other folders

from Disce import QueryResults

class Search(flask.views.MethodView):  # Class for searching

    def get(self): # The main search page

        return render_template('index.html', version = version.version)

    def post(self): # The page for the results

        searchQuery = request.form['searchQuery']

        searchqueryProcessed = searchQuery

   #     QueryResults.get('dog')

        definitionSearch = wordnikbase.wordApi.getDefinitions(searchqueryProcessed,
                                                        partOfSpeech='',
                                                        sourceDictionaries='all',
                                                        limit=200)


        searchqueryProcessedreplaced = searchqueryProcessed

        searchqueryProcessedreplaced = searchqueryProcessedreplaced.replace(" ", "%20")

  #      url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
   #           'v=1.0&q=' + searchqueryProcessedreplaced + '&imgsz=small|medium|large')

        apiUrl = 'http://127.0.0.1:4000/api/v1.0/' + searchqueryProcessedreplaced

        apiRequest = urllib2.Request(apiUrl)

        apiResponse = urllib2.urlopen(apiRequest)

        apiResults = simplejson.load(apiResponse)

        apiData = apiResults["results"]

        for i in apiData:

            apiList = []

            imageUrl = i["imageUrl"]

            wordnikResults = i["wordnikResults"]

            wikiResults = i["wikiResults"]

            apiList.append(imageUrl)

            apiList.append(wordnikResults)

            apiList.append(wikiResults)

    #    imageRequest = urllib2.Request(url, None, {'Referer': 'localhost'})

     #   imageResponse = urllib2.urlopen(imageRequest)

      #  imageResults = simplejson.load(imageResponse)

       # data = imageResults['results']

 #       imagehits = data['results']

        #for h in data:

         #   urllist = []

          #  test = h['imageUrl']

           # urllist.append(test) # TODO: Get more than one image


        return render_template('results.html',
                                searchQuery = searchqueryProcessed,
                                definitionResults =  apiList[1],
                                wikipediaResults = apiList[2],
                                imageResults = apiList[0],
                                version = version.version)
