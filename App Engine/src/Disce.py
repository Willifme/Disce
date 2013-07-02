import os

import jinja2
import webapp2

from google.appengine.api import users

from Search import Search

from SearchResults import Results


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

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

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/disce', Search),
    ('/disce/results', Results)
], debug=True)