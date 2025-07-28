from django.db import models
from django.utils.crypto import get_random_string

class UserManager(models.Manager):
    def create_user(self, login, pwd, name=None, last_name=None):
        user = self.model(login=login, pwd=pwd, name=name, last_name=last_name)
        user.save()
        return user
