import requests
import simplejson

client_id = "290910061097.apps.googleusercontent.com"
client_secret="38xorQwbOrcrPbFQG-3_NuHG"

def get_authorize_url(target_url):
	host = "https://accounts.google.com/o/oauth2/auth"
	gplus_scope = "https://www.googleapis.com/auth/plus.me"

	query = dict(response_type="code",
			client_id=client_id,
			redirect_uri=target_url,
			scope=gplus_scope,
			approval_prompt="force")

	query_string = '&'.join([k+'='+str(v) for (k,v) in query.items()])
	return "%s?%s" % (host, query_string)

def handle_callback(code, target_url):
	payload = {'code':code,'client_id':client_id,
		'client_secret':client_secret, 'redirect_uri':target_url,
		'grant_type':"authorization_code"}
	url = "https://accounts.google.com/o/oauth2/token"
	headers={"Content-Type":"application/x-www-form-urlencoded"}
	r = requests.post(url, data=payload,headers=headers)
	if r.status_code == 200:
		token = simplejson.loads(r.content)['access_token']
	else:
		return "Error getting auth token"

	d = requests.get("https://www.googleapis.com/plus/v1/people/me",
		headers={"Authorization":("OAuth %s" % token)}) 
	if d.status_code == 200:
		data = simplejson.loads(d.content)
		return dict(name=data['displayName'],image=data['image']['url'])
	else:
		return "Error getting api data"
