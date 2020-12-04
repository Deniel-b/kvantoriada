from databases.crud import Crud
from flask import Flask, config, render_template
from flask import url_for, g
import os
from databases.persondb import *

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return app.send_static_file("file")


@app.route('/register')
def register():
    pass


@app.route('/login', methods=['GET'])
def login():
    data = Crud.parser()
    Crud.comparison(data[0], data[1])


@app.route('/append_user', methods=["GET", "POST"])
def append_user():
    Crud.create_row()


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    Crud.delete_row()


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
