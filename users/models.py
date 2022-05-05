from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(null=True)
    is_teacher = models.BooleanField(null=True)
    profile_img = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_studying = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username
