import re


class EmailValidator:
    @staticmethod
    def validate(email) -> bool:
        """Validate an email address format"""

        return bool(re.fullmatch(r"^[^\s@\.]+(\.)*[^\s@]+@\w+\.\w{2,}$", email))
