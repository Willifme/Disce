import urllib2
import simplejson

class GoogleImageResults():

    @staticmethod
    def googleimageresults(searchQuery):

        searchQuery = searchQuery.replace(" ", "%20")

        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
        'v=1.0&q=' + searchQuery + '&imgsz=small|medium|large')


        imageRequest = urllib2.Request(url, None, {'Referer': 'localhost'})

        imageResponse = urllib2.urlopen(imageRequest)

        imageResults = simplejson.load(imageResponse)

        data = imageResults['responseData']

        imagehits = data['results']

        for h in imagehits:

            urllist = []

            imageUrl = h['url']

            urllist.append(imageUrl) # TODO: Get more than one image

        try:

            return urllist[0]

        except UnboundLocalError:

            return "No Google Images results found"