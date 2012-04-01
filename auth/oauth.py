def dict_to_querystring(query):
	return '&'.join([k+'='+str(v) for (k,v) in query.items()])

def querystring_to_dict(query):
	return dict([(k,v) for k,v in [p.split('=') for p in query.split('&')]])

def get_user_information():
	