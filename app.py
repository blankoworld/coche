# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

FLASKR_SETTINGS = 'settings.cfg'

# create our little application :)
app = Flask(__name__)
app.config.from_pyfile(FLASKR_SETTINGS, silent=True)

if __name__ == '__main__':
    app.run() # app.run(host='0.0.0.0') # run server publicly
