import sys

from flask import Flask

sys.path.append('src')  # for importing modules in other folders

#from search import Search  # the 'search' module is in the src folder

import results

from changelog import Changelog # the 'changelog' module is in the src folder

from index import Index

app = Flask(__name__)

app.config.from_object('config')

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET', 'POST'])

app.add_url_rule('/changelog',
                view_func=Changelog.as_view('changelog'),
                methods=['GET'])

app.add_url_rule('/search',
                view_func=results.MainResults.as_view('results'),
                methods=['GET', 'POST'])

app.add_url_rule('/search/<searchQuery>',
                 view_func=results.DirectURLInput.as_view('optionalresults'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
