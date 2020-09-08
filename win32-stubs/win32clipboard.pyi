__all__=['ChangeClipboardChain', 'CloseClipboard', 'CountClipboardFormats', 'EmptyClipboard', 'EnumClipboardFormats', 'GetClipboardData', 'GetClipboardDataHandle', 'GetClipboardFormatName', 'GetClipboardOwner', 'GetClipboardSequenceNumber', 'GetClipboardViewer', 'GetGlobalMemory', 'GetOpenClipboardWindow', 'GetPriorityClipboardFormat', 'IsClipboardFormatAvailable', 'OpenClipboard', 'RegisterClipboardFormat', 'SetClipboardData', 'SetClipboardText', 'SetClipboardViewer']
from typing import *
from .win32typing import *
"""A module which supports the Windows Clipboard API."""


def ChangeClipboardChain(hWndRemove:'int',hWndNewNext:'int') -> 'int':
    """
    The ChangeClipboardChain 

function removes a specified window from the chain of clipboard viewers.

Args:

      hWndRemove(int):Integer handle to the window to be removed from the chain. The handle must have been passed to the SetClipboardViewer function.
      hWndNewNext(int):Integer handle to the window that follows the hWndRemove window in the clipboard viewer chain. (This is the handle returned by SetClipboardViewer, unless the sequence was changed in response to a WM_CHANGECBCHAIN message.)CommentsThe window identified by hWndNewNext replaces the hWndRemove window in the chain. The SetClipboardViewer function sends a WM_CHANGECBCHAIN message to the first window in the clipboard viewer chain.Win32 API References

Returns:

      int:Search for ChangeClipboardChain at msdn, google or google groups.
Return ValueThe return value indicates the result of passing the 

WM_CHANGECBCHAIN message to the windows in the clipboard viewer chain. 

Because a window in the chain typically returns FALSE when it processes 

WM_CHANGECBCHAIN, the return value from ChangeClipboardChain is typically 

FALSE. If there is only one window in the chain, the return value is 

typically TRUE.

        
    """
    pass
        

def CloseClipboard() -> 'None':
    """
    None

Args:



Returns:

      None:Search for CloseClipboard at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is None. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def CountClipboardFormats() -> 'int':
    """
    The CountClipboardFormats 

function retrieves the number of different data formats currently on the 

clipboard.

Args:



Returns:

      int:Search for CountClipboardFormats at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the number of 

different data formats currently on the clipboard. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def EmptyClipboard() -> 'None':
    """
    The EmptyClipboard function empties 

the clipboard and frees handles to data in the clipboard. The function then 

assigns ownership of the clipboard to the window that currently has the 

clipboard open.

Args:



Returns:

      None:Search for EmptyClipboard at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is None. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def EnumClipboardFormats(format:'int'=0) -> 'int':
    """
    The EnumClipboardFormats 

function lets you enumerate the data formats that are currently available 

on the clipboard.

Args:

      format(int):Specifies a clipboard format that is known to be available. To start an enumeration of clipboard formats, set format to zero. When format is zero, the function retrieves the first available clipboard format. For subsequent calls during an enumeration, set format to the result of the previous EnumClipboardFormat call.CommentsClipboard data formats are stored in an ordered list. To perform an enumeration of clipboard data formats, you make a series of calls to the EnumClipboardFormats function. For each call, the format parameter specifies an available clipboard format, and the function returns the next available clipboard format. You must open the clipboard before enumerating its formats. Use the OpenClipboard function to open the clipboard. The EnumClipboardFormats function fails if the clipboard is not open. The EnumClipboardFormats function enumerates formats in the order that they were placed on the clipboard. If you are copying information to the clipboard, add clipboard objects in order from the most descriptive clipboard format to the least descriptive clipboard format. If you are pasting information from the clipboard, retrieve the first clipboard format that you can handle. That will be the most descriptive clipboard format that you can handle. The system provides automatic type conversions for certain clipboard formats. In the case of such a format, this function enumerates the specified format, then enumerates the formats to which it can be converted.  For more information, see Standard Clipboard Formats and Synthesized Clipboard Formats.Win32 API References

Returns:

      int:Search for EnumClipboardFormats at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the clipboard 

format that follows the specified format. In other words, the next 

available clipboard format. 

If there are no more clipboard formats to enumerate, the return value is 

zero. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def GetClipboardData(format:'int') -> 'Union[str, Any]':
    """
    None

Args:

      format(int):Specifies a clipboard format. For a description of the standard clipboard formats, see Standard Clipboard Formats. In Unicode builds (ie, python 3k), the default is CF_UNICODETEXT.CommentsAn application can enumerate the available formats in advance by using the EnumClipboardFormats function. The clipboard controls the handle that the GetClipboardData function returns, not the application. The application should copy the data immediately. The application cannot rely on being able to make long-term use of the handle. The application must not free the handle nor leave it locked. The system performs implicit data format conversions between certain clipboard formats when an application calls the GetClipboardData function. For example, if the CF_OEMTEXT format is on the clipboard, a window can retrieve data in the CF_TEXT format. The format on the clipboard is converted to the requested format on demand. For more information, see Synthesized Clipboard Formats.Win32 API References

Returns:

      Union[str, Any]:Search for Standard Clipboard Formats at msdn, google or google groups.
 To Do CF_METAFILEPICT format returns a pointer to a METAFILEPICT struct which contains the metafile 

handle, 

rather than returning the handle directly.  This code currently fails with 

error: (6, 'GetClipboardData:GetMetafileBitsEx(NULL)', 'The handle is invalid.')
Return ValueIf the function fails, the standard win32api.error exception 

is raised.  If the function succeeds, the return value is as 

described in the following table:



Format


Result type



CF_HDROPA tuple of Unicode filenames.
CF_UNICODETEXTA unicode object.
CF_OEMTEXTA string object.
CF_TEXTA string object.
CF_ENHMETAFILEA string with binary data obtained from GetEnhMetaFileBits
CF_METAFILEPICTA string with binary data obtained from GetMetaFileBitsEx (currently broken)
CF_BITMAPAn integer handle to the bitmap.
All other formatsA string with binary data obtained directly from the 

global memory referenced by the handle.

        
    """
    pass
        

def GetClipboardDataHandle(format:'int') -> 'int':
    """
    None

Args:

      format(int):Specifies a clipboard format. For a description of the standard clipboard formats, see Standard Clipboard Formats.

Returns:

      int
        
    """
    pass
        

def GetClipboardFormatName(format:'int') -> 'str':
    """
    The GetClipboardFormatName 

function retrieves from the clipboard the name of the specified registered 

format.

Args:

      format(int):Specifies the type of format to be retrieved. This parameter must not specify any of the predefined clipboard formats.Win32 API References

Returns:

      str:Search for GetClipboardFormatName at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the string containing 

the format. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def GetClipboardOwner() -> 'int':
    """
    The GetClipboardOwner function 

retrieves the window handle of the current owner of the clipboard.

Args:



Returns:

      int:Search for GetClipboardOwner at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the handle of the 

window that owns the clipboard. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def GetClipboardSequenceNumber() -> 'int':
    """
    The 

GetClipboardSequenceNumber function returns the clipboard sequence number 

for the current window station.

Args:



Returns:

      int:Search for GetClipboardSequenceNumber at msdn, google or google groups.
Return ValueThe return value is the clipboard sequence number. If you do not 

have WINSTA_ACCESSCLIPBOARD access to the window station, the function 

returns zero.

        
    """
    pass
        

def GetClipboardViewer() -> 'int':
    """
    The GetClipboardViewer function 

retrieves the handle of the first window in the clipboard viewer chain.

Args:



Returns:

      int:Search for GetClipboardViewer at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the handle of the 

first window in the clipboard viewer chain. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def GetGlobalMemory(hglobal:'int') -> 'str':
    """
    Returns the contents of the specified 

global memory object.

Args:

      hglobal(int):The handle to the global memory object

Returns:

      str
        
    """
    pass
        

def GetOpenClipboardWindow() -> 'int':
    """
    The GetOpenClipboardWindow 

function retrieves the handle of the window that currently has the 

clipboard open.

Args:



Returns:

      int:Search for GetOpenClipboardWindow at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the handle of the 

window that has the clipboard open. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def GetPriorityClipboardFormat(formats:'Any') -> 'int':
    """
    Returns the first available clipboard format in the specified 

list.

Args:

      formats(Any):Sequence of integers identifying clipboard formats, in priority order. For a description of the standard clipboard formats, see Standard Clipboard Formats.Win32 API References

Returns:

      int:Search for Standard Clipboard Formats at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is the first clipboard 

format in the list for which data is available. If the clipboard is 

empty, the return value is NULL. If the clipboard contains data, but not 

in any of the specified formats, the return value is -1.

        
    """
    pass
        

def IsClipboardFormatAvailable(format:'int') -> 'int':
    """
    The 

IsClipboardFormatAvailable function determines whether the clipboard 

contains data in the specified format.

Args:

      format(int):Specifies a clipboard format. For a description of the standard clipboard formats, see Standard Clipboard Formats.CommentsTypically, an application that recognizes only one clipboard format would call this function when processing the WM_INITMENU or WM_INITMENUPOPUP message. The application would then enable or disable the Paste menu item, depending on the return value. Applications that recognize more than one clipboard format should use the GetPriorityClipboardFormat function for this purpose.Win32 API References

Returns:

      int:Search for Standard Clipboard Formats at msdn, google or google groups.
Return ValueIf the clipboard format is available, the return value is nonzero.

        
    """
    pass
        

def OpenClipboard(hWnd:'int'=None) -> 'None':
    """
    The OpenClipboard function opens the 

clipboard for examination and prevents other applications from modifying 

the clipboard content.

Args:

      hWnd(int):Integer handle to the window to be associated with the open clipboard. If this parameter is None, the open clipboard is associated with the current task.CommentsOpenClipboard fails if another window has the clipboard open. An application should call the CloseClipboard function after every successful call to OpenClipboard. The window identified by the hWnd parameter does not become the clipboard owner unless the EmptyClipboard function is called.Win32 API References

Returns:

      None:Search for OpenClipboard at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is None. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def RegisterClipboardFormat(name:'str') -> 'None':
    """
    The 

RegisterClipboardFormat function registers a new clipboard format. 

This format can then be used as a valid clipboard format.

Args:

      name(str):String that names the new format.CommentsIf a registered format with the specified name already exists, a new format is not registered and the return value identifies the existing format. This enables more than one application to copy and paste data using the same registered clipboard format. Note that the format name comparison is case-insensitive. Registered clipboard formats are identified by values in the range 0xC000 through 0xFFFF.Win32 API References

Returns:

      None:Search for RegisterClipboardFormat at msdn, google or google groups.
Return ValueIf the function succeeds, the return value identifies the 

registered clipboard format. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def SetClipboardData(format:'int',hMem:'Union[Any, int]') -> 'int':
    """
    The SetClipboardData function 

places data on the clipboard in a specified clipboard format. The window 

must be the current clipboard owner, and the application must have called 

the OpenClipboard function. (When responding to the WM_RENDERFORMAT and 

WM_RENDERALLFORMATS messages, the clipboard owner must not call 

OpenClipboard before calling SetClipboardData.)

Args:

      format(int):Specifies a clipboard format. For a description of the standard clipboard formats, see Standard Clipboard Formats.
      hMem(Union[Any, int]):Integer handle to the data in the specified format, or string, unicode, or any object that supports the buffer interface. A global memory object is allocated, and the object's buffer is copied to the new memory. This parameter can be 0, indicating that the window provides data in the specified clipboard format (renders the format) upon request. If a window delays rendering, it must process the WM_RENDERFORMAT and WM_RENDERALLFORMATS messages. After SetClipboardData is called, the system owns the object identified by the hMem parameter. The application can read the data, but must not free the handle or leave it locked. If the hMem parameter identifies a memory object, the object must have been allocated using the GlobalAlloc function with the GMEM_MOVEABLE and GMEM_DDESHARE flags.CommentsThe uFormat parameter can identify a registered clipboard format, or it can be one of the standard clipboard formats. For more information, see Registered Clipboard Formats and Standard Clipboard Formats. The system performs implicit data format conversions between certain clipboard formats when an application calls the GetClipboardData function. For example, if the CF_OEMTEXT format is on the clipboard, a window can retrieve data in the CF_TEXT format. The format on the clipboard is converted to the requested format on demand. For more information, see Synthesized Clipboard Formats.Win32 API References

Returns:

      int:Search for SetClipboardData at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is integer handle 

of the data. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def SetClipboardText(text:'Union[str, Any]',format:'int') -> 'int':
    """
    Convienience function to 

call SetClipboardData with text.

Args:

      text(Union[str, Any]):The text to place on the clipboard.
      format(int):The clipboard format to use - must be CF_TEXT or CF_UNICODETEXTCommentsYou may pass a Unicode or string/bytes object to this function, but depending on the value of the 'format' param, it may be converted to the appropriate type for that param.Many applications will want to call this function twice, with the same string specified but CF_UNICODETEXT specified the second.Win32 API References

Returns:

      int:Search for SetClipboardData at msdn, google or google groups.
Return ValueIf the function succeeds, the return value is integer handle 

of the data. 

If the function fails, win32api.error is raised with the GetLastError 

info.

        
    """
    pass
        

def SetClipboardViewer(hWndNewViewer:'int') -> 'int':
    """
    The SetClipboardViewer function 

adds the specified window to the chain of clipboard viewers. Clipboard 

viewer windows receive a WM_DRAWCLIPBOARD message whenever the content of 

the clipboard changes.

Args:

      hWndNewViewer(int):Integer handle to the window to be added to the clipboard chain.CommentsThe windows that are part of the clipboard viewer chain, called clipboard viewer windows, must process the clipboard messages WM_CHANGECBCHAIN and WM_DRAWCLIPBOARD. Each clipboard viewer window calls the SendMessage function to pass these messages to the next window in the clipboard viewer chain. A clipboard viewer window must eventually remove itself from the clipboard viewer chain by calling the ChangeClipboardChain function -- for example, in response to theWM_DESTROY message.Win32 API References

Returns:

      int:Search for SetClipboardViewer at msdn, google or google groups.
Return ValueReturns a handle to the next window in chain, or None if no other viewer exists.



If the function succeeds, the return value identifies the next 

window in the clipboard viewer chain. 

If an error occurs or there are no other windows in the clipboard viewer 

chain, win32api.error is raised with the GetLastError info.

        
    """
    pass
        