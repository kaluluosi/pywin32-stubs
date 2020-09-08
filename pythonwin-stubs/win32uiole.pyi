__all__=['', 'AfxOleInit', 'CreateInsertDialog', 'CreateOleClientItem', 'CreateOleDocument', 'DaoGetEngine', 'GetIDispatchForWindow', 'OleGetUserCtrl', 'OleSetUserCtrl', 'SetMessagePendingDelay', 'EnableNotRespondingDialog', 'EnableNotRespondingDialog', 'COleClientItem_activeState', 'COleClientItem_activeUIState', 'COleClientItem_emptyState', 'COleClientItem_loadedState', 'COleClientItem_openState', 'OLE_CHANGED', 'OLE_CHANGED_ASPECT', 'OLE_CHANGED_STATE', 'OLE_CLOSED', 'OLE_RENAMED', 'OLE_SAVED']
from typing import *
from win32helper.win32typing import *
"""A module, encapsulating the Microsoft Foundation Classes OLE functionality."""


def AfxOleInit(enabled:'bool') -> 'None':
    """
    None

Args:

      enabled(bool):

Returns:

      None
        
    """
    pass
        

def CreateInsertDialog() -> 'PyCOleInsertDialog':
    """
    Creates a InsertObject dialog. 

self*/, PyObject *args)

Args:



Returns:

      PyCOleInsertDialog
        
    """
    pass
        

def CreateOleClientItem() -> 'PyCOleClientItem':
    """
    None

Args:



Returns:

      PyCOleClientItem
        
    """
    pass
        

def CreateOleDocument(template:'PyCDocTemplate',fileName:'str'=None) -> 'PyCOleDocument':
    """
    Creates an OLE document.

Args:

      template(PyCDocTemplate):The template to be attached to this document.
      fileName(str):The filename for the document.

Returns:

      PyCOleDocument
        
    """
    pass
        

def DaoGetEngine() -> 'PyIDispatch':
    """
    None

Args:



Returns:

      PyIDispatch
        
    """
    pass
        

def GetIDispatchForWindow() -> 'PyIDispatch':
    """
    Gets an OCX IDispatch pointer, if the window has one!

Args:



Returns:

      PyIDispatch
        
    """
    pass
        

def OleGetUserCtrl() -> 'int':
    """
    Returns the application name.

Args:



Returns:

      int
        
    """
    pass
        

def OleSetUserCtrl(bUserCtrl:'int') -> 'int':
    """
    Sets or clears the user control flag.

Args:

      bUserCtrl(int):Specifies whether the user-control flag is to be set or cleared.

Returns:

      int
        
    """
    pass
        

def SetMessagePendingDelay(delay:'int') -> 'None':
    """
    None

Args:

      delay(int):

Returns:

      None
        
    """
    pass
        

def EnableNotRespondingDialog(enabled:'bool') -> 'None':
    """
    None

Args:

      enabled(bool):

Returns:

      None
        
    """
    pass
        

def EnableNotRespondingDialog(enabled:'bool') -> 'None':
    """
    None

Args:

      enabled(bool):

Returns:

      None
        
    """
    pass
        
COleClientItem_activeState = ...
COleClientItem_activeUIState = ...
COleClientItem_emptyState = ...
COleClientItem_loadedState = ...
COleClientItem_openState = ...
OLE_CHANGED = ...
OLE_CHANGED_ASPECT = ...
OLE_CHANGED_STATE = ...
OLE_CLOSED = ...
OLE_RENAMED = ...
OLE_SAVED = ...