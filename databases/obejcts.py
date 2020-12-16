class User:
    def __init__(self, id, name, surname, email, password, age, birth, gender, type):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.age = age
        self.birth = birth
        self.gender = gender
        self.type = type


class Appoint:
    def __init__(self, id, timestart, timeend, data, doctor, room):
        self.id = id
        self.timestart = timestart
        self.timeend = timeend
        self.data = data
        self.doctor = doctor
        self.room = room


class Appointreg:
    def __init__(self, id, timestart, is_busy, doctor):
        self.id = id
        self.timestart = timestart
        self.is_busy = is_busy
        self.doctor = doctor

class Doctorapps:
    def __init__(self, surname, name, patronymic, timestart, data):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.timestart = timestart
        self.data = data
