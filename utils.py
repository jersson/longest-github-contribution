from datetime import datetime


def log_error(error):
    """
    This logging function just print a formated error message
    """
    print(error)


def date_diff_in_days(higher_date: datetime, lower_date: datetime):
    # casted_higher_date = datetime.strptime(higher_date, "%Y-%m-%d")
    # casted_lower_date = datetime.strptime(lower_date, "%Y-%m-%d")
    # datemetime_diff = casted_higher_date - casted_lower_date
    datemetime_diff = higher_date - lower_date
    return datemetime_diff.days
