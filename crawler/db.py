#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

class DB(object):
	def __init__(self, host, port, database):
		
		self.db = MongoClient(host = host, port = port)[database]
		
		
	def normalize_collection(self, collection_name):
		return collection_name.lower().replace(".", "").replace(" ", "_")
		
		
	def save_data_day(self, data, collection):
	
		i_programmes = iter(data['programmes'])
		next(i_programmes)
		for programme in data['programmes']:
			
			duration = None
			try:
				duration =  datetime.strptime(next(i_programmes)['time'], "%H:%M") - datetime.strptime(programme['time'], "%H:%M")
			except (StopIteration, KeyError):
				pass
				
			
			if duration:
				programme['duration'] = duration.seconds / 60 / 10
			else:
				programme['duration'] = 6
		
		
		
		self.db[self.normalize_collection(collection)].save(data)
	
	def save_channel(self, channel_name):
	
		collection_name = self.normalize_collection(channel_name)
		channel = self.db.channels.find_one({"_id" : collection_name})
		
		order = channel['order'] if channel else self.db.channels.count()
		
		self.db.channels.save({"name" : channel_name, 
		  "_id" : collection_name,
		  "order" : order})
	
