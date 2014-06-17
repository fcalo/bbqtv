#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class DB(object):
	def __init__(self, host, port, database):
		
		self.db = MongoClient(host = host, port = port)[database]
		
		
	def normalize_collection(self, collection_name):
		return collection_name.lower().replace(".", "")
		
		
	def save_data_day(self, data, collection):
	
		self.db[self.normalize_collection(collection)].save(data)
	
