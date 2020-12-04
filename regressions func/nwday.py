from datetime import datetime
from peewee import *
from databases.persondb import *

# всякие импорты

# данные, которые мы хотим получить от пациента или от базы данных
user_id = int(input())
def predict(user_id):
    row = Humans.get(Humans.ID == user_id)
    age = row.Age  # ввод возраста ПАЦИЕНТА
    imya = row.Name  # ввод имени
    familiya = row.Surname  # ввод фамилии
    #     # узнаём реальное время и ложим в список




    deystv = str(input("Что делаем?: "))  # ввод действия справка, осмотр, лечение
    kabinet = str(input("Какой врач вам нужен?: "))  # ввод кабинета
    probl = str(input(
        "Кол-во сопустсвующих заболеваний: "))  # ввод проблем (болит голова и печень, а ещё бы пятно на руке посмотреть)

    # списки, словари и т.д
    inpspis = [imya, familiya, age, deystv, kabinet,
               probl]  # список: имя, фамилия, возраст, действие, кабинет, кол-во проблем

    # обозначаем время которое тратится на обычного, молодого человека(в секундах)
    spravka = 300  # справка
    osmotr = 600  # осмотр и консультация
    lechenie = 900  # лечение и консультация
    # секунды, которые мы будем добавлять при осложнениях
    minbonus = 30
    srbonus = 60
    maxbonus = 120

    # --------------------------------------------------------------------------

    balance = 0  # количество минут в сеансе

    # --------------------------------------------------------------------------

    # булевы значения

    baby = False
    old = False
    bon = True



    spis = inpspis.copy()
    # добавляем время по действиям
    if spis[3].lower() == "осмотр":
        balance = int(balance) + int(osmotr)
    elif spis[3].lower() == "справка":
        balance = int(balance) + int(spravka)
    elif spis[3].lower() == "лечение":
        balance = int(balance) + int(lechenie)
    else:
        bon = False
        balance = int(srbonus) * int(probl)

    # бонусы и штрафы врачам
    if kabinet.lower() == "психолог":
        ultrabonus = int(maxbonus) * 10
        balance = int(balance) + int(ultrabonus)
    elif kabinet.lower() == "травматолог":
        balance = int(balance) + int(maxbonus)
    elif kabinet.lower() == "дерматолог":
        balance = int(balance) - maxbonus - 180

    # если ребёнок
    if int(spis[2]) < 6:
        baby = True
        balance = int(balance) + int(maxbonus)
    # если старик
    if int(spis[2]) >= 60:
        old = True
        balance = int(balance) + int(maxbonus)
    if int(probl) > 1 and bon:
        balance100 = int(minbonus) * int(probl)
        balance = int(balance) + int(balance100)

    timelol = False

    # функция ручного добавления времени
    if timelol == True:
        balance = int(balance) + 300
        timelol = False

    # Определение врача

    return balance
