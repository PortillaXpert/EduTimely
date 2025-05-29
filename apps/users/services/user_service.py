def get_user_role(user):
    if user.groups.filter(name="Coordinador").exists():
        return "Coordinador"
    elif user.groups.filter(name="Docente").exists():
        return "Docente"
    return "Sin rol"

def assign_role(user, role_name):
    from django.contrib.auth.models import Group
    group, _ = Group.objects.get_or_create(name=role_name)
    user.groups.add(group)