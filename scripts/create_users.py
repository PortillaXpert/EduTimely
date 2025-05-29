import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edutimely_core.settings')
django.setup()

from django.contrib.auth.models import Group
from apps.users.models.user import CustomUser

def create_roles():
    for role in ['Coordinador', 'Docente']:
        Group.objects.get_or_create(name=role)

def create_user(username, password, role):
    user, created = CustomUser.objects.get_or_create(username=username)
    if created:
        user.set_password(password)
        user.save()
        group = Group.objects.get(name=role)
        user.groups.add(group)
        print(f"Usuario '{username}' con rol '{role}' creado.")
    else:
        print(f"Usuario '{username}' ya existe.")

if __name__ == "__main__":
    create_roles()
    create_user('coordinador1', 'admin1234', 'Coordinador')
    create_user('docente1', 'admin1234', 'Docente')