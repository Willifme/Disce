from flask import Flask
from flask.ext import restful
from WikipediaBase import WikiQueryResults
from GoogleImagesBase import GoogleImageResults

import WordnikBase

app = Flask(__name__)
api = restful.Api(app)

class HelloWorld(restful.Resource):
    def get(self, searchQuery):
        return {'hello' : searchQuery}

api.add_resource(HelloWorld, '/<string:searchQuery>')

class QueryResults(restful.Resource):

    @staticmethod
#    @app.route('/api/v1.0/<string:searchQuery>', methods = ['GET'])
    def get(searchQuery):



        try:

            wordnikResults = WordnikBase.wordApi.getDefinitions(searchQuery, partOfSpeech='',  sourceDictionaries='all', limit=200)[0].text

            wikiResults = WikiQueryResults.wikiqueryresults(searchQuery)

        except TypeError or IndexError:

            wordnikResults = "No definition found"

            wikiResults = "No Wikipedia results"

        results = [

            {

                "imageUrl" : GoogleImageResults.googleimageresults(searchQuery),

                "wordnikResults" : wordnikResults,

                "wikiResults" :  wikiResults
            }

    ]

        return { 'results' : results }


api.add_resource(QueryResults, "/api/v1.0/<string:searchQuery>")

if __name__ == '__main__':
    app.run(debug = True, port = 4000)