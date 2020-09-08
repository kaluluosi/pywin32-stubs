from typing import Any, TYPE_CHECKING

from .callable import CallableBase


if TYPE_CHECKING:
    # type checking 的时候会导入, 非typing 的时候不导入
    # 用来解决type checking 的时候循环导入报错问题
    # 注意：这种方式包起来，只能用字符串类型声明
    from .module import Module


class Function(CallableBase):
    """Method文档解析类
    """

    def __init__(self,html_path:str,  name:str=None, module:'Module'=None):
        super(Function, self).__init__(html_path, name)
        self._module = module
        

    @property
    def module(self)->'Module':
        if self._module:
            return self._module

        # 如果_module没有赋值,那么这个method就是直接通过meth.html 解析出来的
        html_name = self.soup.h1.a['href']
        
        # 延迟导入
        from .module import Module

        # 先从module缓存里找
        if html_name in Module.all_modules:
            self._module = Module.all_modules[html_name]
            return self._module

        # 没找到就用解析出来的module文档名创建一个
        self._module = Module(html_name)
        return self._module

    def __str__(self) -> str:

        method_head = f"def {self.name}({','.join([str(p) for p in self.parameters])}) -> '{self.return_type}':"

        template = f'''
{method_head}
    """
    {self.docstring}
    """
    pass
        '''
        return template