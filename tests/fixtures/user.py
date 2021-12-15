from datetime import date, timedelta

from app.user import User


def __u(*args) -> User:
    """user factory"""
    return User(*args)


def __d(years=0) -> date:
    """date factory"""
    return date.today() - timedelta(years * 365)


fixtures = [
    (__u("john", "doe", "johndoe@gmail.com", "p4ssw0rd", __d(24)), True),
    (__u("", "doe", "johndoe@gmail.com", "p4ssw0rd", __d(23)), False),
    (__u("john", None, "johndoe@gmail.com", "p4ssw0rd", __d(22)), False),
    (__u("john", "doe", "johndoe@gmail.com", "p4ssw0rd", __d()), False),
    (__u("john", "doe", "johndoe@gmail.com", "p4ssw0rd", __d(12)), False),
    (__u("john", "doe", None, "p4ssw0rd", __d(26)), False),
    (__u("john", "doe", "bad-email-format", "p4ssw0rd", __d(23)), False),
    (__u("john", "doe", "johndoe@gmail.com", "p4ss", __d(24)), False),
    (__u("john", "doe", "johndoe@gmail.com", "longpassword" * 10, __d(24)), False),
]
