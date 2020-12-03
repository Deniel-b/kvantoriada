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
        

    def create_row(self, name, surname, timestart, timeend, age, birth, gender, diseases, doctor):
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
                "TimeEnd": timeend, "Age": age, "Birth": birth, "Gender": gender, "Diseases": diseases, "Doctor": doctor}}
        print(temp)
        return json.dumps(temp, ensure_ascii=False)



    def get_patient(self, id):
        row = Humans.select().where(Humans.ID == id).get() 
        return Patients(row.ID, row.Name, row.Surname, row.TimeStart, row.TimeEnd, row.Age, row.Birth, row.Gender,
                    row.Diseases, row.Doctor)


    def update_row(self, id, name=Humans.Name, surname=Humans.Surname, timestart=Humans.TimeStart, timeend=Humans.TimeEnd,
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
        print(row)
        return row


    def delete_row(self, id):
        row = Humans.delete().where(Humans.ID == id)
        row.execute()
        print(row)
        return row