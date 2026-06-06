pywin32-stubs
=============

.. warning::

   **DEPRECATED** — This package is no longer maintained.
   Use the official stubs package instead::

       pip install types-pywin32

   See: https://pypi.org/project/types-pywin32/

pywin32-stubs is generated from pywin32.chm, it contains:

- win32-stubs
- win32comext-stubs
- pythonwin-stubs
- win32helper : this package defines win32typing and constants.

Installation
------------

**Deprecated.** Use `types-pywin32 <https://pypi.org/project/types-pywin32/>`_ instead.

.. code:: shell

    pip install pywin32-stubs

Usage
-----

.. code:: python

    import win32gui
    import win32helper.win32con as con

    win32gui.MessageBox(0, "hello", 'world', con.MB_OK)
