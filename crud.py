from databases.persondb import Humans
from databases.obejcts import Patients
import peewee
from flask import json


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


def get_patient(id):
    row = Humans.select().where(Humans.ID == id).get()
    return Patients(row.ID, row.Name, row.Surname, row.TimeStart, row.TimeEnd, row.Age, row.Birth, row.Gender,
                 row.Diseases, row.Doctor)


def update_row(id, name=Humans.Name, surname=Humans.Surname, timestart=Humans.TimeStart, timeend=Humans.TimeEnd,
               age=Humans.Age, birth=Humans.Birth, gender=Humans.Gender, diseases=Humans.Diseases,
               doctor=Humans.Doctor):
    row = Humans.get(Humans.ID == id)
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


def delete_row(id):
    row = Humans.delete().where(Humans.ID == id)
    row.execute()


get_patient(0)
