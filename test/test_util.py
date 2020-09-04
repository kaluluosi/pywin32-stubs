from unittest import TestCase

from os import path

from stub_generator.util import doc_path, is_exist

class UtilTest(TestCase):

    def test_doc_path(self):
        self.assertTrue(path.exists(doc_path("win32api.html")), "文档路径存在")

    def test_is_exist(self):
        self.assertTrue(is_exist("win32api.html"), "文档存在")