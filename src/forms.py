from flask.ext.wtf import Form, TextField

class SearchForm(Form):

    searchQuery = TextField('searchQuery')