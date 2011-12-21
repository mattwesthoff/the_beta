from auth.google_oauth import get_authorize_url, handle_callback
from auth.fb_oauth import get_fb_auth_url, get_fb_userdata
from bottle import route, run, request, redirect

#https://github.com/iurisilvio/bottle-chat/blob/master/chat.py
#http://devcenter.heroku.com/articles/python

@route('/')
def index():
	return "<a href='/gauth'>Sign in using google</a><br/>\
	<a href='/fbauth'>Sign in using facebook</a>"

@route('/gauth')
def google_auth():
	redirect(get_authorize_url("http://localhost:8080/gauthcallback"))

@route('/gauthcallback')
def gauth_callback():
	if request.query.code:
		user_data = handle_callback(request.query.code, "http://localhost:8080/gauthcallback")
		return "<img src='%s'/>%s" % (user_data['image'], user_data['name'])
	else:
		return "Nothin'"

@route('/fbauth')
def fb_auth():
	redirect(get_fb_auth_url("http://localhost:8080/fbauthcallback"))

@route('/fbauthcallback')
def fbauth_callback():
	if request.query.code:
		user_data = get_fb_userdata(request.query.code, "http://localhost:8080/fbauthcallback")
		return "<img src='%s'/>%s" % (user_data['image'], user_data['name'])
	else:
		return "Nothin'"

run(host='localhost', port=8080)
