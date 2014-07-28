# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, g, jsonify, request
from flask.ext.sendmail import Message
from bbqtv.services import bbqtv_db, mail
from bbqtv.services import seo
from datetime import datetime, timedelta
import time

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    g.title = u"Programación TV hoy"
    channels = bbqtv_db.get_channels()
    keywords = seo.get_keywords(channels.clone())
    g.keywords = keywords.lower()
    g.description = u"Toda la programación de la TV. ¿Que quieres ver hoy? La programación de %s y más" % keywords
    return render_template('index.html', channels = channels, now = bbqtv_db.get_now())


@frontend.route('/programacion/<channel_id>')
@frontend.route('/programacion/<channel_id>/<date>')
def programacion( channel_id, date = None):
    
    d = datetime.strptime(date, "%Y%m%d") if date else datetime.now()
    channel = bbqtv_db.get_channel_day(channel_id, d)
    
    
    keywords = seo.get_keywords(channel['programmes']) if 'programmes' in channel else ""
    
    g.keywords = keywords.lower()
    g.description = u"Toda la programación de %s. Todos los programas %s y más" % (channel['name'], keywords)
    
    
    months = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }
    
    weekday={
        0 : u"Lunes", 
        1 : u"Martes", 
        2 : u"Miércoles",
        3 : u"Jueves", 
        4 : u"Viernes", 
        5 : u"Sábado",
        6 : u"Domingo"
    }
    
    data_next = {}
    d_next = d + timedelta(days = 1)
    print d_next
    data_next['link'] = "/programacion/%s/%s" % (channel_id, d_next.strftime("%Y%m%d"))
    data_next['day_of_week'] = weekday[d_next.weekday()]
    data_next['day'] = d_next.day
    data_next['month'] = months[d_next.month]
    data_prev = {}
    d_prev = d - timedelta(days = 1)
    data_prev['link'] = "/programacion/%s/%s" % (channel_id, d_prev.strftime("%Y%m%d"))
    data_prev['day_of_week'] = weekday[d_prev.weekday()]
    data_prev['day'] = d_prev.day
    data_prev['month'] = months[d_prev.month]
    
    g.title = u"Programación %s %s" % (channel['name'], "Hoy" if not date else d.strftime('%d/%m/%Y'))
    
    return render_template('channel.html', \
      channels = bbqtv_db.get_channels() , \
      channel = channel, \
      data_next = data_next, \
      data_prev = data_prev, \
      now = not d,
      date = d)
      
@frontend.route('/contact', methods=['GET', 'POST'])
def contact():
    
    msg = Message(request.form['subject'],
       sender=(request.form['name'], request.form['email']),
       recipients=["to@example.com"],
       body=request.form['msg'])
      
    try:
        mail.send(msg)
        return jsonify({"ok":True, "info":"Gracias por su mensaje"})
    except:
        return jsonify({"ok":False, "info":"Ocurrio un error. <a href='mailto:%s'>%s</a>" % (g.admin_email, g.admin_email)})
    

