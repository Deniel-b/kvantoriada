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


class Appointmeta:
    def __init__(self, id, timestart, is_busy, doctor):
        self.id = id
        self.timestart = timestart
        self.is_busy = is_busy
        self.doctor = doctor

class Doctorapps:
    def __init__(self, id, name, timestart, data):
        self.id = id
        self.name = name
        self.timestart = timestart
        self.data = data


class Busy_doctor:
    def __init__(self, name, is_busy):
        self.name = name
        self.is_busy = is_busy


class Busy_time:
    def __init__(self, time, is_busy):
        self.time = time
        self.is_busy = is_busy
