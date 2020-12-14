from databases.crud import Crud
from flask import Flask, config, render_template
from flask import url_for, g, request, jsonify
import os
from predict.nwday import predict
from databases.persondb import *

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route('/reg', methods=["GET", "POST"])
def register():
    data = request.json
    print(data)
    temp = Crud.create_user(data['surname'], data['name'], data['patronymic'], data['gender'], data['login'],
                            data['password'])
    return jsonify({'ans': temp})


@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.json
    print(data)
    return jsonify({"ans": Crud.comparison(data['login'], data['password'])})


@app.route('/append_user', methods=["GET", "POST"])
def append_user():
    Crud.create_row()


@app.route('/time', methods=["GET", "POST"])
def time_post():
    data = request.json
    return jsonify({"ans": predict(data['name'])})


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    Crud.delete_row()


@app.route('/get_appointment', methods=["POST"])
def get_appointments():
    data = request.json
    return jsonify({"ans": Crud.get_appointmentslist(data['email'])})


@app.route('/timechoose', methods=['POST'])
def time_choose():
    data = request.json
    return jsonify({"ans": Crud.get_time(data['direction'])})

'''@app.context_processor
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
    return r'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
