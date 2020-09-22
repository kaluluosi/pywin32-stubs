from unittest import TestCase

from os import path
import sys
from unittest import main

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
        self.assertEqual(type_cvt('Object'), 'typing.Any')
        self.assertEqual(type_cvt('string'), 'str')

        self.assertEqual(type_cvt("PyHANDLE, PyHANDLE, int, int"), "typing.Tuple[int, int, int, int]")
        self.assertEqual(type_cvt("(int,int,int,int,string)"), "typing.Tuple[int, int, int, int, str]")

        self.assertEqual(type_cvt("[PyNETRESOURCE, ...]"), "typing.List[win32typing.PyNETRESOURCE]")
        self.assertEqual(type_cvt("(PyUnicode,...)"), "typing.Tuple[str, ...]")

        self.assertEqual(type_cvt("((str, str), ...)"), "typing.Tuple[typing.Tuple[str, str], ...]")