class TodoListExistsError(Exception):
    def __init__(_):
        super().__init__("User already have a todo list")
