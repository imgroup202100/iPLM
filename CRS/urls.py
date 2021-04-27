from django.conf.urls import url
from . import views

#This code is for creating new pages and redirecting to their URLS.

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^admin_login/$', views.admin_login, name='admin_login'),
    url(r'^chairperson_login/$', views.chairperson_login, name='chairperson_login'),
    url(r'^faculty_login/$', views.faculty_login, name='faculty_login'),
    url(r'^student_login/$', views.student_login, name='student_login'),
    url(r'^applicant_login/$', views.applicant_login, name='applicant_login'),
]