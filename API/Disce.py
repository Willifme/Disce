from flask import Flask, jsonify
from WikipediaBase import WikiQueryResults
from GoogleImagesBase import GoogleImageResults

import WordnikBase

app = Flask(__name__)

class QueryResults():

    @staticmethod
    @app.route('/api/v1.0/<string:searchQuery>', methods = ['GET'])
    def queryresults(searchQuery):

        results = [

            {

                "imageUrl" : GoogleImageResults.googleimageresults(searchQuery),

                "wordnikResults" : WordnikBase.wordApi.getDefinitions(searchQuery, partOfSpeech='',  sourceDictionaries='all', limit=200)[0].text,

                "wikiResults" :  WikiQueryResults.wikiqueryresults(searchQuery)
            }

    ]

        print results

        return jsonify( { 'results' : results } )

if __name__ == '__main__':
    app.run(debug = True, port = 4000)