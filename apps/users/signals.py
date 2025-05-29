
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from apps.users.models.user import CustomUser
from edutimely_core.constants.roles import COORDINATOR, TEACHER

@receiver(post_save, sender=CustomUser)
def assign_group_on_user_creation(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.is_coordinator:
        group, _ = Group.objects.get_or_create(name=COORDINATOR)
        instance.groups.add(group)

    if instance.is_teacher:
        group, _ = Group.objects.get_or_create(name=TEACHER)
        instance.groups.add(group)
