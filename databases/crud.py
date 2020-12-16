from databases.persondb import *
from databases.obejcts import *
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
    def comparison(email, password):
        if Users.select().where(Users.Email == email):
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
    def get_patient_by_email(email):
        row = Users.select().where(Users.Email == email).get()
        temp = {"Name": row.Name, "Surname": row.Surname, "Patronymic": row.Patronymic, "Age": row.Age,
                "Birth": row.Birth, "Gender": row.Gender}
        return json.dumps(temp, ensure_ascii=True)

    @staticmethod
    def get_patient_by_id(key):
        row = Users.select().where(Users.ID == key).get()
        temp = {"Name": row.Name, "Surname": row.Surname, "Patronymic": row.Patronymic, "Age": row.Age,
                "Birth": row.Birth, "Gender": row.Gender}
        return temp

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
    def get_doctor(doc_id):
        row = Doctors.select().where(Doctors.id == doc_id).get()
        return row.Name

    @staticmethod
    def get_room(room_id):
        row = Rooms.select().where(Rooms.id == room_id).get()
        return row.room_num

    @staticmethod
    def get_appointmentslist(email):
        key = Crud.get_id(email)
        row = Appointments.select().where(Appointments.Key_id == key)
        res = []
        for app in row:
            doc = Doctors.select().where(Doctors.id == app.doctor_id).get()
            room = doc.room_id
            res.append(Appoint(app.id, app.TimeStart, app.TimeEnd, app.Data, Crud.get_doctor(app.doctor_id),
                               Crud.get_room(room)).__dict__)
        return res

    @staticmethod
    def get_doctorlist(login):
        doc = Doctors.select().where(Doctors.login == login).get()
        row = Appointments.select().where(Appointments.doctor_id == doc.id and Appointments.is_busy == True)
        res = []
        for app in row:
            tmp = Crud.get_patient_by_id(app.Key_id)
            res.append(Doctorapps(tmp['Surname'], tmp["Name"], tmp['Patronymic'], app.TimeStart, app.Data).__dict__)
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
    def get_direct_id(direction):
        row = Directions.select().where(Directions.direction == direction).get()
        return row.id

    @staticmethod
    def get_time(direction, data):
        doctors = Doctors.select().where(Doctors.direction_id == Crud.get_direct_id(direction)).get()
        if Appointments.select().where(Appointments.Data == data):
            row = Appointments.select().where(Appointments.doctor_id == doctors.id and Appointments.Data == data)
            res = []
            for tmp in row:
                res.append(Appointreg(tmp.id, tmp.TimeStart, tmp.is_busy, Crud.get_doctor(tmp.doctor_id)).__dict__)
            return res
        else:
            """row = Appointments.select().where(Appointments.doctor_id == doctors.id)
            res = []
            for tmp in row:
                res.append(Appointreg(tmp.id, tmp.TimeStart, tmp.is_busy, Crud.get_doctor(tmp.doctor_id)).__dict__)
            return res"""
            return True
