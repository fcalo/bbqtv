# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g
from bbqtv.services import bbqtv_db
from datetime import datetime
import time

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
	return render_template('index.html', channels = bbqtv_db.get_channels())


@frontend.route('/programacion/<channel_id>')
@frontend.route('/programacion/<channel_id>/<date>')
def programacion( channel_id, date = None):
	
	channel = bbqtv_db.get_channel_day(channel_id, datetime.strptime(date, "%Y%m%d") if date else datetime.now())
	
	g.title = u"Programación %s %s" % (channel['name'], "Hoy" if not date else channel['date'].strftime('%d/%m/%Y'))
	
	return render_template('channel.html', \
	  channels = bbqtv_db.get_channels() , \
	  channel = channel, \
	  now = not date)
