from datetime import datetime
from peewee import *
from databases.persondb import *

# всякие импорты

# данные, которые мы хотим получить от пациента или от базы данных
# SQL
user_id = int(input())
row = Humans.get(Humans.ID == user_id)
age = row.Age  # ввод возраста ПАЦИЕНТА
imya = row.Name  # ввод имени
familiya = row.Surname  # ввод фамилии

# realcrzap = [int(datetime.now().strftime('%Y')),int(datetime.now().strftime('%m')),int(datetime.now().strftime('%d')),
#              int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M'))]
# узнаём реальное время и ложим в список


kab = {
    "101": ["Иванов Иван Иваныч", "психолог", "8 00", "14 00"],
    "102": ["Петров Пётр Петрович", "травматолог", "8 30", "17 00"],
    "103": ["Зубенко Михаил Петрович", "дерматолог", "8 30", "15 00"]
}  # набор кабинетов

# input

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
normbonus = 90
maxbonus = 120

# --------------------------------------------------------------------------

balance = 0  # количество минут в сеансе

# --------------------------------------------------------------------------

# булевы значения

baby = False
old = False
bon = True
psih = False

# определяем кабинет


spis = inpspis.copy()
# добавляем время по действиям
if spis[3].lower() == "осмотр":
    balance = int(balance) + int(osmotr)
    print("осмотр")
elif spis[3].lower() == "справка":
    balance = int(balance) + int(spravka)
    print("справка")
elif spis[3].lower() == "лечение":
    balance = int(balance) + int(lechenie)
    print("лечение")
else:
    bon = False
    balance1 = int(srbonus) * int(probl)
    print("не определено")

# бонусы и штрафы врачам
if kabinet.lower() == "психолог":
    ultrabonus = int(maxbonus) * 10
    balance = int(balance) + int(ultrabonus)
    print("Сеанс у психолога очень долгий, поэтому добавляем 10ти кратный бонус ко времени")
    psih = True
elif kabinet.lower() == "травматолог":
    balance = int(balance) + int(maxbonus)
    print("Травматологу добавлен максимальный бонус")
elif kabinet.lower() == "дерматолог":
    balance = int(balance) - maxbonus - 180
    print("Штраф дерматологу, потому что процедура более менее быстрая")

# если ребёнок
if int(spis[2]) < 6:
    baby = True
    balance = int(balance) + int(maxbonus)
    print("Добавлен максивальный бонус из-за ребёнка")
# если старик
if int(spis[2]) >= 60:
    old = True
    balance = int(balance) + int(maxbonus)
    print("Добавлен максимальный бонус в связи со старость")
if int(probl) > 1 and bon == True:
    balance100 = int(minbonus) * int(probl)
    balance = int(balance) + int(balance100)
    print("даём средние бонусы на множество сопуствующих заболеваний")

timelol = False

# функция ручного добавления времени
if timelol == True:
    balance = int(balance) + 300
    tinelol = False

# Определение врача
if psih == True:
    vrach = kab("101")[0]

# log
i = 0

while i <= 10:
    i += 1
    print("")
print("Пациент: " + spis[0] + " " + spis[1])
print('Время вашего обслуживания: ' + str(balance) + " ")
