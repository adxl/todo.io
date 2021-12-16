import re


class EmailValidator:
    @staticmethod
    def validate(email) -> bool:
        return bool(re.fullmatch("^[^\s@\.]+(\.)*[^\s@]+@\w+\.\w{2,}$", email))
