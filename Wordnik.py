#!/usr/bin/env python

from wordnik import *

apiUrl = 'http://api.wordnik.com/v4'

apiKey = '2027a52c68f211b1363050d094c008da6478757f13f96727b'

client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)

def getDefinition(searchString):

    print "Take reference at www.wordnik.com for proper spelling.Wordnik has a weird captial thing going on."

    definitions = wordApi.getDefinitions(searchString,
                                         partOfSpeech='',
                                         sourceDictionaries='all',
                                         limit=200)

    print definitions[0].text