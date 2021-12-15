from datetime import date, timedelta
from unittest import TestCase

from app.user import User


def d(age=0) -> date:
    """date factory"""
    return date.today() - timedelta(age * 365)


class TestUserValid(TestCase):
    def setUp(self):
        self.user = User("John", "Doe", "johndoe@gmail.com", "p4ssw0rd", d(24))

    # user's first name tests

    def test_correct_first_name(self):
        result = self.user.set_first_name("Will")
        self.assertIsInstance(result, User)

    def test_bad_type_first_name(self):
        self.assertRaises(TypeError, self.user.set_first_name, 1.4)

    def test_empty_string_first_name(self):
        self.assertRaises(TypeError, self.user.set_first_name, "")

    def test_none_type_first_name(self):
        self.assertRaises(TypeError, self.user.set_first_name, None)

    def test_no_first_name(self):
        self.assertRaises(TypeError, self.user.set_first_name)

    # user's last name tests

    def test_correct_last_name(self):
        result = self.user.set_last_name("Smith")
        self.assertIsInstance(result, User)

    def test_bad_type_last_name(self):
        self.assertRaises(TypeError, self.user.set_last_name, 1.4)

    def test_empty_string_last_name(self):
        self.assertRaises(TypeError, self.user.set_last_name, "")

    def test_none_type_last_name(self):
        self.assertRaises(TypeError, self.user.set_last_name, None)

    def test_no_last_name(self):
        self.assertRaises(TypeError, self.user.set_last_name)

    # user's email tests

    def test_correct_email(self):
        result = self.user.set_email("willsmith@gmail.com")
        self.assertIsInstance(result, User)

    def test_bad_type_email(self):
        self.assertRaises(TypeError, self.user.set_email, 1.4)

    def test_empty_string_email(self):
        self.assertRaises(TypeError, self.user.set_email, "")

    def test_none_type_email(self):
        self.assertRaises(TypeError, self.user.set_email, None)

    def test_no_email(self):
        self.assertRaises(TypeError, self.user.set_email)

    # user's password tests

    def test_correct_password(self):
        result = self.user.set_password("p4$$w0rD")
        self.assertIsInstance(result, User)

    def test_bad_type_password(self):
        self.assertRaises(TypeError, self.user.set_password, 1.4)

    def test_empty_string_password(self):
        self.assertRaises(TypeError, self.user.set_password, "")

    def test_none_type_password(self):
        self.assertRaises(TypeError, self.user.set_password, None)

    def test_no_password(self):
        self.assertRaises(TypeError, self.user.set_password)

    # user's birth date tests

    def test_correct_birth_date(self):
        result = self.user.set_birth_date(date(2005, 11, 25))
        self.assertIsInstance(result, User)

    def test_bad_type_birth_date(self):
        self.assertRaises(TypeError, self.user.set_birth_date, 1.4)

    def test_empty_string_birth_date(self):
        self.assertRaises(TypeError, self.user.set_birth_date, "")

    def test_none_type_birth_date(self):
        self.assertRaises(TypeError, self.user.set_birth_date, None)

    def test_no_birth_date(self):
        self.assertRaises(TypeError, self.user.set_birth_date)

    # user validity tests

    def test_is_valid(self):
        result = self.user.is_valid()
        self.assertTrue(result)

    def test_good_email(self):
        self.user.set_email("willsmith@gmail.com")
        result = self.user.is_valid()
        self.assertTrue(result)

    def test_bad_email(self):
        self.user.set_email("bad-email")
        result = self.user.is_valid()
        self.assertFalse(result)

    def test_short_password(self):
        self.user.set_password("p")
        result = self.user.is_valid()
        self.assertFalse(result)

    def test_long_password(self):
        self.user.set_password("l0ngPa$$w0rD" * 10)
        result = self.user.is_valid()
        self.assertFalse(result)

    def test_younger_than_13(self):
        self.user.set_birth_date(d(10))
        result = self.user.is_valid()
        self.assertFalse(result)
