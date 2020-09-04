from typed_ast.ast27 import Param
from stub_generator.html_analyzer import Constant, Method, Module, Paramter
from unittest import TestCase
from unittest.mock import Mock
from stub_generator.html_analyzer import Module


class ModuleTest(TestCase):
    """测试Module类

    Args:
        TestCase ([type]): [description]
    """

    def setUp(self) -> None:
        self.module = Module("win32api.html")

    def test_get_name(self):
        self.assertEqual(self.module.name, "win32api", "获取模块名")

    def test_get_description(self):
        self.assertEqual(self.module.description, "A module, encapsulating the Windows Win32 API.", "获取模块描述")

    def test_get_methods(self):
        
        self.assertGreater(len(list(self.module.methods)), 0, "函数数量大于0")

        for method in self.module.methods:
            self.assertEqual(method.name, "AbortSystemShutdown", "函数名字正确")
            pass

class MethodTest(TestCase):
    """测试Method类

    Args:
        TestCase ([type]): [description]
    """

    def setUp(self) -> None:
        self.method = Method("win32api__Apply_meth.html")

    
    def test_get_name(self):
        self.assertEqual(self.method.name, "Apply", "名字不匹配")

    def test_get_description(self):
        self.assertEqual(self.method.description, "Calls a Python function, but traps Win32 exceptions.", "函数描述不匹配")

    
    def test_get_paramters(self):
        """这个用例相当于把Paramter也测试了
        """

        param_results = [
            {
                "name":"exceptionHandler",
                "type":["object"]
            },
            {
                "name":"func",
                "type":["object"]
            },
            {
                "name":"args",
                "type":["tuple"]
            },
        ]
        
        for index, param in enumerate(self.method.parameters):
            self.assertEqual(param.name, param_results[index]["name"], "参数名")
            self.assertEqual(param.type, param_results[index]["type"], "类型名")

    def test_return_type(self):

        self.assertEqual(self.method.return_type, "object", '返回类型')


class ConstantTest(TestCase):

    def setUp(self) -> None:
        self.constant = Constant("mapi_CCSF_NO_MSGID.html")
    
    def test_get_name(self):
        self.assertEqual(self.constant.name, 'CCSF_NO_MSGID', "名字匹配")

    def test_get_description(self):
        self.assertEqual(self.constant.description, 'const mapi.CCSF_NO_MSGID;')

    def test_get_module_name(self):
        self.assertEqual(self.constant.module_name, 'mapi')