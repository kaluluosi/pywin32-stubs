from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, TYPE_CHECKING
import builtins

from .util import doc_path, is_exist , type_cvt
from bs4.element import Tag
from .doc import Doc
import keyword
import re

class Paramter:

    @staticmethod
    def _is_unrecognized_name(name:str) -> bool:
        """是否无法识别的名字"""
        for c in "[]().,":
            if c in name:
                return True
        return False

    @staticmethod
    def _is_keyword(name:str) -> bool:
        if name in keyword.kwlist:
            return True
        elif name in ["object"]:
            return True
        elif name in builtins.__dict__:
            return True
        else:
            return False

    def __init__(self, def_dt:Tag, desc_dd:Tag, duplicate_number:int=0):
        self._param_name:str 
        self._param_types:str = ""

        strings = list(def_dt.strings)
        self._param_name = strings[0]

        if self._is_unrecognized_name(self._param_name):
            self._param_name = "arg"
        else:
            self._param_name = self._param_name.strip().replace(" ","_")

        if len(strings) > 1:
            # 如果字符串大于1，则有可能有类型
            if ':' in def_dt.text:
                # 如果字符串以：开头，就应该是类型
                self._param_types = def_dt.text.split(':')[1].strip()

        # 检查是否有默认值
        self._default = None
        if '=' in self._param_name:
            self._param_name, self._default = self._param_name.split('=')
            try:
                eval(self._default)
            except Exception as e:
                # 尝试eval一下这个默认值，如果eval不过，那么就可能是文档描述弃用
                self._default = None

        self._name = self._param_name.strip().replace('/', '_') or 'arg'
        # 如果名字跟关键字冲突
        if self._is_keyword(self._name):
            self._name = '_'+self._name

        if self._name.startswith("[") and self._name.endswith("...]"):
            self._name = self._name.replace('[','').split(',')[0]

        self._type =type_cvt(self._param_types.strip())
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
    def type(self) -> str:
        return self._type

    def __str__(self) -> str:
        if self._type:
            code = f"{self.name}:'{self.type}'"
        else:
            code = f"{self.name}"

        if self.default:
            code += f"={self.default}"
        return code


class CallableBase(Doc):

    def __init__(self, html_path:str,  name:str=None) -> None:
        super(CallableBase, self).__init__(html_path)
        self._name:str = name or ""
        self._description:str = ""
        self._paramters:Optional[Sequence[Paramter]] = None

    @property
    def docstring(self)->str:

        args_doc = '\n'.join(f"      {p.name}({p.type}):{p.description}" for p in self.parameters)
        docstr = f"""{self.description}

Args:

{args_doc}

Returns:

      {self.return_type}{ ':'+self.return_desc if self.return_desc else '' }
        """
        return docstr

    @property
    def parameters(self)-> Sequence[Paramter]:
        """
        返回参数
        """

        if self._paramters:
            return self._paramters

        paramter_tag:Tag = self.soup.body.find('h3', text="Parameters")
        
        self._paramters = []
        if paramter_tag:
            def_dt:Tag = paramter_tag.find_next_sibling('dt')

            param_counter:Dict[str, int] = {}
            while def_dt:
                desc_dd:Tag = def_dt.find_next_sibling('dd')
                if desc_dd == None:
                    # 意味着这个dt不是参数
                    break

                paramter = Paramter(def_dt, desc_dd)
                # 参数计数，用来解决同名变量问题
                if paramter.name not in param_counter:
                    param_counter[paramter.name] = 0
                else:
                    param_counter[paramter.name] += 1
                
                paramter.duplicate_number = param_counter[paramter.name]
                self._paramters.append(paramter)

                def_dt = desc_dd.find_next_sibling('dt', recursive=False)
        
        self._paramters.sort(key=lambda p:p.default!=None)

        return self._paramters


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
    def return_type(self) ->str:
        """
        返回类型
        """
        define = self.soup.body.p.text
        if '=' not in define:
            return "None"
        
        type_str:str = self.soup.body.p.text.split("=")[0].strip()
        return type_cvt(type_str)

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
        raise NotImplementedError()
