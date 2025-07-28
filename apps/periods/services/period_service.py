import datetime
from apps.periods.models.period import Period


def calculate_end_date(start_date, period_length_months):
    if not start_date or not period_length_months:
        return None

    new_year = start_date.year
    new_month = start_date.month + period_length_months
    new_day = start_date.day

    while new_month > 12:
        new_month -= 12
        new_year += 1

    last_day_of_month = (datetime.date(new_year, new_month % 12 or 12, 1) - datetime.timedelta(days=1)).day
    return datetime.date(new_year, new_month % 12 or 12, min(new_day, last_day_of_month))
