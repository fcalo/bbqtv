from flask import Flask
from bbqtv.services import bbqtv_db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    
    bbqtv_db.init_app(app)

    from bbqtv.blueprints.frontend import frontend
    app.register_blueprint(frontend)

    return app
