from flask.ext.sendmail import Mail
from db import DB
from seo import SEO


bbqtv_db = DB()
seo = SEO()
mail = Mail()
