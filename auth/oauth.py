def dict_to_querystring(query):
	return '&'.join([k+'='+str(v) for (k,v) in query.items()])

