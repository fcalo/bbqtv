from pymongo import MongoClient
from datetime import datetime

class DB(object):
	def __init__(self):
		pass
		
	def init_app(self, app):
		self.db = MongoClient(host = app.config['DB_HOST'], 
		  port = app.config['DB_PORT'])[app.config['DB_NAME']]
		
	def get_channels(self, limit = None):
		if limit:
			return self.db.channels.find().limit(limit).sort("order", 1)
		else:
			return self.db.channels.find().sort("order", 1)


	def get_grid(self):
		grid = {}
		for c in self.get_channels(limit = 7):
			grid[c['name']] = self.get_channel_day(c['_id'], datetime.now())
		
		return grid
			


	def get_channel_day(self, collection_name, date):
		channel_data = self.db[collection_name].find_one({"date" : datetime(date.year, date.month, date.day) })
		if not channel_data:
			channel_data = {}
		
		channel = self.db.channels.find_one({"_id" : collection_name})
		if channel:
			channel_data['name'] = channel['name']
		
		return channel_data
