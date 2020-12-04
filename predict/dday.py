from datetime import datetime

times = datetime.now().strftime('%H:%M')  # просто так узнал время
print(times)  # просто так дал лог
# указываем кол-во времени затрачиваемое на процесс в среднем в минутах
osmotr = 6  # время на осмотр

lechenie = 10  # время на лечение

spravka = 2  # время на взятие или подпись справки

# условный список с уже оформленным расписанием
spis = {
    # список кабинетов
    "101 кабинет": ["17 30", "20 00", "18 00", "18 30"],
    # начало и конец работы, так же начало и конец перерыва в 101 кабинете
    # расписание по дням
    "30day": ["17 30", "17 35", "17 40", "17 50", "17 55"]  # записи на 30 число
}
# характеристика 1 человека [пол, возраст, операция]
lspis = ["девушка", "16", "справка"]


# функция добавления сеанса
def zap(lspis, spis):
    realcrzap = [int(datetime.now().strftime('%Y')), int(datetime.now().strftime('%m')),
                 int(datetime.now().strftime('%d')), int(datetime.now().strftime('%H')),
                 int(datetime.now().strftime('%M'))]  # узнаём реальное время и ложим в список
    print(realcrzap)
    crzap = [2020, 11, 30, 18, 35]  # тестовое время запроса [год,месяц,день,час,минута]
    day = crzap[2]  # выявляем из списка день
    hour = crzap[3]  # выявляем из списка часы
    minut = crzap[4]  # выявляем из списка  минуты
    slday = str(day) + "day"  # выявляем день для словаря
    vremya = str(hour) + " " + str(minut)  # даём премя через пробел в строковой ворме
    print("Запрос создан: " + slday + " в " + vremya)  # просто тупа лог
    ss = spis[str(slday)].copy()  # копируем записи из словаря
    poslind = len(ss) - 1  # выявляем последний элемент списка
    zanvr = ss[poslind].split()  # делим на часы и минуты
    zanchas = int(zanvr[0])  # фиксируем последний занятый час
    zanmin = int(zanvr[1])  # фиксируем последнюю занятую минуту
    print("Последнее занятое время: " + str(zanchas) + ":" + str(zanmin))  # даём лог
    # если ты пришёл вовремя или после последнего сеанса
    if hour >= zanchas and minut >= zanmin or hour > zanchas and minut <= zanmin:
        zanchas = hour
        zanmin = minut
    newseanshour = zanchas  # приравниваем последний час к реальному
    # дальше идут условия при выборе действия
    newseansmin = int()
    if lspis[2] == "справка":
        newseansmin = zanmin + spravka  # время начала нового сеанса
    elif lspis[2] == "осмотр":
        newseansmin = zanmin + osmotr  # время начала нового сеанса
    elif lspis[2] == "лечение":
        newseansmin = zanmin + lechenie  # время начала нового сеанса
    # если нужно перейти на другой час или день
    elif newseansmin >= 60:
        newseansmin = newseansmin - 60
        newseanshour += 1
    # барьеры ПОМЕЧУ КАПСОМ АААААААААААААААААААААААААААААААА
    kabinp = "101 кабинет"  # кабинет, где будут проходить сеансы
    sk = spis[str(kabinp)].copy()
    starter = sk[0]  # достали время начала работы
    # делим на часы и минуты
    sstarter = starter.split()
    hourstart = sstarter[0]
    minstart = sstarter[1]
    ender = sk[1]  # достали время конца работы
    # делим на часы и минуты
    sender = ender.split()
    hourender = sender[0]
    minender = sender[1]
    per1 = sk[2]  # достали время начала перерыв
    # делим на часы и минуты
    sper1 = per1.split()
    hourper1 = sper1[0]
    minper1 = sper1[1]
    per2 = sk[3]  # достали время окончания верерыва
    # делим на часы и минуты
    sper2 = per2.split()
    hourper2 = sper2[0]
    minper2 = sper2[1]
    if int(newseanshour) >= int(hourper1) and int(newseansmin) >= int(minper1):
        newseanshour = hourper2
        newseansmin = minper2
        if int(hour) >= int(hourper2) and int(minut) >= int(minper2) or int(hour) > int(hourper2) and int(minut) <= int(
                minper2):
            newseanshour = crzap[3]
            newseansmin = crzap[4]
            if lspis[2] == "справка":
                newseansmin = zanmin + spravka  # время начала нового сеанса
            elif lspis[2] == "осмотр":
                newseansmin = zanmin + osmotr  # время начала нового сеанса
            elif lspis[2] == "лечение":
                newseansmin = zanmin + lechenie  # время начала нового сеанса
    print("Время вашего сеанса: " + str(newseanshour) + ":" + str(newseansmin))


zap(lspis, spis)
