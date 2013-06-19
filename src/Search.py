import os
import jinja2
import webapp2
import Wordnik

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'])

class Search(webapp2.RequestHandler):

    test = "test"
    
    def get(self):

        disce_values = {}

        template = JINJA_ENVIRONMENT.get_template('/resources/www/disce.html')

        self.response.write(template.render(disce_values))

    @staticmethod
    def post(self):

        self.response.headers['Content-Type'] = 'text/plain'

        test = "test"

        self.response.write('Take reference at www.wordnik.com for proper spelling.Wordnik has a weird captial thing going on.\n you should not be able to see this!')

        self.redirect('/disce/results')

        searchQuery = self.request.get('searchQuery')

        definitions = Wordnik.wordApi.getDefinitions(searchQuery,
                                                     partOfSpeech='',
                                                     sourceDictionaries='all',
                                                     limit=200)
