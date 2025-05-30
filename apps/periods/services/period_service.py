# apps/periods/services/period_service.py

from apps.periods.models.period import Period
from django.core.exceptions import ValidationError
from django.db import transaction


class PeriodService:

    @staticmethod
    def create_period(name, start_date, end_date, is_active=False):
        if start_date >= end_date:
            raise ValidationError("La fecha de inicio debe ser anterior a la de finalización.")

        if is_active:
            # Solo puede haber un periodo activo a la vez
            Period.objects.filter(is_active=True).update(is_active=False)

        period = Period.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active
        )
        return period

    @staticmethod
    def update_period(period_id, name, start_date, end_date, is_active):
        period = Period.objects.get(id=period_id)

        if start_date >= end_date:
            raise ValidationError("La fecha de inicio debe ser anterior a la de finalización.")

        with transaction.atomic():
            period.name = name
            period.start_date = start_date
            period.end_date = end_date

            if is_active:
                Period.objects.filter(is_active=True).exclude(id=period.id).update(is_active=False)
            period.is_active = is_active

            period.save()
        return period

    @staticmethod
    def delete_period(period_id):
        Period.objects.get(id=period_id).delete()

    @staticmethod
    def get_active_period():
        return Period.objects.filter(is_active=True).first()

    @staticmethod
    def list_periods():
        return Period.objects.all().order_by('-start_date')
