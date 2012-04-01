import requests
import simplejson
from oauth import dict_to_querystring, querystring_to_dict

fb_client_id = "294900203884700"
fb_client_secret = "77a2975f2aa7216fe8b8081bbe02516f"
#http://developers.facebook.com/docs/authentication/
#https://developers.facebook.com/apps/294900203884700/summary?save=1

def fb_get_authorize_url(target_url):
	host = "https://www.facebook.com/dialog/oauth"
	query = dict_to_querystring(dict(client_id=fb_client_id, redirect_uri=target_url))
	return "%s?%s" % (host, query)

def fb_handle_callback(code, target_url):
	payload = {'code':code,'client_id':fb_client_id,
		'client_secret':fb_client_secret, 'redirect_uri':target_url,
		'grant_type':"authorization_code"}
	url = "https://graph.facebook.com/oauth/access_token"
	headers={"Content-Type":"application/x-www-form-urlencoded"}
	r = requests.post(url, data=payload,headers=headers)
	if r.status_code == 200:
		token = querystring_to_dict(r.content)['access_token']
		d = requests.get("https://graph.facebook.com/me?access_token=%s" % token)
		if d.status_code == 200:
			data = simplejson.loads(d.content)
			return dict(name=data['name'],
				image=("https://graph.facebook.com/%s/picture" % data['username']))
		else:
			return "Error getting data"
	else:
		return "Error getting auth token"