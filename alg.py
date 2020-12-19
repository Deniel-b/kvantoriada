from databases.persondb import *
from peewee import *


class Alg:
    @staticmethod
    def add_time(app_id, user_id):
        user = Users.select().where(Users.ID == user_id).get()
        row = Appointments.select().where(Appointments.id == app_id)
        # данные пациента
        old = user.Age # возраст

        # Бонусы и штрафы
        bonusmin = 30
        bonussr = 60
        bonusmax = 120

        timepr = 0  # главная переменная отвечающая за время

        # Знакомство с пациентом ОНА ЖЕ ПЕРЕМЕННАЯ ВРЕМЕНИ(в секундах)
        timepr += 30
        a = row.direction_id
        # если направление к психологу
        if str(a) == '1':
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
        elif str(a) == '2':
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
        elif str(a) == '3':
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

