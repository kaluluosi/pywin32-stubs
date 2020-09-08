
import os
import shutil
from stub_generator.module import ModuleList
from stub_generator.object import ObjectList


if not os.path.isdir('win32-stubs'):
    os.mkdir('win32-stubs')

win32_object = ObjectList("win32_objects.html")
objects_file = os.path.join("win32-stubs","win32typing.py")
with open(objects_file, 'w', encoding='utf-8') as f:
    lines = []
    lines.append("from typing import *")
    _all = []
    for _class in win32_object:
        if not _class.name.endswith("*"):
            lines.append(str(_class))
            _all.append(_class.name)
            print(f"win32typing <<< {_class.name}")
    lines.insert(0, f"__all__={_all}\n")
    f.writelines(lines)



win32_modules = ModuleList("win32_modules.html")

for module in win32_modules:
    with open(os.path.join("win32-stubs", f"{module.name}.pyi"), 'w', encoding='utf8') as pyi:
        pyi.write(str(module))
        print(f"win32 <<< {module.name}")