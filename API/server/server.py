from flask import Flask, jsonify, views, render_template
from WikipediaBase import WikiQueryResults
from GoogleImagesBase import GoogleImageResults

import WordnikBase

app = Flask(__name__)

class QueryResults(views.MethodView):

    def getResults(self, searchQuery):

	try:

            wordnikResults = WordnikBase.wordApi.getDefinitions(searchQuery, partOfSpeech='',  sourceDictionaries='all', limit=200)[0].text

            wikiResults = WikiQueryResults.wikiqueryresults(searchQuery)

	    imageURL = GoogleImageResults.googleimageresults(searchQuery)

        except TypeError or IndexError or UnboundLocalError or simplejson.JSONDecodeError:

	    imageURL = "UnboundLocalError - No Google Images URL found"

            wordnikResults = "No Wordnik definition found"

            wikiResults = "No Wikipedia results found"

            print "JSON could not be decoded I wonder why?"

        results = [

            {

		"imageURL" : imageURL,

		"wordnikResults" : wordnikResults,

		"wikiResults" :  wikiResults

            }

        ]

	return results

    def get(self, searchQuery):

	"""searchQueryimageURL= request.args.get("imageURL", "", type=str)

	searchQuerywordnikResults = request.args.get("wordnikResults", "", type=str) For later usage if seperate results are needed from different sources in a requests like way

	searchQuerywikiResults = request.args.get("wikiResults", "", type=str)"""

	return jsonify(results = self.getResults(searchQuery))

@app.route("/dev/jstest")
def JSONTest():

	return render_template("index.html")

app.add_url_rule("/<string:searchQuery>",
                 view_func=QueryResults.as_view("queryresults"),
                 methods=["GET"])

if __name__ == "__main__":

    app.run(debug = True, port = 4000)
