from pygments.formatters.other import TestcaseFormatter
from typed_ast.ast27 import Param
from stub_generator.html_analyzer import Constant, ConstantList, Method, Module, ModuleList, Paramter
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
                "type":["typing.Any"],
                "desc":"An object which will be called when a win32 \n\nexception occurs."
            },
            {
                "name":"func",
                "type":["typing.Any"],
                "desc":"The function call call under the protection of the Win32 \n\nexception handler."
            },
            {
                "name":"args",
                "type":["tuple"],
                "desc":"Args for the function."
            },
        ]
        
        for index, param in enumerate(self.method.parameters):
            self.assertEqual(param.name, param_results[index]["name"], "参数名")
            self.assertEqual(param.type, param_results[index]["type"], "类型名")
            self.assertIsNotNone(param.description, "描述")

    def test_return_type(self):

        self.assertEqual(self.method.return_type, "typing.Any", '返回类型')

    def test_no_return(self):
        method = Method("win32api__AbortSystemShutdown_meth.html")
        self.assertEqual(method.return_type, "None","无返回值")

    def test_no_paramlist_method(self):

        method = Method("win32api__DebugBreak_meth.html")
        self.assertFalse(method.parameters, "参数列表为空")

    def test_paramter_no_type(self):
        method = Method("win32api__FormatMessage_meth.html")
        self.assertTrue(method.parameters, "参数解析正常")

    def test_duplicate_paramter(self):

        method = Method("win32api__SetStdHandle_meth.html")
        for i, p in enumerate(method.parameters):
            self.assertEqual(p.duplicate_number, i, "重复变量名编号")


class ConstantTest(TestCase):

    def setUp(self) -> None:
        self.constant = Constant("mapi_CCSF_NO_MSGID.html")
    
    def test_get_name(self):
        self.assertEqual(self.constant.name, 'CCSF_NO_MSGID', "名字匹配")

    def test_get_description(self):
        self.assertEqual(self.constant.description, 'const mapi.CCSF_NO_MSGID;')

    def test_get_module_name(self):
        self.assertEqual(self.constant.module_name, 'mapi')

class ConstantListTest(TestCase):

    def setUp(self) -> None:
        self.constant_list = ConstantList("constants.html")

    def test_get_constants(self):
        constant_list = list(self.constant_list)
        self.assertGreater(len(constant_list), 0, "解析常亮数量正确")


class ModuleListTest(TestCase):

    def setUp(self) -> None:
        self.module_list = ModuleList("win32_modules.html")

    def test_get_modules(self):
        module_list = list(self.module_list)
        self.assertEqual(len(module_list), 34, "解析模块数量正确")