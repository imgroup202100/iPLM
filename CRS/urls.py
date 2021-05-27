from django.conf.urls import url
from . import views

#This code is for creating new pages and redirecting to their URLS.

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^admin_login/$', views.admin_login, name='admin_login'),
    url(r'^chairperson_login/$', views.chairperson_login, name='chairperson_login'),
    url(r'^faculty_login/$', views.faculty_login, name='faculty_login'),
    url(r'^student_login/$', views.student_login, name='student_login'),
    url(r'^student/$', views.students, name='students'),
    url(r'^chairperson/$', views.chairperson, name='chairperson'),
    url(r'^faculty/$', views.faculty, name='faculty'),
    url(r'^applicant/$', views.applicant, name='applicant'),
    url(r'^admin_access/$', views.admin, name='admin'),
    url(r'^faculty_applicant/$', views.faculty_applicant, name='faculty_applicant'),
    url(r'^faculty_applicant_form/$', views.faculty_applicant_form, name='faculty_applicant_form'),
    url(r'^faculty_applicant_form_submitted/$', views.faculty_applicant_form_submitted, name='faculty_applicant_form_submitted'),
    url(r'^student_applicant/$', views.student_applicant, name='student_applicant'),
    
]