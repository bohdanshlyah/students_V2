"""Students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Students.students.views.students import students_list, students_add, students_edit, students_delete
from Students.students.views.groups import groups_list, groups_add, groups_edit, groups_delete
from Students.students.views.journal import journal

urlpatterns = [
    # Students urls
    url(r'^$', students_list, name='home'),
    url(r'^students/add/$', students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_delete, name='students_delete'),

    # Groups urls
    url(r'^groups/$', groups_list, name="groups"),
    url(r'^groups/add/$', groups_add, name="groups_add"),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name="groups_edit"),
    url(r'^groups/(?P<gid>\d+)/delete$', groups_delete, name="groups_delete"),

    # journal
    url(r'^journal/$', journal, name="journal"),

    # media
    url(r'^media/$', students_list, name="home"),

    url(r'^admin/', admin.site.urls)
]




