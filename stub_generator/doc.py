from bs4 import BeautifulSoup
import os.path as path
from .util import doc_path
from bs4.element import Tag


class Doc:

    def __init__(self, html_name:str):
        self.html_name = html_name
        self.html_path = doc_path(html_name)
        with open(self.html_path) as html:
            self.soup = BeautifulSoup(html, 'lxml')
        self.doc_dir = path.dirname(html_name)

    @property
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    def description(self) -> str:
        raise NotImplementedError()