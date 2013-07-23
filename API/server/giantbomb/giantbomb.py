import urllib2


__author__ = "Leandro Voltolino <xupisco@gmail.com>"
__version__ = "0.7"

try:
    import simplejson
except ImportError:
    try:
        import json as simplejson
    except ImportError:
        try:
            from django.utils import simplejson
        except:
            raise Exception("GiantBomb wrapper requires the simplejson library (or Python 2.6) to work. http://www.undefined.org/python/")


class GiantBombError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.giantbomb.com/'

    @staticmethod
    def defaultRepr(obj):
        return unicode("<%s: %s>" % (obj.id, obj.name)).encode('utf-8')

    def checkResponse(self, resp):
        if resp['status_code'] == 1:
            return resp['results']
        else:
            raise GiantBombError('Error code %s: %s' % (resp['status_code'], resp['error']))

    def search(self, query, offset=0):
        results = simplejson.load(urllib2.urlopen(self.base_url + "/search/?api_key=%s&resources=game&query=%s&field_list=id,name,image&offset=%s&format=json" % (self.api_key, urllib2.quote(query), offset)))
        return [SearchResult.NewFromJsonDict(x) for x in self.checkResponse(results)]

    def getGame(self, id):
        if type(id).__name__ != 'int':
            id = id.id
        game = simplejson.load(urllib2.urlopen(self.base_url + "/game/%s/?api_key=%s&field_list=id,name,deck,image,images,genres,original_release_date,platforms,videos,api_detail_url,site_detail_url&format=json" % (id, self.api_key)))
        return Game.NewFromJsonDict(self.checkResponse(game))

    def getGames(self, plat, offset=0):
        if type(plat).__name__ != 'int':
            plat = plat.id
        games = simplejson.load(urllib2.urlopen(self.base_url + "/games/?api_key=%s&field_list=id,name,deck,image,images,genres,original_release_date,api_detail_url,site_detail_url&platforms=%s&offset=%s&format=json" % (self.api_key, plat, offset)))
        return [SearchResult.NewFromJsonDict(x) for x in self.checkResponse(games)]

    def getVideo(self, id):
        if type(id).__name__ != 'int':
            id = id.id
        video = simplejson.load(urllib2.urlopen(self.base_url + "/video/%s/?api_key=%s&format=json" % (id, self.api_key)))
        return Video.NewFromJsonDict(self.checkResponse(video))

    def getPlatform(self, id):
        platform = simplejson.load(urllib2.urlopen(self.base_url + "/platform/%s/?api_key=%s&&field_list=id,name,abbreviation,deck,image&format=json" % (id, self.api_key)))
        return Platform.NewFromJsonDict(self.checkResponse(platform))

    def getPlatforms(self, offset=0):
        platforms = simplejson.load(urllib2.urlopen(self.base_url + "/platforms/?api_key=%s&field_list=id,name,abbreviation,deck&offset=%s&format=json" % (self.api_key, offset)))
        return self.checkResponse(platforms)


class Game:
    def __init__(self,
                 id=None,
                 name=None,
                 deck=None,
                 platforms=None,
                 image=None,
                 images=None,
                 genres=None,
                 original_release_date=None,
                 videos=None,
                 api_detail_url=None,
                 site_detail_url=None):

        self.id = id
        self.name = name
        self.deck = deck
        self.platforms = platforms
        self.image = image
        self.images = images
        self.genres = genres
        self.original_release_date = original_release_date
        self.videos = videos
        self.api_detail_url = api_detail_url
        self.site_detail_url = site_detail_url

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Game(id=data.get('id'),
                        name=data.get('name', None),
                        deck=data.get('deck', None),
                        platforms=[Platform.NewFromJsonDict(x) for x in data.get('platforms', [])],
                        image=Image.NewFromJsonDict(data.get('image', [])),
                        images=[Image.NewFromJsonDict(x) for x in data.get('images', [])],
                        genres=[Genre.NewFromJsonDict(x) for x in data.get('genres', [])],
                        original_release_date=data.get('original_release_date', None),
                        videos=[Videos.NewFromJsonDict(x) for x in data.get('videos', [])],
                        api_detail_url=data.get('api_detail_url', None),
                        site_detail_url=data.get('site_detail_url', None))
        return None

    def __repr__(self):
        return Api.defaultRepr(self)


class Platform:
    def __init__(self,
                 id=None,
                 name=None,
                 abbreviation=None,
                 deck=None,
                 api_detail_url=None,
                 image=None):

        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.deck = deck
        self.api_detail_url = api_detail_url
        self.image = image

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Platform(id=data.get('id'),
                        name=data.get('name', None),
                        abbreviation=data.get('abbreviation', None),
                        deck=data.get('deck', None),
                        api_detail_url=data.get('api_detail_url', None),
                        image=Image.NewFromJsonDict(data.get('image', None)))
        return None

    def __repr__(self):
        return Api.defaultRepr(self)


class Image:
    def __init__(self,
                 icon=None,
                 medium=None,
                 tiny=None,
                 small=None,
                 thumb=None,
                 screen=None,
                 super=None):

        self.icon = icon
        self.medium = medium
        self.tiny = tiny
        self.small = small
        self.thumb = thumb
        self.screen = screen
        self.super = super

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Image(icon=data.get('icon_url', None),
                         medium=data.get('medium_url', None),
                         tiny=data.get('tiny_url', None),
                         small=data.get('small_url', None),
                         thumb=data.get('thumb_url', None),
                         screen=data.get('screen_url', None),
                         super=data.get('super_url', None),)
        return None


class Genre:
    def __init__(self,
                 id=None,
                 name=None,
                 api_detail_url=None):

        self.id = id
        self.name = name
        self.api_detail_url = api_detail_url

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Genre(id=data.get('id'),
                         name=data.get('name', None),
                         api_detail_url=data.get('api_detail_url', None))
        return None

    def __repr__(self):
        return Api.defaultRepr(self)


class Videos:
    def __init__(self,
                 id=None,
                 name=None,
                 deck=None,
                 image=None,
                 url=None,
                 publish_date=None):

        self.id = id
        self.name = name
        self.deck = deck
        self.image = image
        self.url = url
        self.publish_date = publish_date

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Videos(id=data.get('id'),
                         name=data.get('name', None),
                         deck=data.get('deck', None),
                         image=Image.NewFromJsonDict(data.get('image', None)),
                         url=data.get('url', None),
                         publish_date=data.get('publish_date', None),)
        return None

    def __repr__(self):
        return Api.defaultRepr(self)


class Video:
    def __init__(self,
                 id=None,
                 name=None,
                 deck=None,
                 image=None,
                 url=None,
                 publish_date=None,
                 site_detail_url=None):

        self.id = id
        self.name = name
        self.deck = deck
        self.image = image
        self.url = url
        self.publish_date = publish_date
        self.site_detail_url = site_detail_url

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return Video(id=data.get('id'),
                         name=data.get('name', None),
                         deck=data.get('deck', None),
                         image=Image.NewFromJsonDict(data.get('image', None)),
                         url=data.get('url', None),
                         publish_date=data.get('publish_date', None),
                         site_detail_url=data.get('site_detail_url', None))
        return None

    def __repr__(self):
        return Api.defaultRepr(self)


class SearchResult:
    def __init__(self,
                 id=None,
                 name=None,
                 api_detail_url=None,
                 image=None):

        self.id = id
        self.name = name
        self.api_detail_url = api_detail_url
        self.image = image

    @staticmethod
    def NewFromJsonDict(data):
        if data:
            return SearchResult(id=data.get('id'),
                                name=data.get('name', None),
                                api_detail_url=data.get('api_detail_url', None),
                                image=data.get('image', None))
        return None

    def __repr__(self):
        return Api.defaultRepr(self)
