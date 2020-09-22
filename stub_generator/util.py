import builtins
from os import path
import typing
from typing import Any, Dict, Iterable, Sequence, Union
import win32helper.win32typing as win32typing


DOC_PATH: str = path.join(path.dirname(__file__), "..", "pywin32docs")


def doc_path(html_name: str) -> str:
    return path.join(DOC_PATH, html_name)


def is_exist(html_name: str) -> bool:
    return path.exists(doc_path(html_name))

def list2str(seq:Sequence[str]):
    return f"{seq}".replace("'","")


def type_cvt(type_name: Union[str, Sequence[str]]) -> str:
    # print(type_name)

    if isinstance(type_name, str):
        type_name = type_name.strip()

        if type_name.startswith("[") and type_name.endswith("...]"):

            return f"typing.List[{type_cvt(type_name[1:-6])}]"
        elif ',' in type_name:
            type_name = type_name.replace(r"(", "").replace(r")", "")
            type_names = type_name.replace(' ', '').split(',')
            
            more = None
            if "..." in type_names:
                more = type_names.pop()
            
            if more:
                _types = type_cvt(','.join(type_names))
                return f"typing.Tuple[{list2str(_types)}, ...]"
            else:
                types = [type_cvt(type_name.strip()) for type_name in type_names]
                return f"typing.Tuple{list2str(types)}"
        elif '/' in type_name:
            return type_cvt(type_name.split('/'))

        type_map: Dict[str, Any] = {}
        type_map.update(builtins.__dict__)

        custom_cvt = {
            "string": "str",
            "object": "typing.Any",
            "PyHANDLE": "int",
            "PyUnicode": "str",
            "int tuple": "typing.Tuple[int]",
            "integer":"int",
            "character":"str",
            "any":"typing.Any",
        }
        
        if type_name in custom_cvt:
            return custom_cvt[type_name]
        elif type_name in typing.__dict__:
            return "typing."+type_name
        elif type_name in win32typing.__dict__:
            return "win32typing."+type_name
        elif type_name in builtins.__dict__:
            return type_name

        return "typing.Any"
    elif isinstance(type_name, Iterable):
        if len(type_name) > 1:
            types = []
            for name in type_name:
                types.append(type_cvt(name))
            # 去个重
            types = list(set(types))
            return f"typing.Union{list2str(types)}"
        else:
            return type_cvt(type_name[0])

    return "typing.Any"
