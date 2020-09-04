
from typing import Dict, Iterable, List
from bs4 import BeautifulSoup
import os.path as path

DOC_PATH: str = path.join(path.dirname(__file__), "..", "pywin32docs")
def doc_path(html_name: str)->str:
    return path.join(DOC_PATH, html_name)

class Doc:

    def __init__(self, html_name:str):
        self.html_path = doc_path(html_name)
        self.soup = BeautifulSoup(open(self.html_path), 'lxml')
        self.doc_dir = path.dirname(html_name)

    @property
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    def description(self) -> str:
        raise NotImplementedError()

class value:

    def name(self):
        raise NotImplementedError()

    def type(self):
        raise NotImplementedError()

class Method(Doc):

    def __init__(self,html_path:str,  name:str=None, module:'Module'=None):
        super(Method, self).__init__(html_path)
        self._module = module
        self._name = name
        self._description = ""
        self._module = module

    def name(self):
        """
        返回函数名
        """
        if self._name:
            return self._name
        else:
            self._name = self.soup.body.h1.a.string.strip('.')
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

    def parameters(self):
        """
        返回参数
        """
        raise NotImplementedError()


class Module(Doc):

    MODULES:Dict[str, 'Module'] = {}

    def __init__(self, html_path: str):
        super(Module, self).__init__(html_path)
        self.MODULES[self.name] = self
        self.method_map: Dict[str, Method] = {}

    @property
    def name(self) -> str:
        """
        返回模块名
        """
        
        text = self.soup.h1.string
        return text.split(' ')[1]
    
    def description(self) -> str:
        return self.soup.p.string

    @property
    def methods(self) -> Iterable[Method]:
        if self.method_map:
            return self.method_map.values()
        
        method_dt_list = self.soup.dl.find_all('dt')

        for dt in method_dt_list:
            method_name = dt.a.string
            method_html_path = dt.a['href']
            method = Method(method_name, self,method_html_path)
            self.method_map[method_name] = method
            yield method

class Constant(Doc):

    def name(self):
        ...


class ConstantDef(Doc):

    ...

if __name__ == "__main__":
    
    method = Method('C:/Users/Administrator/Desktop/win32stubs/pywin32docs/win32api__InitiateSystemShutdown_meth.html')
    print(method.description)
    print(method.module.name)