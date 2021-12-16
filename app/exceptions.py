class TodoListExistsError(Exception):
    def __init__(_):
        super().__init__("User already have a todo list")


class UserNotValidError(Exception):
    def __init__(_):
        super().__init__("User is not valid")
