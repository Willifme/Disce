import os

from google.appengine.api import users

import jinja2
import webapp2
import Wordnik

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

url_linktext = 'test'

class MainPage(webapp2.RequestHandler):

    def get(self):

        mainmenu_values = {}
        template = JINJA_ENVIRONMENT.get_template('/resources/www/index.html')

        self.response.write(template.render(mainmenu_values))
        user = users.get_current_user()

  #      if user:
         #   self.redirect('/disce')
   #     else:
    #        self.redirect(users.create_login_url(self.request.uri))

class Disce(webapp2.RequestHandler):


    def get(self):

        disce_values = {}

        template = JINJA_ENVIRONMENT.get_template('/resources/www/disce.html')

        self.response.write(template.render(disce_values))

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

    test = "test"

class Results(webapp2.RequestHandler):


    def get(self):
        url_linktext = 'test'
        disce_values = {'url_linktext': url_linktext}
        template = JINJA_ENVIRONMENT.get_template('/resources/www/results.html')

        self.response.write(template.render(disce_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/disce', Disce),
    ('/disce/results', Results)
], debug=True)