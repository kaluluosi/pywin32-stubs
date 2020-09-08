from bs4.element import Tag
from .constant import Constant, ConstantList
from .util import is_exist
from typing import Dict, Iterable
from .doc import Doc
from .function import Function


class Module(Doc):

    all_modules:Dict[str, 'Module'] = {}

    def __init__(self, html_path: str):
        super(Module, self).__init__(html_path)
        self.all_modules[html_path] = self
        self._method_map: Dict[str, 'Function'] = {}

    @property
    def name(self) -> str:
        """
        返回模块名
        """
        
        text = self.soup.h1.string
        return text.split(' ')[1]
    
    @property
    def description(self) -> str:
        return self.soup.p.string.strip() if self.soup.p.string else ""

    @property
    def functions(self) -> Iterable['Function']:
        if self._method_map:
            return self._method_map.values()
        
        function_dt_list = self.soup.dl.find_all('dt')

        for dt in function_dt_list:
            method_name = dt.a.string
            method_html_name = dt.a['href']
            if is_exist(method_html_name):
                method = Function(method_html_name,method_name, self)
                self._method_map[method_name] = method
                yield method

    def __str__(self):
        lines = []
        lines.append("from typing import *")
        lines.append("from .win32typing import *")
        lines.append(f'"""{self.description}"""')
        lines.append("")

        _all = []

        for function in self.functions:
            lines.append(str(function))
            _all.append(function.name)

        constant_list = ConstantList("constants.html")
        constant: Constant
        for constant in constant_list:
            if constant.module_name == self.name:
                lines.append(str(constant))
                _all.append(constant.name)

        lines.insert(0, f"__all__={_all}")
        return '\n'.join(lines)

class ModuleList(Doc):
    """
    解析整个Module页的所有Module
    """

    def __init__(self, html_name:str) -> None:
        super(ModuleList, self).__init__(html_name)

    def __iter__(self):
        module_tag:Tag = self.soup.body.find('h1', text="Modules")
        
        while module_tag:
            module_tag = module_tag.find_next('li')
            if not module_tag:
                break
            
            yield Module(module_tag.a['href'])

