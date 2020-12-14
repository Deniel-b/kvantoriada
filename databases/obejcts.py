class Patients:
    def __init__(self, id, name, surname, timestart, timeend, age, birth, gender, diseases, doctor):
        self.id = id
        self.name = name
        self.surname = surname
        self.timestart = timestart
        self.timeend = timeend
        self.age = age
        self.birth = birth
        self.gender = gender
        self.diseases = diseases
        self.doctor = doctor


class Users:
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
    def __init__(self, id, timestart, timeend, data, doctor):
        self.id = id
        self.timestart = timestart
        self.timeend = timeend
        self.data = data
        self.doctor = doctor


class Appointreg:
    def __init__(self, id, timestart, timeend, data, is_busy, doctor):
        self.id = id
        self.timestart = timestart
        self.timeend = timeend
        self.data = data
        self.is_busy = is_busy
        self.doctor = doctor
