from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock
from app.Item import Item
from app.todolist import TodoList

class TodoListTest(TestCase):
    
    def setUp(self):
        self.todolist = TodoList()
        self.item = Item(name="test",content="test")
        return super().setUp()
    

    # todolist item tests

    def test_validate_add_item(self):
        result = self.todolist.set_item(item=self.item)
        self.assertIsInstance(result, TodoList)
    
    def test_invalidate_add_item_is_bad_type(self):
        self.assertRaises(TypeError, self.todolist.set_item, 1.2)
    
    def test_invalidate_add_item_is_none(self):
        self.assertRaises(TypeError, self.todolist.set_item, None)
    
    def test_invalidate_add_item_is_duplicate(self):
        self.todolist.verify_updated_at  = MagicMock(name="verify_updated_at",return_value=True)
        self.todolist.set_item(item=self.item)
        self.assertRaises(ValueError,self.todolist.set_item, self.item)
    
    def test_validate_add_item_after_thirty_minutes(self):
        self.todolist.verify_updated_at  = MagicMock(name="verify_updated_at",return_value=True)
        self.todolist.set_item(item=self.item)
        self.assertEqual(self.todolist.get_length(),1)

    def test_invalidate_add_item_before_thirty_minutes(self):
        self.todolist.verify_updated_at  = MagicMock(name="verify_updated_at",return_value=False)
        self.assertRaises(ValueError, self.todolist.set_item, self.item)
    
    def test_validate_add_item_after_thirty_minutes_and_length_less_than_10(self):
        self.todolist.verify_updated_at  = MagicMock(name="verify_updated_at",return_value=True)
        self.todolist.verify_length  = MagicMock(name="verify_length",return_value=True)
        result = self.todolist.set_item(item=self.item)
        self.assertIsInstance(result, TodoList)
    
    def test_invalidate_add_item_after_thirty_minutes_and_length_better_than_10(self):
        self.todolist.verify_updated_at  = MagicMock(name="verify_updated_at",return_value=True)
        self.todolist.verify_length  = MagicMock(name="verify_length",return_value=False)
        self.assertRaises(ValueError, self.todolist.set_item, self.item)
    

    # todolist updated_at tests

    def test_validate_updated_at(self):
        self.todolist.set_updated_at(updated_at=datetime.now() - timedelta(minutes=40))
        result = self.todolist.verify_updated_at()
        self.assertTrue(result)
    
    def test_invalid_updated_at(self):
        self.todolist.set_updated_at(updated_at=datetime.now() - timedelta(minutes=15))
        result = self.todolist.verify_updated_at()
        self.assertFalse(result)