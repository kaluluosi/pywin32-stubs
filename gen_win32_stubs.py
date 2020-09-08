
import os
import shutil
from stub_generator.module import ModuleList
from stub_generator.object import ObjectList


if not os.path.isdir('win32-stubs'):
    os.mkdir('win32-stubs')

win32_modules = ModuleList("win32_modules.html")

for module in win32_modules:
    with open(os.path.join("win32-stubs", f"{module.name}.pyi"), 'w', encoding='utf8') as pyi:
        pyi.write(str(module))
        print(f"win32 <<< {module.name}")


