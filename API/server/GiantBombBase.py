import giantbomb

giantBomb = giantbomb.giantbomb.Api("8b696cf1b3bd34411ad61fe5abf3aae480ebe3e4")

games = giantBomb.getGame(94, 12300)

print games