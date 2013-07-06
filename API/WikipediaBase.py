from wikiapi import WikiApi

class WikiQueryResults():

    @staticmethod
    def wikiqueryresults(searchQuery):

        wiki = WikiApi({})

        wiki = WikiApi({ 'locale' : 'en' }) # Top specify your locale, 'en' is default

        wikiSearch = wiki.find(searchQuery)

        wikiArticle = wiki.get_article(wikiSearch[0])

        return wikiArticle.summary