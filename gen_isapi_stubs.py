
import os
from stub_generator.module import ModuleList


if not os.path.isdir('isapi-stubs'):
    os.mkdir('isapi-stubs')

win32_modules = ModuleList("isapi_modules.html")

for module in win32_modules:
    with open(os.path.join("isapi-stubs", f"{module.name.split('.')[-1]}.pyi"), 'w', encoding='utf8') as pyi:
        if module.html_name == "isapi.html":
            continue
        pyi.write(str(module))
        print(f"isapi <<< {module.name}")


