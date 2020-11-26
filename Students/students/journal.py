import random
from Students.students.time import days


def check_list():
    number = days()
    ch_lst = []
    for i in range(number):
        ch_lst.append({'day_number': i + 1, 'check': checked()})
    return ch_lst


def checked():
    if random.randint(0, 1) == 0:
        return 'checked'
    else:
        return ''
