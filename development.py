from bbqtv import create_app
app = create_app('/path/to/config.cfg')
app.debug = True
app.run()
