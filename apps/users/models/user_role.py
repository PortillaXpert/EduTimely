from django.db import models
from apps.users.models.user import User
from apps.users.models.role import Role


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Meta:
    unique_together = ('user', 'role')

