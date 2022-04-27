__all__=['', 'OpenThemeData', 'CloseThemeData', 'DrawThemeBackground', 'DrawThemeText', 'GetThemeBackgroundContentRect', 'GetThemeBackgroundExtent', 'IsThemeActive', 'IsAppThemed', 'GetWindowTheme', 'EnableThemeDialogTexture', 'IsThemeDialogTextureEnabled', 'GetThemeAppProperties', 'EnableTheming', 'SetWindowTheme', 'GetCurrentThemeName', 'ETDT_DISABLE', 'ETDT_ENABLE', 'ETDT_ENABLETAB', 'ETDT_USETABTEXTURE']
import typing
import win32typing
""""""


def OpenThemeData(hwnd:'int',pszClassList:'str') -> 'win32typing.PyHTHEME':
    """
    None

Args:

      hwnd(typing.Any):Window handle of the control/window to be themed
      pszClassList(str):Class name (or list of names) to match to theme data section.  if the list contains more than one name, the names are tested one at a time for a match. If a match is found, OpenThemeData() returns a theme handle associated with the matching class. This param is a list (instead of just a single class name) to provide the class an opportunity to get the "best" match between the class and the current theme.  For example, a button might pass L"OkButton, Button" if its ID=ID_OK.  If the current theme has an entry for OkButton, that will be used.  Otherwise, we fall back on the normal Button entry.

Returns:

      win32typing.PyHTHEME
        
    """
    pass
        

def CloseThemeData(hTheme:'win32typing.PyHTHEME') -> 'None':
    """
    Closes the theme data handle.  This should be done 

when the window being themed is destroyed or 

whenever a WM_THEMECHANGED msg is received 

(followed by an attempt to create a new Theme data 

handle).

Args:

      hTheme(win32typing.PyHTHEME):Open theme data handle (returned from prior call to OpenThemeData() API).

Returns:

      None
        
    """
    pass
        

def DrawThemeBackground(hTheme:'win32typing.PyHTHEME',hdc:'typing.Any',iPartId:'typing.Any',iStateId:'typing.Any',pRect:'typing.Any',pClipRect:'typing.Any') -> 'None':
    """
    Draws the theme-specified border and fill for 

the "iPartId" and "iStateId".  This could be 

based on a bitmap file, a border and fill, or 

other image description.

Args:

      hTheme(win32typing.PyHTHEME):theme data handle
      hdc(typing.Any):HDC to draw into
      iPartId(typing.Any):part number to draw
      iStateId(typing.Any):state number (of the part) to draw
      pRect(typing.Any):defines the size/location of the part
      pClipRect(typing.Any):optional clipping rect (don't draw outside it)

Returns:

      None
        
    """
    pass
        

def DrawThemeText(hTheme:'win32typing.PyHTHEME',hdc:'typing.Any',iPartId:'typing.Any',iStateId:'typing.Any',pszText:'str',dwCharCount:'typing.Any',dwTextFlags:'typing.Any',dwTextFlags2:'typing.Any',pRect:'typing.Any') -> 'None':
    """
    Draws the text using the theme-specified 

color and font for the "iPartId" and "iStateId".

Args:

      hTheme(win32typing.PyHTHEME):theme data handle
      hdc(typing.Any):HDC to draw into
      iPartId(typing.Any):part number to draw
      iStateId(typing.Any):state number (of the part) to draw
      pszText(str):actual text to draw
      dwCharCount(typing.Any):number of chars to draw (-1 for all)
      dwTextFlags(typing.Any):same as DrawText() "uFormat" param
      dwTextFlags2(typing.Any):additional drawing options
      pRect(typing.Any):defines the size/location of the part

Returns:

      None
        
    """
    pass
        

def GetThemeBackgroundContentRect(hTheme:'win32typing.PyHTHEME',hdc:'typing.Any',iPartId:'typing.Any',iStateId:'typing.Any',pBoundingRect:'typing.Any') -> 'typing.Any':
    """
    Gets the size of the content for the theme-defined 

background.  This is usually the area inside the borders or Margins.

Args:

      hTheme(win32typing.PyHTHEME):theme data handle
      hdc(typing.Any):(optional) device content to be used for drawing
      iPartId(typing.Any):part number to draw
      iStateId(typing.Any):state number (of the part) to draw
      pBoundingRect(typing.Any):the outer RECT of the part being drawnReturn ValueThe result is a rect with the content area

Returns:

      typing.Any:the outer RECT of the part being drawnReturn ValueThe result is a rect with the content area

        
    """
    pass
        

def GetThemeBackgroundExtent(hTheme:'win32typing.PyHTHEME',hdc:'typing.Any',iPartId:'typing.Any',iStateId:'typing.Any',pContentRect:'typing.Any') -> 'typing.Any':
    """
    Calculates the size/location of the theme- 

specified background based on the "pContentRect".

Args:

      hTheme(win32typing.PyHTHEME):theme data handle
      hdc(typing.Any):(optional) device content to be used for drawing
      iPartId(typing.Any):part number to draw
      iStateId(typing.Any):state number (of the part) to draw
      pContentRect(typing.Any):RECT that defines the content areaReturn ValueResult is a rect with the overall size/location of part

Returns:

      typing.Any:RECT that defines the content areaReturn ValueResult is a rect with the overall size/location of part

        
    """
    pass
        

def IsThemeActive() -> 'typing.Any':
    """
    None

Args:



Returns:

      typing.Any
        
    """
    pass
        

def IsAppThemed() -> 'typing.Any':
    """
    Returns True if a theme is active and available to 

the current process

Args:



Returns:

      typing.Any
        
    """
    pass
        

def GetWindowTheme(hwnd:'int') -> 'win32typing.PyHTHEME':
    """
    If window is themed, returns its most recent 

HTHEME from OpenThemeData() - otherwise, returns NULL.

Args:

      hwnd(typing.Any):The window to get the HTHEME of

Returns:

      win32typing.PyHTHEME
        
    """
    pass
        

def EnableThemeDialogTexture(hdlg:'typing.Any',dwFlags:'typing.Any') -> 'None':
    """
    Enables/disables dialog background theme. 

This method can be used to 

tailor dialog compatibility with child windows and controls that 

may or may not coordinate the rendering of their client area backgrounds 

with that of their parent dialog in a manner that supports seamless 

background texturing.

Args:

      hdlg(typing.Any):The window handle of the target dialog
      dwFlags(typing.Any):ETDT_ENABLE to enable the theme-defined dialog background texturing, ETDT_DISABLE to disable background texturing, ETDT_ENABLETAB to enable the theme-defined background texturing using the Tab texture

Returns:

      None
        
    """
    pass
        

def IsThemeDialogTextureEnabled(hdlg:'typing.Any') -> 'typing.Any':
    """
    Reports whether the dialog supports background texturing.

Args:

      hdlg(typing.Any):The window handle of the target dialog

Returns:

      typing.Any
        
    """
    pass
        

def GetThemeAppProperties() -> 'typing.Any':
    """
    Returns the app property flags that control theming

Args:



Returns:

      typing.Any
        
    """
    pass
        

def EnableTheming(fEnable:'typing.Any') -> 'None':
    """
    Enables or disables themeing for the current user 

in the current and future sessions.

Args:

      fEnable(typing.Any):if False, disable theming & turn themes off. if True, enable themeing and, if user previously had a theme active, make it active now.

Returns:

      None
        
    """
    pass
        

def SetWindowTheme(hwnd:'int',pszSubAppName:'typing.Union[str, typing.Any]',pszSubIdList:'typing.Union[str, typing.Any]') -> 'None':
    """
    Rredirects an existing Window to use a different 

section of the current theme information than its class normally asks for.

Args:

      hwnd(typing.Any):The handle of the window (cannot be 0)
      pszSubAppName(typing.Union[str, typing.Any]):App (group) name to use in place of the calling app's name.  If NULL, the actual calling app name will be used.
      pszSubIdList(typing.Union[str, typing.Any]):A semicolon separated list of class Id names to use in place of actual list passed by the window's class.  if NULL, the id list from the calling class is used.

Returns:

      None
        
    """
    pass
        

def GetCurrentThemeName() -> 'typing.Tuple[str, str, str]':
    """
    Get the name of the current theme in-use, the 

canonical color scheme name (not the display name) and the 

canonical size name (not the display name).

Args:



Returns:

      typing.Tuple[str, str, str]
        
    """
    pass
        
ETDT_DISABLE = ...
ETDT_ENABLE = ...
ETDT_ENABLETAB = ...
ETDT_USETABTEXTURE = ...
