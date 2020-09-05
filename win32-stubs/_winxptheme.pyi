from pywintypes import *
__all__=['OpenThemeData', 'CloseThemeData', 'DrawThemeBackground', 'DrawThemeText', 'GetThemeBackgroundContentRect', 'GetThemeBackgroundExtent', 'IsThemeActive', 'IsAppThemed', 'GetWindowTheme', 'EnableThemeDialogTexture', 'IsThemeDialogTextureEnabled', 'GetThemeAppProperties', 'EnableTheming', 'SetWindowTheme', 'GetCurrentThemeName', 'ETDT_DISABLE', 'ETDT_ENABLE', 'ETDT_ENABLETAB', 'ETDT_USETABTEXTURE']
import typing
""""""


def OpenThemeData(hwnd:int,pszClassList:str) -> typing.Any:
    """
    None


Args:

      hwnd(int):Window handle of the control/window to be themed
      pszClassList(str):Class name (or list of names) to match to theme data section.  if the list contains more than one name, the names are tested one at a time for a match. If a match is found, OpenThemeData() returns a theme handle associated with the matching class. This param is a list (instead of just a single class name) to provide the class an opportunity to get the "best" match between the class and the current theme.  For example, a button might pass L"OkButton, Button" if its ID=ID_OK.  If the current theme has an entry for OkButton, that will be used.  Otherwise, we fall back on the normal Button entry.

Returns:

      typing.Any
        
    """
    pass


def CloseThemeData(hTheme:typing.Any) -> None:
    """
    Closes the theme data handle.  This should be done 

when the window being themed is destroyed or 

whenever a WM_THEMECHANGED msg is received 

(followed by an attempt to create a new Theme data 

handle).


Args:

      hTheme(typing.Any):Open theme data handle (returned from prior call to OpenThemeData() API).

Returns:

      None
        
    """
    pass


def DrawThemeBackground(hTheme:typing.Any,hdc:int,iPartId:int,iStateId:int,pRect:typing.Any,pClipRect:typing.Any) -> None:
    """
    Draws the theme-specified border and fill for 

the "iPartId" and "iStateId".  This could be 

based on a bitmap file, a border and fill, or 

other image description.


Args:

      hTheme(typing.Any):theme data handle
      hdc(int):HDC to draw into
      iPartId(int):part number to draw
      iStateId(int):state number (of the part) to draw
      pRect(typing.Any):defines the size/location of the part
      pClipRect(typing.Any):optional clipping rect (don't draw outside it)

Returns:

      None
        
    """
    pass


def DrawThemeText(hTheme:typing.Any,hdc:int,iPartId:int,iStateId:int,pszText:str,dwCharCount:int,dwTextFlags:int,dwTextFlags2:int,pRect:typing.Any) -> None:
    """
    Draws the text using the theme-specified 

color and font for the "iPartId" and "iStateId".


Args:

      hTheme(typing.Any):theme data handle
      hdc(int):HDC to draw into
      iPartId(int):part number to draw
      iStateId(int):state number (of the part) to draw
      pszText(str):actual text to draw
      dwCharCount(int):number of chars to draw (-1 for all)
      dwTextFlags(int):same as DrawText() "uFormat" param
      dwTextFlags2(int):additional drawing options
      pRect(typing.Any):defines the size/location of the part

Returns:

      None
        
    """
    pass


def GetThemeBackgroundContentRect(hTheme:typing.Any,hdc:int,iPartId:int,iStateId:int,pBoundingRect:typing.Any) -> typing.Any:
    """
    Gets the size of the content for the theme-defined 

background.  This is usually the area inside the borders or Margins.


Args:

      hTheme(typing.Any):theme data handle
      hdc(int):(optional) device content to be used for drawing
      iPartId(int):part number to draw
      iStateId(int):state number (of the part) to draw
      pBoundingRect(typing.Any):the outer RECT of the part being drawnReturn ValueThe result is a rect with the content area

Returns:

      typing.Any:the outer RECT of the part being drawnReturn ValueThe result is a rect with the content area

        
    """
    pass


def GetThemeBackgroundExtent(hTheme:typing.Any,hdc:int,iPartId:int,iStateId:int,pContentRect:typing.Any) -> typing.Any:
    """
    Calculates the size/location of the theme- 

specified background based on the "pContentRect".


Args:

      hTheme(typing.Any):theme data handle
      hdc(int):(optional) device content to be used for drawing
      iPartId(int):part number to draw
      iStateId(int):state number (of the part) to draw
      pContentRect(typing.Any):RECT that defines the content areaReturn ValueResult is a rect with the overall size/location of part

Returns:

      typing.Any:RECT that defines the content areaReturn ValueResult is a rect with the overall size/location of part

        
    """
    pass


def IsThemeActive() -> bool:
    """
    None


Args:



Returns:

      bool
        
    """
    pass


def IsAppThemed() -> bool:
    """
    Returns True if a theme is active and available to 

the current process


Args:



Returns:

      bool
        
    """
    pass


def GetWindowTheme(hwnd:int) -> typing.Any:
    """
    If window is themed, returns its most recent 

HTHEME from OpenThemeData() - otherwise, returns NULL.


Args:

      hwnd(int):The window to get the HTHEME of

Returns:

      typing.Any
        
    """
    pass


def EnableThemeDialogTexture(hdlg:int,dwFlags:int) -> None:
    """
    Enables/disables dialog background theme. 

This method can be used to 

tailor dialog compatibility with child windows and controls that 

may or may not coordinate the rendering of their client area backgrounds 

with that of their parent dialog in a manner that supports seamless 

background texturing.


Args:

      hdlg(int):The window handle of the target dialog
      dwFlags(int):ETDT_ENABLE to enable the theme-defined dialog background texturing, ETDT_DISABLE to disable background texturing, ETDT_ENABLETAB to enable the theme-defined background texturing using the Tab texture

Returns:

      None
        
    """
    pass


def IsThemeDialogTextureEnabled(hdlg:int) -> bool:
    """
    Reports whether the dialog supports background texturing.


Args:

      hdlg(int):The window handle of the target dialog

Returns:

      bool
        
    """
    pass


def GetThemeAppProperties() -> int:
    """
    Returns the app property flags that control theming


Args:



Returns:

      int
        
    """
    pass


def EnableTheming(fEnable:bool) -> None:
    """
    Enables or disables themeing for the current user 

in the current and future sessions.


Args:

      fEnable(bool):if False, disable theming & turn themes off. if True, enable themeing and, if user previously had a theme active, make it active now.

Returns:

      None
        
    """
    pass


def SetWindowTheme(hwnd:int,pszSubAppName:Union[str,None],pszSubIdList:Union[str,None]) -> None:
    """
    Rredirects an existing Window to use a different 

section of the current theme information than its class normally asks for.


Args:

      hwnd(int):The handle of the window (cannot be 0)
      pszSubAppName(str,None):App (group) name to use in place of the calling app's name.  If NULL, the actual calling app name will be used.
      pszSubIdList(str,None):A semicolon separated list of class Id names to use in place of actual list passed by the window's class.  if NULL, the id list from the calling class is used.

Returns:

      None
        
    """
    pass


def GetCurrentThemeName() -> typing.Any:
    """
    Get the name of the current theme in-use, the 

canonical color scheme name (not the display name) and the 

canonical size name (not the display name).


Args:



Returns:

      typing.Any
        
    """
    pass

ETDT_DISABLE = ...
ETDT_ENABLE = ...
ETDT_ENABLETAB = ...
ETDT_USETABTEXTURE = ...