from unittest import TestCase
from unittest.mock import Mock
from stub_generator.constant import Constant, ConstantList
from stub_generator.function import Function
from stub_generator.module import Module, ModuleList

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
        
        self.assertGreater(len(list(self.module.functions)), 0, "函数数量大于0")

        for method in self.module.functions:
            self.assertEqual(method.name, "AbortSystemShutdown", "函数名字正确")
            pass

class ModuleListTest(TestCase):

    def setUp(self) -> None:
        self.module_list = ModuleList("win32_modules.html")

    def test_get_modules(self):
        module_list = list(self.module_list)
        self.assertEqual(len(module_list), 34, "解析模块数量正确")

