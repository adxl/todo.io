from unittest import TestCase

from app.Item import Item


class ItemTest(TestCase):
    def setUp(self):
        self.item = Item(name="Voiture", content="description")
        return super().setUp()

    # item name tests

    def test_correct_name(self):
        result = self.item.set_name("Chaussure")
        self.assertIsInstance(result, Item)

    def test_bad_type_name(self):
        self.assertRaises(TypeError, self.item.set_name, 1.4)

    def test_empty_string_name(self):
        self.assertRaises(TypeError, self.item.set_name, "")

    def test_none_type_name(self):
        self.assertRaises(TypeError, self.item.set_name, None)

    def test_no_name(self):
        self.assertRaises(TypeError, self.item.set_name)

    # item content tests

    def test_correct_content(self):
        result = self.item.set_content("description")
        self.assertIsInstance(result, Item)

    def test_bad_type_content(self):
        self.assertRaises(TypeError, self.item.set_content, [1, 2, 3])

    def test_empty_string_content(self):
        result = self.item.set_content("")
        self.assertIsInstance(result, Item)

    def test_none_type_content(self):
        self.assertRaises(TypeError, self.item.set_content, None)

    def test_no_content(self):
        self.assertRaises(TypeError, self.item.set_content)
