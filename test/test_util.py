from unittest import TestCase

from os import path

from stub_generator.util import doc_path, is_exist, type_cvt

class UtilTest(TestCase):

    def test_doc_path(self):
        self.assertTrue(path.exists(doc_path("win32api.html")), "文档路径存在")

    def test_is_exist(self):
        self.assertTrue(is_exist("win32api.html"), "文档存在")


    def test_type_convert(self):

        doc_types = [
            "PyHANDLE",
            "string",
            "object",
            "tuple"
        ]

        self.assertEqual(type_cvt('tuple'), 'tuple')
        self.assertEqual(type_cvt('PyHANDLE'), 'int')
        self.assertEqual(type_cvt('object'), 'typing.Any')
        self.assertEqual(type_cvt('string'), 'str')