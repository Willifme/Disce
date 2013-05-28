import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import Wordnik

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

DEFAULT_SEARCH_NAME = 'searchterm_name'


# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def searchterm_key(searchterm_name=DEFAULT_SEARCH_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Search', searchterm_name)

class Search(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)

#class MainPage(webapp2.RequestHandler):

    #def get(self):

    #    template = JINJA_ENVIRONMENT.get_template('index.html')
   #     self.response.write(template.render(template_values))
        
class Disce(webapp2.RequestHandler):
    
    def get(self):
        
        disce_values = {
            
            
        }
        template = JINJA_ENVIRONMENT.get_template('disce.html')
        
        self.response.write(template.render(disce_values))
    
    def post(self):
    
        self.response.headers['Content-Type'] = 'text/plain'
    
        self.response.write('Take reference at www.wordnik.com for proper spelling.Wordnik has a weird captial thing going on.\n')
        
        search = Search(parent=searchterm_key('searchterm_name'))
        
        search.content = self.request.get('searchQuery')
        
        definitions = Wordnik.wordApi.getDefinitions(search.content,
                                            partOfSpeech='',
                                            sourceDictionaries='all',
                                            limit=200)
        
        self.response.write(definitions[0].text+"\n")

application = webapp2.WSGIApplication([
    ('/', Disce),
    ('/disce', Disce)
], debug=True)