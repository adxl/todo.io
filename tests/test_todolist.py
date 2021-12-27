from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock

from app.Item import Item
from app.todolist import TodoList
from app.user import User
from tests.conf import date_factory as d


class TodoListTest(TestCase):
    def setUp(self):
        self.user = User("John", "Doe", "johndoe@gmail.com", "p4ssw0rd", d(24))
        self.todolist = self.user.create_todo_list()
        self.item = Item(name="test", content="test")
        return super().setUp()

    # todolist item tests

    def test_list_owner(self):
        self.assertEqual(self.todolist.get_owner(), self.user.get_email())

    def test_validate_add_item(self):
        result = self.todolist.add_item(item=self.item)
        self.assertIsInstance(result, TodoList)

    def test_invalidate_add_item_is_bad_type(self):
        self.assertRaises(TypeError, self.todolist.add_item, 1.2)

    def test_invalidate_add_item_is_none(self):
        self.assertRaises(TypeError, self.todolist.add_item, None)

    def test_invalidate_add_item_is_duplicate(self):
        self.todolist.verify_updated_at = MagicMock(
            name="verify_updated_at", return_value=True
        )
        self.todolist.add_item(item=self.item)
        self.assertRaises(ValueError, self.todolist.add_item, self.item)

    def test_unique_items(self):
        self.todolist.verify_updated_at = MagicMock(
            name="verify_updated_at", return_value=True
        )

        item_1 = Item("same_name", "some_content")
        item_2 = Item("same_name", "another_content")

        self.todolist.add_item(item_1)
        self.assertEqual(self.todolist.get_length(), 1)

        self.assertRaises(ValueError, self.todolist.add_item, item_2)

    def test_validate_add_item_after_thirty_minutes(self):
        self.todolist.verify_updated_at = MagicMock(
            name="verify_updated_at", return_value=True
        )
        self.todolist.add_item(item=self.item)
        self.assertEqual(self.todolist.get_length(), 1)

    def test_invalidate_add_item_before_thirty_minutes(self):
        self.todolist.verify_updated_at = MagicMock(
            name="verify_updated_at", return_value=False
        )
        self.assertRaises(ValueError, self.todolist.add_item, self.item)

    def test_length_lesser_than_10(self):
        self.todolist.verify_length = MagicMock(name="verify_length", return_value=True)
        result = self.todolist.add_item(item=self.item)
        self.assertIsInstance(result, TodoList)

    def test_length_greater_than_10(self):
        self.todolist.verify_length = MagicMock(
            name="verify_length", return_value=False
        )
        self.assertRaises(ValueError, self.todolist.add_item, self.item)

    def test_add_trigger_email_on_8th_insert(self):
        self.todolist.verify_updated_at = MagicMock(
            name="verify_updated_at", return_value=True
        )

        for i in range(7):
            self.todolist.add_item(Item(str(i), str(i)))

        self.assertEqual(self.todolist.get_length(), 7)

        with self.assertRaises(NotImplementedError) as context:
            self.todolist.add_item(Item("some_name", "some_content"))

        expected_message = f"Email sent to {self.user.get_email()} successfully !"
        self.assertEqual(str(context.exception), expected_message)

    # todolist updated_at tests

    def test_validate_updated_at(self):
        self.todolist.set_updated_at(updated_at=datetime.now() - timedelta(minutes=40))
        result = self.todolist.verify_updated_at()
        self.assertTrue(result)

    def test_invalid_updated_at(self):
        self.todolist.set_updated_at(updated_at=datetime.now() - timedelta(minutes=15))
        result = self.todolist.verify_updated_at()
        self.assertFalse(result)
