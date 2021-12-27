from datetime import datetime, timedelta

from app.email_sender import EmailSender as es
from app.Item import Item


class TodoList:
    def __init__(self, owner) -> None:
        self.__owner = owner
        self.__items = set()
        self.__updated_at = datetime.now() - timedelta(minutes=30)

    def get_owner(self):
        return self.__owner

    def get_items(self):
        return self.__items

    def add_item(self, item: Item):
        if not item or type(item) is not Item:
            raise TypeError()
        if self.verify_updated_at() is False:
            raise ValueError("Waiting 30 min")

        if self.verify_length() is False:
            raise ValueError("Too many items")

        if any(_item for _item in self.__items if item.get_name() == _item.get_name()):
            raise ValueError("Item already exists")

        self.__items.add(item)
        self.set_updated_at(updated_at=datetime.now())

        if self.get_length() == 8:
            es.send(self.__owner)

        return self

    def get_length(self):
        return len(self.__items)

    def verify_length(self):
        return len(self.__items) != 10

    def get_updated_at(self):
        return self.__updated_at

    def set_updated_at(self, updated_at: datetime):
        if not updated_at or type(updated_at) is not datetime:
            raise TypeError()
        self.__updated_at = updated_at
        return self

    def verify_updated_at(self):
        return datetime.now() - timedelta(minutes=30) > self.__updated_at
