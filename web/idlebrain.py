#!/usr/bin/python

# Abhinay Omkar : abhiomkar AT gmail DOT com
# http://abhiomkar.in

import web
import sys

sys.path.append(sys.path[0] + '/../config')

import idlebrain_mobile_config as config

urls = (
    '/',                'IdlebrainIndex',
    '/latest/',         'IdlebrainLatestUpdates',
    '/news/',           'IdlebrainNewsToday',
    '/reviews/', 	'IdlebrainMovieReviews',
    '/wallpapers/',     'IdlebrainWallpapers',
    '/interviews/',     'IdlebrainCelebrityInterviews'
)

db = web.database(dbn='sqlite', db=config.database)

app = web.application(urls, globals())
render = web.template.render('template/')

class IdlebrainIndex:
	def GET(self):
		return render.IdlebrainIndex()
		
class IdlebrainLatestUpdates:
	def GET(self):
		query = """
			select html from pages where url_m = 'foobarm'
			"""
		className = self.__class__.__name__
		try:
			return db.select('pages', where="class='"+className+"'")[0]['html']
		except IndexError:
			return "Couldn't find the page"
		# return render.IdlebrainIndex()
if __name__ == "__main__":
    app.run()
