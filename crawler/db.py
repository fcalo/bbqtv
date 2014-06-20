#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class DB(object):
	def __init__(self, host, port, database):
		
		self.db = MongoClient(host = host, port = port)[database]
		
		
	def normalize_collection(self, collection_name):
		return collection_name.lower().replace(".", "").replace(" ", "_")
		
		
	def save_data_day(self, data, collection):
	
		self.db[self.normalize_collection(collection)].save(data)
	
	def save_channel(self, channel_name):
	
		collection_name = self.normalize_collection(channel_name)
		channel = self.db.channels.find_one({"collection" : collection_name})
		
		order = channel['order'] if channel else self.db.channels.count()
		
		self.db.channels.save({"name" : channel_name, 
		  "collection" : collection_name,
		  "order" : order})
	
