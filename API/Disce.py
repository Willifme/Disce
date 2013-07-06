from flask import Flask, jsonify

import WikipediaBase

app = Flask(__name__)

class QueryResults():

    @app.route('/api/v1.0', methods = ['GET'])
    def queryresults():

        results = [

            {
                "wikiResults" : WikipediaBase.wikiArticle.summary.decode('utf-8')
            }

    ]
        return jsonify( { 'results' : results } )

if __name__ == '__main__':
    app.run(debug = True)