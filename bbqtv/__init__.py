from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    #~ app.config.from_pyfile(config_filename)

    #~ from yourapplication.model import db
    #~ db.init_app(app)

    from bbqtv.blueprints.frontend import frontend
    app.register_blueprint(frontend)

    return app
