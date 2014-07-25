from flask import Flask, g

from bbqtv.services import bbqtv_db, mail


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    
    mail.init_app(app)
    bbqtv_db.init_app(app)
    
    from bbqtv.blueprints.frontend import frontend
    app.register_blueprint(frontend)
    
    @app.before_request
    def before_request():
        g.admin_email = app.config['ADMIN_EMAIL']
    
    return app
