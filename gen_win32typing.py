import os
import shutil
from stub_generator.module import ModuleList
from stub_generator.object import ObjectList


win32_objects = ObjectList("win32_objects.html")
win32com_object = ObjectList("com_objects.html")
pythonwin_objects = ObjectList("pythonwin_objects.html")
isapi_objects = ObjectList("isapi_objects.html")


objects_file = os.path.join("stub_generator","win32typing.py")
with open(objects_file, 'w', encoding='utf-8') as f:
    lines = []
    lines.append("import typing")
    _all = ['']
    for _class in win32_objects:
        if not _class.name.endswith("*"):
            lines.append(str(_class))
            _all.append(_class.name)
            print(f"win32typing <<< {_class.name}")
    for _class in win32com_object:
        if not _class.name.endswith("*"):
            lines.append(str(_class))
            _all.append(_class.name)
            print(f"win32typing <<< {_class.name}")
    for _class in pythonwin_objects:
        if not _class.name.endswith("*"):
            lines.append(str(_class))
            _all.append(_class.name)
            print(f"pythonwin <<< {_class.name}")
    for _class in isapi_objects:
        if not _class.name.endswith("*"):
            lines.append(str(_class))
            _all.append(_class.name)
            print(f"isapi <<< {_class.name}")

    lines.insert(0, f"__all__={_all}\n")
    f.writelines(lines)


shutil.copy(objects_file, os.path.join("win32helper", "win32typing.py"))

