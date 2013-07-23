import urllib2
import simplejson

apiList = []

def getResults(searchQuery):

    apiUrl = "http://127.0.0.1:4000/api/v1.0/"

    apiRequest = urllib2.Request(apiUrl + searchQuery)

    apiResponse = urllib2.urlopen(apiRequest)

    apiResults = simplejson.load(apiResponse)

    apiData = apiResults['results']

    for i in apiData:

        imageUrl = i['imageUrl']

        wordnikResults = i['wordnikResults']

        wikiResults = i['wikiResults']

        apiList.append(imageUrl)

        apiList.append(wordnikResults)

        apiList.append(wikiResults)

    apiList[0] = imageUrl # Removes the previous entry so this list does not exponentially expand every time something is searched

    apiList[1] = wordnikResults # Removes the previous entry so this list does not exponentially expand every time something is searched

    apiList[2] = wikiResults # Removes the previous entry so this list does not exponentially expand every time something is searched
