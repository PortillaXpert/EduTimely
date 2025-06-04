from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.conf import settings

from apps.teachers.models.teacher import Teacher


@receiver(post_save, sender=Teacher)
def assign_teacher_group(sender, instance, created, **kwargs):
    if created and instance.user:
        group, _ = Group.objects.get_or_create(name="Docente")
        instance.user.groups.add(group)
