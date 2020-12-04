from databases.persondb import Humans
from databases.obejcts import Patients
import peewee
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
        temp = {row.ID: {"Name": row.name, "Surname": row.surname, "TimeStart": row.timestart,
                         "TimeEnd": row.timeend, "Age": row.age, "Birth": row.birth, "Gender": row.gender,
                         "Diseases": row.diseases, "Doctor": row.doctor}}
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

