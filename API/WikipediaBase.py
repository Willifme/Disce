from wikiapi import WikiApi

wiki = WikiApi({})

wiki = WikiApi({ 'locale' : 'en' }) # Top specify your locale, 'en' is default

wikiSearch = wiki.find('Eiffel Tower')

wikiArticle = wiki.get_article(wikiSearch[0])