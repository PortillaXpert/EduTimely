from django.db import models
from apps.users.models.user_manager import UserManager

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    roles = models.ManyToManyField('Role')
    objects = UserManager()

    def __str__(self):
        return self.login