#!/usr/bin/env python

from wordnik import *

import webapp2

apiUrl = 'http://api.wordnik.com/v4'

apiKey = '2027a52c68f211b1363050d094c008da6478757f13f96727b'

client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)

class Definition(webapp2.RequestHandler):

    def get(self):

        webapp2.response.headers['Content-Type'] = 'text/plain'
        
        self.write('Take reference at www.wordnik.com for proper spelling.Wordnik has a weird captial thing going on.')
        
        definitions = wordApi.getDefinitions('badger',
                                            partOfSpeech='',
                                            sourceDictionaries='all',
                                            limit=200)
        
        response.write(definitions[0].text)