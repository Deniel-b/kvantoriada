from databases.persondb import *
from databases.obejcts import Patients
import peewee
from flask import jsonify
import json


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
    def comparison(login, password):
        if Users.select().where(Users.Login == login):
            row = Users.select().where(Users.Login == login).get()
            if row.Password == password:
                return 'true'
            else:
                return 'false'
        else:
            return 'false'



    @staticmethod
    def create_row(name, surname, timestart, timeend, age, birth, gender, diseases, doctor):
        row = Humans(
            Name=name,
            Surname=surname,
            TimeStart=timestart,
            TimeEnd=timeend,
            Age=age,
            Birth=birth,
            Gender=gender,
            Diseases=diseases,
            Doctor=doctor
        )
        row.save()
        temp = {row.ID: {"Name": name, "Surname": surname, "TimeStart": timestart,
                         "TimeEnd": timeend, "Age": age, "Birth": birth, "Gender": gender, "Diseases": diseases,
                         "Doctor": doctor}}
        print(temp)
        return json.dumps(temp, ensure_ascii=False)

    @staticmethod
    def get_patient(user_id):
        row = Humans.select().where(Humans.ID == user_id).get()
        temp = {"Name": row.Name, "Surname": row.Surname, "TimeStart": row.TimeStart,
                         "TimeEnd": row.TimeEnd, "Age": row.Age, "Birth": row.Birth, "Gender": row.Gender,
                         "Diseases": row.Diseases, "Doctor": row.Doctor}
        return json.dumps(temp, ensure_ascii=True)

    @staticmethod
    def update_row(user_id, name=Humans.Name, surname=Humans.Surname, timestart=Humans.TimeStart,
                   timeend=Humans.TimeEnd,
                   age=Humans.Age, birth=Humans.Birth, gender=Humans.Gender, diseases=Humans.Diseases,
                   doctor=Humans.Doctor):
        row = Humans.get(Humans.ID == user_id)
        row.Name = name
        row.Surname = surname
        row.TimeStart = timestart
        row.TimeEnd = timeend
        row.Age = age
        row.Birth = birth
        row.Gender = gender
        row.Diseases = diseases
        row.Doctor = doctor
        row.save()
        temp = {row.ID: {"Name": name, "Surname": surname, "TimeStart": timestart,
                         "TimeEnd": timeend, "Age": age, "Birth": birth, "Gender": gender, "Diseases": diseases,
                         "Doctor": doctor}}
        return json.dumps(temp)

    @staticmethod
    def delete_row(user_id):
        row = Humans.delete().where(Humans.ID == user_id)
        row.execute()
