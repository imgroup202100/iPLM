from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_chairperson = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)