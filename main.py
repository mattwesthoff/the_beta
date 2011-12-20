from auth.google_oauth import get_authorize_url, handle_callback
from bottle import route, run, request, redirect

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

run(host='localhost', port=8080)
