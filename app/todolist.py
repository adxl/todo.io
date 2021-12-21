from datetime import date, datetime,timedelta
from typing import List
from app.Item import Item

class TodoList():
    __items:List[Item]
    __length:int=0
    __updated_at:datetime=None

    def __init__(self) -> None:
        self.__items = []
        self.__length = 0

    # items

    def get_items(self):
        return self.__items
    
    def set_item(self,item:Item):
        if not item or type(item) is not Item:
            raise TypeError()
        if self.verify_updated_at() is False:
            raise ValueError("Waiting 30 min")
        if self.verify_length() is False:
            raise ValueError("You have reached the limit of items in your list")
        self.__items.append(item)
        self.set_length()
        self.set_updated_at(updated_at=datetime.now())
        return self
        
    # length

    def get_length(self):
        return self.__length
    
    def set_length(self):
        self.__length = self.__length + 1
        return self
    
    def verify_length(self):
        if self.__length == 10: return False
        return True
    
    # updated_at

    def get_updated_at(self):
        return self.__updated_at
    
    def set_updated_at(self,updated_at:datetime):
        if not updated_at or type(updated_at) is not datetime:
            raise TypeError()
        self.__updated_at = updated_at
        return self
    
    def verify_updated_at(self):
        if(self.__updated_at is None): return True
        if((datetime.now() - timedelta(minutes = 30)) > self.__updated_at): return True
        return False