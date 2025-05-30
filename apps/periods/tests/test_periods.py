from django.test import TestCase
from apps.periods.models.period import Period
from datetime import date, timedelta

class PeriodModelTest(TestCase):
    def test_valid_period_creation(self):
        start = date.today()
        period = Period.objects.create(name='2025-1', start_date=start, duration=3)
        self.assertEqual(str(period), '2025-1')
        self.assertTrue(period.start_date, start)
