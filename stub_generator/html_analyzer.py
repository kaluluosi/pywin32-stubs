
from cgitb import html
from email.policy import default
from functools import wraps
from typing import Any, Dict, Iterable, List, Sequence, Optional, Callable
from bs4 import BeautifulSoup
import os.path as path
from .util import doc_path, is_exist , type_cvt
from bs4.element import Tag
import re

def singleton(cls):
    _instance = {}

    @wraps(cls)
    def _singlenton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singlenton


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

    def __init__(self, method:'Method' , def_dt:Tag, desc_dd:Tag, duplicate_number:int=0):
        self._method = method
        self._param_name:str 
        self._param_types:str = ""

        strings = list(def_dt.strings)
        self._param_name = strings[0].strip()
        if len(strings) > 1:
            # 如果字符串大于1，则有可能有类型
            if ':' in strings[1]:
                # 如果字符串以：开头，就应该是类型
                self._param_types = strings[1].replace(':', '').strip()


        # 检查是否有默认值
        self._default = None
        if '=' in self._param_name:
            self._param_name, self._default = self._param_name.split('=')
            try:
                eval(self._default)
            except Exception as e:
                # 尝试eval一下这个默认值，如果eval不过，那么就可能是文档描述弃用
                self._default = None

        self._name = self._param_name.strip()
        self._type =list(set([ type_cvt(t) for t in re.split("/",self._param_types.strip())]))
        self._description = desc_dd.text.replace('\n', '')

        self._duplicate_number = duplicate_number

    @property
    def description(self):
        return self._description

    @property
    def duplicate_number(self) -> int:
        return self._duplicate_number

    @duplicate_number.setter
    def duplicate_number(self, value: int):
        self._duplicate_number = value
    
    @property
    def default(self) -> Any:
        return self._default

    @property
    def name(self) -> str:
        return f"{self._name}{self.duplicate_number if self.duplicate_number !=0 else ''}"

    @property
    def type(self) -> Sequence[str]:
        return self._type

    def __str__(self) -> str:
        if self._type:
            type_hint = f"Union[{','.join(self.type)}]" if len(self.type)>1 else f"{self.type[0]}"
            code = f"{self.name}:{type_hint}"
        else:
            code = f"{self.name}"

        if self.default:
            code += f"={self.default}"
        return code

class Method(Doc):

    def __init__(self,html_path:str,  name:str=None, module:'Module'=None):
        super(Method, self).__init__(html_path)
        self._module:Optional['Module'] = module
        self._name:str = name or ""
        self._description:str = ""
        self._paramters:Optional[Sequence[Paramter]] = None
        

    @property
    def docstring(self)->str:

        args_doc = '\n'.join(f"      {p.name}({','.join(p.type)}):{p.description}" for p in self.parameters)
        
        docstr = f"""{self.description}


Args:

{args_doc}

Returns:

      {self.return_type}{ ':'+self.return_desc if self.return_desc else '' }
        """
        return docstr

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
        
        if not param_start:
            # 意味着这个函数没有参数列表
            return []

        param_defines = param_start.find_next_siblings(['dt','dd'])        

        self._paramters = []

        def count(paramters:Iterable[Paramter], filter:Callable[[Paramter], bool]):
            c = 0
            for p in paramters:
                if filter(p):
                    c+=1
            return c

        for i in range(0, len(param_defines), 2):
            if i+1 >= len(param_defines):
                break
            def_dt:Tag = param_defines[i]
            desc_dd:Tag = param_defines[i+1]
            paramter = Paramter(self ,def_dt, desc_dd)
            duplicate_number = count(self._paramters, lambda p: p.name==paramter.name)
            paramter.duplicate_number = duplicate_number
            self._paramters.append(paramter)
        
        self._paramters.sort(key=lambda p:p.default!=None)

        return self._paramters

    @property
    def return_type(self) ->str:
        """
        返回类型
        """
        define = self.soup.body.p.text
        if '=' not in define:
            return "None"
        
        type = self.soup.body.p.text.split("=")[0].strip()
        return type_cvt(type)

    @property
    def return_desc(self)->str:
        """返回类型描述
        """
        result_set = self.soup.find_all('h3', text='Return Value')
        if result_set:
            dd:Tag = result_set[0].parent
            return dd.text
        return ""

    def __str__(self)->str:        
        method_head = f"def {self.name}({','.join([str(p) for p in self.parameters])}) -> {self.return_type}:"

        template = f'''
{method_head}
    """
    {self.docstring}
    """
    pass
'''
        return template

class ConstantList(Doc):

    def __init__(self, html_name:str)->None:
        super(ConstantList, self).__init__(html_name)

    def __iter__(self):
        contant_tag:Tag = self.soup.body.find('h1', text="Constants")

        while contant_tag:
            contant_tag = contant_tag.find_next('li')
            if not contant_tag:
                break
            
            yield Constant(contant_tag.a['href'])

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

    def __str__(self):
        return f"{self.name} = ..."

class ModuleList(Doc):

    def __init__(self, html_name:str) -> None:
        super(ModuleList, self).__init__(html_name)

    def __iter__(self):
        module_tag:Tag = self.soup.body.find('h1', text="Modules")
        
        while module_tag:
            module_tag = module_tag.find_next('li')
            if not module_tag:
                break
            
            yield Module(module_tag.a['href'])

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
        return self.soup.p.string.strip() if self.soup.p.string else ""

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

    def __str__(self):
        lines = []
        lines.append("from pywintypes import *")
        lines.append("import typing")
        lines.append(f'"""{self.description}"""')
        lines.append("")

        _all = []

        for method in self.methods:
            lines.append(str(method))
            _all.append(method.name)

        constant_list = ConstantList("constants.html")
        constant: Constant
        for constant in constant_list:
            if constant.module_name == self.name:
                lines.append(str(constant))
                _all.append(constant.name)

        lines.insert(1, f"__all__={_all}")
        return '\n'.join(lines)


class Object(Doc):

    def __init__(self, html_name:str) -> None:
        super(Object, self).__init__(html_name)


