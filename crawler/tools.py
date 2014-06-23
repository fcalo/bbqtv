#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2


def download_url(url, logger = None):
		
		req = urllib2.Request(url)
		
		downloaded = False
		tries = 0
		while not downloaded:
			try:
				tries += 1
				resp = urllib2.urlopen(req)
				downloaded = True
			except urllib2.URLError as e:
				if logger:
					logger.info("[download_url] Error descargando %s - %s" % (url, str(e)))
				else:
					print ("[download_url] Error descargando %s - %s" % (url, str(e)))
				if tries > 5:
					raise
				else:
					if logger:
						logger.info("[download_url] Reintentando ...")
					else:
						print("[download_url] Reintentando ...")
				time.sleep(tries)
			
		return resp.read()
