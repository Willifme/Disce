from flask import Flask

import sys

sys.path.append('src')  # for importing modules in other folders

from search import Search  # the 'search' module is in the src folder

from changelog import Changelog # the 'changelog' module is in the src folder

app = Flask(__name__)

app.add_url_rule('/',
                view_func=Search.as_view('search'),
                methods=['GET', 'POST'])

app.add_url_rule('/changelog',
                view_func=Changelog.as_view('changelog'),
                methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
