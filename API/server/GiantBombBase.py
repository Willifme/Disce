import sys

sys.path.append('giantbomb')  # for importing modules in other folders

from giantbomb import giantbomb  # the 'giantbomb' module is in the src folder

giantBomb = giantbomb.Api("8b696cf1b3bd34411ad61fe5abf3aae480ebe3e4")

results = giantBomb.search('Yogventures')

test = giantBomb.getGame(results[0])

for i in test.deck:

    print str(i.decode)

#print test