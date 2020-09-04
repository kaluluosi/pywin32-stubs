
from cgitb import html
from typing import Dict, Iterable, List, Sequence, Optional
from bs4 import BeautifulSoup
import os.path as path
from .util import doc_path, is_exist 


from bs4.element import Tag


class Doc:

    def __init__(self, html_name:str):
        self.html_path = doc_path(html_name)
        with open(self.html_path) as html:
            self.soup = BeautifulSoup(html, 'lxml')
        self.doc_dir = path.dirname(html_name)

    @property
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    def description(self) -> str:
        raise NotImplementedError()

class Paramter:

    def __init__(self, def_dt:Tag, desc_dd:Tag):
        param_name:str
        param_types:str
        param_name, param_types = def_dt.text.strip().split(":")

        self._name = param_name.strip()
        self._type = param_types.strip().split('/')

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> Sequence[str]:
        return self._type

class Method(Doc):

    def __init__(self,html_path:str,  name:str=None, module:'Module'=None):
        super(Method, self).__init__(html_path)
        self._module:Optional[Module] = module
        self._name:str = name or ""
        self._description:str = ""
        self._paramters:Optional[Sequence[Paramter]] = None
        self._docstring = self.soup.text

    @property
    def docstring(self)->str:
        return self._docstring

    @property
    def name(self) -> str:
        """
        返回函数名
        """
        if self._name:
            return self._name
        else:
            self._name = self.soup.title.string.split('.')[1]
            return self._name

    @property
    def description(self) -> str:
        if self._description:
            return self._description
        self._description = self.soup.body.find_all('p')[1].string
        return self._description

    @property
    def module(self)->'Module':
        if self._module:
            return self._module

        html_name = self.soup.h1.a['href']
        self._module = Module(html_name)
        return self._module

    @property
    def parameters(self)-> Sequence[Paramter]:
        """
        返回参数
        """

        if self._paramters:
            return self._paramters

        param_start:Tag = self.soup.body.find('h3', text="Parameters")
        param_defines = param_start.find_next_siblings(['dt','dd'])        

        self._paramters = []

        for i in range(0, len(param_defines), 2):
            def_dt:Tag = param_defines[i]
            desc_dd:Tag = param_defines[i+1]
            self._paramters.append(Paramter(def_dt, desc_dd))

        return self._paramters

    @property
    def return_type(self) ->str:
        """
        返回类型
        """
        return self.soup.body.p.text.split("=")[0].strip()

class Module(Doc):

    MODULES:Dict[str, 'Module'] = {}

    def __init__(self, html_path: str):
        super(Module, self).__init__(html_path)
        self.MODULES[self.name] = self
        self._method_map: Dict[str, Method] = {}

    @property
    def name(self) -> str:
        """
        返回模块名
        """
        
        text = self.soup.h1.string
        return text.split(' ')[1]
    
    @property
    def description(self) -> str:
        return self.soup.p.string.strip()

    @property
    def methods(self) -> Iterable[Method]:
        if self._method_map:
            return self._method_map.values()
        
        method_dt_list = self.soup.dl.find_all('dt')

        for dt in method_dt_list:
            method_name = dt.a.string
            method_html_name = dt.a['href']
            if is_exist(method_html_name):
                method = Method(method_html_name,method_name, self)
                self._method_map[method_name] = method
                yield method

class Constant(Doc):

    def __init__(self, html_name:str) -> None:
        super(Constant, self).__init__(html_name)

    @property
    def name(self) -> str:
        return self.soup.h1.text
    
    @property
    def description(self) -> str:
        return self.soup.b.text
 
    @property
    def module_name(self):
        const_kw = 'const '
        start = self.description.index(const_kw) + len(const_kw)
        return self.description[start:].split('.')[0]


class ConstantDef(Doc):

    ...

