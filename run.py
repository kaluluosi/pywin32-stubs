
import os
from stub_generator.html_analyzer import *


win32_modules = ModuleList("win32_modules.html")

if not path.isdir('win32-stubs'):
    os.mkdir('win32-stubs')


for module in win32_modules:

    with open(path.join("win32-stubs", f"{module.name}.pyi"), 'w', encoding='utf8') as pyi:
        pyi.write(str(module))
