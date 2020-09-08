from typing import Dict, Iterable
from .doc import Doc
from bs4.element import Tag

class ConstantList(Doc):
    """
    实现单例模式,降低耗时
    """
    __instance = None
    __first_init = True

    def __init__(self, html_name:str)->None:
        if self.__first_init:
            super(ConstantList, self).__init__(html_name)
            self.cache:Dict[str, Constant] = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(cls)
        return cls.__instance

    def __iter__(self):
        contant_tag:Tag = self.soup.body.find('h1', text="Constants")

        while contant_tag:
            contant_tag = contant_tag.find_next('li')
            if not contant_tag:
                break

            html_name = contant_tag.a['href']
            if html_name not in self.cache:
                self.cache[html_name] = Constant(contant_tag.a['href'])
            yield self.cache[html_name]

class Constant(Doc):

    def __init__(self, html_name:str) -> None:
        super(Constant, self).__init__(html_name)
        self._name = self.soup.h1.text
        self._description = self.soup.b.text

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def description(self) -> str:
        return self._description
 
    @property
    def module_name(self):
        const_kw = 'const '
        start = self.description.index(const_kw) + len(const_kw)
        return self.description[start:].split('.')[0]

    def __str__(self):
        return f"{self.name} = ..."
