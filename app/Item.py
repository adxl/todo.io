class Item:
    def __init__(self, name: str, content: str = "") -> None:
        self.set_name(name=name)
        self.set_content(content=content)

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not name or type(name) is not str:
            raise TypeError()
        self.__name = name

        return self

    def get_content(self):
        return self.__content

    def set_content(self, content: str):
        if (not content and content is None) or type(content) is not str:
            raise TypeError()
        if len(content) > 1000:
            raise ValueError()
        self.__content = content

        return self
