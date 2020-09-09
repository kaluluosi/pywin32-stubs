from unittest import TestCase
from stub_generator.constant import Constant, ConstantList
from stub_generator.function import Function
from stub_generator.module import Module, ModuleList

class FunctionTest(TestCase):
    """测试Method类

    Args:
        TestCase ([type]): [description]
    """

    def setUp(self) -> None:
        self.method = Function("win32api__Apply_meth.html")

    
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
                "type":"Any",
                "desc":"An object which will be called when a win32 \n\nexception occurs."
            },
            {
                "name":"func",
                "type":"Any",
                "desc":"The function call call under the protection of the Win32 \n\nexception handler."
            },
            {
                "name":"args",
                "type":"tuple",
                "desc":"Args for the function."
            },
        ]
        
        for index, param in enumerate(self.method.parameters):
            self.assertEqual(param.name, param_results[index]["name"], "参数名")
            self.assertEqual(param.type, param_results[index]["type"], "类型名")
            self.assertIsNotNone(param.description, "描述")

        func = Function("win32api__FindFiles_meth.html")
        paramters = list(func.parameters)
        self.assertEqual(len(paramters), 1)
        self.assertEqual(paramters[0].name, 'fileSpec')
        self.assertEqual(paramters[0].type, 'str')

        func = Function("win32file__GetFileAttributesEx_meth.html")
        paramters = list(func.parameters)
        self.assertEqual(len(paramters), 3)
        self.assertEqual(paramters[0].name, 'FileName')
        self.assertEqual(paramters[0].type, 'str')
        self.assertEqual(paramters[1].name, 'InfoLevelId')
        self.assertEqual(paramters[1].type, 'int')
        self.assertEqual(paramters[2].name, 'Transaction')
        self.assertEqual(paramters[2].type, 'int')

        func = Function("win32gui__ExtFloodFill_meth.html")
        paramters = list(func.parameters)
        self.assertEqual(len(paramters), 5)
        self.assertEqual(paramters[0].name, 'arg')
        self.assertEqual(paramters[0].type, 'int')
        self.assertEqual(paramters[1].name, 'XStart')
        self.assertEqual(paramters[1].type, 'int')
        self.assertEqual(paramters[2].name, 'YStart')
        self.assertEqual(paramters[2].type, 'int')
        self.assertEqual(paramters[3].name, 'Color')
        self.assertEqual(paramters[3].type, 'int')
        self.assertEqual(paramters[4].name, 'FillType')
        self.assertEqual(paramters[4].type, 'int')

    def test_return_type(self):

        self.assertEqual(self.method.return_type, "Any", '返回类型')

    def test_no_return(self):
        method = Function("win32api__AbortSystemShutdown_meth.html")
        self.assertEqual(method.return_type, "None","无返回值")

    def test_no_paramlist_method(self):

        method = Function("win32api__DebugBreak_meth.html")
        self.assertFalse(method.parameters, "参数列表为空")

    def test_paramter_no_type(self):
        method = Function("win32api__FormatMessage_meth.html")
        self.assertTrue(method.parameters, "参数解析正常")

    def test_duplicate_paramter(self):

        method = Function("win32api__SetStdHandle_meth.html")
        for i, p in enumerate(method.parameters):
            self.assertEqual(p.duplicate_number, i, "重复变量名编号")

    def test_get_module(self):
        self.assertIsNotNone(self.method.module, "module 不为空")
        self.assertEqual(self.method.module.name, "win32api", "模块名匹配")
