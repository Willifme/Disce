import os

import jinja2
import webapp2

from Search import Search

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class Results(webapp2.RequestHandler):

    def get(self):
        search = Search(webapp2.RequestHandler)
        url_linktext = 'test'
        disce_values = {'url_linktext': url_linktext}
        template = JINJA_ENVIRONMENT.get_template('/resources/www/results.html')

        self.response.write(template.render(disce_values))
