from bs4.element import Tag
from stub_generator.util import is_exist, type_cvt
from typing import Dict, Iterable
from .doc import Doc
from .callable import CallableBase

class Property:

    @staticmethod
    def is_validate_def(def_dt:Tag):
        def_str = def_dt.b.text.replace("unsigned", "").strip()
        return len(def_str.split(' '))>1

    def __init__(self, def_dt:Tag, desc_dd:Tag):
        def_str = def_dt.b.text.replace("unsigned", "").strip()
        if not self.is_validate_def(def_dt):
            raise Exception(f"{def_dt.text} is no a valide property define!")
        self._type = ''.join(def_str.split(' ')[0:-1])
        self._name = def_str.split(' ')[-1]
        self._type = type_cvt(self._type)
        self._description = desc_dd.text.replace('\n','')

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def description(self):
        return self._description 

    def __str__(self):

        template = f'''
      @property
      def {self.name}(self)->'{self.type}':
         """{self.description}"""
         pass
'''
        return template

class Method(CallableBase):

    def __init__(self, html_name:str, name:str=None, _class:'Class'=None):
        super(Method, self).__init__(html_name, name)
        self._class = _class

    @property
    def cls(self):
        # 返回这个函数从属的class对象
        if self._class:
            return self._class
        return None

    def __str__(self):
        method_head = f"def {self.name}(self,{','.join([str(p) for p in self.parameters])}) -> '{self.return_type}':"
        template = f'''
      {method_head}
         """
         {self.docstring}
         """
         pass
'''
        return template

class Class(Doc):

    all_classes:Dict[str, 'Class'] = {}

    def __init__(self, html_name:str) -> None:
        super(Class, self).__init__(html_name)
        self._method_map:Dict[str, Method] = {}
        self._properties_map:Dict[str, Property] = {}

    @property
    def name(self) -> str:
        """
        返回类名
        """
        
        text = self.soup.h1.string
        return text.split(' ')[0]

    @property
    def description(self) -> str:
        return self.soup.p.string.strip() if self.soup.p.string else ""

    @property
    def methods(self) -> Iterable[Method]:
        if self._method_map:
            return self._method_map

        method_tag:Tag = self.soup.body.find('h3', text="Methods")

        if method_tag:
            method_dl:Tag = method_tag.find_next('dl')
            method_dt_list = method_dl.find_all('dt')

            for dt in method_dt_list:
                method_name:str = dt.a.string

                if method_name.startswith("__") or method_name.startswith("_"):
                    continue

                method_html_name = dt.a['href']
                if is_exist(method_html_name):
                    method = Method(method_html_name,method_name, self)
                    if method.name in self._method_map:
                        continue
                    self._method_map[method_name] = method
                    yield method

    @property
    def properties(self) -> Iterable[Property]:
        if self._properties_map:
            return self._properties_map

        property_tag:Tag = self.soup.body.find('h3', text="Properties")

        if property_tag:
            property_dl:Tag = property_tag.find_next('dl')
            property_dt_list = property_dl.find_all('dt', recursive=False)

            for def_dt in property_dt_list:
                if Property.is_validate_def(def_dt):
                    desc_dd = def_dt.find_next('dd')
                    property = Property(def_dt, desc_dd)
                    if property.name in self._properties_map:
                        continue
                    self._properties_map[property.name] = property
                    yield property

    def __str__(self):
        lines = ["\n"]
        lines.append(f"class {self.name}(object):")
        lines.append(f'      """{self.description}"""')
        lines.append("")
        lines.append("      def __new__(cls):")
        lines.append("""         raise Exception('This class just for typing, can not be instanced!')""")
        lines.append("")

        property_add = []
        for property in self.properties:
            if property.name not in property_add:
                lines.append(str(property))
                property_add.append(property)

        method_added = []
        for method in self.methods:
            if method.name not in method_added:
                lines.append(str(method))
                method_added.append(method.name)

        return '\n'.join(lines)

class ObjectList(Doc):

    """解析整个Objects页面的所有Class
    """

    def __init__(self, html_name:str) -> None:
        super(ObjectList, self).__init__(html_name)

    
    def __iter__(self):
        object_tag = self.soup.body.find('h1', text="Objects")

        while object_tag:
            object_tag = object_tag.find_next('li')
            if not object_tag:
                break

            if '.' in object_tag.text:
                continue

            yield Class(object_tag.a['href'])