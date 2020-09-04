from os import path


DOC_PATH: str = path.join(path.dirname(__file__), "..", "pywin32docs")
def doc_path(html_name: str)->str:
    return path.join(DOC_PATH, html_name)

def is_exist(html_name:str) -> bool:
    return path.exists(doc_path(html_name))