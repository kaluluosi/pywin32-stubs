pywin32-stubs
=============

pywin32-stubs is generated from pywin32.chm, it contains: - win32-stubs
- win32comext-stubs - pythonwin-stubs - win32helper : this package
defines win32typing and constants.

Installation
============

    pip install pywin32-stubs

Usage
=====

.. code:: python

    import win32gui
    import win32helper.win32con as con

    win32gui.MessageBox(0, "hello", 'shit', con.MB_OK)

