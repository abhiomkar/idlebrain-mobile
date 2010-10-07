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
    '/reviews/', 		'IdlebrainMovieReviews',
    '/wallpapers/',     'IdlebrainWallpapers',
    '/interviews/',     'IdlebrainCelebrityInterviews'
)

app = web.application(urls, globals())

class IdlebrainIndex:
	def GET(self):
		# render = web.template.render('template/IdlebrainIndex.html')
		render = web.template.render('template/')
		return render.IdlebrainIndex()
		
if __name__ == "__main__":
    app.run()