import datetime


def time():
    t = [
        {'month': tr_month()},
        {'year': year()}
    ]
    return t


def month():
    return datetime.datetime.now().date().month


def tr_month():
    if month() == 1:
        return u"Січень"
    elif month() == 2:
        return u"Лютий"
    elif month() == 3:
        return u"Березень"
    elif month() == 4:
        return u"Квітень"
    elif month() == 5:
        return u"Травень"
    elif month() == 6:
        return u"Червень"
    elif month() == 7:
        return u"Липень"
    elif month() == 8:
        return u"Серпень"
    elif month() == 9:
        return u"Вересень"
    elif month() == 10:
        return u"Жовтень"
    elif month() == 11:
        return u"Листопад"
    elif month() == 12:
        return u"Грудень"


def year():
    return datetime.datetime.now().date().year


def days():
    m = month()
    y = year()
    if m == 2:
        if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
            return 29
        else:
            return 28
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30

