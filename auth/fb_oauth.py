from oauth import dict_to_querystring

client_id = "294900203884700"

#http://developers.facebook.com/docs/authentication/
#https://developers.facebook.com/apps/294900203884700/summary?save=1

def get_authorize_url(target_url):
	host = "https://www.facebook.com/dialog/oauth"
	query = dict_to_querystring(dict(client_id=client_id, redirect_url=target_url))
	return "%s?%s" % (host, query)


print get_authorize_url("test")
