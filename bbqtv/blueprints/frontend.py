# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g
from bbqtv.services import bbqtv_db
from bbqtv.services import seo
from datetime import datetime
import time

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
	g.title = u"Programación TV hoy"
	channels = bbqtv_db.get_channels()
	keywords = seo.get_keywords(channels.clone())
	g.keywords = keywords.lower()
	g.description = u"Toda la programación de la TV. ¿Que quieres ver hoy? La programación de %s y más" % keywords
	print channels
	return render_template('index.html', channels = channels)


@frontend.route('/programacion/<channel_id>')
@frontend.route('/programacion/<channel_id>/<date>')
def programacion( channel_id, date = None):
	
	channel = bbqtv_db.get_channel_day(channel_id, datetime.strptime(date, "%Y%m%d") if date else datetime.now())
	
	keywords = seo.get_keywords(channel['programmes'])
	g.keywords = keywords.lower()
	g.description = u"Toda la programación de %s. Todos los programas %s y más" % (channel['name'], keywords)
	
	g.title = u"Programación %s %s" % (channel['name'], "Hoy" if not date else channel['date'].strftime('%d/%m/%Y'))
	
	return render_template('channel.html', \
	  channels = bbqtv_db.get_channels() , \
	  channel = channel, \
	  now = not date)
