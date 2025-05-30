from apps.schedules.models.schedule import Schedule
from django.core.exceptions import ValidationError
from django.db import transaction
from datetime import time


class ScheduleService:

    @staticmethod
    def validate_conflicts(period, environment, instructor, day, start_time, end_time, exclude_id=None):
        conflicts = Schedule.objects.filter(
            period=period,
            day=day,
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if exclude_id:
            conflicts = conflicts.exclude(id=exclude_id)

        # Verifica si el ambiente está ocupado
        if conflicts.filter(environment=environment).exists():
            raise ValidationError("El ambiente ya está ocupado en ese horario.")

        # Verifica si el instructor está ocupado
        if conflicts.filter(instructor=instructor).exists():
            raise ValidationError("El instructor ya tiene un horario asignado en ese horario.")

    @staticmethod
    def create_schedule(period, instructor, program, environment, day, start_time, end_time):
        if start_time >= end_time:
            raise ValidationError("La hora de inicio debe ser anterior a la de finalización.")

        ScheduleService.validate_conflicts(period, environment, instructor, day, start_time, end_time)

        return Schedule.objects.create(
            period=period,
            instructor=instructor,
            program=program,
            environment=environment,
            day=day,
            start_time=start_time,
            end_time=end_time
        )

    @staticmethod
    def update_schedule(schedule_id, period, instructor, program, environment, day, start_time, end_time):
        if start_time >= end_time:
            raise ValidationError("La hora de inicio debe ser anterior a la de finalización.")

        ScheduleService.validate_conflicts(period, environment, instructor, day, start_time, end_time, exclude_id=schedule_id)

        with transaction.atomic():
            schedule = Schedule.objects.get(id=schedule_id)
            schedule.period = period
            schedule.instructor = instructor
            schedule.program = program
            schedule.environment = environment
            schedule.day = day
            schedule.start_time = start_time
            schedule.end_time = end_time
            schedule.save()
            return schedule

    @staticmethod
    def delete_schedule(schedule_id):
        Schedule.objects.get(id=schedule_id).delete()

    @staticmethod
    def list_schedules():
        return Schedule.objects.select_related('period', 'instructor', 'program', 'environment').order_by('day', 'start_time')
