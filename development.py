from bbqtv import create_app
app = create_app('bbqtv.conf')
app.debug = True
app.run()
