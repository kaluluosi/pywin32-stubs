__all__=['', 'CreateConsoleScreenBuffer', 'GetConsoleDisplayMode', 'AttachConsole', 'AllocConsole', 'FreeConsole', 'GetConsoleProcessList', 'GetConsoleCP', 'GetConsoleOutputCP', 'SetConsoleCP', 'SetConsoleOutputCP', 'GetConsoleSelectionInfo', 'AddConsoleAlias', 'GetConsoleAliases', 'GetConsoleAliasExes', 'GetConsoleWindow', 'GetNumberOfConsoleFonts', 'SetConsoleTitle', 'GetConsoleTitle', 'GenerateConsoleCtrlEvent', 'GetStdHandle']
import typing
import win32typing
"""Interface to the Windows Console functions for dealing with character-mode applications"""


def CreateConsoleScreenBuffer(DesiredAccess:'typing.Any',ShareMode:'typing.Any',Flags:'typing.Any',SecurityAttributes:'win32typing.PySECURITY_ATTRIBUTES'=None) -> 'win32typing.PyConsoleScreenBuffer':
    """
    Creates a new console screen buffer

Args:

      DesiredAccess(typing.Any):GENERIC_READ and/or GENERIC_WRITE
      ShareMode(typing.Any):FILE_SHARE_READ and/or FILE_SHARE_WRITE
      Flags(typing.Any):CONSOLE_TEXTMODE_BUFFER is currently only valid flag
      SecurityAttributes(win32typing.PySECURITY_ATTRIBUTES):Specifies security descriptor and inheritance for handle

Returns:

      win32typing.PyConsoleScreenBuffer
        
    """
    pass
        

def GetConsoleDisplayMode() -> 'typing.Any':
    """
    Returns the current console's display mode

Args:



Returns:

      typing.Any:win32console.GetConsoleDisplayMode

int = GetConsoleDisplayMode()Returns the current console's display mode
Comments

Only exists on Wix XP and later
Return ValueCONSOLE_FULLSCREEN,CONSOLE_FULLSCREEN_HARDWARE

        
    """
    pass
        

def AttachConsole(ProcessId:'typing.Any') -> 'None':
    """
    Attaches to console of another process

Args:

      ProcessId(typing.Any):Pid of another process, or ATTACH_PARENT_PROCESSCommentsCalling process must not already be attached to another console

Returns:

      None
        
    """
    pass
        

def AllocConsole() -> 'None':
    """
    Creates a new console for the calling process

Args:



Returns:

      None
        
    """
    pass
        

def FreeConsole() -> 'None':
    """
    Detaches process from its current console

Args:



Returns:

      None
        
    """
    pass
        

def GetConsoleProcessList() -> 'typing.Tuple[typing.Any, ...]':
    """
    Returns pids of all processes attached to current console

Args:



Returns:

      typing.Tuple[typing.Any, ...]
        
    """
    pass
        

def GetConsoleCP() -> 'typing.Any':
    """
    Returns the input code page for calling process's console

Args:



Returns:

      typing.Any
        
    """
    pass
        

def GetConsoleOutputCP() -> 'typing.Any':
    """
    Returns the output code page for calling process's console

Args:



Returns:

      typing.Any
        
    """
    pass
        

def SetConsoleCP(CodePageId:'typing.Any') -> 'None':
    """
    Sets the input code page for calling process's console

Args:

      CodePageId(typing.Any):The code page to set

Returns:

      None
        
    """
    pass
        

def SetConsoleOutputCP(CodePageID:'typing.Any') -> 'None':
    """
    Sets the output code page for calling process's console

Args:

      CodePageID(typing.Any):The code page to set

Returns:

      None
        
    """
    pass
        

def GetConsoleSelectionInfo() -> 'typing.Any':
    """
    Returns info on text selection within the current console

Args:



Returns:

      typing.Any:win32console.GetConsoleSelectionInfo

dict = GetConsoleSelectionInfo()Returns info on text selection within the current console
Return ValueReturns a dictionary containing {Flags:int, SelectionAnchor: PyCOORD, Selection:PySMALL_RECT} 

Flags will contain a combination of 

CONSOLE_NO_SELECTION,CONSOLE_SELECTION_IN_PROGRESS,CONSOLE_SELECTION_NOT_EMPTY,CONSOLE_MOUSE_SELECTION,CONSOLE_MOUSE_DOWN

        
    """
    pass
        

def AddConsoleAlias(Source:'typing.Any',Target:'typing.Any',ExeName:'typing.Any') -> 'None':
    """
    Creates a new console alias

Args:

      Source(typing.Any):The string to be mapped to the target string
      Target(typing.Any):String to be substituted for Source.  If None, alias is removed
      ExeName(typing.Any):Name of executable that will use alias

Returns:

      None
        
    """
    pass
        

def GetConsoleAliases(ExeName:'typing.Any') -> 'typing.Any':
    """
    Retrieves aliases defined under specified executable

Args:

      ExeName(typing.Any):Name of executable for which to return aliasesReturn ValueReturns a unicode string containing null-terminated pairs of aliases and their target text of the form "alias1=replacementtext1\\0alias2=replacementtext2\\0"

Returns:

      typing.Any:Name of executable for which to return aliasesReturn ValueReturns a unicode string containing null-terminated pairs of aliases and their target text 

of the form "alias1=replacementtext1\\0alias2=replacementtext2\\0"

        
    """
    pass
        

def GetConsoleAliasExes() -> 'typing.Any':
    """
    Lists all executables that have console aliases defined

Args:



Returns:

      typing.Any:win32console.GetConsoleAliasExes
PyUNICODE = GetConsoleAliasExes()Lists all executables that have console aliases defined
Return ValueReturns a unicode string containing executable names separated by NULLS

        
    """
    pass
        

def GetConsoleWindow() -> 'typing.Any':
    """
    Returns a handle to the console's window, or 0 if none exists

Args:



Returns:

      typing.Any:win32console.GetConsoleWindow

int = GetConsoleWindow()Returns a handle to the console's window, or 0 if none exists
Return ValueThis function may raise NotImplementedError if it does not exist on 

the platform, or a PyHANDLE object with a value of 0.  It will never 

raise a win32 exception.

        
    """
    pass
        

def GetNumberOfConsoleFonts() -> 'typing.Any':
    """
    Returns the number of fonts available to the console

Args:



Returns:

      typing.Any
        
    """
    pass
        

def SetConsoleTitle(ConsoleTitle:'typing.Any') -> 'None':
    """
    Sets the title of the console window

Args:

      ConsoleTitle(typing.Any):New title for the console

Returns:

      None
        
    """
    pass
        

def GetConsoleTitle() -> 'typing.Any':
    """
    Returns the title of the console window

Args:



Returns:

      typing.Any
        
    """
    pass
        

def GenerateConsoleCtrlEvent(CtrlEvent:'typing.Any',ProcessGroupId:'typing.Any'=0) -> 'None':
    """
    Sends a control signal to a group of processes attached to a common 

console

Args:

      CtrlEvent(typing.Any):Signal to be sent to specified process group - CTRL_C_EVENT or CTRL_BREAK_EVENT
      ProcessGroupId(typing.Any):Pid of a process group, use 0 for calling process

Returns:

      None
        
    """
    pass
        

def GetStdHandle(StdHandle:'typing.Any') -> 'win32typing.PyConsoleScreenBuffer':
    """
    Returns one of calling process's standard handles

Args:

      StdHandle(typing.Any):Specifies the handle to return - STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLEReturn ValueReturns a PyConsoleScreenBuffer wrapping the handle, or None if specified handle does not exist

Returns:

      win32typing.PyConsoleScreenBuffer:Specifies the handle to return - 

STD_INPUT_HANDLE, STD_OUTPUT_HANDLE, or STD_ERROR_HANDLEReturn ValueReturns a PyConsoleScreenBuffer wrapping the handle, or None if specified handle does not exist

        
    """
    pass
        