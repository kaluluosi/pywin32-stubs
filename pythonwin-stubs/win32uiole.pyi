__all__=['', 'AfxOleInit', 'CreateInsertDialog', 'CreateOleClientItem', 'CreateOleDocument', 'DaoGetEngine', 'GetIDispatchForWindow', 'OleGetUserCtrl', 'OleSetUserCtrl', 'SetMessagePendingDelay', 'EnableNotRespondingDialog', 'EnableNotRespondingDialog', 'COleClientItem_activeState', 'COleClientItem_activeUIState', 'COleClientItem_emptyState', 'COleClientItem_loadedState', 'COleClientItem_openState', 'OLE_CHANGED', 'OLE_CHANGED_ASPECT', 'OLE_CHANGED_STATE', 'OLE_CLOSED', 'OLE_RENAMED', 'OLE_SAVED']
import typing
from win32helper import win32typing
"""A module, encapsulating the Microsoft Foundation Classes OLE functionality."""


def AfxOleInit(enabled:'typing.Any') -> 'None':
    """
    None

Args:

      enabled(typing.Any):

Returns:

      None
        
    """
    pass
        

def CreateInsertDialog() -> 'win32typing.PyCOleInsertDialog':
    """
    Creates a InsertObject dialog. 

self*/, PyObject *args)

Args:



Returns:

      win32typing.PyCOleInsertDialog
        
    """
    pass
        

def CreateOleClientItem() -> 'win32typing.PyCOleClientItem':
    """
    None

Args:



Returns:

      win32typing.PyCOleClientItem
        
    """
    pass
        

def CreateOleDocument(template:'win32typing.PyCDocTemplate',fileName:'str'=None) -> 'win32typing.PyCOleDocument':
    """
    Creates an OLE document.

Args:

      template(win32typing.PyCDocTemplate):The template to be attached to this document.
      fileName(str):The filename for the document.

Returns:

      win32typing.PyCOleDocument
        
    """
    pass
        

def DaoGetEngine() -> 'win32typing.PyIDispatch':
    """
    None

Args:



Returns:

      win32typing.PyIDispatch
        
    """
    pass
        

def GetIDispatchForWindow() -> 'win32typing.PyIDispatch':
    """
    Gets an OCX IDispatch pointer, if the window has one!

Args:



Returns:

      win32typing.PyIDispatch
        
    """
    pass
        

def OleGetUserCtrl() -> 'typing.Any':
    """
    Returns the application name.

Args:



Returns:

      typing.Any
        
    """
    pass
        

def OleSetUserCtrl(bUserCtrl:'typing.Any') -> 'typing.Any':
    """
    Sets or clears the user control flag.

Args:

      bUserCtrl(typing.Any):Specifies whether the user-control flag is to be set or cleared.

Returns:

      typing.Any
        
    """
    pass
        

def SetMessagePendingDelay(delay:'typing.Any') -> 'None':
    """
    None

Args:

      delay(typing.Any):

Returns:

      None
        
    """
    pass
        

def EnableNotRespondingDialog(enabled:'typing.Any') -> 'None':
    """
    None

Args:

      enabled(typing.Any):

Returns:

      None
        
    """
    pass
        

def EnableNotRespondingDialog(enabled:'typing.Any') -> 'None':
    """
    None

Args:

      enabled(typing.Any):

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