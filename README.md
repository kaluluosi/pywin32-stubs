
# pywin32-stubs

> **⚠️ DEPRECATED**
>
> This package is no longer maintained. Use the official stubs package instead:
>
> ```shell
> pip install types-pywin32
> ```
>
> See: <https://pypi.org/project/types-pywin32/>

pywin32-stubs is generated from pywin32.chm, it contains:

- win32-stubs
- win32comext-stubs
- pythonwin-stubs
- win32helper : this package defines win32typing and constants.

vscode uninstalled stubs
![image](https://user-images.githubusercontent.com/1620585/187332660-19fab0a8-899a-4c3b-bdfa-e581312876f5.png)

vscode installed stubs
![image](https://user-images.githubusercontent.com/1620585/187332828-3903b028-e4a8-4ad1-b6b7-9d98966514d5.png)

## Installation

> **Deprecated.** Use [`types-pywin32`](https://pypi.org/project/types-pywin32/) instead.

```shell
pip install pywin32-stubs
```

## Usage

```python
import win32gui
import win32helper.win32con as con

win32gui.MessageBox(0, "hello", 'world', con.MB_OK)

```
