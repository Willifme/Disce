from flask.ext.wtf import Form, TextField, Required

class SearchForm(Form):

    searchQuery = TextField('searchQuery', validators= [Required()])