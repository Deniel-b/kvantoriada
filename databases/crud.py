from databases.persondb import *
from databases.obejcts import *
import peewee
from flask import jsonify
import json
import hashlib


class Crud:
    def __init__(self, name, surname, timestart, timeend, age, birth, gender, diseases, doctor):
        self.name = name
        self.surname = surname
        self.timestart = timestart
        self.timeend = timeend
        self.age = age
        self.birth = birth
        self.gender = gender
        self.diseases = diseases
        self.doctor = doctor

    @staticmethod
    def parser(jsfile):
        with open(jsfile, "r") as read_file:
            data = json.load(read_file)
        return data

    @staticmethod
    def comparison(email, password):
        if Users.select().where(Users.Email == email):
            print("True")
            if Crud.comparison_hash(email, password):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def create_row(name, surname, email, password, age, birth, gender, type=0):
        row = Users(
            Name=name,
            Surname=surname,
            Email=email,
            Password=password,
            Age=age,
            Birth=birth,
            Gender=gender,
            Type=type
        )
        row.save()
        temp = {
            row.ID: {"Name": name, "Surname": surname, "Email": email, "Password": password, "Age": age, "Birth": birth,
                     "Gender": gender, "Type": type}}
        return json.dumps(temp, ensure_ascii=False)

    @staticmethod
    def create_user(surname, name, patronymic, gender, email, password):
        row = Users(
            Surname=surname,
            Name=name,
            Patronymic=patronymic,
            Email=email,
            Password=Crud.hashing_password(password),
            Gender=gender,
            Type=False
        )
        if not Users.select().where(Users.Email == email):
            row.save()
            return True
        elif Users.select().where(Users.Email == email):
            return 'LoginBusy'
        else:
            return False

    @staticmethod
    def get_patient(email):
        row = Users.select().where(Users.Email == email).get()
        temp = {"Name": row.Name, "Surname": row.Surname, "Age": row.Age, "Birth": row.Birth, "Gender": row.Gender}
        return json.dumps(temp, ensure_ascii=True)

    @staticmethod
    def get_usertype(email):
        row = Users.select().where(Users.Email == email).get()
        return row.Type

    @staticmethod
    def delete_row(email):
        row = Users.delete().where(Users.Email == email)
        row.execute()

    @staticmethod
    def get_id(email):
        row = Users.select().where(Users.Email == email).get()
        return row.ID

    @staticmethod
    def get_appointmentslist(email):
        key = Crud.get_id(email)
        row = Appointments.select().where(Appointments.Key_id == key)
        res = []
        for app in row:
            res.append(Appoint(app.id, app.TimeStart, app.TimeEnd, app.Data).__dict__)
        return res

    @staticmethod
    def comparison_hash(email, password):
        row = Users.select().where(Users.Email == email).get()
        pass_tmp = row.Password
        if Crud.hashing_password(password) == pass_tmp:
            return True
        else:
            return False

    @staticmethod
    def hashing_password(password):
        tmp = hashlib.md5(password.encode())
        return tmp.hexdigest()

    @staticmethod
    def get_doctor(doc_key):
        row = Doctor.select().where(Doctor.id == doc_key)
        return row.Name

    @staticmethod
    def get_time(direct_id):
        doctors = Doctor.select().where(Doctor.direction_id == direct_id).get()
        docs = []
        for i in doctors:
            docs.append(i.id.__dict__)
        return docs
        '''row = Appointments.select().where(Appointments.doctor_key == doctors.id).get()
        res = []
        for i in row:
            res.append(Appointreg(i.id, i.TimeStart, i.TimeEnd, i.Data, i.is_busy, Crud.get_doctor(i.doctor_id)))
        return res'''
