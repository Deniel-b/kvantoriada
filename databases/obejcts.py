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
    def __init__(self, id, login, password, name):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
