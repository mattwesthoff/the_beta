import requests
import simplejson
from oauth import dict_to_querystring, querystring_to_dict

fb_client_id = "294900203884700"
fb_client_secret = "77a2975f2aa7216fe8b8081bbe02516f"
fb_auth_url = "https://graph.facebook.com/oauth/access_token"
fb_auth_host="https://www.facebook.com/dialog/oauth"
fb_auth_data = {
	'client_id':fb_client_id,
	'client_secret':fb_client_secret,
	'grant_type':"authorization_code"}

def get_fb_auth_url(target_url):
	query = dict_to_querystring(dict(client_id=fb_client_id, redirect_uri=target_url))
	return "%s?%s" % (fb_auth_host, query)

def get_fb_userdata(code, target_url):
	fb_auth_data['code'] = code
	fb_auth_data['redirect_uri'] = target_url
	r = requests.post(fb_auth_url,
		data=fb_auth_data, 
		headers={"Content-Type":"application/x-www-form-urlencoded"})
	
	if r.status_code == 200:
		token = querystring_to_dict(r.content)['access_token']
	else:
		return "Error getting auth token"
	
	d = requests.get("https://graph.facebook.com/me?access_token=%s" % token)
	if d.status_code == 200:
		data = simplejson.loads(d.content)
		return dict(name=data['name'],
			image=("https://graph.facebook.com/%s/picture" % data['username']))
	else:
		return "Error getting data"	
