from flask import Flask
from flask.ext import restful
from WikipediaBase import WikiQueryResults
from GoogleImagesBase import GoogleImageResults
from urllib2 import HTTPError

import WordnikBase

app = Flask(__name__)
api = restful.Api(app, catch_all_404s=True)

class QueryResults(restful.Resource):

    @staticmethod
    def get(searchQuery):

        try:

            wordnikResults = WordnikBase.wordApi.getDefinitions(searchQuery, partOfSpeech='',  sourceDictionaries='all', limit=200)[0].text

            wikiResults = WikiQueryResults.wikiqueryresults(searchQuery)

        except TypeError or IndexError or HTTPError:

            wordnikResults = "No Wordnik definition found"

            wikiResults = "No Wikipedia results found"

        results = [

            {

                "imageUrl" : GoogleImageResults.googleimageresults(searchQuery),

                "wordnikResults" : wordnikResults,

                "wikiResults" :  wikiResults
            }

    ]
        return { "results" : results }

api.add_resource(QueryResults, "/api/v1.0/<string:searchQuery>")

if __name__ == '__main__':
    app.run(debug = True, port = 4000, host = '0.0.0.0')