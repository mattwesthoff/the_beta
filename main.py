from auth.google_oauth import get_authorize_url, handle_callback
from auth.fb_oauth import fb_get_authorize_url, fb_handle_callback
from bottle import route, run, request, redirect

#https://github.com/iurisilvio/bottle-chat/blob/master/chat.py
#http://devcenter.heroku.com/articles/python

@route('/')
def index():
	return "<a href='/gauth'>Sign in using google</a>"

@route('/gauth')
def google_auth():
	redirect(get_authorize_url("http://localhost:8080/gauthcallback"))

@route('/gauthcallback')
def gauth_callback():
	if request.query.code:
		user_data = handle_callback(request.query.code, "http://localhost:8080/gauthcallback")
		return "<img src='%s0'/>%s" % (user_data['image'], user_data['name'])
	else:
		return "Nothin'"

@route('/fbauth')
def fb_auth():
	redirect(fb_get_authorize_url("http://localhost:8080/fbauthcallback"))

@route('/fbauthcallback')
def fbauth_callback():
	if request.query.code:
		return fb_handle_callback(request.query.code, "http://localhost:8080/fbauthcallback")
	else:
		return "Nothin'"

run(host='localhost', port=8080)
