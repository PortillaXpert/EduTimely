from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.login