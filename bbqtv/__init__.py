from flask import Flask
import bbqtv.views

def create_app(config_filename):
    app = Flask(__name__)
    #~ app.config.from_pyfile(config_filename)

    #~ from yourapplication.model import db
    #~ db.init_app(app)

    #~ from yourapplication.views.admin import admin
    #~ from yourapplication.views.frontend import frontend
    #~ app.register_blueprint(admin)
    #~ app.register_blueprint(frontend)

    return app



