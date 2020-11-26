# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse

from Students.students.students import students
from Students.students.groups import groups
from Students.students.journal import check_list
from Students.students.time import time


# Views for Students
def students_list(request):
    return render(request, "students/students_list.html", {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s Form</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s Form</h1>' % sid)


# Views for Groups
def groups_list(request):
    return render(request, "students/groups_list.html", {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s Form</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s Form</h1>' % gid)


# View for Journal
def journal(request):
    return render(request, "students/journal.html", {'journal': check_list, 'time': time, 'students': students})
