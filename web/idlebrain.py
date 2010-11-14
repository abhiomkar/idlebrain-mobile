#!/usr/bin/python

# Abhinay Omkar : abhiomkar AT gmail DOT com
# http://abhiomkar.in

import web
import sys
import re
from BeautifulSoup import BeautifulSoup

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
		web.header('Content-Type', 'text/html')
		# className = self.__class__.__name__
		try:
			html = db.select('pages', where="url='/'")[0]['html']
		except IndexError:
			return render.ErrorPage() # "Couldn't find the page"

		soup = BeautifulSoup(html)
		trTag = soup.find(text=re.compile("Latest")).findNext('tr')

		# print trTag
		return repr(trTag)

if __name__ == "__main__":
    app.run()
