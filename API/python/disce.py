import urllib2
import simplejson

apiList = []

def getResults(apiUrl, searchQuery):

    apiRequest = urllib2.Request(apiUrl + searchQuery)

    apiResponse = urllib2.urlopen(apiRequest)

    print "User searched for: " + apiUrl + searchQuery

    apiResults = simplejson.load(apiResponse)

    apiData = apiResults['results']

    for i in apiData:

        imageUrl = i['imageUrl']

        wordnikResults = i['wordnikResults']

        wikiResults = i['wikiResults']

        apiList.append(imageUrl)

        apiList.append(wordnikResults)

        apiList.append(wikiResults)
