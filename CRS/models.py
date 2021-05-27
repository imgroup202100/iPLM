from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_chairperson = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    studentNumber = models.CharField(max_length=150)

class facultyApplicant(models.Model):
    lastName = models.CharField(max_length = 150)
    firstName = models.CharField(max_length = 150)
    middleName = models.CharField(max_length = 150)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length = 150)
    CV = models.FileField(upload_to='facultyApplicant/', blank=True, null=True)
    certificates = models.FileField(upload_to='facultyApplicant/',blank=True, null=True)
    credentials = models.FileField(upload_to='facultyApplicant/',blank=True, null=True)
    TOR = models.FileField(upload_to='facultyApplicant/',blank=True, null=True)

