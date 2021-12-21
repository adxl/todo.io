from datetime import date, timedelta


def date_factory(age=0) -> date:
    """date factory"""
    return date.today() - timedelta(age * 365)
