__all__=['EnumFontFamilies', 'set_logger', 'LOGFONT', 'CreateFontIndirect', 'GetObject', 'GetObjectType', 'PyGetMemory', 'PyGetString', 'PySetString', 'PySetMemory', 'PyGetArraySignedLong', 'PyGetBufferAddressAndLen', 'FlashWindow', 'FlashWindowEx', 'GetWindowLong', 'GetClassLong', 'SetWindowLong', 'CallWindowProc', 'SendMessage', 'SendMessageTimeout', 'PostMessage', 'PostThreadMessage', 'ReplyMessage', 'RegisterWindowMessage', 'DefWindowProc', 'EnumWindows', 'EnumThreadWindows', 'EnumChildWindows', 'DialogBox', 'DialogBoxParam', 'DialogBoxIndirect', 'DialogBoxIndirectParam', 'CreateDialogIndirect', 'DialogBoxIndirectParam', 'EndDialog', 'GetDlgItem', 'GetDlgItemInt', 'SetDlgItemInt', 'GetDlgCtrlID', 'GetDlgItemText', 'SetDlgItemText', 'GetNextDlgTabItem', 'GetNextDlgGroupItem', 'SetWindowText', 'GetWindowText', 'InitCommonControls', 'InitCommonControlsEx', 'LoadCursor', 'SetCursor', 'GetCursor', 'GetCursorInfo', 'CreateAcceleratorTable', 'DestroyAccleratorTable', 'LoadMenu', 'DestroyMenu', 'SetMenu', 'GetMenu', 'LoadIcon', 'CopyIcon', 'DrawIcon', 'DrawIconEx', 'CreateIconIndirect', 'CreateIconFromResource', 'LoadImage', 'DeleteObject', 'BitBlt', 'StretchBlt', 'PatBlt', 'SetStretchBltMode', 'GetStretchBltMode', 'TransparentBlt', 'MaskBlt', 'AlphaBlend', 'ImageList_Add', 'ImageList_Create', 'ImageList_Destroy', 'ImageList_Draw', 'ImageList_DrawEx', 'ImageList_GetIcon', 'ImageList_GetImageCount', 'ImageList_LoadImage', 'ImageList_LoadBitmap', 'ImageList_Remove', 'ImageList_Replace', 'ImageList_ReplaceIcon', 'ImageList_SetBkColor', 'ImageList_SetOverlayImage', 'MessageBox', 'MessageBeep', 'CreateWindow', 'DestroyWindow', 'EnableWindow', 'FindWindow', 'FindWindowEx', 'DragAcceptFiles', 'DragDetect', 'SetDoubleClickTime', 'GetDoubleClickTime', 'HideCaret', 'SetCaretPos', 'GetCaretPos', 'ShowCaret', 'ShowWindow', 'IsWindowVisible', 'IsWindowEnabled', 'SetFocus', 'GetFocus', 'UpdateWindow', 'BringWindowToTop', 'SetActiveWindow', 'GetActiveWindow', 'SetForegroundWindow', 'GetForegroundWindow', 'GetClientRect', 'GetDC', 'SaveDC', 'RestoreDC', 'DeleteDC', 'CreateCompatibleDC', 'CreateCompatibleBitmap', 'CreateBitmap', 'SelectObject', 'GetCurrentObject', 'GetWindowRect', 'GetStockObject', 'PostQuitMessage', 'WaitMessage', 'SetWindowPos', 'GetWindowPlacement', 'SetWindowPlacement', 'RegisterClass', 'UnregisterClass', 'PumpMessages', 'PumpWaitingMessages', 'GetMessage', 'TranslateMessage', 'DispatchMessage', 'TranslateAccelerator', 'PeekMessage', 'Shell_NotifyIcon', 'GetSystemMenu', 'DrawMenuBar', 'MoveWindow', 'CloseWindow', 'DeleteMenu', 'RemoveMenu', 'CreateMenu', 'CreatePopupMenu', 'TrackPopupMenu', 'CommDlgExtendedError', 'ExtractIcon', 'ExtractIconEx', 'DestroyIcon', 'GetIconInfo', 'ScreenToClient', 'ClientToScreen', 'PaintDesktop', 'RedrawWindow', 'GetTextExtentPoint32', 'GetTextMetrics', 'GetTextCharacterExtra', 'SetTextCharacterExtra', 'GetTextAlign', 'SetTextAlign', 'GetTextFace', 'GetMapMode', 'SetMapMode', 'GetGraphicsMode', 'SetGraphicsMode', 'GetLayout', 'SetLayout', 'GetPolyFillMode', 'SetPolyFillMode', 'GetWorldTransform', 'SetWorldTransform', 'ModifyWorldTransform', 'CombineTransform', 'GetWindowOrgEx', 'SetWindowOrgEx', 'GetViewportOrgEx', 'SetViewportOrgEx', 'GetWindowExtEx', 'SetWindowExtEx', 'GetViewportExtEx', 'SetViewportExtEx', 'GradientFill', 'GetOpenFileName', 'InsertMenuItem', 'SetMenuItemInfo', 'GetMenuItemInfo', 'GetMenuItemCount', 'GetMenuItemRect', 'GetMenuState', 'SetMenuDefaultItem', 'GetMenuDefaultItem', 'AppendMenu', 'InsertMenu', 'EnableMenuItem', 'CheckMenuItem', 'GetSubMenu', 'ModifyMenu', 'GetMenuItemID', 'SetMenuItemBitmaps', 'CheckMenuRadioItem', 'SetMenuInfo', 'GetMenuInfo', 'DrawFocusRect', 'DrawText', 'LineTo', 'Ellipse', 'Pie', 'Arc', 'ArcTo', 'AngleArc', 'Chord', 'ExtFloodFill', 'SetPixel', 'GetPixel', 'GetROP2', 'SetROP2', 'SetPixelV', 'MoveToEx', 'GetCurrentPositionEx', 'GetArcDirection', 'SetArcDirection', 'Polygon', 'Polyline', 'PolylineTo', 'PolyBezier', 'PolyBezierTo', 'PlgBlt', 'CreatePolygonRgn', 'ExtTextOut', 'GetTextColor', 'SetTextColor', 'GetBkMode', 'SetBkMode', 'GetBkColor', 'SetBkColor', 'DrawEdge', 'FillRect', 'FillRgn', 'PaintRgn', 'FrameRgn', 'InvertRgn', 'EqualRgn', 'PtInRegion', 'PtInRect', 'RectInRegion', 'SetRectRgn', 'CombineRgn', 'DrawAnimatedRects', 'CreateSolidBrush', 'CreatePatternBrush', 'CreateHatchBrush', 'CreatePen', 'GetSysColor', 'GetSysColorBrush', 'InvalidateRect', 'FrameRect', 'InvertRect', 'WindowFromDC', 'GetUpdateRgn', 'GetWindowRgn', 'SetWindowRgn', 'GetWindowRgnBox', 'ValidateRgn', 'InvalidateRgn', 'GetRgnBox', 'OffsetRgn', 'Rectangle', 'RoundRect', 'BeginPaint', 'EndPaint', 'BeginPath', 'EndPath', 'AbortPath', 'CloseFigure', 'FlattenPath', 'FillPath', 'WidenPath', 'StrokePath', 'StrokeAndFillPath', 'GetMiterLimit', 'SetMiterLimit', 'PathToRegion', 'GetPath', 'CreateRoundRectRgn', 'CreateRectRgnIndirect', 'CreateEllipticRgnIndirect', 'CreateWindowEx', 'GetParent', 'SetParent', 'GetCursorPos', 'GetDesktopWindow', 'GetWindow', 'GetWindowDC', 'IsIconic', 'IsWindow', 'IsChild', 'ReleaseCapture', 'GetCapture', 'SetCapture', '_TrackMouseEvent', 'ReleaseDC', 'CreateCaret', 'DestroyCaret', 'ScrollWindowEx', 'SetScrollInfo', 'GetScrollInfo', 'GetClassName', 'WindowFromPoint', 'ChildWindowFromPoint', 'ChildWindowFromPoint', 'ListView_SortItems', 'ListView_SortItemsEx', 'CreateDC', 'GetSaveFileNameW', 'GetOpenFileNameW', 'SystemParametersInfo', 'SetLayeredWindowAttributes', 'GetLayeredWindowAttributes', 'UpdateLayeredWindow', 'AnimateWindow', 'CreateBrushIndirect', 'ExtCreatePen', 'DrawTextW', 'EnumPropsEx', 'RegisterDeviceNotification', 'UnregisterDeviceNotification', 'RegisterHotKey', 'CLR_NONE', 'ILC_COLOR', 'ILC_COLOR16', 'ILC_COLOR24', 'ILC_COLOR32', 'ILC_COLOR4', 'ILC_COLOR8', 'ILC_COLORDDB', 'ILC_MASK', 'ILD_BLEND', 'ILD_BLEND25', 'ILD_BLEND50', 'ILD_FOCUS', 'ILD_MASK', 'ILD_NORMAL', 'ILD_SELECTED', 'ILD_TRANSPARENT', 'IMAGE_BITMAP', 'IMAGE_CURSOR', 'IMAGE_ICON', 'LR_CREATEDIBSECTION', 'LR_DEFAULTCOLOR', 'LR_DEFAULTSIZE', 'LR_LOADFROMFILE', 'LR_LOADMAP3DCOLORS', 'LR_LOADTRANSPARENT', 'LR_MONOCHROME', 'LR_SHARED', 'LR_VGACOLOR', 'NIF_ICON', 'NIF_INFO', 'NIF_MESSAGE', 'NIF_STATE', 'NIF_TIP', 'NIIF_ERROR', 'NIIF_ICON_MASK', 'NIIF_INFO', 'NIIF_NONE', 'NIIF_NOSOUND', 'NIIF_WARNING', 'NIM_ADD', 'NIM_DELETE', 'NIM_MODIFY', 'NIM_SETFOCUS', 'NIM_SETVERSION', 'TPM_BOTTOMALIGN', 'TPM_CENTERALIGN', 'TPM_LEFTALIGN', 'TPM_LEFTBUTTON', 'TPM_NONOTIFY', 'TPM_RETURNCMD', 'TPM_RIGHTALIGN', 'TPM_RIGHTBUTTON', 'TPM_TOPALIGN', 'TPM_VCENTERALIGN']
from typing import *
from .win32typing import *
""""""


def EnumFontFamilies(hdc:'int',Family:'Union[str]',EnumFontFamProc:'Any',Param:'Any') -> 'int':
    """
    Enumerates the available font families.

Args:

      hdc(int):Handle to a device context for which to enumerate available fonts
      Family(Union[str]):Family of fonts to enumerate. If none, first member of each font family will be returned.
      EnumFontFamProc(Any):The Python function called with each font family. This function is called with 4 arguments.
      Param(Any):An arbitrary object to be passed to the callback functionCommentsThe parameters that the callback function will receive are as follows:PyLOGFONT - contains the font parameters None - Placeholder for a TEXTMETRIC structure, not supported yet int - Font type, combination of DEVICE_FONTTYPE, RASTER_FONTTYPE, TRUETYPE_FONTTYPE object - The Param originally passed in to EnumFontFamilies

Returns:

      int
        
    """
    pass
        

def set_logger(logger:'Any') -> 'None':
    """
    Sets a logger object for exceptions and error information

Args:

      logger(Any):A logger object, generally from the standard logger package.CommentsOnce a logger has been set for the module, unhandled exceptions, such as from a window's WNDPROC, will be written (via logger.exception()) to the log instead of to stderr. Note that using this with the Python 2.3 logging package will prevent the traceback from being written to the log.  However, it is possible to use the Python 2.4 logging package directly with Python 2.3

Returns:

      None
        
    """
    pass
        

def LOGFONT() -> 'PyLOGFONT':
    """
    Creates a LOGFONT object.

Args:



Returns:

      PyLOGFONT
        
    """
    pass
        

def CreateFontIndirect(lplf:'PyLOGFONT') -> 'Any':
    """
    function creates a logical font that has the specified characteristics. 

The font can subsequently be selected as the current font for any device context.

Args:

      lplf(PyLOGFONT):A LOGFONT object as returned by win32gui::LOGFONT

Returns:

      Any
        
    """
    pass
        

def GetObject(handle:'int') -> 'Any':
    """
    Returns a struct containing the parameters used to create a GDI object

Args:

      handle(int):Handle to the object.CommentsThe result depends on the type of the handle.Object type as determined by win32gui::GetObjectTypeReturned objectOBJ_FONTPyLOGFONTOBJ_BITMAPPyBITMAPOBJ_PENDict representing a LOGPEN struct

Returns:

      Any
        
    """
    pass
        

def GetObjectType(h:'int') -> 'int':
    """
    Returns the type (OBJ_* constant) of a GDI handle

Args:

      h(int):A handle to a GDI object

Returns:

      int
        
    """
    pass
        

def PyGetMemory(addr:'int',len:'int') -> 'Any':
    """
    Returns a buffer object from and address and length

Args:

      addr(int):Address of the memory to reference.
      len(int):Number of bytes to return.CommentsIf zero is passed a ValueError will be raised.

Returns:

      Any
        
    """
    pass
        

def PyGetString(addr:'int',len:'int') -> 'str':
    """
    Returns a string from an address.

Args:

      addr(int):Address of the memory to reference
      len(int):Number of characters to read.  If not specified, the string must be NULL terminated.Return ValueIf win32gui.UNICODE is True, this will return a unicode object.

Returns:

      str:Number of characters to read.  If not specified, the 

string must be NULL terminated.Return ValueIf win32gui.UNICODE is True, this will return a unicode object.

        
    """
    pass
        

def PySetString(addr:'int',String:'str',maxLen:'int') -> 'Any':
    """
    None

Args:

      addr(int):Address of the memory to reference
      String(str):The string to copy
      maxLen(int):Maximum number of chars to copy (optional)

Returns:

      Any
        
    """
    pass
        

def PySetMemory(addr:'int',String:'Any') -> 'Any':
    """
    Copies bytes to an address.

Args:

      addr(int):Address of the memory to reference
      String(Any):The string to copy

Returns:

      Any
        
    """
    pass
        

def PyGetArraySignedLong(array:'Any',index:'int') -> 'Any':
    """
    Returns a signed long from an array object at specified index

Args:

      array(Any):array object to use
      index(int):index of offset

Returns:

      Any
        
    """
    pass
        

def PyGetBufferAddressAndLen(obj:'Any') -> 'Any':
    """
    Returns a buffer object address and len

Args:

      obj(Any):the buffer object

Returns:

      Any
        
    """
    pass
        

def FlashWindow(hwnd:'int',bInvert:'int') -> 'int':
    """
    The FlashWindow function flashes the specified window one time. It does not change the active state of the window.

Args:

      hwnd(int):Handle to a window
      bInvert(int):Indicates if window should toggle between active and inactive

Returns:

      int
        
    """
    pass
        

def FlashWindowEx(hwnd:'int',dwFlags:'int',uCount:'int',dwTimeout:'int') -> 'int':
    """
    The FlashWindowEx function flashes the specified window a specified number of times.

Args:

      hwnd(int):Handle to a window
      dwFlags(int):Combination of win32con.FLASHW_* flags
      uCount(int):Nbr of times to flash
      dwTimeout(int):Elapsed time between flashes, in milliseconds

Returns:

      int
        
    """
    pass
        

def GetWindowLong(hwnd:'int',index:'int') -> 'int':
    """
    None

Args:

      hwnd(int):
      index(int):

Returns:

      int
        
    """
    pass
        

def GetClassLong(hwnd:'int',index:'int') -> 'int':
    """
    None

Args:

      hwnd(int):
      index(int):

Returns:

      int
        
    """
    pass
        

def SetWindowLong(hwnd:'int',index:'int',value:'Any') -> 'int':
    """
    Places a long value at the specified offset into the extra window memory of the given window.

Args:

      hwnd(int):The handle to the window
      index(int):The index of the item to set.
      value(Any):The value to set.CommentsThis function calls the SetWindowLongPtr Api functionIf index is GWLP_WNDPROC, then the value parameter must be a callable object (or a dictionary) to use as the new window procedure.

Returns:

      int
        
    """
    pass
        

def CallWindowProc(wndproc:'int',hwnd:'int',msg:'int',wparam:'Union[str, int]',lparam:'Union[str, int]') -> 'int':
    """
    None

Args:

      wndproc(int):The wndproc to call - this is generally the return value of SetWindowLong(GWL_WNDPROC)
      hwnd(int):Handle to the window
      msg(int):A window message
      wparam(Union[str, int]):Type is dependent on the message
      lparam(Union[str, int]):Type is dependent on the message

Returns:

      int
        
    """
    pass
        

def SendMessage(hwnd:'int',message:'int',wparam:'Union[str, int]'=None,lparam:'Union[str, int]'=None) -> 'int':
    """
    Sends a message to the window.

Args:

      hwnd(int):The handle to the Window
      message(int):The ID of the message to post
      wparam(Union[str, int]):Type depends on the message
      lparam(Union[str, int]):Type depends on the message

Returns:

      int
        
    """
    pass
        

def SendMessageTimeout(hwnd:'int',message:'int',wparam:'int',lparam:'int',flags:'int',timeout:'int') -> 'Tuple[int, int]':
    """
    Sends a message to the window.

Args:

      hwnd(int):The handle to the Window
      message(int):The ID of the message to post
      wparam(int):An integer whose value depends on the message
      lparam(int):An integer whose value depends on the message
      flags(int):Send options
      timeout(int):Timeout duration in milliseconds.Return ValueThe result is the result of the SendMessageTimeout call, plus the last 'result' param. If the timeout period expires, a pywintypes.error exception will be thrown, with zero as the error code.  See the Microsoft documentation for more information.

Returns:

      Tuple[int, int]:Timeout duration in milliseconds.Return ValueThe result is the result of the SendMessageTimeout call, plus the last 'result' param. 

If the timeout period expires, a pywintypes.error exception will be thrown, 

with zero as the error code.  See the Microsoft documentation for more information.

        
    """
    pass
        

def PostMessage(hwnd:'int',message:'int',wparam:'int'=0,lparam:'int'=0) -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the Window
      message(int):The ID of the message to post
      wparam(int):An integer whose value depends on the message
      lparam(int):An integer whose value depends on the message

Returns:

      None
        
    """
    pass
        

def PostThreadMessage(threadId:'int',message:'int',wparam:'int',lparam:'int') -> 'None':
    """
    None

Args:

      threadId(int):The ID of the thread to post the message to.
      message(int):The ID of the message to post
      wparam(int):An integer whose value depends on the message
      lparam(int):An integer whose value depends on the message

Returns:

      None
        
    """
    pass
        

def ReplyMessage(result:'int') -> 'int':
    """
    Used to reply to a message sent through the SendMessage function without returning control to the function that called SendMessage.

Args:

      result(int):Specifies the result of the message processing. The possible values are based on the message sent.

Returns:

      int
        
    """
    pass
        

def RegisterWindowMessage(name:'Union[str, Any]') -> 'int':
    """
    Defines a new window message that is guaranteed to be unique throughout the system. The message value can be used when sending or posting messages.

Args:

      name(Union[str, Any]):The string

Returns:

      int
        
    """
    pass
        

def DefWindowProc(hwnd:'int',message:'int',wparam:'int',lparam:'int') -> 'int':
    """
    None

Args:

      hwnd(int):The handle to the Window
      message(int):The ID of the message to send
      wparam(int):An integer whose value depends on the message
      lparam(int):An integer whose value depends on the message

Returns:

      int
        
    """
    pass
        

def EnumWindows(callback:'Any',extra:'Any') -> 'None':
    """
    Enumerates all top-level windows on the screen by passing the handle to each window, in turn, to an application-defined callback function.

Args:

      callback(Any):A Python function to be used as the callback.  Function can return False to stop enumeration, or raise an exception.
      extra(Any):Any python object - this is passed to the callback function as the second param (first is the hwnd).

Returns:

      None
        
    """
    pass
        

def EnumThreadWindows(dwThreadId:'int',callback:'Any',extra:'Any') -> 'None':
    """
    Enumerates all top-level windows associated with a thread on the screen by passing the handle to each window, in turn, to an application-defined callback function. EnumThreadWindows continues until the last top-level window associated with the thread is enumerated or the callback function returns FALSE

Args:

      dwThreadId(int):The id of the thread for which the windows need to be enumerated.
      callback(Any):A Python function to be used as the callback.
      extra(Any):Any python object - this is passed to the callback function as the second param (first is the hwnd).

Returns:

      None
        
    """
    pass
        

def EnumChildWindows(hwnd:'int',callback:'Any',extra:'Any') -> 'None':
    """
    Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to an application-defined callback function. EnumChildWindows continues until the last child window is enumerated or the callback function returns FALSE.

Args:

      hwnd(int):The handle to the window to enumerate.
      callback(Any):A Python function to be used as the callback.
      extra(Any):Any python object - this is passed to the callback function as the second param (first is the hwnd).

Returns:

      None
        
    """
    pass
        

def DialogBox(hInstance:'int',TemplateName:'PyResourceId',hWndParent:'int',DialogFunc:'Any',InitParam:'int'=0) -> 'int':
    """
    Creates a modal dialog box.

Args:

      hInstance(int):Handle to module that contains the dialog template
      TemplateName(PyResourceId):Name or resource id of the dialog resource
      hWndParent(int):Handle to dialog's parent window
      DialogFunc(Any):Dialog box procedure to process messages
      InitParam(int):Initialization data to be passed to above procedure during WM_INITDIALOG processing

Returns:

      int
        
    """
    pass
        

def DialogBoxParam() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def DialogBoxIndirect(hInstance:'int',controlList:'PyDialogTemplate',hWndParent:'int',DialogFunc:'Any',InitParam:'Any'=0) -> 'int':
    """
    None

Args:

      hInstance(int):Handle to module creating the dialog box
      controlList(PyDialogTemplate):Sequence of items defining the dialog box and subcontrols
      hWndParent(int):Handle to dialog's parent window
      DialogFunc(Any):Dialog box procedure to process messages
      InitParam(Any):Initialization data to be passed to above procedure during WM_INITDIALOG processing

Returns:

      int
        
    """
    pass
        

def DialogBoxIndirectParam() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def CreateDialogIndirect(hInstance:'int',controlList:'PyDialogTemplate',hWndParent:'int',DialogFunc:'Any',InitParam:'int'=0) -> 'int':
    """
    None

Args:

      hInstance(int):Handle to module creating the dialog box
      controlList(PyDialogTemplate):Sequence containing a PyDLGTEMPLATE, followed by variable number of PyDLGITEMTEMPLATEs
      hWndParent(int):Handle to dialog's parent window
      DialogFunc(Any):Dialog box procedure to process messages
      InitParam(int):Initialization data to be passed to above procedure during WM_INITDIALOG processing

Returns:

      int
        
    """
    pass
        

def DialogBoxIndirectParam() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def EndDialog(hwnd:'int',result:'int') -> 'None':
    """
    Ends a dialog box.

Args:

      hwnd(int):Handle to the window.
      result(int):result

Returns:

      None
        
    """
    pass
        

def GetDlgItem(hDlg:'int',IDDlgItem:'int') -> 'Any':
    """
    Retrieves the handle to a control in the specified dialog box.

Args:

      hDlg(int):Handle to a dialog window
      IDDlgItem(int):Identifier of one of the dialog's controls

Returns:

      Any
        
    """
    pass
        

def GetDlgItemInt(hDlg:'int',IDDlgItem:'int',Signed:'Any') -> 'None':
    """
    Returns the integer value of a dialog control

Args:

      hDlg(int):Handle to a dialog window
      IDDlgItem(int):Identifier of one of the dialog's controls
      Signed(Any):Indicates whether control value should be interpreted as signed

Returns:

      None
        
    """
    pass
        

def SetDlgItemInt(hDlg:'int',IDDlgItem:'int',Value:'int',Signed:'Any') -> 'None':
    """
    Places an integer value in a dialog control

Args:

      hDlg(int):Handle to a dialog window
      IDDlgItem(int):Identifier of one of the dialog's controls
      Value(int):Value to placed in the control
      Signed(Any):Indicates if the input value is signed

Returns:

      None
        
    """
    pass
        

def GetDlgCtrlID(hwnd:'int') -> 'int':
    """
    Retrieves the identifier of the specified control.

Args:

      hwnd(int):The handle to the control

Returns:

      int
        
    """
    pass
        

def GetDlgItemText(hDlg:'int',IDDlgItem:'int') -> 'str':
    """
    Returns the text of a dialog control

Args:

      hDlg(int):Handle to a dialog window
      IDDlgItem(int):The Id of a control within the dialog

Returns:

      str
        
    """
    pass
        

def SetDlgItemText(hDlg:'int',IDDlgItem:'int',String:'Union[str, Any]') -> 'None':
    """
    Sets the text for a window or control

Args:

      hDlg(int):Handle to a dialog window
      IDDlgItem(int):The Id of a control within the dialog
      String(Union[str, Any]):The text to put in the control

Returns:

      None
        
    """
    pass
        

def GetNextDlgTabItem(hDlg:'int',hCtl:'int',bPrevious:'int') -> 'Any':
    """
    Retrieves a handle to the first control that has the WS_TABSTOP style that precedes (or follows) the specified control.

Args:

      hDlg(int):handle to dialog box
      hCtl(int):handle to known control
      bPrevious(int):direction flag

Returns:

      Any
        
    """
    pass
        

def GetNextDlgGroupItem(hDlg:'int',hCtl:'int',bPrevious:'int') -> 'Any':
    """
    Retrieves a handle to the first control in a group of controls that precedes (or follows) the specified control in a dialog box.

Args:

      hDlg(int):handle to dialog box
      hCtl(int):handle to known control
      bPrevious(int):direction flag

Returns:

      Any
        
    """
    pass
        

def SetWindowText() -> 'None':
    """
    Sets the window text.

Args:



Returns:

      None
        
    """
    pass
        

def GetWindowText(hwnd:'int') -> 'str':
    """
    Get the window text.

Args:

      hwnd(int):The handle to the windowCommentsNote that previous versions of PyWin32 returned a (empty) Unicode object when the string was empty, or an MBCS encoded string value otherwise.  A String is now returned in all cases.

Returns:

      str
        
    """
    pass
        

def InitCommonControls() -> 'None':
    """
    Initializes the common controls.

Args:



Returns:

      None
        
    """
    pass
        

def InitCommonControlsEx(flag:'int') -> 'None':
    """
    Initializes specific common controls.

Args:

      flag(int):One of the ICC_ constants

Returns:

      None
        
    """
    pass
        

def LoadCursor(hinstance:'int',resid:'int') -> 'Any':
    """
    Loads a cursor.

Args:

      hinstance(int):The module to load from
      resid(int):The resource ID

Returns:

      Any
        
    """
    pass
        

def SetCursor(hcursor:'int') -> 'Any':
    """
    None

Args:

      hcursor(int):

Returns:

      Any
        
    """
    pass
        

def GetCursor() -> 'Any':
    """
    None

Args:



Returns:

      Any
        
    """
    pass
        

def GetCursorInfo() -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about the global cursor.

Args:



Returns:

      Tuple[Any, Any, Any, Any]
        
    """
    pass
        

def CreateAcceleratorTable(accels:'Tuple[Tuple[int, int, int], ...]') -> 'Any':
    """
    Creates an accelerator table

Args:

      accels(Tuple[Tuple[int, int, int], ...]):A sequence of (fVirt, key, cmd), as per the Win32 ACCEL structure.

Returns:

      Any
        
    """
    pass
        

def DestroyAccleratorTable(haccel:'int') -> 'None':
    """
    Destroys an accelerator table

Args:

      haccel(int):

Returns:

      None
        
    """
    pass
        

def LoadMenu(hinstance:'int',resource_id:'Union[str, int]') -> 'Any':
    """
    Loads a menu

Args:

      hinstance(int):
      resource_id(Union[str, int]):

Returns:

      Any
        
    """
    pass
        

def DestroyMenu() -> 'None':
    """
    Destroys a previously loaded menu.

Args:



Returns:

      None
        
    """
    pass
        

def SetMenu(hwnd:'int',hmenu:'int') -> 'None':
    """
    Sets the menu for the specified window.

Args:

      hwnd(int):
      hmenu(int):

Returns:

      None
        
    """
    pass
        

def GetMenu() -> 'None':
    """
    Gets the menu for the specified window.

Args:



Returns:

      None
        
    """
    pass
        

def LoadIcon(hinstance:'int',resource_id:'Union[str, int]') -> 'Any':
    """
    Loads an icon

Args:

      hinstance(int):
      resource_id(Union[str, int]):

Returns:

      Any
        
    """
    pass
        

def CopyIcon(hicon:'int') -> 'Any':
    """
    Copies an icon

Args:

      hicon(int):Existing icon

Returns:

      Any
        
    """
    pass
        

def DrawIcon(hDC:'int',X:'int',Y:'int',hicon:'int') -> 'None':
    """
    None

Args:

      hDC(int):handle to DC
      X(int):x-coordinate of upper-left corner
      Y(int):y-coordinate of upper-left corner
      hicon(int):handle to icon

Returns:

      None
        
    """
    pass
        

def DrawIconEx(hDC:'int',xLeft:'int',yTop:'int',hIcon:'int',cxWidth:'int',cyWidth:'int',istepIfAniCur:'int',hbrFlickerFreeDraw:'PyGdiHANDLE',diFlags:'int') -> 'None':
    """
    Draws an icon or cursor into the specified device context, 

performing the specified raster operations, and stretching or compressing the 

icon or cursor as specified.

Args:

      hDC(int):handle to device context
      xLeft(int):x-coord of upper left corner
      yTop(int):y-coord of upper left corner
      hIcon(int):handle to icon
      cxWidth(int):icon width
      cyWidth(int):icon height
      istepIfAniCur(int):frame index, animated cursor
      hbrFlickerFreeDraw(PyGdiHANDLE):handle to background brush, can be None
      diFlags(int):icon-drawing flags (win32con.DI_*)

Returns:

      None
        
    """
    pass
        

def CreateIconIndirect(iconinfo:'PyICONINFO') -> 'int':
    """
    Creates an icon or cursor from an ICONINFO structure.

Args:

      iconinfo(PyICONINFO):Tuple defining the icon parameters

Returns:

      int
        
    """
    pass
        

def CreateIconFromResource(bits:'str',fIcon:'bool',ver:'int'=0x00030000) -> 'int':
    """
    Creates an icon or cursor from resource bits describing the icon.

Args:

      bits(str):The bits
      fIcon(bool):True if an icon, False if a cursor.
      ver(int):Specifies the version number of the icon or cursor format for the resource bits pointed to by the presbits parameter. This parameter can be 0x00030000.

Returns:

      int
        
    """
    pass
        

def LoadImage(hinst:'int',name:'Union[str, int]',type:'int',cxDesired:'int',cyDesired:'int',fuLoad:'int') -> 'Any':
    """
    Loads a bitmap, cursor or icon

Args:

      hinst(int):Handle to an instance of the module that contains the image to be loaded. To load an OEM image, set this parameter to zero.
      name(Union[str, int]):Specifies the image to load. If the hInst parameter is non-zero and the fuLoad parameter omits LR_LOADFROMFILE, name specifies the image resource in the hInst module. If the image resource is to be loaded by name, the name parameter is a string that contains the name of the image resource.
      type(int):Specifies the type of image to be loaded.
      cxDesired(int):Specifies the width, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CXICON or SM_CXCURSOR system metric value to set the width. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource width.
      cyDesired(int):Specifies the height, in pixels, of the icon or cursor. If this parameter is zero and the fuLoad parameter is LR_DEFAULTSIZE, the function uses the SM_CYICON or SM_CYCURSOR system metric value to set the height. If this parameter is zero and LR_DEFAULTSIZE is not used, the function uses the actual resource height.
      fuLoad(int):

Returns:

      Any
        
    """
    pass
        

def DeleteObject(handle:'PyGdiHANDLE') -> 'None':
    """
    Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object. After the object is deleted, the specified handle is no longer valid.

Args:

      handle(PyGdiHANDLE):handle to the object to delete.

Returns:

      None
        
    """
    pass
        

def BitBlt(hdcDest:'int',x:'int',y:'int',width:'int',height:'int',hdcSrc:'int',nXSrc:'int',nYSrc:'int',dwRop:'int') -> 'None':
    """
    Performs a bit-block transfer of the color data corresponding 

to a rectangle of pixels from the specified source device context into a 

destination device context.

Args:

      hdcDest(int):handle to destination DC
      x(int):x-coord of destination upper-left corner
      y(int):y-coord of destination upper-left corner
      width(int):width of destination rectangle
      height(int):height of destination rectangle
      hdcSrc(int):handle to source DC
      nXSrc(int):x-coordinate of source upper-left corner
      nYSrc(int):y-coordinate of source upper-left corner
      dwRop(int):raster operation code

Returns:

      None
        
    """
    pass
        

def StretchBlt(hdcDest:'int',x:'int',y:'int',width:'int',height:'int',hdcSrc:'int',nXSrc:'int',nYSrc:'int',nWidthSrc:'int',nHeightSrc:'int',dwRop:'int') -> 'None':
    """
    Copies a bitmap from a source rectangle into a destination 

rectangle, stretching or compressing the bitmap to fit the dimensions of the 

destination rectangle, if necessary

Args:

      hdcDest(int):handle to destination DC
      x(int):x-coord of destination upper-left corner
      y(int):y-coord of destination upper-left corner
      width(int):width of destination rectangle
      height(int):height of destination rectangle
      hdcSrc(int):handle to source DC
      nXSrc(int):x-coord of source upper-left corner
      nYSrc(int):y-coord of source upper-left corner
      nWidthSrc(int):width of source rectangle
      nHeightSrc(int):height of source rectangle
      dwRop(int):raster operation code

Returns:

      None
        
    """
    pass
        

def PatBlt(hdc:'int',XLeft:'int',YLeft:'int',Width:'int',Height:'int',Rop:'int') -> 'None':
    """
    Paints a rectangle by combining the current brush with existing colors

Args:

      hdc(int):Handle to a device context
      XLeft(int):Horizontal pos
      YLeft(int):Vertical pos
      Width(int):Width of rectangular area
      Height(int):Height of rectangular area
      Rop(int):Raster operation, one of PATCOPY,PATINVERT,DSTINVERT,BLACKNESS,WHITENESS

Returns:

      None
        
    """
    pass
        

def SetStretchBltMode(hdc:'int',StretchMode:'int') -> 'int':
    """
    None

Args:

      hdc(int):Handle to a device context
      StretchMode(int):One of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS, or WHITEONBLACK (from win32con)Return ValueIf the function succeeds, the return value is the previous stretching mode. If the function fails, the return value is zero.

Returns:

      int:One of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS, or WHITEONBLACK (from win32con)Return ValueIf the function succeeds, the return value is the previous stretching mode. 

If the function fails, the return value is zero.

        
    """
    pass
        

def GetStretchBltMode(hdc:'int') -> 'int':
    """
    None

Args:

      hdc(int):Handle to a device contextReturn ValueReturns one of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS,WHITEONBLACK, or 0 on error.

Returns:

      int:Handle to a device contextReturn ValueReturns one of BLACKONWHITE,COLORONCOLOR,HALFTONE,STRETCH_ANDSCANS,STRETCH_DELETESCANS,STRETCH_HALFTONE,STRETCH_ORSCANS,WHITEONBLACK, or 0 on error.

        
    """
    pass
        

def TransparentBlt(Dest:'int',XOriginDest:'int',YOriginDest:'int',WidthDest:'int',HeightDest:'int',Src:'int',XOriginSrc:'int',YOriginSrc:'int',WidthSrc:'int',HeightSrc:'int',Transparent:'int') -> 'None':
    """
    Transfers color from one DC to another, with one color treated as transparent

Args:

      Dest(int):Destination device context handle
      XOriginDest(int):X pos of dest rect
      YOriginDest(int):Y pos of dest rect
      WidthDest(int):Width of dest rect
      HeightDest(int):Height of dest rect
      Src(int):Source DC handle
      XOriginSrc(int):X pos of src rect
      YOriginSrc(int):Y pos of src rect
      WidthSrc(int):Width of src rect
      HeightSrc(int):Height of src rect
      Transparent(int):RGB color value that will be transparent

Returns:

      None
        
    """
    pass
        

def MaskBlt(Dest:'int',XDest:'int',YDest:'int',Width:'int',Height:'int',Src:'int',XSrc:'int',YSrc:'int',Mask:'PyGdiHANDLE',xMask:'int',yMask:'int',Rop:'int') -> 'None':
    """
    Combines the color data for the source and destination 

bitmaps using the specified mask and raster operation.

Args:

      Dest(int):Destination device context handle
      XDest(int):X pos of dest rect
      YDest(int):Y pos of dest rect
      Width(int):Width of rect to be copied
      Height(int):Height of rect to be copied
      Src(int):Source DC handle
      XSrc(int):X pos of src rect
      YSrc(int):Y pos of src rect
      Mask(PyGdiHANDLE):Handle to monochrome bitmap used to mask color
      xMask(int):X pos in mask
      yMask(int):Y pos in mask
      Rop(int):Foreground and background raster operations.  See MSDN docs for how to construct this value.CommentsThis function is not supported on Win9x.Win32 API References

Returns:

      None
        
    """
    pass
        

def AlphaBlend(Dest:'int',XOriginDest:'int',YOriginDest:'int',WidthDest:'int',HeightDest:'int',Src:'int',XOriginSrc:'int',YOriginSrc:'int',WidthSrc:'int',HeightSrc:'int',blendFunction:'PyBLENDFUNCTION') -> 'None':
    """
    Transfers color information using alpha blending

Args:

      Dest(int):Destination device context handle
      XOriginDest(int):X pos of dest rect
      YOriginDest(int):Y pos of dest rect
      WidthDest(int):Width of dest rect
      HeightDest(int):Height of dest rect
      Src(int):Source DC handle
      XOriginSrc(int):X pos of src rect
      YOriginSrc(int):Y pos of src rect
      WidthSrc(int):Width of src rect
      HeightSrc(int):Height of src rect
      blendFunction(PyBLENDFUNCTION):Alpha blending parameters

Returns:

      None
        
    """
    pass
        

def ImageList_Add(himl:'int',hbmImage:'PyGdiHANDLE',hbmMask:'PyGdiHANDLE') -> 'int':
    """
    Adds an image or images to an image list.

Args:

      himl(int):Handle to the image list.
      hbmImage(PyGdiHANDLE):Handle to the bitmap that contains the image or images. The number of images is inferred from the width of the bitmap.
      hbmMask(PyGdiHANDLE):Handle to the bitmap that contains the mask. If no mask is used with the image list, this parameter is ignoredReturn ValueReturns the index of the first new image if successful, or -1 otherwise.

Returns:

      int:Handle to the bitmap that contains the mask. If no mask is used with the image list, this parameter is ignoredReturn ValueReturns the index of the first new image if successful, or -1 otherwise.

        
    """
    pass
        

def ImageList_Create() -> 'Any':
    """
    Create an image list

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_Destroy() -> 'Any':
    """
    Destroy an imagelist

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_Draw() -> 'Any':
    """
    Draw an image on an HDC

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_DrawEx() -> 'Any':
    """
    Draw an image on an HDC

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_GetIcon() -> 'Any':
    """
    Extract an icon from an imagelist

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_GetImageCount() -> 'int':
    """
    Return count of images in imagelist

Args:



Returns:

      int
        
    """
    pass
        

def ImageList_LoadImage() -> 'Any':
    """
    Loads bitmaps, cursors or icons, creates imagelist

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_LoadBitmap() -> 'Any':
    """
    Creates an image list from the specified bitmap resource.

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_Remove() -> 'Any':
    """
    Remove an image from an imagelist

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_Replace() -> 'Any':
    """
    Replace an image in an imagelist with a bitmap image

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_ReplaceIcon() -> 'Any':
    """
    Replace an image in an imagelist with an icon image

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_SetBkColor() -> 'Any':
    """
    Set the background color for the imagelist

Args:



Returns:

      Any
        
    """
    pass
        

def ImageList_SetOverlayImage(hImageList:'int',iImage:'int',iOverlay:'int') -> 'None':
    """
    Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image.

Args:

      hImageList(int):
      iImage(int):
      iOverlay(int):

Returns:

      None
        
    """
    pass
        

def MessageBox(parent:'int',text:'Union[str]',caption:'Union[str]',flags:'int') -> 'int':
    """
    Displays a message box

Args:

      parent(int):The parent window
      text(Union[str]):The text for the message box
      caption(Union[str]):The caption for the message box
      flags(int):

Returns:

      int
        
    """
    pass
        

def MessageBeep(type:'int') -> 'None':
    """
    Plays a waveform sound.

Args:

      type(int):The type of the beep

Returns:

      None
        
    """
    pass
        

def CreateWindow(className:'Union[str, int]',windowTitle:'str',style:'int',x:'int',y:'int',width:'int',height:'int',parent:'int',menu:'int',hinstance:'int',reserved:'None') -> 'int':
    """
    Creates a new window.

Args:

      className(Union[str, int]):
      windowTitle(str):
      style(int):The style for the window.
      x(int):
      y(int):
      width(int):
      height(int):
      parent(int):Handle to the parent window.
      menu(int):Handle to the menu to use for this window.
      hinstance(int):
      reserved(None):Must be None

Returns:

      int
        
    """
    pass
        

def DestroyWindow(hwnd:'int') -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      None
        
    """
    pass
        

def EnableWindow(hWnd:'int',bEnable:'Any') -> 'int':
    """
    Enables and disables keyboard and mouse input to a window

Args:

      hWnd(int):Handle to window
      bEnable(Any):True to enable input to the window, False to disable inputReturn ValueReturns True if window was already disabled when call was made, False otherwise

Returns:

      int:True to enable input to the window, False to disable inputReturn ValueReturns True if window was already disabled when call was made, False otherwise

        
    """
    pass
        

def FindWindow(ClassName:'PyResourceId',WindowName:'str') -> 'int':
    """
    Retrieves a handle to the top-level window whose class name and window name match the specified strings.

Args:

      ClassName(PyResourceId):Name or atom of window class to find, can be None
      WindowName(str):Title of window to find, can be None

Returns:

      int
        
    """
    pass
        

def FindWindowEx(Parent:'int',ChildAfter:'int',ClassName:'PyResourceId',WindowName:'str') -> 'int':
    """
    Retrieves a handle to the top-level window whose class name and window name match the specified strings.

Args:

      Parent(int):Window whose child windows will be searched.  If 0, desktop window is assumed.
      ChildAfter(int):Child window after which to search in Z-order, can be 0 to search all
      ClassName(PyResourceId):Name or atom of window class to find, can be None
      WindowName(str):Title of window to find, can be None

Returns:

      int
        
    """
    pass
        

def DragAcceptFiles(hwnd:'int',fAccept:'int') -> 'None':
    """
    Registers whether a window accepts dropped files.

Args:

      hwnd(int):Handle to the Window
      fAccept(int):Value that indicates if the window identified by the hWnd parameter accepts dropped files. This value is True to accept dropped files or False to discontinue accepting dropped files.

Returns:

      None
        
    """
    pass
        

def DragDetect(hwnd:'int',point:'Tuple[int, int]') -> 'None':
    """
    captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point.

Args:

      hwnd(int):Handle to the Window
      point(Tuple[int, int]):Initial position of the mouse, in screen coordinates. The function determines the coordinates of the drag rectangle by using this point.Return ValueIf the user moved the mouse outside of the drag rectangle while holding down the left button , the return value is nonzero. If the user did not move the mouse outside of the drag rectangle while holding down the left button , the return value is zero.

Returns:

      None:Initial position of the mouse, in screen coordinates. The function determines the coordinates of the drag rectangle by using this point.Return ValueIf the user moved the mouse outside of the drag rectangle while holding down the left button , the return value is nonzero. 

If the user did not move the mouse outside of the drag rectangle while holding down the left button , the return value is zero.

        
    """
    pass
        

def SetDoubleClickTime(newVal:'int') -> 'None':
    """
    None

Args:

      newVal(int):

Returns:

      None
        
    """
    pass
        

def GetDoubleClickTime() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def HideCaret(hWnd:'int') -> 'None':
    """
    Hides the caret

Args:

      hWnd(int):Window that owns the caret, can be 0.

Returns:

      None
        
    """
    pass
        

def SetCaretPos(x:'int',y:'int') -> 'None':
    """
    Changes the position of the caret

Args:

      x(int):horizontal position
      y(int):vertical position

Returns:

      None
        
    """
    pass
        

def GetCaretPos() -> 'Tuple[int, int]':
    """
    Returns the current caret position

Args:



Returns:

      Tuple[int, int]
        
    """
    pass
        

def ShowCaret(hWnd:'int') -> 'None':
    """
    Shows the caret at its current position

Args:

      hWnd(int):Window that owns the caret, can be 0.

Returns:

      None
        
    """
    pass
        

def ShowWindow(hWnd:'int',cmdShow:'int') -> 'Any':
    """
    Shows or hides a window and changes its state

Args:

      hWnd(int):The handle to the window
      cmdShow(int):Combination of win32con.SW_* flags

Returns:

      Any
        
    """
    pass
        

def IsWindowVisible(hwnd:'int') -> 'int':
    """
    Indicates if the window has the WS_VISIBLE style.

Args:

      hwnd(int):The handle to the window

Returns:

      int
        
    """
    pass
        

def IsWindowEnabled(hwnd:'int') -> 'int':
    """
    Indicates if the window is enabled.

Args:

      hwnd(int):The handle to the window

Returns:

      int
        
    """
    pass
        

def SetFocus(hwnd:'int') -> 'None':
    """
    Sets focus to the specified window.

Args:

      hwnd(int):The handle to the window

Returns:

      None
        
    """
    pass
        

def GetFocus() -> 'None':
    """
    Returns the HWND of the window with focus.

Args:



Returns:

      None
        
    """
    pass
        

def UpdateWindow(hwnd:'int') -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      None
        
    """
    pass
        

def BringWindowToTop(hwnd:'int') -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      None
        
    """
    pass
        

def SetActiveWindow(hwnd:'int') -> 'Any':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      Any
        
    """
    pass
        

def GetActiveWindow() -> 'Any':
    """
    None

Args:



Returns:

      Any
        
    """
    pass
        

def SetForegroundWindow(hwnd:'int') -> 'Any':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      Any
        
    """
    pass
        

def GetForegroundWindow() -> 'Any':
    """
    None

Args:



Returns:

      Any
        
    """
    pass
        

def GetClientRect(hwnd:'int') -> 'Tuple[Any, Any, Any, Any]':
    """
    Returns the rectangle of the client area of a window, in client coordinates

Args:

      hwnd(int):The handle to the window

Returns:

      Tuple[Any, Any, Any, Any]
        
    """
    pass
        

def GetDC(hwnd:'int') -> 'Any':
    """
    Gets the device context for the window.

Args:

      hwnd(int):The handle to the window

Returns:

      Any
        
    """
    pass
        

def SaveDC(hdc:'int') -> 'int':
    """
    Save the state of a device context

Args:

      hdc(int):Handle to device contextReturn ValueReturns a value identifying the state that can be passed to win32gui::RestoreDC.  On error, returns 0.

Returns:

      int:Handle to device contextReturn ValueReturns a value identifying the state that can be passed to win32gui::RestoreDC.  On error, returns 0.

        
    """
    pass
        

def RestoreDC(hdc:'int',SavedDC:'int') -> 'None':
    """
    Restores a device context state

Args:

      hdc(int):Handle to a device context
      SavedDC(int):Identifier of state to be restored, as returned by win32gui::SaveDC.

Returns:

      None
        
    """
    pass
        

def DeleteDC(hdc:'int') -> 'None':
    """
    Deletes a DC

Args:

      hdc(int):The source DC

Returns:

      None
        
    """
    pass
        

def CreateCompatibleDC(dc:'int') -> 'Any':
    """
    Creates a memory device context (DC) compatible with the specified device.

Args:

      dc(int):handle to DC

Returns:

      Any
        
    """
    pass
        

def CreateCompatibleBitmap(hdc:'int',width:'int',height:'int') -> 'PyGdiHANDLE':
    """
    Creates a bitmap compatible with the device that is associated with the specified device context.

Args:

      hdc(int):handle to DC
      width(int):width of bitmap, in pixels
      height(int):height of bitmap, in pixels

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def CreateBitmap(width:'int',height:'int',cPlanes:'int',cBitsPerPixel:'int',bitmap_bits:'None') -> 'PyGdiHANDLE':
    """
    Creates a bitmap

Args:

      width(int):bitmap width, in pixels
      height(int):bitmap height, in pixels
      cPlanes(int):number of color planes
      cBitsPerPixel(int):number of bits to identify color
      bitmap_bits(None):Must be None

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def SelectObject(hdc:'int',object:'int') -> 'Any':
    """
    Selects an object into the specified device context (DC). The new object replaces the previous object of the same type.

Args:

      hdc(int):handle to DC
      object(int):The GDI object

Returns:

      Any
        
    """
    pass
        

def GetCurrentObject(hdc:'int',ObjectType:'int') -> 'int':
    """
    Retrieves currently selected object from a DC

Args:

      hdc(int):Handle to a device context
      ObjectType(int):Type of object to retrieve, one of win32con.OBJ_*;

Returns:

      int
        
    """
    pass
        

def GetWindowRect(hwnd:'int') -> 'Tuple[Any, Any, Any, Any]':
    """
    Returns the rectangle for a window in screen coordinates

Args:

      hwnd(int):The handle to the window

Returns:

      Tuple[Any, Any, Any, Any]
        
    """
    pass
        

def GetStockObject(Object:'int') -> 'int':
    """
    Creates a handle to one of the standard system Gdi objects

Args:

      Object(int):One of *_BRUSH, *_PEN, *_FONT, or *_PALLETTE constants

Returns:

      int
        
    """
    pass
        

def PostQuitMessage(rc:'int') -> 'None':
    """
    None

Args:

      rc(int):

Returns:

      None
        
    """
    pass
        

def WaitMessage() -> 'None':
    """
    Waits for a message

Args:



Returns:

      None
        
    """
    pass
        

def SetWindowPos(hWnd:'int',InsertAfter:'int',X:'int',Y:'int',cx:'int',cy:'int',Flags:'int') -> 'None':
    """
    Sets the position and size of a window

Args:

      hWnd(int):Handle to the window
      InsertAfter(int):Window that hWnd will be placed below.  Can be a window handle or one of HWND_BOTTOM,HWND_NOTOPMOST,HWND_TOP, or HWND_TOPMOST
      X(int):New X coord
      Y(int):New Y coord
      cx(int):New width of window
      cy(int):New height of window
      Flags(int):Combination of win32con.SWP_* flags

Returns:

      None
        
    """
    pass
        

def GetWindowPlacement() -> 'tuple':
    """
    Returns placement information about the current window.

Args:



Returns:

      tuple:win32gui.GetWindowPlacement

tuple = GetWindowPlacement()Returns placement information about the current window.
Return ValueThe result is a tuple of 

(flags, showCmd, (minposX, minposY), (maxposX, maxposY), (normalposX, normalposY))



Item


Description



flagsOne of the WPF_* constants
showCmdCurrent state - one of the SW_* constants.
minposSpecifies the coordinates of the window's upper-left corner when the window is minimized.
maxposSpecifies the coordinates of the window's upper-left corner when the window is maximized.
normalposSpecifies the window's coordinates when the window is in the restored position.

        
    """
    pass
        

def SetWindowPlacement(hWnd:'int',placement:'Any') -> 'None':
    """
    Sets the windows placement

Args:

      hWnd(int):Handle to a window
      placement(Any):A tuple representing the WINDOWPLACEMENT structure.

Returns:

      None
        
    """
    pass
        

def RegisterClass(wndClass:'PyWNDCLASS') -> 'int':
    """
    Registers a window class.

Args:

      wndClass(PyWNDCLASS):An object describing the window class.

Returns:

      int
        
    """
    pass
        

def UnregisterClass(atom:'PyResourceId',hinst:'int') -> 'None':
    """
    None

Args:

      atom(PyResourceId):The atom or classname identifying the class previously registered.
      hinst(int):The handle to the instance unregistering the class, can be None

Returns:

      None
        
    """
    pass
        

def PumpMessages() -> 'None':
    """
    Runs a message loop until a WM_QUIT message is received.

Args:



Returns:

      None:win32gui::PumpWaitingMessages
Return ValueReturns exit code from PostQuitMessage when a WM_QUIT message is received

        
    """
    pass
        

def PumpWaitingMessages() -> 'int':
    """
    Pumps all waiting messages for the current thread.

Args:



Returns:

      int:Search for PeekMessage and DispatchMessage at msdn, google or google groups.
Return ValueReturns non-zero (exit code from PostQuitMessage) if a WM_QUIT message was received, else 0

        
    """
    pass
        

def GetMessage(hwnd:'int',min:'int',max:'int') -> 'Any':
    """
    None

Args:

      hwnd(int):
      min(int):
      max(int):

Returns:

      Any
        
    """
    pass
        

def TranslateMessage(msg:'Any') -> 'int':
    """
    None

Args:

      msg(Any):

Returns:

      int
        
    """
    pass
        

def DispatchMessage(msg:'Any') -> 'int':
    """
    None

Args:

      msg(Any):

Returns:

      int
        
    """
    pass
        

def TranslateAccelerator(hwnd:'int',haccel:'int',msg:'Any') -> 'int':
    """
    None

Args:

      hwnd(int):
      haccel(int):
      msg(Any):

Returns:

      int
        
    """
    pass
        

def PeekMessage(hwnd:'int',filterMin:'int',filterMax:'int',removalOptions:'int') -> 'Any':
    """
    None

Args:

      hwnd(int):
      filterMin(int):
      filterMax(int):
      removalOptions(int):

Returns:

      Any
        
    """
    pass
        

def Shell_NotifyIcon(Message:'int',nid:'PyNOTIFYICONDATA') -> 'None':
    """
    Adds, removes or modifies a taskbar icon.

Args:

      Message(int):One of win32gui.NIM_* flags
      nid(PyNOTIFYICONDATA):Tuple containing NOTIFYICONDATA info

Returns:

      None
        
    """
    pass
        

def GetSystemMenu(hwnd:'int',bRevert:'int') -> 'int':
    """
    None

Args:

      hwnd(int):The handle to the window
      bRevert(int):Return ValueThe result is a HMENU to the menu.

Returns:

      int:Return ValueThe result is a HMENU to the menu.

        
    """
    pass
        

def DrawMenuBar(hwnd:'int') -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the window

Returns:

      None
        
    """
    pass
        

def MoveWindow(hwnd:'int',x:'int',y:'int',width:'int',height:'int',bRepaint:'int') -> 'None':
    """
    None

Args:

      hwnd(int):The handle to the window
      x(int):
      y(int):
      width(int):
      height(int):
      bRepaint(int):

Returns:

      None
        
    """
    pass
        

def CloseWindow() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def DeleteMenu(hmenu:'int',position:'int',flags:'int') -> 'None':
    """
    None

Args:

      hmenu(int):The handle to the menu
      position(int):The position to delete.
      flags(int):

Returns:

      None
        
    """
    pass
        

def RemoveMenu(hmenu:'int',position:'int',flags:'int') -> 'None':
    """
    None

Args:

      hmenu(int):The handle to the menu
      position(int):The position to delete.
      flags(int):

Returns:

      None
        
    """
    pass
        

def CreateMenu() -> 'int':
    """
    None

Args:



Returns:

      int:win32gui.CreateMenu

int = CreateMenu()
Return ValueThe result is a HMENU to the new menu.

        
    """
    pass
        

def CreatePopupMenu() -> 'int':
    """
    None

Args:



Returns:

      int:win32gui.CreatePopupMenu

int = CreatePopupMenu()
Return ValueThe result is a HMENU to the new menu.

        
    """
    pass
        

def TrackPopupMenu(hmenu:'int',flags:'Any',x:'int',y:'int',reserved:'int',hwnd:'Any',prcRect:'PyRECT') -> 'int':
    """
    Display popup shortcut menu

Args:

      hmenu(int):The handle to the menu
      flags(Any):flags
      x(int):x pos
      y(int):y pos
      reserved(int):reserved
      hwnd(Any):owner window
      prcRect(PyRECT):Pointer to rec (can be None)

Returns:

      int
        
    """
    pass
        

def CommDlgExtendedError() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def ExtractIcon(hinstance:'int',moduleName:'Union[str]',index:'int') -> 'int':
    """
    None

Args:

      hinstance(int):
      moduleName(Union[str]):
      index(int):CommentsYou must destroy the icon handle returned by calling the win32gui::DestroyIcon function.Return ValueThe result is a HICON.

Returns:

      int:Comments

You must destroy the icon handle returned by calling the win32gui::DestroyIcon function.
Return ValueThe result is a HICON.

        
    """
    pass
        

def ExtractIconEx(moduleName:'str',index:'int',numIcons:'int'=1) -> 'int':
    """
    None

Args:

      moduleName(str):
      index(int):
      numIcons(int):CommentsYou must destroy each icon handle returned by calling the win32gui::DestroyIcon function.Return ValueIf index==-1, the result is an integer with the number of icons in the file, otherwise it is 2 arrays of icon handles.

Returns:

      int:
Comments

You must destroy each icon handle returned by calling the win32gui::DestroyIcon function.
Return ValueIf index==-1, the result is an integer with the number of icons in 

the file, otherwise it is 2 arrays of icon handles.

        
    """
    pass
        

def DestroyIcon(hicon:'int') -> 'None':
    """
    None

Args:

      hicon(int):The icon to destroy.

Returns:

      None
        
    """
    pass
        

def GetIconInfo(hicon:'int') -> 'PyICONINFO':
    """
    Returns parameters for an icon or cursor

Args:

      hicon(int):The icon to queryReturn ValueThe result is a tuple of (fIcon, xHotspot, yHotspot, hbmMask, hbmColor) The hbmMask and hbmColor items are bitmaps created for the caller, so must be freed.

Returns:

      PyICONINFO:The icon to queryReturn ValueThe result is a tuple of (fIcon, xHotspot, yHotspot, hbmMask, hbmColor) 

The hbmMask and hbmColor items are bitmaps created for the caller, so must be freed.

        
    """
    pass
        

def ScreenToClient(hWnd:'int',Point:'Tuple[int, int]') -> 'Tuple[int, int]':
    """
    Convert screen coordinates to client coords

Args:

      hWnd(int):Handle to a window
      Point(Tuple[int, int]):Screen coordinates to be converted

Returns:

      Tuple[int, int]
        
    """
    pass
        

def ClientToScreen(hWnd:'int',Point:'Tuple[int, int]') -> 'Tuple[int, int]':
    """
    Convert client coordinates to screen coords

Args:

      hWnd(int):Handle to a window
      Point(Tuple[int, int]):Client coordinates to be converted

Returns:

      Tuple[int, int]
        
    """
    pass
        

def PaintDesktop(hdc:'int') -> 'None':
    """
    Fills a DC with the destop background

Args:

      hdc(int):Handle to a device context

Returns:

      None
        
    """
    pass
        

def RedrawWindow(hWnd:'int',rcUpdate:'Tuple[int, int, int, int]',hrgnUpdate:'PyGdiHANDLE',flags:'int') -> 'None':
    """
    Causes a portion of a window to be redrawn

Args:

      hWnd(int):Handle to window to be redrawn
      rcUpdate(Tuple[int, int, int, int]):Rectangle (left, top, right, bottom) identifying part of window to be redrawn, can be None
      hrgnUpdate(PyGdiHANDLE):Handle to region to be redrawn, can be None to indicate entire client area
      flags(int):Combination of win32con.RDW_* flags

Returns:

      None
        
    """
    pass
        

def GetTextExtentPoint32(hdc:'int',str:'str') -> 'Tuple[Any, Any]':
    """
    Computes the width and height of the specified string of text.

Args:

      hdc(int):The device context
      str(str):The string to measure.

Returns:

      Tuple[Any, Any]
        
    """
    pass
        

def GetTextMetrics() -> 'dict':
    """
    Returns info for the font selected into a DC

Args:



Returns:

      dict
        
    """
    pass
        

def GetTextCharacterExtra(hdc:'int') -> 'int':
    """
    Returns the space between characters

Args:

      hdc(int):Handle to a device context

Returns:

      int
        
    """
    pass
        

def SetTextCharacterExtra(hdc:'int',CharExtra:'int') -> 'int':
    """
    Sets the spacing between characters

Args:

      hdc(int):Handle to a device context
      CharExtra(int):Space between adjacent chars, in logical unitsReturn ValueReturns the previous spacing

Returns:

      int:Space between adjacent chars, in logical unitsReturn ValueReturns the previous spacing

        
    """
    pass
        

def GetTextAlign(hdc:'int') -> 'int':
    """
    Returns horizontal and vertical alignment for text in a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns combination of win32con.TA_* flags

Returns:

      int:Handle to a device contextReturn ValueReturns combination of win32con.TA_* flags

        
    """
    pass
        

def SetTextAlign(hdc:'int',Mode:'int') -> 'int':
    """
    Sets horizontal and vertical alignment for text in a device context

Args:

      hdc(int):Handle to a device context
      Mode(int):Combination of win32con.TA_* constantsReturn ValueReturns the previous alignment flags

Returns:

      int:Combination of win32con.TA_* constantsReturn ValueReturns the previous alignment flags

        
    """
    pass
        

def GetTextFace(hdc:'int') -> 'str':
    """
    Retrieves the name of the font currently selected in a DC

Args:

      hdc(int):Handle to a device contextCommentsCalls unicode api function (GetTextFaceW)

Returns:

      str
        
    """
    pass
        

def GetMapMode(hdc:'int') -> 'int':
    """
    Returns the method a device context uses to translate logical units to physical units

Args:

      hdc(int):Handle to a device contextReturn ValueReturns one of win32con.MM_* values

Returns:

      int:Handle to a device contextReturn ValueReturns one of win32con.MM_* values

        
    """
    pass
        

def SetMapMode(hdc:'int',MapMode:'int') -> 'int':
    """
    Sets the method used for translating logical units to device units

Args:

      hdc(int):Handle to a device context
      MapMode(int):The new mapping mode (win32con.MM_*)Return ValueReturns the previous mapping mode, one of win32con.MM_* constants

Returns:

      int:The new mapping mode (win32con.MM_*)Return ValueReturns the previous mapping mode, one of win32con.MM_* constants

        
    """
    pass
        

def GetGraphicsMode(hdc:'int') -> 'int':
    """
    Determines if advanced GDI features are enabled for a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns GM_COMPATIBLE or GM_ADVANCED

Returns:

      int:Handle to a device contextReturn ValueReturns GM_COMPATIBLE or GM_ADVANCED

        
    """
    pass
        

def SetGraphicsMode(hdc:'int',Mode:'int') -> 'int':
    """
    Enables or disables advanced graphics features for a DC

Args:

      hdc(int):Handle to a device context
      Mode(int):GM_COMPATIBLE or GM_ADVANCED (from win32con)Return ValueReturns the previous mode, one of win32con.GM_COMPATIBLE or win32con.GM_ADVANCED

Returns:

      int:GM_COMPATIBLE or GM_ADVANCED (from win32con)Return ValueReturns the previous mode, one of win32con.GM_COMPATIBLE or win32con.GM_ADVANCED

        
    """
    pass
        

def GetLayout(hdc:'int') -> 'int':
    """
    Retrieves the layout mode of a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns one of win32con.LAYOUT_*

Returns:

      int:Handle to a device contextReturn ValueReturns one of win32con.LAYOUT_*

        
    """
    pass
        

def SetLayout(hdc:'int',Layout:'int') -> 'int':
    """
    Sets the layout for a device context

Args:

      hdc(int):Handle to a device context
      Layout(int):One of win32con.LAYOUT_* constantsReturn ValueReturns the previous layout mode

Returns:

      int:One of win32con.LAYOUT_* constantsReturn ValueReturns the previous layout mode

        
    """
    pass
        

def GetPolyFillMode(hdc:'int') -> 'int':
    """
    Returns the polygon filling mode for a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns win32con.ALTERNATE or win32con.WINDING

Returns:

      int:Handle to a device contextReturn ValueReturns win32con.ALTERNATE or win32con.WINDING

        
    """
    pass
        

def SetPolyFillMode(hdc:'int',PolyFillMode:'int') -> 'int':
    """
    Sets the polygon filling mode for a device context

Args:

      hdc(int):Handle to a device context
      PolyFillMode(int):One of ALTERNATE or WINDINGReturn ValueReturns the previous mode, one of win32con.ALTERNATE or win32con.WINDING

Returns:

      int:One of ALTERNATE or WINDINGReturn ValueReturns the previous mode, one of win32con.ALTERNATE or win32con.WINDING

        
    """
    pass
        

def GetWorldTransform(hdc:'int') -> 'PyXFORM':
    """
    Retrieves a device context's coordinate space translation matrix

Args:

      hdc(int):Handle to a device contextCommentsDC's mode must be set to GM_ADVANCED.  See win32gui::SetGraphicsMode.

Returns:

      PyXFORM
        
    """
    pass
        

def SetWorldTransform(hdc:'int',Xform:'PyXFORM') -> 'None':
    """
    Transforms a device context's coordinate space

Args:

      hdc(int):Handle to a device context
      Xform(PyXFORM):Matrix defining the transformationCommentsDC's mode must be set to GM_ADVANCED.  See win32gui::SetGraphicsMode.

Returns:

      None
        
    """
    pass
        

def ModifyWorldTransform(hdc:'int',Xform:'PyXFORM',Mode:'int') -> 'None':
    """
    Combines a coordinate tranformation with device context's current transformation

Args:

      hdc(int):Handle to a device context
      Xform(PyXFORM):Transformation to be applied.  Ignored if Mode is MWT_IDENTITY.
      Mode(int):One of win32con.MWT_* values specifying how transformations will be combinedCommentsDC's mode must be set to GM_ADVANCED.  See win32gui::SetGraphicsMode.

Returns:

      None
        
    """
    pass
        

def CombineTransform(xform1:'PyXFORM',xform2:'PyXFORM') -> 'PyXFORM':
    """
    Combines two coordinate space transformations

Args:

      xform1(PyXFORM):First transformation
      xform2(PyXFORM):Second transformation

Returns:

      PyXFORM
        
    """
    pass
        

def GetWindowOrgEx(hdc:'int') -> 'Tuple[int, int]':
    """
    Retrievs the window origin for a DC

Args:

      hdc(int):Handle to a device context

Returns:

      Tuple[int, int]
        
    """
    pass
        

def SetWindowOrgEx(hdc:'int',X:'int',Y:'int') -> 'Tuple[int, int]':
    """
    Changes the window origin for a DC

Args:

      hdc(int):Handle to a device context
      X(int):New X coord in logical units
      Y(int):New Y coord in logical unitsReturn ValueReturns the previous origin

Returns:

      Tuple[int, int]:New Y coord in logical unitsReturn ValueReturns the previous origin

        
    """
    pass
        

def GetViewportOrgEx(hdc:'int') -> 'Tuple[int, int]':
    """
    Retrievs the origin for a DC's viewport

Args:

      hdc(int):Handle to a device context

Returns:

      Tuple[int, int]
        
    """
    pass
        

def SetViewportOrgEx(hdc:'int',X:'int',Y:'int') -> 'Tuple[int, int]':
    """
    Changes the viewport origin for a DC

Args:

      hdc(int):Handle to a device context
      X(int):New X coord in logical units
      Y(int):New Y coord in logical unitsReturn ValueReturns the previous origin as (x,y)

Returns:

      Tuple[int, int]:New Y coord in logical unitsReturn ValueReturns the previous origin as (x,y)

        
    """
    pass
        

def GetWindowExtEx(hdc:'int') -> 'Tuple[int, int]':
    """
    Retrieves the window extents for a DC

Args:

      hdc(int):Handle to a device contextReturn ValueReturns the extents as (x,y) in logical units

Returns:

      Tuple[int, int]:Handle to a device contextReturn ValueReturns the extents as (x,y) in logical units

        
    """
    pass
        

def SetWindowExtEx(hdc:'int',XExtent:'int',YExtent:'int') -> 'Tuple[int, int]':
    """
    Changes the window extents for a DC

Args:

      hdc(int):Handle to a device context
      XExtent(int):New X extent in logical units
      YExtent(int):New Y extent in logical unitsReturn ValueReturns the previous extents

Returns:

      Tuple[int, int]:New Y extent in logical unitsReturn ValueReturns the previous extents

        
    """
    pass
        

def GetViewportExtEx(hdc:'int') -> 'Tuple[int, int]':
    """
    Retrieves the viewport extents for a DC

Args:

      hdc(int):Handle to a device contextReturn ValueReturns the extents as (x,y) in logical units

Returns:

      Tuple[int, int]:Handle to a device contextReturn ValueReturns the extents as (x,y) in logical units

        
    """
    pass
        

def SetViewportExtEx(hdc:'int',XExtent:'int',YExtent:'int') -> 'Tuple[int, int]':
    """
    Changes the viewport extents for a DC

Args:

      hdc(int):Handle to a device context
      XExtent(int):New X extent in logical units
      YExtent(int):New Y extent in logical unitsReturn ValueReturns the previous extents as (x,y) in logical units

Returns:

      Tuple[int, int]:New Y extent in logical unitsReturn ValueReturns the previous extents as (x,y) in logical units

        
    """
    pass
        

def GradientFill(hdc:'int',Vertex:'Tuple[PyTRIVERTEX, ...]',Mesh:'tuple',Mode:'int') -> 'None':
    """
    Shades triangles or rectangles by interpolating between vertex colors

Args:

      hdc(int):Handle to device context
      Vertex(Tuple[PyTRIVERTEX, ...]):Sequence of TRIVERTEX dicts defining color info
      Mesh(tuple):Sequence of tuples containing either 2 or 3 ints that index into the trivertex array to define either triangles or rectangles
      Mode(int):win32con.GRADIENT_FILL_* value defining whether to fill by triangle or by rectangle

Returns:

      None
        
    """
    pass
        

def GetOpenFileName(OPENFILENAME:'Union[str, bytes]') -> 'int':
    """
    Creates an Open dialog box that lets the user specify the drive, directory, and the name of a file or set of files to open.

Args:

      OPENFILENAME(Union[str, bytes]):A string packed into an OPENFILENAME structure, probably via the struct module.CommentsThe win32gui::GetOpenFileNameW function is far more convenient to use.Return ValueIf the user presses OK, the function returns TRUE.  Otherwise, use CommDlgExtendedError for error details (ie, a win32gui.error is raised).  If the user cancels the dialog, the winerror attribute of the exception will be zero.

Returns:

      int:A string packed into an OPENFILENAME structure, probably via the struct module.Comments

The win32gui::GetOpenFileNameW function is far more convenient to use.
Return ValueIf the user presses OK, the function returns TRUE.  Otherwise, use CommDlgExtendedError for error details 

(ie, a win32gui.error is raised).  If the user cancels the dialog, the winerror attribute of the exception will be zero.

        
    """
    pass
        

def InsertMenuItem(hMenu:'int',uItem:'int',fByPosition:'int',menuItem:'Any') -> 'None':
    """
    Inserts a menu item

Args:

      hMenu(int):Handle to the menu
      uItem(int):The menu item identifier or the menu item position.
      fByPosition(int):Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.
      menuItem(Any):A string or buffer in the format of a MENUITEMINFO structure.

Returns:

      None
        
    """
    pass
        

def SetMenuItemInfo(hMenu:'int',uItem:'int',fByPosition:'int',menuItem:'Any') -> 'None':
    """
    Sets menu information

Args:

      hMenu(int):Handle to the menu
      uItem(int):The menu item identifier or the menu item position.
      fByPosition(int):Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.
      menuItem(Any):A string or buffer in the format of a MENUITEMINFO structure.

Returns:

      None
        
    """
    pass
        

def GetMenuItemInfo(hMenu:'int',uItem:'int',fByPosition:'int',menuItem:'Any') -> 'None':
    """
    Gets menu information

Args:

      hMenu(int):Handle to the menu
      uItem(int):The menu item identifier or the menu item position.
      fByPosition(int):Boolean value of True if uItem is set to a menu item position. This parameter is set to False if uItem is set to a menu item identifier.
      menuItem(Any):A string or buffer in the format of a MENUITEMINFO structure.

Returns:

      None
        
    """
    pass
        

def GetMenuItemCount(hMenu:'int') -> 'int':
    """
    None

Args:

      hMenu(int):Handle to the menu

Returns:

      int
        
    """
    pass
        

def GetMenuItemRect(hWnd:'int',hMenu:'int',uItem:'int') -> 'Tuple[int, int, int, int]':
    """
    None

Args:

      hWnd(int):
      hMenu(int):Handle to the menu
      uItem(int):

Returns:

      Tuple[int, int, int, int]
        
    """
    pass
        

def GetMenuState(hMenu:'int',uID:'int',flags:'int') -> 'int':
    """
    None

Args:

      hMenu(int):Handle to the menu
      uID(int):
      flags(int):

Returns:

      int
        
    """
    pass
        

def SetMenuDefaultItem(hMenu:'int',uItem:'int',fByPos:'int') -> 'None':
    """
    None

Args:

      hMenu(int):Handle to the menu
      uItem(int):
      fByPos(int):

Returns:

      None
        
    """
    pass
        

def GetMenuDefaultItem(hMenu:'int',fByPos:'int',flags:'int') -> 'int':
    """
    None

Args:

      hMenu(int):Handle to the menu
      fByPos(int):
      flags(int):

Returns:

      int
        
    """
    pass
        

def AppendMenu() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def InsertMenu() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def EnableMenuItem() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def CheckMenuItem() -> 'int':
    """
    None

Args:



Returns:

      int
        
    """
    pass
        

def GetSubMenu(hMenu:'int',nPos:'int') -> 'Any':
    """
    None

Args:

      hMenu(int):Handle to the menu
      nPos(int):

Returns:

      Any
        
    """
    pass
        

def ModifyMenu(hMnu:'int',uPosition:'int',uFlags:'int',uIDNewItem:'int',newItem:'str') -> 'None':
    """
    Changes an existing menu item. This function is used to specify the content, appearance, and behavior of the menu item.

Args:

      hMnu(int):handle to menu
      uPosition(int):menu item to modify
      uFlags(int):options
      uIDNewItem(int):identifier, menu, or submenu
      newItem(str):menu item content

Returns:

      None
        
    """
    pass
        

def GetMenuItemID(hMenu:'int',nPos:'int') -> 'int':
    """
    Retrieves the menu item identifier of a menu item located at the specified position in a menu.

Args:

      hMenu(int):handle to menu
      nPos(int):position of menu item

Returns:

      int
        
    """
    pass
        

def SetMenuItemBitmaps(hMenu:'int',uPosition:'int',uFlags:'int',hBitmapUnchecked:'PyGdiHANDLE',hBitmapChecked:'PyGdiHANDLE') -> 'None':
    """
    Associates the specified bitmap with a menu item. Whether the menu item is selected or clear, the system displays the appropriate bitmap next to the menu item.

Args:

      hMenu(int):handle to menu
      uPosition(int):menu item
      uFlags(int):options
      hBitmapUnchecked(PyGdiHANDLE):handle to unchecked bitmap, can be None
      hBitmapChecked(PyGdiHANDLE):handle to checked bitmap, can be None

Returns:

      None
        
    """
    pass
        

def CheckMenuRadioItem(hMenu:'int',idFirst:'int',idLast:'int',idCheck:'int',uFlags:'int') -> 'None':
    """
    Checks a specified menu item and makes it a 

radio item. At the same time, the function clears all other menu items in 

the associated group and clears the radio-item type flag for those items.

Args:

      hMenu(int):handle to menu
      idFirst(int):identifier or position of first item
      idLast(int):identifier or position of last item
      idCheck(int):identifier or position of item to check
      uFlags(int):options

Returns:

      None
        
    """
    pass
        

def SetMenuInfo(hmenu:'int',info:'Any') -> 'None':
    """
    Sets information for a specified menu.

Args:

      hmenu(int):handle to menu
      info(Any):menu information in the format of a buffer.CommentsSee win32gui_struct for helper functions.This function will raise NotImplementedError on early platforms (eg, Windows NT.)

Returns:

      None
        
    """
    pass
        

def GetMenuInfo(hmenu:'int',info:'Any') -> 'None':
    """
    Gets information about a specified menu.

Args:

      hmenu(int):handle to menu
      info(Any):A buffer to fill with the information.CommentsSee win32gui_struct for helper functions.This function will raise NotImplementedError on early platforms (eg, Windows NT.)

Returns:

      None
        
    """
    pass
        

def DrawFocusRect(hDC:'int',rc:'Tuple[int, int, int, int]') -> 'None':
    """
    Draws a standard focus outline around a rectangle

Args:

      hDC(int):Handle to a device context
      rc(Tuple[int, int, int, int]):Tuple of (left,top,right,bottom) defining the rectangle

Returns:

      None
        
    """
    pass
        

def DrawText(hDC:'Union[int]',String:'str',nCount:'int',Rect:'PyRECT',Format:'int') -> 'Tuple[int, PyRECT]':
    """
    Draws formatted text on a device context

Args:

      hDC(Union[int]):The device context on which to draw
      String(str):The text to be drawn
      nCount(int):The number of characters, use -1 for simple null-terminated string
      Rect(PyRECT):Tuple of 4 ints specifying the position (left, top, right, bottom)
      Format(int):Formatting flags, combination of win32con.DT_* valuesReturn ValueReturns the height of the drawn text, and the rectangle coordinates

Returns:

      Tuple[int, PyRECT]:Formatting flags, combination of win32con.DT_* valuesReturn ValueReturns the height of the drawn text, and the rectangle coordinates

        
    """
    pass
        

def LineTo(hdc:'int',XEnd:'int',YEnd:'int') -> 'None':
    """
    Draw a line from current position to specified point

Args:

      hdc(int):Handle to a device context
      XEnd(int):Horizontal position in logical units
      YEnd(int):Vertical position in logical units

Returns:

      None
        
    """
    pass
        

def Ellipse(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int') -> 'None':
    """
    Draws a filled ellipse on a device context

Args:

      hdc(int):Device context on which to draw
      LeftRect(int):Left limit of ellipse
      TopRect(int):Top limit of ellipse
      RightRect(int):Right limit of ellipse
      BottomRect(int):Bottom limit of ellipse

Returns:

      None
        
    """
    pass
        

def Pie(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',XRadial1:'int',YRadial1:'int',XRadial2:'int',YRadial2:'int') -> 'None':
    """
    Draws a section of an ellipse cut by 2 radials

Args:

      hdc(int):Device context on which to draw
      LeftRect(int):Left limit of ellipse
      TopRect(int):Top limit of ellipse
      RightRect(int):Right limit of ellipse
      BottomRect(int):Bottom limit of ellipse
      XRadial1(int):Horizontal pos of Radial1 endpoint
      YRadial1(int):Vertical pos of Radial1 endpoint
      XRadial2(int):Horizontal pos of Radial2 endpoint
      YRadial2(int):Vertical pos of Radial2 endpoint

Returns:

      None
        
    """
    pass
        

def Arc(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',XRadial1:'int',YRadial1:'int',XRadial2:'int',YRadial2:'int') -> 'None':
    """
    Draws an arc defined by an ellipse and 2 radials

Args:

      hdc(int):Device context on which to draw
      LeftRect(int):Left limit of ellipse
      TopRect(int):Top limit of ellipse
      RightRect(int):Right limit of ellipse
      BottomRect(int):Bottom limit of ellipse
      XRadial1(int):Horizontal pos of Radial1 endpoint
      YRadial1(int):Vertical pos of Radial1 endpoint
      XRadial2(int):Horizontal pos of Radial2 endpoint
      YRadial2(int):Vertical pos of Radial2 endpoint

Returns:

      None
        
    """
    pass
        

def ArcTo(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',XRadial1:'int',YRadial1:'int',XRadial2:'int',YRadial2:'int') -> 'None':
    """
    Draws an arc defined by an ellipse and 2 radials

Args:

      hdc(int):Device context on which to draw
      LeftRect(int):Left limit of ellipse
      TopRect(int):Top limit of ellipse
      RightRect(int):Right limit of ellipse
      BottomRect(int):Bottom limit of ellipse
      XRadial1(int):Horizontal pos of Radial1 endpoint
      YRadial1(int):Vertical pos of Radial1 endpoint
      XRadial2(int):Horizontal pos of Radial2 endpoint
      YRadial2(int):Vertical pos of Radial2 endpointCommentsDraws exactly as win32gui::Arc, but changes current drawing position

Returns:

      None
        
    """
    pass
        

def AngleArc(hdc:'int',Y:'int',Y1:'int',Radius:'int',StartAngle:'float',SweepAngle:'float') -> 'None':
    """
    Draws a line from current pos and a section of a circle's arc

Args:

      hdc(int):Handle to a device context
      Y(int):x pos of circle
      Y1(int):y pos of circle
      Radius(int):Radius of circle
      StartAngle(float):Angle where arc starts, in degrees
      SweepAngle(float):Angle that arc covers, in degrees

Returns:

      None
        
    """
    pass
        

def Chord(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',XRadial1:'int',YRadial1:'int',XRadial2:'int',YRadial2:'int') -> 'None':
    """
    Draws a chord defined by an ellipse and 2 radials

Args:

      hdc(int):Device context on which to draw
      LeftRect(int):Left limit of ellipse
      TopRect(int):Top limit of ellipse
      RightRect(int):Right limit of ellipse
      BottomRect(int):Bottom limit of ellipse
      XRadial1(int):Horizontal pos of Radial1 endpoint
      YRadial1(int):Vertical pos of Radial1 endpoint
      XRadial2(int):Horizontal pos of Radial2 endpoint
      YRadial2(int):Vertical pos of Radial2 endpoint

Returns:

      None
        
    """
    pass
        

def ExtFloodFill(Unknow:'int',XStart:'int',YStart:'int',Color:'int',FillType:'int') -> 'None':
    """
    Fills an area with current brush

Args:

      Unknow(int):Handle to a device context
      XStart(int):Horizontal starting pos
      YStart(int):Vertical starting pos
      Color(int):RGB color value.  See win32api::RGB.
      FillType(int):One of win32con.FLOODFILL* values

Returns:

      None
        
    """
    pass
        

def SetPixel(hdc:'int',X:'int',Y:'int',Color:'int') -> 'int':
    """
    Set the color of a single pixel

Args:

      hdc(int):Handle to a device context
      X(int):Horizontal pos
      Y(int):Vertical pos
      Color(int):RGB color to be set.Return ValueReturns the RGB color actually set, which may be different from the one passed in

Returns:

      int:RGB color to be set.Return ValueReturns the RGB color actually set, which may be different from the one passed in

        
    """
    pass
        

def GetPixel(hdc:'int',XPos:'int',YPos:'int') -> 'int':
    """
    Returns the RGB color of a single pixel

Args:

      hdc(int):Handle to a device context
      XPos(int):Horizontal pos
      YPos(int):Vertical pos

Returns:

      int
        
    """
    pass
        

def GetROP2(hdc:'int') -> 'int':
    """
    Returns the foreground mixing mode of a DC

Args:

      hdc(int):Handle to a device contextReturn ValueReturns one of win32con.R2_* values

Returns:

      int:Handle to a device contextReturn ValueReturns one of win32con.R2_* values

        
    """
    pass
        

def SetROP2(hdc:'int',DrawMode:'int') -> 'int':
    """
    Sets the foreground mixing mode of a DC

Args:

      hdc(int):Handle to a device context
      DrawMode(int):Mixing mode, one of win32con.R2_*.Return ValueReturns previous mode

Returns:

      int:Mixing mode, one of win32con.R2_*.Return ValueReturns previous mode

        
    """
    pass
        

def SetPixelV(hdc:'int',X:'int',Y:'int',Color:'int') -> 'None':
    """
    Sets the color of a single pixel to an approximation of specified color

Args:

      hdc(int):Handle to a device context
      X(int):Horizontal pos
      Y(int):Vertical pos
      Color(int):RGB color to be set.

Returns:

      None
        
    """
    pass
        

def MoveToEx(hdc:'int',X:'int',Y:'int') -> 'Tuple[int, int]':
    """
    Changes the current drawing position

Args:

      hdc(int):Device context handle
      X(int):Horizontal pos in logical units
      Y(int):Vertical pos in logical unitsReturn ValueReturns the previous position as (X, Y)

Returns:

      Tuple[int, int]:Vertical pos in logical unitsReturn ValueReturns the previous position as (X, Y)

        
    """
    pass
        

def GetCurrentPositionEx(hdc:'int') -> 'Tuple[int, int]':
    """
    Returns a device context's current drawing position

Args:

      hdc(int):Device context

Returns:

      Tuple[int, int]
        
    """
    pass
        

def GetArcDirection(hdc:'int') -> 'int':
    """
    Returns the direction in which rectangles and arcs are drawn

Args:

      hdc(int):Handle to a device contextReturn ValueRecturns one of win32con.AD_* values

Returns:

      int:Handle to a device contextReturn ValueRecturns one of win32con.AD_* values

        
    """
    pass
        

def SetArcDirection(hdc:'int',ArcDirection:'int') -> 'int':
    """
    Sets the drawing direction for arcs and rectangles

Args:

      hdc(int):Handle to a device context
      ArcDirection(int):One of win32con.AD_* constantsReturn ValueReturns the previous direction, or 0 on error.

Returns:

      int:One of win32con.AD_* constantsReturn ValueReturns the previous direction, or 0 on error.

        
    """
    pass
        

def Polygon(hdc:'int',Points:'List[Any]') -> 'None':
    """
    Draws a closed filled polygon defined by a sequence of points

Args:

      hdc(int):Handle to a device context
      Points(List[Any]):Sequence of POINT tuples: ((x,y),...)

Returns:

      None
        
    """
    pass
        

def Polyline(hdc:'int',Points:'List[Any]') -> 'None':
    """
    Connects a sequence of points using currently selected pen

Args:

      hdc(int):Handle to a device context
      Points(List[Any]):Sequence of POINT tuples: ((x,y),...)

Returns:

      None
        
    """
    pass
        

def PolylineTo(hdc:'int',Points:'List[Any]') -> 'None':
    """
    Draws a series of lines starting from current position.  Updates current position with end point.

Args:

      hdc(int):Handle to a device context
      Points(List[Any]):Sequence of POINT tuples: ((x,y),...)

Returns:

      None
        
    """
    pass
        

def PolyBezier(hdc:'int',Points:'List[Any]') -> 'None':
    """
    Draws a series of Bezier curves starting from first point specified.

Args:

      hdc(int):Handle to a device context
      Points(List[Any]):Sequence of POINT tuples: ((x,y),...).CommentsNumber of points must be a multiple of 3 plus 1.

Returns:

      None
        
    """
    pass
        

def PolyBezierTo(hdc:'int',Points:'List[Any]') -> 'None':
    """
    Draws a series of Bezier curves starting from current drawing position.

Args:

      hdc(int):Handle to a device context
      Points(List[Any]):Sequence of POINT tuples: ((x,y),...).CommentsPoints must contain 3 points for each curve.  Current position is updated with last endpoint.

Returns:

      None
        
    """
    pass
        

def PlgBlt(Dest:'int',Point:'tuple',Src:'int',XSrc:'int',YSrc:'int',Width:'int',Height:'int',Mask:'PyGdiHANDLE'=None,xMask:'int'=0,yMask:'int'=0) -> 'None':
    """
    Copies color from a rectangle into a parallelogram

Args:

      Dest(int):Destination DC
      Point(tuple):Sequence of 3 POINT tuples (x,y) describing a paralellogram
      Src(int):Source device context
      XSrc(int):Left edge of source rectangle
      YSrc(int):Top of source rectangle
      Width(int):Width of source rectangle
      Height(int):Height of source rectangle
      Mask(PyGdiHANDLE):Handle to monochrome bitmap to mask source, can be None
      xMask(int):x pos in mask
      yMask(int):y pos in mask

Returns:

      None
        
    """
    pass
        

def CreatePolygonRgn(Points:'List[Any]',PolyFillMode:'int') -> 'PyGdiHANDLE':
    """
    Creates a region from a sequence of vertices

Args:

      Points(List[Any]):Sequence of POINT tuples: ((x,y),...).
      PolyFillMode(int):Filling mode, one of ALTERNATE, WINDING

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def ExtTextOut(hdc:'int',int:'Any',int1:'Any',int2:'Any',rect:'PyRECT',string:'Any',tuple:'Tuple[Tuple[Any, Any], ...]') -> 'int':
    """
    Writes text to a DC.

Args:

      hdc(int):Handle to a device context
      int(Any):The x coordinate to write the text to.
      int1(Any):The y coordinate to write the text to.
      int2(Any):Specifies the rectangle type. This parameter can be one, both, or neither of ETO_CLIPPED and ETO_OPAQUE
      rect(PyRECT):Specifies the text's bounding rectangle.  (Can be None.)
      string(Any):The text to write.
      tuple(Tuple[Tuple[Any, Any], ...]):Optional array of values that indicate distance between origins of character cells.Win32 API References

Returns:

      int:Search for ExtTextOut at msdn, google or google groups.
Return ValueAlways none.  If the function fails, an exception is raised.

        
    """
    pass
        

def GetTextColor(hdc:'int') -> 'int':
    """
    Returns the text color for a DC

Args:

      hdc(int):Handle to a device contextReturn ValueReturns an RGB color.  On error, returns CLR_INVALID

Returns:

      int:Handle to a device contextReturn ValueReturns an RGB color.  On error, returns CLR_INVALID

        
    """
    pass
        

def SetTextColor(hdc:'int',color:'int') -> 'int':
    """
    Changes the text color for a device context

Args:

      hdc(int):Handle to a device context
      color(int):The RGB color value - see win32api::RGBReturn ValueReturns the previous color, or CLR_INVALID on failure

Returns:

      int:The RGB color value - see win32api::RGBReturn ValueReturns the previous color, or CLR_INVALID on failure

        
    """
    pass
        

def GetBkMode(hdc:'int') -> 'int':
    """
    Returns the background mode for a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns OPAQUE, TRANSPARENT, or 0 on failure

Returns:

      int:Handle to a device contextReturn ValueReturns OPAQUE, TRANSPARENT, or 0 on failure

        
    """
    pass
        

def SetBkMode(hdc:'Union[int]',BkMode:'int') -> 'int':
    """
    Sets the background mode for a device context

Args:

      hdc(Union[int]):Handle to a device context
      BkMode(int):OPAQUE or TRANSPARENTReturn ValueReturns the previous mode, or 0 on failure

Returns:

      int:OPAQUE or TRANSPARENTReturn ValueReturns the previous mode, or 0 on failure

        
    """
    pass
        

def GetBkColor(hdc:'int') -> 'int':
    """
    Returns the background color for a device context

Args:

      hdc(int):Handle to a device contextReturn ValueReturns an RGB color value.  On error, returns CLR_INVALID.

Returns:

      int:Handle to a device contextReturn ValueReturns an RGB color value.  On error, returns CLR_INVALID.

        
    """
    pass
        

def SetBkColor(hdc:'Union[int]',color:'int') -> 'int':
    """
    Sets the background color for a device context

Args:

      hdc(Union[int]):Handle to a device context
      color(int):Return ValueReturns the previous color, or CLR_INVALID on failure

Returns:

      int:Return ValueReturns the previous color, or CLR_INVALID on failure

        
    """
    pass
        

def DrawEdge(hdc:'int',rc:'PyRECT',edge:'int',Flags:'int') -> 'PyRECT':
    """
    Draws edge(s) of a rectangle

Args:

      hdc(int):Handle to a device context
      rc(PyRECT):Rectangle whose edge(s) will be drawn
      edge(int):Combination of win32con.BDR_* flags, or one of win32con.EDGE_* flags
      Flags(int):Combination of win32con.BF_* flagsReturn ValueBF_ADJUST flag causes input rectange to be shrunk by size of border.. Rectangle is always returned.

Returns:

      PyRECT:Combination of win32con.BF_* flagsReturn ValueBF_ADJUST flag causes input rectange to be shrunk by size of border.. Rectangle is always returned.

        
    """
    pass
        

def FillRect(hDC:'int',rc:'PyRECT',hbr:'PyGdiHANDLE') -> 'None':
    """
    Fills a rectangular area with specified brush

Args:

      hDC(int):Handle to a device context
      rc(PyRECT):Rectangle to be filled
      hbr(PyGdiHANDLE):Handle to brush to be used to fill area

Returns:

      None
        
    """
    pass
        

def FillRgn(hdc:'int',hrgn:'PyGdiHANDLE',hbr:'PyGdiHANDLE') -> 'None':
    """
    Fills a region with specified brush

Args:

      hdc(int):Handle to the device context
      hrgn(PyGdiHANDLE):Handle to the region
      hbr(PyGdiHANDLE):Brush to be used

Returns:

      None
        
    """
    pass
        

def PaintRgn(hdc:'int',hrgn:'PyGdiHANDLE') -> 'None':
    """
    Paints a region with current brush

Args:

      hdc(int):Handle to the device context
      hrgn(PyGdiHANDLE):Handle to the region

Returns:

      None
        
    """
    pass
        

def FrameRgn(hdc:'int',hrgn:'Any',hbr:'Any',Width:'int',Height:'int') -> 'None':
    """
    Draws a frame around a region

Args:

      hdc(int):Handle to the device context
      hrgn(Any):Handle to the region
      hbr(Any):Handle to brush to be used
      Width(int):Frame width
      Height(int):Frame height

Returns:

      None
        
    """
    pass
        

def InvertRgn(hdc:'int',hrgn:'Any') -> 'None':
    """
    Inverts the colors in a region

Args:

      hdc(int):Handle to the device context
      hrgn(Any):Handle to the region

Returns:

      None
        
    """
    pass
        

def EqualRgn(SrcRgn1:'Any',SrcRgn2:'Any') -> 'Any':
    """
    Determines if 2 regions are equal

Args:

      SrcRgn1(Any):Handle to a region
      SrcRgn2(Any):Handle to a region

Returns:

      Any
        
    """
    pass
        

def PtInRegion(hrgn:'Any',X:'int',Y:'int') -> 'Any':
    """
    Determines if a region contains a point

Args:

      hrgn(Any):Handle to a region
      X(int):X coord
      Y(int):Y coord

Returns:

      Any
        
    """
    pass
        

def PtInRect(rect:'Tuple[int, int, int, int]',point:'Tuple[int, int]') -> 'Any':
    """
    Determines if a rectangle contains a point

Args:

      rect(Tuple[int, int, int, int]):The rect to check
      point(Tuple[int, int]):The point

Returns:

      Any
        
    """
    pass
        

def RectInRegion(hrgn:'Any',rc:'PyRECT') -> 'Any':
    """
    Determines if a region and rectangle overlap at any point

Args:

      hrgn(Any):Handle to a region
      rc(PyRECT):Rectangle coordinates in logical units

Returns:

      Any
        
    """
    pass
        

def SetRectRgn(hrgn:'Any',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int') -> 'None':
    """
    Makes an existing region rectangular

Args:

      hrgn(Any):Handle to a region
      LeftRect(int):Left edge in logical units
      TopRect(int):Top edge in logical units
      RightRect(int):Right edge in logical units
      BottomRect(int):Bottom edge in logical units

Returns:

      None
        
    """
    pass
        

def CombineRgn(Dest:'Any',Src1:'Any',Src2:'Any',CombineMode:'int') -> 'int':
    """
    Combines two regions

Args:

      Dest(Any):Handle to existing region that will receive combined region
      Src1(Any):Handle to first region
      Src2(Any):Handle to second region
      CombineMode(int):One of RGN_AND,RGN_COPY,RGN_DIFF,RGN_OR,RGN_XORReturn ValueReturns the type of region created, one of NULLREGION, SIMPLEREGION, COMPLEXREGION

Returns:

      int:One of RGN_AND,RGN_COPY,RGN_DIFF,RGN_OR,RGN_XORReturn ValueReturns the type of region created, one of NULLREGION, SIMPLEREGION, COMPLEXREGION

        
    """
    pass
        

def DrawAnimatedRects(hwnd:'int',idAni:'int',minCoords:'PyRECT',restCoords:'PyRECT') -> 'None':
    """
    Animates a rectangle in the manner of minimizing, mazimizing, or opening

Args:

      hwnd(int):handle to clipping window
      idAni(int):type of animation, win32con.IDANI_*
      minCoords(PyRECT):rectangle coordinates (minimized)
      restCoords(PyRECT):rectangle coordinates (restored)

Returns:

      None
        
    """
    pass
        

def CreateSolidBrush(Color:'int') -> 'PyGdiHANDLE':
    """
    Creates a solid brush of specified color

Args:

      Color(int):RGB color value.  See win32api::RGB.

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def CreatePatternBrush(hbmp:'PyGdiHANDLE') -> 'PyGdiHANDLE':
    """
    Creates a brush using a bitmap as a pattern

Args:

      hbmp(PyGdiHANDLE):Handle to a bitmap

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def CreateHatchBrush(Style:'int',clrref:'int') -> 'PyGdiHANDLE':
    """
    Creates a hatch brush with specified style and color

Args:

      Style(int):Hatch style, one of win32con.HS_* constants
      clrref(int):Rgb color value.  See win32api::RGB.

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def CreatePen(PenStyle:'int',Width:'int',Color:'int') -> 'PyGdiHANDLE':
    """
    Create a GDI pen

Args:

      PenStyle(int):One of win32con.PS_* pen styles
      Width(int):Drawing width in logical units.  Use zero for single pixel.
      Color(int):RGB color value.  See win32api::RGB.

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def GetSysColor(Index:'int') -> 'int':
    """
    Returns the color of a window element

Args:

      Index(int):One of win32con.COLOR_* values

Returns:

      int
        
    """
    pass
        

def GetSysColorBrush(Index:'int') -> 'PyGdiHANDLE':
    """
    Creates a handle to a system color brush

Args:

      Index(int):Index of a window element color (win32con.COLOR_*)

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def InvalidateRect(hWnd:'int',Rect:'PyRECT',Erase:'Any') -> 'None':
    """
    Invalidates a rectangular area of a window and adds it to the window's update region

Args:

      hWnd(int):Handle to the window
      Rect(PyRECT):Client coordinates defining area to be redrawn.  Use None for entire client area.
      Erase(Any):Indicates if background should be erased

Returns:

      None
        
    """
    pass
        

def FrameRect(hDC:'int',rc:'PyRECT',hbr:'PyGdiHANDLE') -> 'None':
    """
    Draws an outline around a rectangle

Args:

      hDC(int):Handle to a device context
      rc(PyRECT):Rectangle around which to draw
      hbr(PyGdiHANDLE):Handle to brush created using CreateHatchBrush, CreatePatternBrush, CreateSolidBrush, or GetStockObject

Returns:

      None
        
    """
    pass
        

def InvertRect(hDC:'int',rc:'PyRECT') -> 'None':
    """
    Inverts the colors in a regtangular region

Args:

      hDC(int):Handle to a device context
      rc(PyRECT):Coordinates of rectangle to invert

Returns:

      None
        
    """
    pass
        

def WindowFromDC(hDC:'int') -> 'int':
    """
    Finds the window associated with a device context

Args:

      hDC(int):Handle to a device contextReturn ValueReturns a handle to the window, or 0 if the DC is not associated with a window

Returns:

      int:Handle to a device contextReturn ValueReturns a handle to the window, or 0 if the DC is not associated with a window

        
    """
    pass
        

def GetUpdateRgn(hWnd:'int',hRgn:'PyGdiHANDLE',Erase:'Any') -> 'int':
    """
    Copies the update region of a window into an existing region

Args:

      hWnd(int):Handle to a window
      hRgn(PyGdiHANDLE):Handle to an existing region to receive update area
      Erase(Any):Indicates if window background is to be erasedReturn ValueReturns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

Returns:

      int:Indicates if window background is to be erasedReturn ValueReturns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

        
    """
    pass
        

def GetWindowRgn(hWnd:'int',hRgn:'PyGdiHANDLE') -> 'int':
    """
    Copies the window region of a window into an existing region

Args:

      hWnd(int):Handle to a window
      hRgn(PyGdiHANDLE):Handle to an existing region that receives window regionReturn ValueReturns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

Returns:

      int:Handle to an existing region that receives window regionReturn ValueReturns type of region, one of COMPLEXREGION, NULLREGION, or SIMPLEREGION

        
    """
    pass
        

def SetWindowRgn(hWnd:'int',hRgn:'PyGdiHANDLE',Redraw:'Any') -> 'None':
    """
    Sets the visible region of a window

Args:

      hWnd(int):Handle to a window
      hRgn(PyGdiHANDLE):Handle to region to be set, can be None
      Redraw(Any):Indicates if window should be completely redrawnCommentsOn success, the system assumes ownership of the region so you should call the handle's Detach() method to prevent it from being automatically closed.

Returns:

      None
        
    """
    pass
        

def GetWindowRgnBox(hWnd:'int') -> 'Tuple[int, PyRECT]':
    """
    Returns the bounding box for a window's region

Args:

      hWnd(int):Handle to a window that has a window region. (see win32gui::SetWindowRgn)CommentsOnly available in winxpguiReturn ValueReturns type of region and rectangle coordinates in device units

Returns:

      Tuple[int, PyRECT]:Handle to a window that has a window region. (see win32gui::SetWindowRgn)Comments

Only available in winxpgui
Return ValueReturns type of region and rectangle coordinates in device units

        
    """
    pass
        

def ValidateRgn(hWnd:'int',hRgn:'PyGdiHANDLE') -> 'None':
    """
    Removes a region from a window's update region

Args:

      hWnd(int):Handle to the window
      hRgn(PyGdiHANDLE):Region to be validated

Returns:

      None
        
    """
    pass
        

def InvalidateRgn(hWnd:'int',hRgn:'PyGdiHANDLE',Erase:'Any') -> 'None':
    """
    Adds a region to a window's update region

Args:

      hWnd(int):Handle to the window
      hRgn(PyGdiHANDLE):Region to be redrawn
      Erase(Any):Indidates if background should be erased

Returns:

      None
        
    """
    pass
        

def GetRgnBox(hrgn:'PyGdiHANDLE') -> 'Tuple[int, PyRECT]':
    """
    Calculates the bounding box of a region

Args:

      hrgn(PyGdiHANDLE):Handle to a regionReturn ValueReturns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION) and rectangle in logical units

Returns:

      Tuple[int, PyRECT]:Handle to a regionReturn ValueReturns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION) and rectangle in logical units

        
    """
    pass
        

def OffsetRgn(hrgn:'PyGdiHANDLE',XOffset:'int',YOffset:'int') -> 'int':
    """
    Relocates a region

Args:

      hrgn(PyGdiHANDLE):Handle to a region
      XOffset(int):Horizontal offset
      YOffset(int):Vertical offsetReturn ValueReturns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION)

Returns:

      int:Vertical offsetReturn ValueReturns type of region (COMPLEXREGION, NULLREGION, or SIMPLEREGION)

        
    """
    pass
        

def Rectangle(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int') -> 'None':
    """
    Creates a solid rectangle using currently selected pen and brush

Args:

      hdc(int):Handle to device context
      LeftRect(int):Position of left edge of rectangle
      TopRect(int):Position of top edge of rectangle
      RightRect(int):Position of right edge of rectangle
      BottomRect(int):Position of bottom edge of rectangle

Returns:

      None
        
    """
    pass
        

def RoundRect(hdc:'int',LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',Width:'int',Height:'int') -> 'None':
    """
    Draws a rectangle with elliptically rounded corners, filled using using current brush

Args:

      hdc(int):Handle to device context
      LeftRect(int):Position of left edge of rectangle
      TopRect(int):Position of top edge of rectangle
      RightRect(int):Position of right edge of rectangle
      BottomRect(int):Position of bottom edge of rectangle
      Width(int):Width of ellipse
      Height(int):Height of ellipse

Returns:

      None
        
    """
    pass
        

def BeginPaint() -> 'Tuple[Any, Any]':
    """
    None

Args:



Returns:

      Tuple[Any, Any]
        
    """
    pass
        

def EndPaint(hwnd:'int',ps:'Any') -> 'None':
    """
    None

Args:

      hwnd(int):
      ps(Any):As returned from win32gui::BeginPaint

Returns:

      None
        
    """
    pass
        

def BeginPath(hdc:'int') -> 'None':
    """
    Initializes a path in a DC

Args:

      hdc(int):Handle to a device context

Returns:

      None
        
    """
    pass
        

def EndPath(hdc:'int') -> 'None':
    """
    None

Args:

      hdc(int):Handle to a device context

Returns:

      None
        
    """
    pass
        

def AbortPath(hdc:'int') -> 'None':
    """
    None

Args:

      hdc(int):Handle to a device context

Returns:

      None
        
    """
    pass
        

def CloseFigure(hdc:'int') -> 'None':
    """
    Closes a section of a path by connecting the beginning pos with the current pos

Args:

      hdc(int):Handle to a device context that contains an open path. See win32gui::BeginPath.

Returns:

      None
        
    """
    pass
        

def FlattenPath(hdc:'int') -> 'None':
    """
    Flattens any curves in current path into a series of lines

Args:

      hdc(int):Handle to a device context that contains a closed path. See win32gui::EndPath.

Returns:

      None
        
    """
    pass
        

def FillPath(hdc:'int') -> 'None':
    """
    Fills a path with currently selected brush

Args:

      hdc(int):Handle to a device context that contains a finalized path. See win32gui::EndPath.CommentsAny open figures are closed and path is deselected from the DC.

Returns:

      None
        
    """
    pass
        

def WidenPath(hdc:'int') -> 'None':
    """
    Widens current path by amount it would increase by if drawn with currently selected pen

Args:

      hdc(int):Handle to a device context that contains a closed path. See win32gui::EndPath.

Returns:

      None
        
    """
    pass
        

def StrokePath(hdc:'int') -> 'None':
    """
    Draws current path with currently selected pen

Args:

      hdc(int):Handle to a device context that contains a closed path. See win32gui::EndPath.

Returns:

      None
        
    """
    pass
        

def StrokeAndFillPath(hdc:'int') -> 'None':
    """
    Combines operations of StrokePath and FillPath with no overlap

Args:

      hdc(int):Handle to a device context that contains a closed path. See win32gui::EndPath.

Returns:

      None
        
    """
    pass
        

def GetMiterLimit(hdc:'int') -> 'float':
    """
    Retrieves the limit of miter joins for a DC

Args:

      hdc(int):Handle to a device context

Returns:

      float
        
    """
    pass
        

def SetMiterLimit(hdc:'int',NewLimit:'float') -> 'float':
    """
    Set the limit of miter joins for a DC

Args:

      hdc(int):Handle to a device context
      NewLimit(float):New limit to be setReturn ValueReturns the previous limit

Returns:

      float:New limit to be setReturn ValueReturns the previous limit

        
    """
    pass
        

def PathToRegion(hdc:'int') -> 'PyGdiHANDLE':
    """
    Converts a closed path in a DC to a region

Args:

      hdc(int):Handle to a device context that contains a closed path. See win32gui::EndPath.CommentsOn success, the path is deselected from the DC

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def GetPath(hdc:'int') -> 'Tuple[tuple, tuple]':
    """
    Returns a sequence of points that describe the current path

Args:

      hdc(int):Handle to a device context containing a finalized path.  See win32gui::EndPathReturn ValueReturns a sequence of POINT tuples, and a sequence of ints designating each point's function (combination of win32con.PT_* values)

Returns:

      Tuple[tuple, tuple]:Handle to a device context containing a finalized path.  See win32gui::EndPathReturn ValueReturns a sequence of POINT tuples, and a sequence of ints designating each point's function (combination of win32con.PT_* values)

        
    """
    pass
        

def CreateRoundRectRgn(LeftRect:'int',TopRect:'int',RightRect:'int',BottomRect:'int',WidthEllipse:'int',HeightEllipse:'int') -> 'Any':
    """
    Create a rectangular region with elliptically rounded corners,

Args:

      LeftRect(int):Position of left edge of rectangle
      TopRect(int):Position of top edge of rectangle
      RightRect(int):Position of right edge of rectangle
      BottomRect(int):Position of bottom edge of rectangle
      WidthEllipse(int):Width of ellipse
      HeightEllipse(int):Height of ellipse

Returns:

      Any
        
    """
    pass
        

def CreateRectRgnIndirect(rc:'PyRECT') -> 'Any':
    """
    Creates a rectangular region,

Args:

      rc(PyRECT):Coordinates of rectangle

Returns:

      Any
        
    """
    pass
        

def CreateEllipticRgnIndirect(rc:'PyRECT') -> 'Any':
    """
    Creates an ellipse region,

Args:

      rc(PyRECT):Coordinates of bounding rectangle in logical units

Returns:

      Any
        
    """
    pass
        

def CreateWindowEx(dwExStyle:'int',className:'Union[str, int]',windowTitle:'str',style:'int',x:'int',y:'int',width:'int',height:'int',parent:'int',menu:'int',hinstance:'int',reserved:'None') -> 'int':
    """
    Creates a new window with Extended Style.

Args:

      dwExStyle(int):extended window style
      className(Union[str, int]):
      windowTitle(str):
      style(int):The style for the window.
      x(int):
      y(int):
      width(int):
      height(int):
      parent(int):Handle to the parent window.
      menu(int):Handle to the menu to use for this window.
      hinstance(int):
      reserved(None):Must be None

Returns:

      int
        
    """
    pass
        

def GetParent(child:'int') -> 'int':
    """
    Retrieves a handle to the specified child window's parent window.

Args:

      child(int):handle to child window

Returns:

      int
        
    """
    pass
        

def SetParent(child:'int',child1:'int') -> 'int':
    """
    changes the parent window of the specified child window.

Args:

      child(int):handle to window whose parent is changing
      child1(int):handle to new parent window

Returns:

      int
        
    """
    pass
        

def GetCursorPos() -> 'Tuple[int, int]':
    """
    retrieves the cursor's position, in screen coordinates.

Args:



Returns:

      Tuple[int, int]
        
    """
    pass
        

def GetDesktopWindow() -> 'int':
    """
    returns the desktop window

Args:



Returns:

      int
        
    """
    pass
        

def GetWindow(hWnd:'int',uCmd:'int') -> 'int':
    """
    returns a window that has the specified relationship (Z order or owner) to the specified window.

Args:

      hWnd(int):handle to original window
      uCmd(int):relationship flag

Returns:

      int
        
    """
    pass
        

def GetWindowDC(hWnd:'int') -> 'int':
    """
    returns the device context (DC) for the entire window, including title bar, menus, and scroll bars.

Args:

      hWnd(int):handle of window

Returns:

      int
        
    """
    pass
        

def IsIconic(hWnd:'int') -> 'None':
    """
    determines whether the specified window is minimized (iconic).

Args:

      hWnd(int):handle to window

Returns:

      None
        
    """
    pass
        

def IsWindow(hWnd:'int') -> 'None':
    """
    determines whether the specified window handle identifies an existing window.

Args:

      hWnd(int):handle to window

Returns:

      None
        
    """
    pass
        

def IsChild(hWndParent:'int',hWnd:'int') -> 'None':
    """
    Tests whether a window is a child window or descendant window of a specified parent window

Args:

      hWndParent(int):handle to parent window
      hWnd(int):handle to window to test

Returns:

      None
        
    """
    pass
        

def ReleaseCapture() -> 'None':
    """
    Releases the moust capture for a window.

Args:



Returns:

      None
        
    """
    pass
        

def GetCapture() -> 'int':
    """
    Returns the window with the mouse capture.

Args:



Returns:

      int
        
    """
    pass
        

def SetCapture() -> 'None':
    """
    Captures the mouse for the specified window.

Args:



Returns:

      None
        
    """
    pass
        

def _TrackMouseEvent(tme:'TRACKMOUSEEVENT') -> 'None':
    """
    Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.

Args:

      tme(TRACKMOUSEEVENT):

Returns:

      None
        
    """
    pass
        

def ReleaseDC(hWnd:'int',hDC:'int') -> 'int':
    """
    Releases a device context.

Args:

      hWnd(int):handle to window
      hDC(int):handle to device context

Returns:

      int
        
    """
    pass
        

def CreateCaret(hWnd:'int',hBitmap:'PyGdiHANDLE',nWidth:'int',nHeight:'int') -> 'None':
    """
    Creates a new caret for a window

Args:

      hWnd(int):handle to owner window
      hBitmap(PyGdiHANDLE):handle to bitmap for caret shape
      nWidth(int):caret width
      nHeight(int):caret height

Returns:

      None
        
    """
    pass
        

def DestroyCaret() -> 'None':
    """
    Destroys caret for current task

Args:



Returns:

      None
        
    """
    pass
        

def ScrollWindowEx(hWnd:'int',dx:'int',dy:'int',rcScroll:'PyRECT',rcClip:'PyRECT',hrgnUpdate:'Any',flags:'int') -> 'Tuple[int, PyRECT]':
    """
    scrolls the content of the specified window's client area.

Args:

      hWnd(int):handle to window to scroll
      dx(int):Amount of horizontal scrolling, in device units
      dy(int):Amount of vertical scrolling, in device units
      rcScroll(PyRECT):Scroll rectangle, can be None for entire client area
      rcClip(PyRECT):Clipping rectangle, can be None
      hrgnUpdate(Any):Handle to region which will be updated with area invalidated by scroll operation, can be None
      flags(int):Scrolling flags, combination of SW_ERASE,SW_INVALIDATE,SW_SCROLLCHILDREN,SW_SMOOTHSCROLL. If SW_SMOOTHSCROLL is specified, use upper 16 bits to specify time in milliseconds.Return ValueReturns the type of region invalidated by scrolling, and a rectangle defining the affected area.

Returns:

      Tuple[int, PyRECT]:Scrolling flags, combination of SW_ERASE,SW_INVALIDATE,SW_SCROLLCHILDREN,SW_SMOOTHSCROLL. 

If SW_SMOOTHSCROLL is specified, use upper 16 bits to specify time in milliseconds.Return ValueReturns the type of region invalidated by scrolling, and a rectangle defining the affected area.

        
    """
    pass
        

def SetScrollInfo(hwnd:'int',nBar:'int',scollInfo:'PySCROLLINFO',bRedraw:'int'=1) -> 'None':
    """
    Sets information about a scroll-bar

Args:

      hwnd(int):The handle to the window.
      nBar(int):Identifies the bar.
      scollInfo(PySCROLLINFO):Scollbar info.
      bRedraw(int):Should the bar be redrawn?Return ValueReturns an int with the current position of the scroll box.

Returns:

      None:Should the bar be redrawn?
Return ValueReturns an int with the current position of the scroll box.

        
    """
    pass
        

def GetScrollInfo(hwnd:'int',nBar:'int',mask:'int') -> 'PySCROLLINFO':
    """
    Returns information about a scroll bar

Args:

      hwnd(int):The handle to the window.
      nBar(int):The scroll bar to examine.  Can be one of win32con.SB_CTL, win32con.SB_VERT or win32con.SB_HORZ
      mask(int):The mask for attributes to retrieve.

Returns:

      PySCROLLINFO
        
    """
    pass
        

def GetClassName(hwnd:'int') -> 'str':
    """
    Retrieves the name of the class to which the specified window belongs.

Args:

      hwnd(int):The handle to the window

Returns:

      str
        
    """
    pass
        

def WindowFromPoint(point:'Tuple[int, int]') -> 'int':
    """
    Retrieves a handle to the window that contains the specified point.

Args:

      point(Tuple[int, int]):The point.

Returns:

      int
        
    """
    pass
        

def ChildWindowFromPoint(hwndParent:'int',point:'Tuple[int, int]') -> 'int':
    """
    Determines which, if any, of the child windows belonging to a parent window contains the specified point.

Args:

      hwndParent(int):The parent.
      point(Tuple[int, int]):The point.

Returns:

      int
        
    """
    pass
        

def ChildWindowFromPoint(hwndParent:'int',point:'Tuple[int, int]') -> 'int':
    """
    Determines which, if any, of the child windows belonging to a parent window contains the specified point.

Args:

      hwndParent(int):The parent.
      point(Tuple[int, int]):The point.

Returns:

      int
        
    """
    pass
        

def ListView_SortItems(hwnd:'int',callback:'Any',param:'Any'=None) -> 'None':
    """
    Uses an application-defined comparison function to sort the items of a list view control.

Args:

      hwnd(int):The handle to the window
      callback(Any):A callback object, taking 3 params.
      param(Any):The third param to the callback function.

Returns:

      None
        
    """
    pass
        

def ListView_SortItemsEx(hwnd:'int',callback:'Any',param:'Any'=None) -> 'None':
    """
    Uses an application-defined comparison function to sort the items of a list view control.

Args:

      hwnd(int):The handle to the window
      callback(Any):A callback object, taking 3 params.
      param(Any):The third param to the callback function.

Returns:

      None
        
    """
    pass
        

def CreateDC(Driver:'str',Device:'str',InitData:'PyDEVMODE') -> 'int':
    """
    Creates a device context for a printer or display device

Args:

      Driver(str):Name of display or print provider, usually DISPLAY or WINSPOOL
      Device(str):Name of specific device, eg printer name returned from GetDefaultPrinter
      InitData(PyDEVMODE):A PyDEVMODE that specifies printing parameters, use None for printer defaults

Returns:

      int
        
    """
    pass
        

def GetSaveFileNameW(hwndOwner:'int'=None,hInstance:'int'=None,Filter:'Any'=None,CustomFilter:'Any'=None,FilterIndex:'int'=0,File:'Any'=None,MaxFile:'int'=1024,InitialDir:'Any'=None,Title:'Any'=None,Flags:'int'=0,DefExt:'Any'=None,TemplateName:'PyResourceId'=None) -> 'Tuple[Any, Any, int]':
    """
    Creates a dialog for user to specify location to save a file or files

Args:

      hwndOwner(int):Handle to window that owns dialog
      hInstance(int):Handle to module that contains dialog template
      Filter(Any):Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'
      CustomFilter(Any):Description to be used for filter that user selected or typed, can also contain a filespec as above
      FilterIndex(int):Specifies which of the filters is initially selected, use 0 for CustomFilter
      File(Any):The file name initially displayed
      MaxFile(int):Number of characters to allocate for selected filename(s), override if large number of files expected
      InitialDir(Any):The starting directory
      Title(Any):The title of the dialog box
      Flags(int):Combination of win32con.OFN_* constants
      DefExt(Any):The default extension to use
      TemplateName(PyResourceId):Name or resource id of dialog box templateCommentsAccepts keyword arguments, all arguments optionalReturn ValueReturns a tuple of 3 values (PyUNICODE, PyUNICODE, int): First is the selected file(s). If multiple files are selected, returned string will be the directory followed by files names separated by nulls, otherwise it will be the full path.  In other words, if you use the OFN_ALLOWMULTISELECT flag you should split this value on \\0 characters and if the length of the result list is 1, it will be the full path, otherwise element 0 will be the directory and the rest of the elements will be filenames in this directory. Second is a unicode string containing user-selected filter, will be None if CustomFilter was not specified Third item contains flags pertaining to users input, such as OFN_READONLY and OFN_EXTENSIONDIFFERENT If the user presses cancel or an error occurs, a win32gui.error is raised.  If the user pressed cancel, the error number (ie, the winerror attribute of the exception) will be zero.

Returns:

      Tuple[Any, Any, int]:Name or resource id of dialog box template
Comments

Accepts keyword arguments, all arguments optional
Return ValueReturns a tuple of 3 values (PyUNICODE, PyUNICODE, int): 

First is the selected file(s). If multiple files are selected, returned string will be the directory followed by files names 

separated by nulls, otherwise it will be the full path.  In other words, if you use the OFN_ALLOWMULTISELECT flag 

you should split this value on \\0 characters and if the length of the result list is 1, it will be 

the full path, otherwise element 0 will be the directory and the rest of the elements will be filenames in 

this directory. 

Second is a unicode string containing user-selected filter, will be None if CustomFilter was not specified 

Third item contains flags pertaining to users input, such as OFN_READONLY and OFN_EXTENSIONDIFFERENT 

If the user presses cancel or an error occurs, a 

win32gui.error is raised.  If the user pressed cancel, the error number (ie, the winerror attribute of the exception) will be zero.

        
    """
    pass
        

def GetOpenFileNameW(hwndOwner:'int'=None,hInstance:'int'=None,Filter:'Any'=None,CustomFilter:'Any'=None,FilterIndex:'int'=0,File:'Any'=None,MaxFile:'int'=1024,InitialDir:'Any'=None,Title:'Any'=None,Flags:'int'=0,DefExt:'Any'=None,TemplateName:'PyResourceId'=None) -> 'Tuple[Any, Any, int]':
    """
    Creates a dialog to allow user to select file(s) to open

Args:

      hwndOwner(int):Handle to window that owns dialog
      hInstance(int):Handle to module that contains dialog template
      Filter(Any):Contains pairs of descriptions and filespecs separated by NULLS, with a final trailing NULL. Example: 'Python Scripts\\0*.py;*.pyw;*.pys\\0Text files\\0*.txt\\0'
      CustomFilter(Any):Description to be used for filter that user selected or typed, can also contain a filespec as above
      FilterIndex(int):Specifies which of the filters is initially selected, use 0 for CustomFilter
      File(Any):The file name initially displayed
      MaxFile(int):Number of characters to allocate for selected filename, override if large number of files expected
      InitialDir(Any):The starting directory
      Title(Any):The title of the dialog box
      Flags(int):Combination of win32con.OFN_* constants
      DefExt(Any):The default extension to use
      TemplateName(PyResourceId):Name or resource id of dialog box templateCommentsAccepts keyword arguments, all arguments optional Input parameters and return values are identical to win32gui::GetSaveFileNameW

Returns:

      Tuple[Any, Any, int]
        
    """
    pass
        

def SystemParametersInfo(Action:'int',Param:'Any'=None,WinIni:'int'=0) -> 'None':
    """
    Queries or sets system-wide parameters. This function can also update the user profile while setting a parameter.

Args:

      Action(int):System parameter to query or set, one of the SPI_GET* or SPI_SET* constants
      Param(Any):depends on action to be taken
      WinIni(int):Flags specifying whether change should be permanent, and if all windows should be notified of change. Combination of SPIF_UPDATEINIFILE, SPIF_SENDCHANGE, SPIF_SENDWININICHANGEActionInput/return typeSPI_GETDESKWALLPAPERReturns the path to the bmp used as wallpaperSPI_SETDESKWALLPAPERParam should be a string specifying a .bmp fileSPI_GETDROPSHADOWReturns a booleanSPI_GETFLATMENUReturns a booleanSPI_GETFONTSMOOTHINGReturns a booleanSPI_GETICONTITLEWRAPReturns a booleanSPI_GETSNAPTODEFBUTTONReturns a booleanSPI_GETBEEPReturns a booleanSPI_GETBLOCKSENDINPUTRESETSReturns a booleanSPI_GETMENUUNDERLINESReturns a booleanSPI_GETKEYBOARDCUESReturns a booleanSPI_GETKEYBOARDPREFReturns a booleanSPI_GETSCREENSAVEACTIVEReturns a booleanSPI_GETSCREENSAVERRUNNINGReturns a booleanSPI_GETMENUDROPALIGNMENTReturns a boolean (True indicates left aligned, False right aligned)SPI_GETMENUFADEReturns a booleanSPI_GETLOWPOWERACTIVEReturns a booleanSPI_GETPOWEROFFACTIVEReturns a booleanSPI_GETCOMBOBOXANIMATIONReturns a booleanSPI_GETCURSORSHADOWReturns a booleanSPI_GETGRADIENTCAPTIONSReturns a booleanSPI_GETHOTTRACKINGReturns a booleanSPI_GETLISTBOXSMOOTHSCROLLINGReturns a booleanSPI_GETMENUANIMATIONReturns a booleanSPI_GETSELECTIONFADEReturns a booleanSPI_GETTOOLTIPANIMATIONReturns a booleanSPI_GETTOOLTIPFADEReturns a boolean (TRUE=fade, False=slide)SPI_GETUIEFFECTSReturns a booleanSPI_GETACTIVEWINDOWTRACKINGReturns a booleanSPI_GETACTIVEWNDTRKZORDERReturns a booleanSPI_GETDRAGFULLWINDOWSReturns a booleanSPI_GETSHOWIMEUIReturns a booleanSPI_GETMOUSECLICKLOCKReturns a booleanSPI_GETMOUSESONARReturns a booleanSPI_GETMOUSEVANISHReturns a booleanSPI_GETSCREENREADERReturns a booleanSPI_GETSHOWSOUNDSReturns a booleanSPI_SETDROPSHADOWParam must be a booleanSPI_SETDROPSHADOWParam must be a booleanSPI_SETMENUUNDERLINESParam must be a booleanSPI_SETKEYBOARDCUESParam must be a booleanSPI_SETMENUFADEParam must be a booleanSPI_SETCOMBOBOXANIMATIONParam must be a booleanSPI_SETCURSORSHADOWParam must be a booleanSPI_SETGRADIENTCAPTIONSParam must be a booleanSPI_SETHOTTRACKINGParam must be a booleanSPI_SETLISTBOXSMOOTHSCROLLINGParam must be a booleanSPI_SETMENUANIMATIONParam must be a booleanSPI_SETSELECTIONFADEParam must be a booleanSPI_SETTOOLTIPANIMATIONParam must be a booleanSPI_SETTOOLTIPFADEParam must be a booleanSPI_SETUIEFFECTSParam must be a booleanSPI_SETACTIVEWINDOWTRACKINGParam must be a booleanSPI_SETACTIVEWNDTRKZORDERParam must be a booleanSPI_SETMOUSESONARParam must be a booleanSPI_SETMOUSEVANISHParam must be a booleanSPI_SETMOUSECLICKLOCKParam must be a booleanSPI_SETFONTSMOOTHINGParam should specify a booleanSPI_SETICONTITLEWRAPParam should specify a booleanSPI_SETSNAPTODEFBUTTONParam is a booleanSPI_SETBEEPParam is a booleanSPI_SETBLOCKSENDINPUTRESETSParam is a booleanSPI_SETKEYBOARDPREFParam is a booleanSPI_SETMOUSEBUTTONSWAPParam is a booleanSPI_SETSCREENSAVEACTIVEParam is a booleanSPI_SETMENUDROPALIGNMENTParam is a boolean (True=left aligned, False=right aligned)SPI_SETLOWPOWERACTIVEParam is a booleanSPI_SETPOWEROFFACTIVEParam is a booleanSPI_SETDRAGFULLWINDOWSParam is a booleanSPI_SETSHOWIMEUIParam is a booleanSPI_SETSCREENREADERParam is a booleanSPI_SETSHOWSOUNDSParam is a booleanSPI_SETMOUSETRAILSParam should be an int specifying the nbr of cursors in the trail (0 or 1 means disabled)SPI_SETWHEELSCROLLLINESParam is an int specifying nbr of linesSPI_SETKEYBOARDDELAYParam is an int in the range 0 - 3SPI_SETKEYBOARDSPEEDParam is an int in the range 0 - 31SPI_SETDOUBLECLICKTIMEParam is an int (in milliseconds),  Use win32gui::GetDoubleClickTime to retrieve the value.SPI_SETDOUBLECLKWIDTHParam is an int.  Use win32api.GetSystemMetrics(SM_CXDOUBLECLK) to retrieve the value.SPI_SETDOUBLECLKHEIGHTParam is an int,  Use win32api.GetSystemMetrics(SM_CYDOUBLECLK) to retrieve the value.SPI_SETMOUSEHOVERHEIGHTParam is an intSPI_SETMOUSEHOVERWIDTHParam is an intSPI_SETMOUSEHOVERTIMEParam is an intSPI_SETSCREENSAVETIMEOUTParam is an int specifying the timeout in secondsSPI_SETMENUSHOWDELAYParam is an int specifying the shortcut menu delay in millisecondsSPI_SETLOWPOWERTIMEOUTParam is an int (in seconds)SPI_SETPOWEROFFTIMEOUTParam is an int (in seconds)SPI_SETDRAGHEIGHTParam is an int. Use win32api.GetSystemMetrics(SM_CYDRAG) to retrieve the value.SPI_SETDRAGWIDTHParam is an int. Use win32api.GetSystemMetrics(SM_CXDRAG) to retrieve the value.SPI_SETBORDERParam is an intSPI_GETFONTSMOOTHINGCONTRASTReturns an intSPI_GETFONTSMOOTHINGTYPEReturns an intSPI_GETMOUSETRAILSReturns an int specifying the nbr of cursor images in the trail, 0 or 1 indicates disabledSPI_GETWHEELSCROLLLINESReturns the nbr of lines to scroll for the mouse wheelSPI_GETKEYBOARDDELAYReturns an intSPI_GETKEYBOARDSPEEDReturns an intSPI_GETMOUSESPEEDReturns an intSPI_GETMOUSEHOVERHEIGHTReturns an intSPI_GETMOUSEHOVERWIDTHReturns an intSPI_GETMOUSEHOVERTIMEReturns an intSPI_GETSCREENSAVETIMEOUTReturns an int (idle time in seconds)SPI_GETMENUSHOWDELAYReturns an int (shortcut delay in milliseconds)SPI_GETLOWPOWERTIMEOUTReturns an int (in seconds)SPI_GETPOWEROFFTIMEOUTReturns an int (in seconds)SPI_GETACTIVEWNDTRKTIMEOUTReturns an int (milliseconds)SPI_GETBORDERReturns an intSPI_GETCARETWIDTHReturns an intSPI_GETFOREGROUNDFLASHCOUNTReturns an intSPI_GETFOREGROUNDLOCKTIMEOUTReturns an intSPI_GETFOCUSBORDERHEIGHTReturns an intSPI_GETFOCUSBORDERWIDTHReturns an intSPI_GETMOUSECLICKLOCKTIMEReturns an int (in milliseconds)SPI_SETFONTSMOOTHINGCONTRASTParam should be an int in the range 1000 to 2200SPI_SETFONTSMOOTHINGTYPEParam should be one of the FE_FONTSMOOTHING* constantsSPI_SETMOUSESPEEDParam should be an int in the range 1 - 20SPI_SETACTIVEWNDTRKTIMEOUTParam is an int (in milliseconds)SPI_SETCARETWIDTHParam is an int (in pixels)SPI_SETFOREGROUNDFLASHCOUNTParam is an intSPI_SETFOREGROUNDLOCKTIMEOUTParam is an int (in milliseconds)SPI_SETFOCUSBORDERHEIGHTReturns an intSPI_SETFOCUSBORDERWIDTHReturns an intSPI_SETMOUSECLICKLOCKTIMEParam is an int (in milliseconds)SPI_GETICONTITLELOGFONTReturns a PyLOGFONT,SPI_SETICONTITLELOGFONTParam must be a PyLOGFONT,SPI_SETLANGTOGGLEParam is ignored. Sets the language toggle hotkey from registry key HKCU\\keyboard layout\\toggleSPI_SETICONSReloads the system icons.  Param is not usedSPI_GETMOUSEReturns a tuple of 3 ints containing the x and y mouse thresholds and the acceleration factor.SPI_SETMOUSEParam should be a sequence of 3 intsSPI_GETDEFAULTINPUTLANGReturns an int (locale id for default language)SPI_SETDEFAULTINPUTLANGParam is an int containing a locale idSPI_GETANIMATIONReturns an intSPI_SETANIMATIONParam is an intSPI_ICONHORIZONTALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new valueSPI_ICONVERTICALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new valueSPI_GETNONCLIENTMETRICSParam must be None.  The result is a dict.SPI_SETNONCLIENTMETRICSParam is a dict in the form of a NONCLIENTMETRICS struct, as returned by SPI_GETNONCLIENTMETRICS operationSPI_GETMINIMIZEDMETRICSReturns a dict representing a MINIMIZEDMETRICS struct.  Param is not used.SPI_SETMINIMIZEDMETRICSParam should be a MINIMIZEDMETRICS dict as returned by SPI_GETMINIMIZEDMETRICS actionSPI_SETDESKPATTERNUnsupported (obsolete)SPI_GETFASTTASKSWITCHUnsupported (obsolete)SPI_SETFASTTASKSWITCHUnsupported (obsolete)SPI_SETSCREENSAVERRUNNINGUnsupported (documented as internal use only)SPI_SCREENSAVERRUNNINGSame as SPI_SETSCREENSAVERRUNNINGSPI_SETPENWINDOWSUnsupported (only relevant for win95)SPI_GETWINDOWSEXTENSIONUnsupported (only relevant for win95)SPI_GETGRIDGRANULARITYUnsupported (obsolete)SPI_SETGRIDGRANULARITYUnsupported (obsolete)SPI_LANGDRIVERUnsupported (use is not documented)SPI_GETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)SPI_SETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)SPI_SETHANDHELDUnsupported (use is not documented)SPI_GETICONMETRICSNot implemented yetSPI_SETICONMETRICSNot implemented yetSPI_GETWORKAREANot implemented yetSPI_SETWORKAREANot implemented yetSPI_GETSERIALKEYSNot implemented yetSPI_SETSERIALKEYSNot implemented yetSPI_SETMOUSEKEYSNot implemented yetSPI_GETMOUSEKEYSNot implemented yetSPI_GETHIGHCONTRASTNot implemented yetSPI_SETHIGHCONTRASTNot implemented yetSPI_GETSOUNDSENTRYNot implemented yetSPI_SETSOUNDSENTRYNot implemented yetSPI_GETSTICKYKEYSNot implemented yetSPI_SETSTICKYKEYSNot implemented yetSPI_GETTOGGLEKEYSNot implemented yetSPI_SETTOGGLEKEYSNot implemented yetSPI_GETACCESSTIMEOUTNot implemented yetSPI_SETACCESSTIMEOUTNot implemented yetSPI_GETFILTERKEYSNot implemented yetSPI_SETFILTERKEYSNot implemented yetCommentsParam and WinIni are not used with any of the SPI_GET operations Boolean parameters can be any object that can be evaluated as True or FalseReturn ValueSPI_SET functions all return None on success.  Types returned by SPI_GET functions are dependent on the operation

Returns:

      None:Flags specifying whether change should be permanent, and if all windows should be notified of change. Combination of SPIF_UPDATEINIFILE, SPIF_SENDCHANGE, SPIF_SENDWININICHANGE



Action


Input/return type



SPI_GETDESKWALLPAPERReturns the path to the bmp used as wallpaper
SPI_SETDESKWALLPAPERParam should be a string specifying a .bmp file
SPI_GETDROPSHADOWReturns a boolean
SPI_GETFLATMENUReturns a boolean
SPI_GETFONTSMOOTHINGReturns a boolean
SPI_GETICONTITLEWRAPReturns a boolean
SPI_GETSNAPTODEFBUTTONReturns a boolean
SPI_GETBEEPReturns a boolean
SPI_GETBLOCKSENDINPUTRESETSReturns a boolean
SPI_GETMENUUNDERLINESReturns a boolean
SPI_GETKEYBOARDCUESReturns a boolean
SPI_GETKEYBOARDPREFReturns a boolean
SPI_GETSCREENSAVEACTIVEReturns a boolean
SPI_GETSCREENSAVERRUNNINGReturns a boolean
SPI_GETMENUDROPALIGNMENTReturns a boolean (True indicates left aligned, False right aligned)
SPI_GETMENUFADEReturns a boolean
SPI_GETLOWPOWERACTIVEReturns a boolean
SPI_GETPOWEROFFACTIVEReturns a boolean
SPI_GETCOMBOBOXANIMATIONReturns a boolean
SPI_GETCURSORSHADOWReturns a boolean
SPI_GETGRADIENTCAPTIONSReturns a boolean
SPI_GETHOTTRACKINGReturns a boolean
SPI_GETLISTBOXSMOOTHSCROLLINGReturns a boolean
SPI_GETMENUANIMATIONReturns a boolean
SPI_GETSELECTIONFADEReturns a boolean
SPI_GETTOOLTIPANIMATIONReturns a boolean
SPI_GETTOOLTIPFADEReturns a boolean (TRUE=fade, False=slide)
SPI_GETUIEFFECTSReturns a boolean
SPI_GETACTIVEWINDOWTRACKINGReturns a boolean
SPI_GETACTIVEWNDTRKZORDERReturns a boolean
SPI_GETDRAGFULLWINDOWSReturns a boolean
SPI_GETSHOWIMEUIReturns a boolean
SPI_GETMOUSECLICKLOCKReturns a boolean
SPI_GETMOUSESONARReturns a boolean
SPI_GETMOUSEVANISHReturns a boolean
SPI_GETSCREENREADERReturns a boolean
SPI_GETSHOWSOUNDSReturns a boolean
SPI_SETDROPSHADOWParam must be a boolean
SPI_SETDROPSHADOWParam must be a boolean
SPI_SETMENUUNDERLINESParam must be a boolean
SPI_SETKEYBOARDCUESParam must be a boolean
SPI_SETMENUFADEParam must be a boolean
SPI_SETCOMBOBOXANIMATIONParam must be a boolean
SPI_SETCURSORSHADOWParam must be a boolean
SPI_SETGRADIENTCAPTIONSParam must be a boolean
SPI_SETHOTTRACKINGParam must be a boolean
SPI_SETLISTBOXSMOOTHSCROLLINGParam must be a boolean
SPI_SETMENUANIMATIONParam must be a boolean
SPI_SETSELECTIONFADEParam must be a boolean
SPI_SETTOOLTIPANIMATIONParam must be a boolean
SPI_SETTOOLTIPFADEParam must be a boolean
SPI_SETUIEFFECTSParam must be a boolean
SPI_SETACTIVEWINDOWTRACKINGParam must be a boolean
SPI_SETACTIVEWNDTRKZORDERParam must be a boolean
SPI_SETMOUSESONARParam must be a boolean
SPI_SETMOUSEVANISHParam must be a boolean
SPI_SETMOUSECLICKLOCKParam must be a boolean
SPI_SETFONTSMOOTHINGParam should specify a boolean
SPI_SETICONTITLEWRAPParam should specify a boolean
SPI_SETSNAPTODEFBUTTONParam is a boolean
SPI_SETBEEPParam is a boolean
SPI_SETBLOCKSENDINPUTRESETSParam is a boolean
SPI_SETKEYBOARDPREFParam is a boolean
SPI_SETMOUSEBUTTONSWAPParam is a boolean
SPI_SETSCREENSAVEACTIVEParam is a boolean
SPI_SETMENUDROPALIGNMENTParam is a boolean (True=left aligned, False=right aligned)
SPI_SETLOWPOWERACTIVEParam is a boolean
SPI_SETPOWEROFFACTIVEParam is a boolean
SPI_SETDRAGFULLWINDOWSParam is a boolean
SPI_SETSHOWIMEUIParam is a boolean
SPI_SETSCREENREADERParam is a boolean
SPI_SETSHOWSOUNDSParam is a boolean
SPI_SETMOUSETRAILSParam should be an int specifying the nbr of cursors in the trail (0 or 1 means disabled)
SPI_SETWHEELSCROLLLINESParam is an int specifying nbr of lines
SPI_SETKEYBOARDDELAYParam is an int in the range 0 - 3
SPI_SETKEYBOARDSPEEDParam is an int in the range 0 - 31
SPI_SETDOUBLECLICKTIMEParam is an int (in milliseconds),  Use win32gui::GetDoubleClickTime to retrieve the value.
SPI_SETDOUBLECLKWIDTHParam is an int.  Use win32api.GetSystemMetrics(SM_CXDOUBLECLK) to retrieve the value.
SPI_SETDOUBLECLKHEIGHTParam is an int,  Use win32api.GetSystemMetrics(SM_CYDOUBLECLK) to retrieve the value.
SPI_SETMOUSEHOVERHEIGHTParam is an int
SPI_SETMOUSEHOVERWIDTHParam is an int
SPI_SETMOUSEHOVERTIMEParam is an int
SPI_SETSCREENSAVETIMEOUTParam is an int specifying the timeout in seconds
SPI_SETMENUSHOWDELAYParam is an int specifying the shortcut menu delay in milliseconds
SPI_SETLOWPOWERTIMEOUTParam is an int (in seconds)
SPI_SETPOWEROFFTIMEOUTParam is an int (in seconds)
SPI_SETDRAGHEIGHTParam is an int. Use win32api.GetSystemMetrics(SM_CYDRAG) to retrieve the value.
SPI_SETDRAGWIDTHParam is an int. Use win32api.GetSystemMetrics(SM_CXDRAG) to retrieve the value.
SPI_SETBORDERParam is an int
SPI_GETFONTSMOOTHINGCONTRASTReturns an int
SPI_GETFONTSMOOTHINGTYPEReturns an int
SPI_GETMOUSETRAILSReturns an int specifying the nbr of cursor images in the trail, 0 or 1 indicates disabled
SPI_GETWHEELSCROLLLINESReturns the nbr of lines to scroll for the mouse wheel
SPI_GETKEYBOARDDELAYReturns an int
SPI_GETKEYBOARDSPEEDReturns an int
SPI_GETMOUSESPEEDReturns an int
SPI_GETMOUSEHOVERHEIGHTReturns an int
SPI_GETMOUSEHOVERWIDTHReturns an int
SPI_GETMOUSEHOVERTIMEReturns an int
SPI_GETSCREENSAVETIMEOUTReturns an int (idle time in seconds)
SPI_GETMENUSHOWDELAYReturns an int (shortcut delay in milliseconds)
SPI_GETLOWPOWERTIMEOUTReturns an int (in seconds)
SPI_GETPOWEROFFTIMEOUTReturns an int (in seconds)
SPI_GETACTIVEWNDTRKTIMEOUTReturns an int (milliseconds)
SPI_GETBORDERReturns an int
SPI_GETCARETWIDTHReturns an int
SPI_GETFOREGROUNDFLASHCOUNTReturns an int
SPI_GETFOREGROUNDLOCKTIMEOUTReturns an int
SPI_GETFOCUSBORDERHEIGHTReturns an int
SPI_GETFOCUSBORDERWIDTHReturns an int
SPI_GETMOUSECLICKLOCKTIMEReturns an int (in milliseconds)
SPI_SETFONTSMOOTHINGCONTRASTParam should be an int in the range 1000 to 2200
SPI_SETFONTSMOOTHINGTYPEParam should be one of the FE_FONTSMOOTHING* constants
SPI_SETMOUSESPEEDParam should be an int in the range 1 - 20
SPI_SETACTIVEWNDTRKTIMEOUTParam is an int (in milliseconds)
SPI_SETCARETWIDTHParam is an int (in pixels)
SPI_SETFOREGROUNDFLASHCOUNTParam is an int
SPI_SETFOREGROUNDLOCKTIMEOUTParam is an int (in milliseconds)
SPI_SETFOCUSBORDERHEIGHTReturns an int
SPI_SETFOCUSBORDERWIDTHReturns an int
SPI_SETMOUSECLICKLOCKTIMEParam is an int (in milliseconds)
SPI_GETICONTITLELOGFONTReturns a PyLOGFONT,
SPI_SETICONTITLELOGFONTParam must be a PyLOGFONT,
SPI_SETLANGTOGGLEParam is ignored. Sets the language toggle hotkey from registry key HKCU\\keyboard layout\\toggle
SPI_SETICONSReloads the system icons.  Param is not used
SPI_GETMOUSEReturns a tuple of 3 ints containing the x and y mouse thresholds and the acceleration factor.
SPI_SETMOUSEParam should be a sequence of 3 ints
SPI_GETDEFAULTINPUTLANGReturns an int (locale id for default language)
SPI_SETDEFAULTINPUTLANGParam is an int containing a locale id
SPI_GETANIMATIONReturns an int
SPI_SETANIMATIONParam is an int
SPI_ICONHORIZONTALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new value
SPI_ICONVERTICALSPACINGFunctions as both a get and set operation.  If Param is None, functions as a get operation, otherwise Param is an int to be set as the new value
SPI_GETNONCLIENTMETRICSParam must be None.  The result is a dict.
SPI_SETNONCLIENTMETRICSParam is a dict in the form of a NONCLIENTMETRICS struct, as returned by SPI_GETNONCLIENTMETRICS operation
SPI_GETMINIMIZEDMETRICSReturns a dict representing a MINIMIZEDMETRICS struct.  Param is not used.
SPI_SETMINIMIZEDMETRICSParam should be a MINIMIZEDMETRICS dict as returned by SPI_GETMINIMIZEDMETRICS action
SPI_SETDESKPATTERNUnsupported (obsolete)
SPI_GETFASTTASKSWITCHUnsupported (obsolete)
SPI_SETFASTTASKSWITCHUnsupported (obsolete)
SPI_SETSCREENSAVERRUNNINGUnsupported (documented as internal use only)
SPI_SCREENSAVERRUNNINGSame as SPI_SETSCREENSAVERRUNNING
SPI_SETPENWINDOWSUnsupported (only relevant for win95)
SPI_GETWINDOWSEXTENSIONUnsupported (only relevant for win95)
SPI_GETGRIDGRANULARITYUnsupported (obsolete)
SPI_SETGRIDGRANULARITYUnsupported (obsolete)
SPI_LANGDRIVERUnsupported (use is not documented)
SPI_GETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)
SPI_SETFONTSMOOTHINGORIENTATIONUnsupported (use is not documented)
SPI_SETHANDHELDUnsupported (use is not documented)
SPI_GETICONMETRICSNot implemented yet
SPI_SETICONMETRICSNot implemented yet
SPI_GETWORKAREANot implemented yet
SPI_SETWORKAREANot implemented yet
SPI_GETSERIALKEYSNot implemented yet
SPI_SETSERIALKEYSNot implemented yet
SPI_SETMOUSEKEYSNot implemented yet
SPI_GETMOUSEKEYSNot implemented yet
SPI_GETHIGHCONTRASTNot implemented yet
SPI_SETHIGHCONTRASTNot implemented yet
SPI_GETSOUNDSENTRYNot implemented yet
SPI_SETSOUNDSENTRYNot implemented yet
SPI_GETSTICKYKEYSNot implemented yet
SPI_SETSTICKYKEYSNot implemented yet
SPI_GETTOGGLEKEYSNot implemented yet
SPI_SETTOGGLEKEYSNot implemented yet
SPI_GETACCESSTIMEOUTNot implemented yet
SPI_SETACCESSTIMEOUTNot implemented yet
SPI_GETFILTERKEYSNot implemented yet
SPI_SETFILTERKEYSNot implemented yet
Comments

Param and WinIni are not used with any of the SPI_GET operations 

Boolean parameters can be any object that can be evaluated as True or False
Return ValueSPI_SET functions all return None on success.  Types returned by SPI_GET functions are dependent on the operation

        
    """
    pass
        

def SetLayeredWindowAttributes(hwnd:'int',Key:'int',Alpha:'int',Flags:'int') -> 'None':
    """
    Sets the opacity and transparency color key of a layered window.

Args:

      hwnd(int):handle to the layered window
      Key(int):Specifies the color key.  Use win32api::RGB to generate value.
      Alpha(int):Opacity, in the range 0-255
      Flags(int):Combination of win32con.LWA_* valuesCommentsThis function only exists on Win2k and laterAccepts keyword arguments

Returns:

      None
        
    """
    pass
        

def GetLayeredWindowAttributes(hwnd:'int') -> 'Tuple[int, int, int]':
    """
    Retrieves the layering parameters of a window with the WS_EX_LAYERED extended style

Args:

      hwnd(int):Handle to a layered windowCommentsThis function only exists on WinXP and later.Accepts keyword arguments.Return ValueReturns a tuple of (color key, alpha, flags)

Returns:

      Tuple[int, int, int]:Handle to a layered windowComments

This function only exists on WinXP and later.

Accepts keyword arguments.
Return ValueReturns a tuple of (color key, alpha, flags)

        
    """
    pass
        

def UpdateLayeredWindow(hwnd:'int',hdcDst:'int'=None,ptDst:'Tuple[Any, Any]'=None,size:'Tuple[Any, Any]'=None,hdcSrc:'int'=None,ptSrc:'Tuple[Any, Any]'=None,Key:'int'=0,blend:'Tuple[int, int, int, int]'=(0,0,255,0),Flags:'int'=0) -> 'None':
    """
    Updates the position, size, shape, content, and translucency of a layered window.

Args:

      hwnd(int):handle to layered window
      hdcDst(int):handle to screen DC, can be None.  *Must* be None if hdcSrc is None
      ptDst(Tuple[Any, Any]):New screen position, can be None.
      size(Tuple[Any, Any]):New size of the layered window, can be None.  *Must* be None if hdcSrc is None.
      hdcSrc(int):handle to surface DC for the window, can be None
      ptSrc(Tuple[Any, Any]):layer position, can be None.  *Must* be None if hdcSrc is None.
      Key(int):Color key, generate using win32api::RGB
      blend(Tuple[int, int, int, int]):PyBLENDFUNCTION specifying alpha blending parameters
      Flags(int):One of the win32con.ULW_* values.  Use 0 if hdcSrc is None.CommentsThis function is only available on Windows 2000 and laterAccepts keyword arguments.

Returns:

      None
        
    """
    pass
        

def AnimateWindow(hwnd:'int',Time:'int',Flags:'int') -> 'None':
    """
    Enables you to produce special effects when showing or hiding windows. There are three types of animation: roll, slide, and alpha-blended fade.

Args:

      hwnd(int):handle to window
      Time(int):Duration of animation in ms
      Flags(int):Animation type, combination of win32con.AW_* flagsCommentsThis function is available on Win2k and laterAccepts keyword args

Returns:

      None
        
    """
    pass
        

def CreateBrushIndirect(lb:'PyLOGBRUSH') -> 'PyGdiHANDLE':
    """
    Creates a GDI brush from a LOGBRUSH struct

Args:

      lb(PyLOGBRUSH):Dict containing brush creation parameters

Returns:

      PyGdiHANDLE
        
    """
    pass
        

def ExtCreatePen(PenStyle:'int',Width:'int',lb:'PyLOGBRUSH',Style:'Tuple[int, ...]'=None) -> 'int':
    """
    Creates a GDI pen object

Args:

      PenStyle(int):Combination of win32con.PS_*.  Must contain either PS_GEOMETRIC or PS_COSMETIC.
      Width(int):Width of pen in logical units.  Must be 1 for PS_COSMETIC.
      lb(PyLOGBRUSH):Dict containing brush creation parameters
      Style(Tuple[int, ...]):Sequence containing lengths of dashes and spaces  Used only with PS_USERSTYLE, otherwise must be None.

Returns:

      int
        
    """
    pass
        

def DrawTextW(hDC:'int',String:'str',Count:'int',Rect:'PyRECT',Format:'int') -> 'Tuple[int, PyRECT]':
    """
    Draws Unicode text on a device context.

Args:

      hDC(int):Handle to a device context
      String(str):Text to be drawn
      Count(int):Number of characters to draw, use -1 for entire null terminated string
      Rect(PyRECT):Rectangle in which to draw text
      Format(int):Formatting flags, combination of win32con.DT_* valuesCommentsAccepts keyword args.Return ValueReturns the height of the drawn text, and the rectangle coordinates

Returns:

      Tuple[int, PyRECT]:Formatting flags, combination of win32con.DT_* valuesComments

Accepts keyword args.
Return ValueReturns the height of the drawn text, and the rectangle coordinates

        
    """
    pass
        

def EnumPropsEx(hWnd:'int',EnumFunc:'Any',Param:'Any') -> 'None':
    """
    None

Args:

      hWnd(int):Handle to a window
      EnumFunc(Any):Callback function
      Param(Any):Arbitrary object to be passed to callback function

Returns:

      None
        
    """
    pass
        

def RegisterDeviceNotification(handle:'int',filter:'Any',flags:'int') -> 'PyHDEVNOTIFY':
    """
    Registers the device or type of device for which a window will receive notifications.

Args:

      handle(int):The handle to a window or a service
      filter(Any):A buffer laid out like one of the DEV_BROADCAST_* structures, generally built by one of the win32gui_struct helpers.
      flags(int):Win32 API References

Returns:

      PyHDEVNOTIFY
        
    """
    pass
        

def UnregisterDeviceNotification() -> 'None':
    """
    Unregisters a Device Notification handle. 

It is generally not necessary to call this function manually, but in some cases, 

handle values may be extracted via the struct module and need to be closed explicitly.

Args:



Returns:

      None
        
    """
    pass
        

def RegisterHotKey(hWnd:'int',id:'int',Modifiers:'int',vk:'int') -> 'None':
    """
    Registers a hotkey for a window

Args:

      hWnd(int):Handle to window that will receive WM_HOTKEY messages
      id(int):Unique id to be used for the hot key
      Modifiers(int):Control keys, combination of win32con.MOD_*
      vk(int):Virtual key codeWin32 API References

Returns:

      None
        
    """
    pass
        
CLR_NONE = ...
ILC_COLOR = ...
ILC_COLOR16 = ...
ILC_COLOR24 = ...
ILC_COLOR32 = ...
ILC_COLOR4 = ...
ILC_COLOR8 = ...
ILC_COLORDDB = ...
ILC_MASK = ...
ILD_BLEND = ...
ILD_BLEND25 = ...
ILD_BLEND50 = ...
ILD_FOCUS = ...
ILD_MASK = ...
ILD_NORMAL = ...
ILD_SELECTED = ...
ILD_TRANSPARENT = ...
IMAGE_BITMAP = ...
IMAGE_CURSOR = ...
IMAGE_ICON = ...
LR_CREATEDIBSECTION = ...
LR_DEFAULTCOLOR = ...
LR_DEFAULTSIZE = ...
LR_LOADFROMFILE = ...
LR_LOADMAP3DCOLORS = ...
LR_LOADTRANSPARENT = ...
LR_MONOCHROME = ...
LR_SHARED = ...
LR_VGACOLOR = ...
NIF_ICON = ...
NIF_INFO = ...
NIF_MESSAGE = ...
NIF_STATE = ...
NIF_TIP = ...
NIIF_ERROR = ...
NIIF_ICON_MASK = ...
NIIF_INFO = ...
NIIF_NONE = ...
NIIF_NOSOUND = ...
NIIF_WARNING = ...
NIM_ADD = ...
NIM_DELETE = ...
NIM_MODIFY = ...
NIM_SETFOCUS = ...
NIM_SETVERSION = ...
TPM_BOTTOMALIGN = ...
TPM_CENTERALIGN = ...
TPM_LEFTALIGN = ...
TPM_LEFTBUTTON = ...
TPM_NONOTIFY = ...
TPM_RETURNCMD = ...
TPM_RIGHTALIGN = ...
TPM_RIGHTBUTTON = ...
TPM_TOPALIGN = ...
TPM_VCENTERALIGN = ...