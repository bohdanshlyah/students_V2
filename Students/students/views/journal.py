# -*- coding: utf-8 -*-

import random
from django.shortcuts import render
from Students.students.time import days, time
from Students.students.views.students import st_list


def journal(request):
    return render(request, "students/journal.html", {'journal': check_lst, 'time': time, 'students': st_list})


def check_lst():
    def checked():
        if random.randint(0, 1) == 0:
            return 'checked'
        else:
            return ''

    number = days()
    ch_lst = []
    for i in range(number):
        ch_lst.append({'day_number': i + 1, 'check': checked()})
    return ch_lst
