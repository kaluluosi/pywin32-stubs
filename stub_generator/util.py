from os import path
import typing
from typing import Any, Dict
import pywintypes
import builtins


DOC_PATH: str = path.join(path.dirname(__file__), "..", "pywin32docs")
def doc_path(html_name: str)->str:
    return path.join(DOC_PATH, html_name)

def is_exist(html_name:str) -> bool:
    return path.exists(doc_path(html_name))



def type_cvt(type_name:str) -> str:
    convert_map:Dict[str, Any] = {}
    convert_map.update(builtins.__dict__)

    convert_map.update({
        "string":"str",
        "PyHANDLE":"int",
        "PyUnicode":"str",
        "PyResourceId ":"int",
        "object":"typing.Any",
        "None":"None",
        "int tuple":"typing.Tuple[int]"
    })


    if type_name in convert_map:
        match = convert_map[type_name]
        if isinstance(match, type):
            return match.__name__
        elif isinstance(match, str):
            return match

    return "typing.Any"
