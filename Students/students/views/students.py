# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'media/1.jpeg'},
        {'id': 2,
         'first_name': u'Андрій',
         'last_name': u'Корост',
         'ticket': 12,
         'image': 'media/2.jpeg'},
        {'id': 3,
         'first_name': u'Богдан',
         'last_name': u'Чекер',
         'ticket': 21,
         'image': 'media/3.jpeg'},
    )
    return render(request, "students/students_list.html", {'students': students})


def st_list():
    students = (
        {'id': 1,
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/1.jpeg'},
        {'id': 2,
         'first_name': u'Андрій',
         'last_name': u'Корост',
         'ticket': 12,
         'image': 'img/2.jpeg'},
        {'id': 3,
         'first_name': u'Богдан',
         'last_name': u'Чекер',
         'ticket': 21,
         'image': 'img/3.jpeg'},
    )
    return students


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s Form</h1>' % sid)