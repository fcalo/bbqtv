

def smart_truncate(content, length=60, suffix=''):
	if len(content) <= length:
		return content
	else:
		return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

class SEO(object):
	def __init__(self):
		pass
		
	def get_keywords(self, data):
		
		return smart_truncate(", ".join([d['name'] if 'name' in d else d['title'] if 'title' in d else "" for d in data]))
