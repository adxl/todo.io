from datetime import date, timedelta

from app.email_validator import EmailValidator as ev
from app.exceptions import TodoListExistsError, UserNotValidError
from app.todolist import TodoList


class User:
    def __init__(self, fname, lname, email, password, bdate):
        self.set_first_name(fname)
        self.set_last_name(lname)
        self.set_email(email)
        self.set_password(password)
        self.set_birth_date(bdate)

        self.todo_list = None

    def set_first_name(self, fname):
        if not fname or type(fname) is not str:
            raise TypeError()
        self.__fname = fname
        return self

    def get_first_name(self):
        return self.__fname

    def set_last_name(self, lname):
        if not lname or type(lname) is not str:
            raise TypeError()
        self.__lname = lname
        return self

    def get_last_name(self):
        return self.__lname

    def set_email(self, email):
        if not email or type(email) is not str:
            raise TypeError()
        self.__email = email
        return self

    def get_email(self):
        return self.__email

    def set_password(self, password):
        if not password or type(password) is not str:
            raise TypeError()
        self.__password = password
        return self

    def get_password(self):
        return self.__password

    def set_birth_date(self, bdate):
        if not bdate or type(bdate) is not date:
            raise TypeError()
        self.__bdate = bdate
        return self

    def get_birth_date(self):
        return self.__bdate

    def is_valid(self):
        return (
            ev.validate(self.__email)
            and 8 <= len(self.__password) <= 40
            and date.today() - timedelta(365 * 13) > self.__bdate
        )

    def create_todo_list(self):
        if self.todo_list is not None:
            raise TodoListExistsError()

        if not self.is_valid():
            raise UserNotValidError()

        self.todo_list = TodoList(self.__email)

        return self.todo_list
