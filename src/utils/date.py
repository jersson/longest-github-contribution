from datetime import datetime, timedelta


def diff_in_days(higher_date: datetime, lower_date: datetime):
    datemetime_diff = higher_date - lower_date
    return datemetime_diff.days


def next_day(current_date: datetime):
    one_day = timedelta(days=1)
    new_day = current_date + one_day
    return new_day
