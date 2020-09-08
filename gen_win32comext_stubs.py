import os
import shutil
from stub_generator.module import ModuleList
from stub_generator.object import ObjectList


if not os.path.isdir('win32comext-stubs'):
    os.mkdir('win32comext-stubs')

win32_modules = ModuleList("com_modules.html")

for module in win32_modules:
    with open(os.path.join("win32comext-stubs", f"{module.name}.pyi"), 'w', encoding='utf8') as pyi:
        pyi.write(str(module))
        print(f"win32comext <<< {module.name}")

