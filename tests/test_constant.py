from unittest import TestCase, skip
from stub_generator.constant import Constant, ConstantList


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