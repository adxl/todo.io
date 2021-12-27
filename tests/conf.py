from datetime import date, timedelta


def date_factory(age=0) -> date:
    """generate a datetime from an age"""

    return date.today() - timedelta(age * 365)
