from databases.persondb import *
from databases.obejcts import *
import json
import datetime
from alg import Alg


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
    def add_timeend(login, direction_id):
        # данные пациента
        user = Users.select().where(Users.Email == login).get()
        old = user.Age  # возраст

        # Бонусы и штрафы
        bonusmin = 30
        bonussr = 60
        bonusmax = 120

        timepr = 0  # главная переменная отвечающая за время

        # Знакомство с пациентом ОНА ЖЕ ПЕРЕМЕННАЯ ВРЕМЕНИ(в секундах)
        timepr += 30
        # если направление к психологу
        if str(direction_id) == '1':
            # штрафы за возраст
            if old >= 60:
                timepr += bonusmax
            if old <= 5:
                timepr += bonusmax
            # штрафы по процедуре
            timepr += bonussr * 10  # этап сбора информации о пациенте
            timepr += bonussr * 10  # нарисовать схему проблемы или расписать шаги

            upr = False
            if upr:  # если требуются какие-то упражнения
                timepr += bonussr * 5  # этап выполнения специальных упражнений
            timepr += bonusmax * 2  # подвод итога
            timepr += bonusmax  # обсуждение домашнего задания
            return timepr / 60

        # если направление к неврологу
        elif str(direction_id) == '2':
            # штрафы за возраст
            if old >= 60:
                timepr += bonusmax
            if old <= 5:
                timepr += bonusmax
            timepr += bonussr  # заполнение карты
            timepr += bonussr * 3  # рассмотр всех результатов проведенных обследований,
            # выписки и другую медицинскую документацию
            # идёт осмотр
            timepr += bonusmin - 20  # Двигательную активность
            timepr += bonusmin - 10  # Симметричность конечностей и плеч
            timepr += bonusmin - 10  # Особенности осанки
            timepr += bonusmin - 20  # Степень дрожания рук и тела в целом
            # итог
            timepr += bonussr
            return timepr / 60
        # если направление к кардиологу
        elif str(direction_id) == '3':
            # штрафы за возраст
            if old >= 60:
                timepr += bonusmax
            if old <= 5:
                timepr += bonusmax
            timepr += bonussr  # заполнение карты
            timepr += bonusmax  # Сбор анамнеза
            # Осмотр пациента: осматривает кожные покровы и видимые слизистые оболочки,
            # что дает возможность определить возможное нарушение кровообращения
            # (характеризуется появлением синюшного окрашивания губ, кончика носа),
            # область сердца (развитие видимой деформации грудной клетки).
            timepr += bonusmax * 3
            # Пальпация
            timepr += bonusmax * 2
            # Перкуссия
            timepr += bonussr
            # Аускультация
            timepr += bonusmax
            # итог
            timepr += bonusmax
            return timepr / 60

    @staticmethod
    def comparison(email, password):
        if Users.select().where(Users.Email == email):
            if password:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def create_user(surname, name, patronymic, email, password, age, gender, snils, polis):
        row = Users(
            Surname=surname,
            Name=name,
            Patronymic=patronymic,
            Email=email,
            Password=password,
            Age=age,
            Gender=gender,
            snils=snils,
            polis=polis,
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
    def update_timeend(id):
        row = Appointments.select().where(Appointments.id == id).get()
        row.TimeEnd = datetime.datetime.today().strftime("%H:%M")
        row.is_ended = True
        row.save()
        return True

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
        if Users.select().where(Users.Email == email):
            row = Users.select().where(Users.Email == email).get()
            return row.Type
        else:
            return False

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
        row = Appointments.select().where((Appointments.Key_id == key) & (Appointments.is_ended == False))
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
        row = Appointments.select().where(Appointments.doctor_id == doc.id and Appointments.is_ended == False)
        res = []
        for app in row:
            tmp = Crud.get_patient_by_id(app.Key_id)
            res.append(
                Doctorapps(app.id, (tmp['Surname'] + ' ' + tmp["Name"] + ' ' + tmp['Patronymic']), app.TimeStart,
                           app.Data).__dict__)
        return res

    @staticmethod
    def get_direct_id(direction):
        row = Directions.select().where(Directions.direction == direction).get()
        return row.id

    @staticmethod
    def get_doctor_id(doctor):
        row = Doctors.select().where(Doctors.Name == doctor).get()
        return row.id

    @staticmethod
    def create_appointment_row(login, timestart, data, doctor, direction):
        obj = datetime.datetime.strptime(timestart, "%H:%M") + datetime.timedelta(
            Crud.add_timeend(login, Crud.get_direct_id(direction)))
        row = Appointments.select().where(
            (Appointments.TimeStart == timestart) & (Appointments.direction_id == Crud.get_direct_id(direction)) & (
                    Appointments.Data == data)).get()
        tmp = row.id
        row = Appointments(
            id=tmp,
            Key_id=Crud.get_id(login),
            TimeStart=timestart,
            TimeEnd=obj.strftime("%H:%M"),
            is_busy=True,
            doctor_id=Crud.get_doctor_id(doctor),
            is_ended=False,
            is_reg=True,
            direction_id=Crud.get_direct_id(direction)
        )
        row.save()
        return row.TimeStart

    @staticmethod
    def get_time(direction, data):
        dir_id = Crud.get_direct_id(direction)
        row = Appointments.select().where((Appointments.direction_id == dir_id) & (Appointments.Data == data))
        res = []
        for tmp in row:
            res.append(Busy_time(tmp.TimeStart, tmp.is_busy).__dict__)
        return res

    """@staticmethod
    def get_time(direction, data, login):
        doctors = Doctors.select().where(Doctors.direction_id == Crud.get_direct_id(direction)).get()
        if Appointments.select().where(Appointments.Data == data):
            row = Appointments.select().where(Appointments.doctor_id == doctors.id and Appointments.Data == data)
            res = []
            for tmp in row:
                res.append(Appointreg(user_id, tmp.TimeStart, tmp.is_busy, Crud.get_doctor(tmp.doctor_id)).__dict__)
            return res
        else:
            return "Undefined date"""

    @staticmethod
    def generate_appointments():
        date = datetime.datetime.today()
        for i in range(8):
            time = datetime.datetime.strptime("08:00", "%H:%M")
            print(date.strftime("%d.%m.%Y"))
            date += datetime.timedelta(days=1)
            for j in range(13):
                for n in range(3):
                    print(time.strftime("%H:%M"))
                    row = Appointments(
                        TimeStart=str(time.strftime("%H:%M")),
                        Data=str(date.strftime("%d.%m.%Y")),
                        is_busy=False,
                        is_reg=False,
                        direction_id=(n + 1)
                    )
                    row.save()
                time += datetime.timedelta(hours=1)

    @staticmethod
    def get_direction(direction_id):
        row = Directions.select().where(Directions.id == direction_id).get()
        return row.direction

    @staticmethod
    def return_direction(date):
        row = Appointments.select().where(
            (Appointments.Data == date) & (Appointments.direction_id != 0) & (Appointments.is_busy == 0))
        temp = Appointments.select().where((Appointments.Data == date) & (Appointments.direction_id != 0))
        not_busy = set()
        all_ = set()
        for tmp in row:
            not_busy.add(Crud.get_direction(tmp.direction_id))
        for tmp in temp:
            all_.add(Crud.get_direction(tmp.direction_id))
        res = []
        for i in all_:
            if i in not_busy:
                res.append(Busy_doctor(i, False).__dict__)
            else:
                res.append(Busy_doctor(i, True).__dict__)
        return res

    @staticmethod
    def return_doctors(direction):
        direction_id = Crud.get_direct_id(direction)
        row = Doctors.select().where(Doctors.direction_id == direction_id)
        res = []
        for i in row:
            res.append(i.Name)
        return res

    @staticmethod
    def add_time(appoint_id):
        row = Appointments.select().where(Appointments.id == appoint_id).get()
        tmp = row.TimeEnd
        row.TimeEnd = (datetime.datetime.strptime(tmp, "%H:%M") + datetime.timedelta(minutes=10)).strftime("%H:%M")
        row.save()
        return row.TimeEnd
