from databases.crud import Crud
from flask import Flask
from flask import request, jsonify
from predict.nwday import predict
from flask_cors import CORS
import sched
import time

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True
CORS(app)

s = sched.scheduler(time.time, time.sleep)


def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))


@app.route('/reg', methods=["POST"])
def register():
    data = request.json
    print(data)
    temp = Crud.create_user(data['surname'], data['name'], data['patronymic'], data['gender'], data['login'],
                            data['password'])
    return jsonify({'ans': temp})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print(data)
    print(Crud.get_usertype(data['login']))
    return jsonify({"ans": Crud.comparison(data['login'], data['password']), "type": Crud.get_usertype(data['login'])})


@app.route('/time', methods=["POST"])
def time_post():
    data = request.json
    return jsonify({"ans": predict(data['name'])})


@app.route('/get_appointment', methods=["POST"])
def get_appointments():
    data = request.json
    return jsonify({"ans": Crud.get_appointmentslist(data['email'])})


@app.route('/create_appointment', methods=["POST"])
def create_appointment():
    data = request.json
    return jsonify({'ans': Crud.create_appointment_row(data['login'], data['time'], data['data'], data['doctor'],
                                                       data['direction'])})


@app.route('/get_doctorappointments', methods=['POST'])
def get_doctor_appointments():
    data = request.json
    return jsonify({'ans': Crud.get_doctorlist(data['login'])})


@app.route("/close_appointment", methods=['POST'])
def close_appointment():
    data = request.json
    print(data['appointmentId'])
    print(Crud.update_timeend(data['appointmentId']))
    return jsonify({'ans': Crud.update_timeend(data['appointmentId'])})


@app.route("/get_direction", methods=["POST"])
def get_direction():
    data = request.json
    print(data)
    print(data['data'])
    print(Crud.return_direction(data['data']))
    return jsonify({'ans': Crud.return_direction(data['data'])})


@app.route("/get_time", methods=["POST"])
def get_time():
    data = request.json
    return jsonify({'ans': Crud.get_time(data['direction'], data['data'])})


@app.route("/get_doctors", methods=["POST"])
def get_doctors():
    data = request.json
    return jsonify({'ans': Crud.return_doctors(data['direction'])})


@app.route("/reg_appointment", methods=["POST"])
def reg_appointment():
    data = request.json
    return jsonify({'ans': Crud.create_appointment_row(data['login'], data['timestart'], data['data'], data['doctor'],
                                                       data['direction'])})


@app.route('/add_time', methods=['POST'])
def add_time():
    data = request.json
    return jsonify({'ans': Crud.add_time(data['id'])})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
