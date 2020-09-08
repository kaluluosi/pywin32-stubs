from typing import List
import unittest
from stub_generator.object import Class, Method, ObjectList, Property


class ClassTest(unittest.TestCase):


    def setUp(self):
        self._class = Class('PyCERT_CONTEXT.html')


    def test_get_class_name(self):
        self.assertEqual(self._class.name, "PyCERT_CONTEXT", "解析的名字不匹配")

    def test_get_class_description(self):
        self.assertEqual(self._class.description, "Handle to a certificate context", "解析的描述不匹配")

    def test_get_methods(self):

        self.assertGreater(len(list(self._class.methods)), 0, "解析的方法数量不正确")
        for method in self._class.methods:
            self.assertEqual(method.name, "CertFreeCertificateContext", "第一个方法名字不正确")

    def test_no_method_class(self):
        _class = Class("COMMTIMEOUTS.html")
        self.assertEqual(list(_class.methods),[], "应该没有方法")

    def test_get_class_properties(self):
        _class = Class("FORM_INFO_1.html")
        property_list:List[Property] = list(_class.properties)
        self.assertGreater(len(property_list), 0, "属性数量应该大于0")
        self.assertEqual(property_list[0].name, "Flags", "名字不匹配")
        self.assertEqual(property_list[1].name, "Name", "名字不匹配")
        self.assertEqual(property_list[2].name, "Size", "名字不匹配")
        self.assertEqual(property_list[3].name, "ImageableArea", "名字不匹配")
        self.assertEqual(property_list[0].type, "int", "名字不匹配")
        self.assertEqual(property_list[1].type, "str", "名字不匹配")
        self.assertEqual(property_list[2].type, "dict", "名字不匹配")
        self.assertEqual(property_list[3].type, "dict", "名字不匹配")

    def test_properties_method(self):
        _class = Class("PyHANDLE.html")
        property_list:List[Property] = list(_class.properties)
        method_list:List[Method] = list(_class.methods)
        self.assertEqual(len(property_list), 1)
        self.assertEqual(len(method_list), 3)

class MethodTest(unittest.TestCase):
    """
    测试Method解析是否正确
    """

    def setUp(self) -> None:
        self.method = Method('PyCERT_CONTEXT__CryptAcquireCertificatePrivateKey_meth.html')

    def test_method_name(self):
        self.assertEqual(self.method.name, "CryptAcquireCertificatePrivateKey", "第一个方法名字不正确")

    def test_metho_description(self):
        self.assertEqual(self.method.description, "Retrieves the private key associated \n\nwith the certificate", "描述不匹配")

    def test_method_paramters(self):
        self.assertEqual(len(list(self.method.parameters)), 1, "参数不匹配")

    def test_method_return_type(self):
        self.assertEqual(self.method.return_type, "Tuple[int, PyCRYPTPROV]", "返回类型不正确")

    def test_multi_paramter_type(self):
        method = Method("win32file__ReadFile_meth.html")
        paramters = list(method.parameters)
        self.assertEqual(paramters[0].name, "hFile")
        self.assertEqual(paramters[1].name, 'buffer_bufSize')
        self.assertEqual(paramters[2].name, 'overlapped')

    def test_return_items(self):
        method = Method("PyACL__GetAce_meth.html")
        paramters = list(method.parameters)
        self.assertEqual(len(paramters), 1)
        self.assertEqual(paramters[0].name, 'index')
        self.assertEqual(paramters[0].type, 'int')

class ObjectListTest(unittest.TestCase):

    def setUp(self):
        self.object_list = ObjectList("win32_objects.html")


    def test_get_classes(self):
        object_list = list(self.object_list)
        self.assertGreater(len(object_list),100, "理应超过100个类" )