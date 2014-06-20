#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from channels import channels
from tools import *
from lxml import etree
import time, logging, logging.handlers
from datetime import timedelta, datetime
import re
from pprint import pprint

from db import DB


class Crawler(object):
	
	def __init__(self, verbose = True):
		self.parser = etree.HTMLParser()
		self.verbose = verbose
		
		#config
		self.config = {}
		config_file = os.path.join(os.path.dirname(__file__), "crawler.conf")
		execfile(config_file, self.config)
		
		#logger
		self.logger = logging.getLogger('CRAWLER')
		hdlr = logging.handlers.TimedRotatingFileHandler(os.path.join(os.path.dirname(__file__), \
		  self.config['log_file']))
		hdlr.suffix = "%Y-%m-%d-%H-%M"
		formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
		hdlr.setFormatter(formatter)
		self.logger.addHandler(hdlr)
		self.logger.setLevel(logging.INFO)
		self.logger.info("[__init__]")
		
		#db
		self.db = DB(self.config['database_host'], self.config['database_port'], self.config['database_name'])
		
		self.depp_days = self.config['depp_days']
		
		
	def run(self):
		
		self.logger.info("[run] Iniciando...")
		
		for channel_url, channel_info in channels.items():
			self.extract_channel(channel_url, channel_info)
		
	def extract_channel(self, channel_url, channel_info, next_day = 0, previous_day = 0 ):
		
		self.logger.info("[run] extrayendo canal de %s" % channel_url)
		
		try:
			self.tree = etree.fromstring(download_url(channel_url), self.parser)
		except AttributeError:
			return False
		
		channel_data = {}
		for key, info in channel_info.items():
			if "inner_xpaths" in info:
				channel_data[key] = []
				extracts = self.extracts(info['xpath'])
				for extract in extracts:
					item = {}
					for inner_key, inner_xpath in info['inner_xpaths'].items():
						try:
							item[inner_key] = extract.xpath(inner_xpath)[0]
						except (IndexError, UnicodeDecodeError):
							pass
							
					
					channel_data[key].append(item)
			else:
				
				try:
					extract =  self.extract(info['xpath'])
				except IndexError:
					if (key == "next" and next_day > 0) \
					  or (key == "previous" and previous_day > 0):
						pass
					else:
						raise
						
				if "regex" in info:
					extract = re.findall(info['regex'], extract)[0]
				if "date_format" in info:
					date = time.strptime(extract.strip(), info['date_format'])
					
					extract = datetime(date.tm_year, date.tm_mon, date.tm_mday)
					if "add_days" in info:
						extract += timedelta(days = info['add_days'])
			
				channel_data[key] = extract
		
		
		
			
		if "next" in channel_data and previous_day == 0 and next_day < self.depp_days:
			self.extract_channel(channel_data['next'], channel_info, next_day = next_day + 1 )

		if "previous" in channel_data and next_day == 0 and previous_day < self.depp_days:
			self.extract_channel(channel_data['previous'], channel_info, previous_day = previous_day + 1 )
		
		channel_name = channel_data['name']
		del channel_data['name']
		del channel_data['next']
		del channel_data['previous']
		self.logger.info("[run] guardando datos para el canal %s (%s)" % (channel_name, channel_data['date']))
		
		if next_day == 0 and previous_day == 0:
			self.db.save_channel(channel_name)
		
		self.db.save_data_day(channel_data, channel_name)
		
		
			
		
	def extract_programme(self):
		pass
		
		
	def extract(self, xpath):
		return self.extracts(xpath)[0]
	
	def extracts(self, xpath):
		try:
			find = etree.XPath(xpath)
			return find(self.tree)
		except:
			if self.verbose:
				print "No se ha podido extrar ", xpath
			
			return ""
		


if __name__ == '__main__':
	
	crawler = Crawler()
	
	crawler.run()
	
	
