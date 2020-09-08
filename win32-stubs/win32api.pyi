__all__=['AbortSystemShutdown', 'InitiateSystemShutdown', 'Apply', 'Beep', 'BeginUpdateResource', 'ChangeDisplaySettings', 'ChangeDisplaySettingsEx', 'ClipCursor', 'CloseHandle', 'CopyFile', 'DebugBreak', 'DeleteFile', 'DragQueryFile', 'DragFinish', 'DuplicateHandle', 'EndUpdateResource', 'EnumDisplayDevices', 'EnumDisplayMonitors', 'EnumDisplaySettings', 'EnumDisplaySettingsEx', 'EnumResourceLanguages', 'EnumResourceNames', 'EnumResourceTypes', 'ExpandEnvironmentStrings', 'ExitWindows', 'ExitWindowsEx', 'FindFiles', 'FindFirstChangeNotification', 'FindNextChangeNotification', 'FindCloseChangeNotification', 'FindExecutable', 'FormatMessage', 'FormatMessageW', 'FreeLibrary', 'GenerateConsoleCtrlEvent', 'GetAsyncKeyState', 'GetCommandLine', 'GetComputerName', 'GetComputerNameEx', 'GetComputerObjectName', 'GetMonitorInfo', 'GetUserName', 'GetUserNameEx', 'GetCursorPos', 'GetCurrentThread', 'GetCurrentThreadId', 'GetCurrentProcessId', 'GetCurrentProcess', 'GetConsoleTitle', 'GetDateFormat', 'GetDiskFreeSpace', 'GetDiskFreeSpaceEx', 'GetDllDirectory', 'GetDomainName', 'GetEnvironmentVariable', 'GetEnvironmentVariableW', 'GetFileAttributes', 'GetFileVersionInfo', 'GetFocus', 'GetFullPathName', 'GetHandleInformation', 'GetKeyboardLayout', 'GetKeyboardLayoutList', 'GetKeyboardLayoutName', 'GetKeyboardState', 'GetKeyState', 'GetLastError', 'GetLastInputInfo', 'GetLocalTime', 'GetLongPathName', 'GetLongPathNameW', 'GetLogicalDrives', 'GetLogicalDriveStrings', 'GetModuleFileName', 'GetModuleFileNameW', 'GetModuleHandle', 'GetPwrCapabilities', 'GetProfileSection', 'GetProcAddress', 'GetProfileVal', 'GetShortPathName', 'GetStdHandle', 'GetSysColor', 'GetSystemDefaultLangID', 'GetSystemDefaultLCID', 'GetSystemDirectory', 'GetSystemFileCacheSize', 'SetSystemFileCacheSize', 'GetSystemInfo', 'GetNativeSystemInfo', 'GetSystemMetrics', 'GetSystemTime', 'GetTempFileName', 'GetTempPath', 'GetThreadLocale', 'GetTickCount', 'GetTimeFormat', 'GetTimeZoneInformation', 'GetVersion', 'GetVersionEx', 'GetVolumeInformation', 'GetWindowsDirectory', 'GetWindowLong', 'GetUserDefaultLangID', 'GetUserDefaultLCID', 'GlobalMemoryStatus', 'GlobalMemoryStatusEx', 'keybd_event', 'mouse_event', 'LoadCursor', 'LoadKeyboardLayout', 'LoadLibrary', 'LoadLibraryEx', 'LoadResource', 'LoadString', 'MessageBeep', 'MessageBox', 'MonitorFromPoint', 'MonitorFromRect', 'MonitorFromWindow', 'MoveFile', 'MoveFileEx', 'OpenProcess', 'OutputDebugString', 'PostMessage', 'PostQuitMessage', 'PostThreadMessage', 'RegCloseKey', 'RegConnectRegistry', 'RegCopyTree', 'RegCreateKey', 'RegCreateKeyEx', 'RegDeleteKey', 'RegDeleteKeyEx', 'RegDeleteTree', 'RegDeleteValue', 'RegEnumKey', 'RegEnumKeyEx', 'RegEnumKeyExW', 'RegEnumValue', 'RegFlushKey', 'RegGetKeySecurity', 'RegLoadKey', 'RegOpenCurrentUser', 'RegOpenKey', 'RegOpenKeyEx', 'RegOpenKeyTransacted', 'RegOverridePredefKey', 'RegQueryValue', 'RegQueryValueEx', 'RegQueryInfoKey', 'RegQueryInfoKeyW', 'RegRestoreKey', 'RegSaveKey', 'RegSaveKeyEx', 'RegSetKeySecurity', 'RegSetValue', 'RegSetValueEx', 'RegUnLoadKey', 'RegisterWindowMessage', 'RegNotifyChangeKeyValue', 'SearchPath', 'SendMessage', 'SetConsoleCtrlHandler', 'SetConsoleTitle', 'SetCursorPos', 'SetDllDirectory', 'SetErrorMode', 'SetFileAttributes', 'SetLastError', 'SetSysColors', 'SetLocalTime', 'SetSystemTime', 'SetClassLong', 'SetClassWord', 'SetWindowWord', 'SetCursor', 'SetEnvironmentVariable', 'SetEnvironmentVariable', 'SetEnvironmentVariableW', 'SetHandleInformation', 'SetStdHandle', 'SetSystemPowerState', 'SetThreadLocale', 'SetTimeZoneInformation', 'SetWindowLong', 'ShellExecute', 'ShowCursor', 'Sleep', 'TerminateProcess', 'ToAsciiEx', 'Unicode', 'UpdateResource', 'VkKeyScan', 'VkKeyScan', 'WinExec', 'WinHelp', 'WriteProfileSection', 'WriteProfileVal', 'HIBYTE', 'LOBYTE', 'HIWORD', 'LOWORD', 'RGB', 'MAKELANGID', 'MAKEWORD', 'MAKELONG']
from typing import *
from .win32typing import *
"""A module, encapsulating the Windows Win32 API."""


def AbortSystemShutdown(computerName:'Union[str]') -> 'None':
    """
    Aborts a system shutdown

Args:

      computerName(Union[str]):Specifies the name of the computer where the shutdown is to be stopped.Win32 API References

Returns:

      None
        
    """
    pass
        

def InitiateSystemShutdown(computerName:'Union[str]',message:'Union[str]',timeOut:'int',bForceClose:'int',bRebootAfterShutdown:'int') -> 'None':
    """
    Initiates a shutdown and optional restart of the specified computer.

Args:

      computerName(Union[str]):Specifies the name of the computer to shut-down, or None
      message(Union[str]):Message to display in a dialog box
      timeOut(int):Specifies the time (in seconds) that the dialog box should be displayed. While this dialog box is displayed, the shutdown can be stopped by the AbortSystemShutdown function. If dwTimeout is zero, the computer shuts down without displaying the dialog box, and the shutdown cannot be stopped by AbortSystemShutdown.
      bForceClose(int):Specifies whether applications with unsaved changes are to be forcibly closed. If this parameter is TRUE, such applications are closed. If this parameter is FALSE, a dialog box is displayed prompting the user to close the applications.
      bRebootAfterShutdown(int):Specifies whether the computer is to restart immediately after shutting down. If this parameter is TRUE, the computer is to restart. If this parameter is FALSE, the system flushes all caches to disk, clears the screen, and displays a message indicating that it is safe to power down.Win32 API References

Returns:

      None
        
    """
    pass
        

def Apply(exceptionHandler:'Any',func:'Any',args:'tuple') -> 'Any':
    """
    Calls a Python function, but traps Win32 exceptions.

Args:

      exceptionHandler(Any):An object which will be called when a win32 exception occurs.
      func(Any):The function call call under the protection of the Win32 exception handler.
      args(tuple):Args for the function.CommentsCalls the specified function in a manner similar to the built-in function apply(), but allows Win32 exceptions to be handled by Python.  If a Win32 exception occurs calling the function, the specified exceptionHandler is called, and its return value determines the action taken.Return valueDescriptionTuple of (exc_type, exc_value)This exception is raised to the Python caller of Apply() - This is conceptually similar to "raise exc_type, exc_value", although exception handlers must not themselves raise exceptions (see below).IntegerMust be one of the win32 exception constants, and this value is returned to Win32.  See the Win32 documentation for details.NoneThe exception is considered not handled (ie, it is as if no exception handler exists).  If a Python exception occurs in the Win32 exception handler, it is as if None were returned (ie, no tracebacks or other diagnostics are printed)

Returns:

      Any
        
    """
    pass
        

def Beep(freq:'int',dur:'int') -> 'None':
    """
    Generates simple tones on the speaker.

Args:

      freq(int):Specifies the frequency, in hertz, of the sound. This parameter must be in the range 37 through 32,767 (0x25 through 0x7FFF).
      dur(int):Specifies the duration, in milliseconds, of the sound.~ One value has a special meaning: If dwDuration is  - 1, the function operates asynchronously and produces sound until called again.Win32 API References

Returns:

      None
        
    """
    pass
        

def BeginUpdateResource(filename:'str',delete:'int') -> 'int':
    """
    Begins an update cycle for a PE file.

Args:

      filename(str):File in which to update resources.
      delete(int):Flag to indicate that all existing resources should be deleted.

Returns:

      int
        
    """
    pass
        

def ChangeDisplaySettings(DevMode:'PyDEVMODE',Flags:'int') -> 'int':
    """
    Changes video mode for default display

Args:

      DevMode(PyDEVMODE):A PyDEVMODE object as returned from EnumDisplaySettings, or None to reset to default settings from registry
      Flags(int):One of the win32con.CDS_* constants, or 0Return ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

Returns:

      int:One of the win32con.CDS_* constants, or 0Return ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

        
    """
    pass
        

def ChangeDisplaySettingsEx(DeviceName:'str'=None,DevMode:'PyDEVMODE'=None,Flags:'int'=0) -> 'int':
    """
    Changes video mode for specified display

Args:

      DeviceName(str):Name of device as returned by win32api::EnumDisplayDevices, use None for default display device
      DevMode(PyDEVMODE):A PyDEVMODE object as returned from win32api::EnumDisplaySettings, or None to reset to default settings from registry
      Flags(int):One of the win32con.CDS_* constants, or 0CommentsAccepts keyword argumentsReturn ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

Returns:

      int:One of the win32con.CDS_* constants, or 0
Comments

Accepts keyword arguments
Return ValueReturns DISP_CHANGE_SUCCESSFUL on success, or one of the DISP_CHANGE_* error constants on failure

        
    """
    pass
        

def ClipCursor(left,_top,_right,_bottom:'Tuple[int, int, int, int]') -> 'None':
    """
    Confines the cursor to a rectangular area on the screen.

Args:

      left,_top,_right,_bottom(Tuple[int, int, int, int]):contains the screen coordinates of the upper-left and lower-right corners of the confining rectangle. If this parameter is omitted or (0,0,0,0), the cursor is free to move anywhere on the screen.Win32 API References

Returns:

      None
        
    """
    pass
        

def CloseHandle(handle:'Union[int]') -> 'None':
    """
    Closes an open handle.

Args:

      handle(Union[int]):A previously opened handle.

Returns:

      None
        
    """
    pass
        

def CopyFile(src:'Any',dest:'Union[str]',bFailOnExist:'int'=0) -> 'None':
    """
    Copies an existing file to a new file

Args:

      src(Any):Name of an existing file.
      dest(Union[str]):Name of file to copy to.
      bFailOnExist(int):Indicates if the operation should fail if the file exists.Win32 API References

Returns:

      None
        
    """
    pass
        

def DebugBreak() -> 'None':
    """
    Breaks into the C debugger

Args:



Returns:

      None
        
    """
    pass
        

def DeleteFile(fileName:'Union[str]') -> 'None':
    """
    Deletes the specified file.

Args:

      fileName(Union[str]):File to delete.Win32 API References

Returns:

      None
        
    """
    pass
        

def DragQueryFile(hDrop:'int',fileNum:'int'=0xFFFFFFFF) -> 'Union[str, int]':
    """
    Retrieves the file names of dropped files.

Args:

      hDrop(int):Handle identifying the structure containing the file names.
      fileNum(int):Specifies the index of the file to query.Win32 API References

Returns:

      Union[str, int]:Search for DragQueryFile at msdn, google or google groups.
Return ValueIf the fileNum parameter is 0xFFFFFFFF (the default) then the return value 

is an integer with the count of files dropped.  If fileNum is between 0 and Count, 

the return value is a string containing the filename. 

If an error occurs, and exception is raised.

        
    """
    pass
        

def DragFinish(hDrop:'int') -> 'None':
    """
    Releases the memory stored by Windows for the filenames.

Args:

      hDrop(int):Handle identifying the structure containing the file names.Win32 API References

Returns:

      None
        
    """
    pass
        

def DuplicateHandle(hSourceProcess:'int',hSource:'int',hTargetProcessHandle:'int',desiredAccess:'int',bInheritHandle:'int',options:'int') -> 'int':
    """
    Duplicates a handle.

Args:

      hSourceProcess(int):Identifies the process containing the handle to duplicate.
      hSource(int):Identifies the handle to duplicate. This is an open object handle that is valid in the context of the source process.
      hTargetProcessHandle(int):Identifies the process that is to receive the duplicated handle. The handle must have PROCESS_DUP_HANDLE access.
      desiredAccess(int):Specifies the access requested for the new handle. This parameter is ignored if the dwOptions parameter specifies the DUPLICATE_SAME_ACCESS flag. Otherwise, the flags that can be specified depend on the type of object whose handle is being duplicated. For the flags that can be specified for each object type, see the following Remarks section. Note that the new handle can have more access than the original handle.
      bInheritHandle(int):Indicates whether the handle is inheritable. If TRUE, the duplicate handle can be inherited by new processes created by the target process. If FALSE, the new handle cannot be inherited.
      options(int):Specifies optional actions. This parameter can be zero, or any combination of the following flagsDUPLICATE_CLOSE_SOURCEloses the source handle. This occurs regardless of any error status returned.DUPLICATE_SAME_ACCESSIgnores the dwDesiredAccess parameter. The duplicate handle has the same access as the source handle.CommentsWhen duplicating a handle for a different process, you should either keep a reference to the returned PyHANDLE, or call .Detach() on it to prevent it from being closed prematurely.

Returns:

      int
        
    """
    pass
        

def EndUpdateResource(handle:'int',discard:'int') -> 'None':
    """
    Ends a resource update cycle of a PE file.

Args:

      handle(int):The update-file handle.
      discard(int):Flag to discard all writes.

Returns:

      None
        
    """
    pass
        

def EnumDisplayDevices(Device:'str'=None,DevNum:'int'=0,Flags:'int'=0) -> 'PyDISPLAY_DEVICE':
    """
    Obtain information about the display devices in a system

Args:

      Device(str):Name of device, use None to obtain information for the display adapter(s) on the machine, based on DevNum
      DevNum(int):Index of device of interest, starting with zero
      Flags(int):Reserved, use 0 if passed inCommentsAccepts keyword arguments

Returns:

      PyDISPLAY_DEVICE
        
    """
    pass
        

def EnumDisplayMonitors(hdc:'int'=None,rcClip:'PyRECT'=None) -> 'list':
    """
    Lists display monitors for a given device context and area

Args:

      hdc(int):Handle to device context, use None for virtual desktop
      rcClip(PyRECT):Clipping rectangle, can be NoneCommentsAccepts keyword argumentsReturn ValueReturns a sequence of tuples.  For each monitor found, returns a handle to the monitor, device context handle, and intersection rectangle: (hMonitor, hdcMonitor, PyRECT)

Returns:

      list:Clipping rectangle, can be None
Comments

Accepts keyword arguments
Return ValueReturns a sequence of tuples.  For each monitor found, returns a handle to the monitor, 

device context handle, and intersection rectangle: (hMonitor, hdcMonitor, PyRECT)

        
    """
    pass
        

def EnumDisplaySettings(DeviceName:'str'=None,ModeNum:'int'=0) -> 'PyDEVMODE':
    """
    List available modes for specified display device

Args:

      DeviceName(str):Name of device as returned by win32api::EnumDisplayDevices, use None for default display device
      ModeNum(int):Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGSCommentsAccepts keyword arguments

Returns:

      PyDEVMODE
        
    """
    pass
        

def EnumDisplaySettingsEx(ModeNum:'int',DeviceName:'str'=None,Flags:'int'=0) -> 'PyDEVMODE':
    """
    Lists available modes for a display device, with optional 

flags

Args:

      ModeNum(int):Index of setting to return, or one of ENUM_CURRENT_SETTINGS, ENUM_REGISTRY_SETTINGS
      DeviceName(str):Name of device as returned by win32api::EnumDisplayDevices. Can be None for default display
      Flags(int):EDS_RAWMODE (2) is only defined flagCommentsAccepts keyword arguments

Returns:

      PyDEVMODE
        
    """
    pass
        

def EnumResourceLanguages(hmodule:'int',lpType:'PyResourceId',lpName:'PyResourceId') -> 'List[int]':
    """
    List languages for a resource

Args:

      hmodule(int):Handle to the module that contains resource
      lpType(PyResourceId):Resource type, can be string or integer
      lpName(PyResourceId):Resource name, can be string or integer

Returns:

      List[int]
        
    """
    pass
        

def EnumResourceNames(hmodule:'int',resType:'PyResourceId') -> 'List[str]':
    """
    Enumerates all the resources of the specified type from the 

nominated file.

Args:

      hmodule(int):The handle to the module to enumerate.
      resType(PyResourceId):The type of resource to enumerate. (win32con.RT_*). If passed as a string, form is '#' sign followed by decimal number. eg RT_ANICURSOR would be '#21'Return ValueThe result is a list of string or integers, one for each resource enumerated.

Returns:

      List[str]:The type of resource to enumerate. (win32con.RT_*). 

If passed as a string, form is '#' sign followed by decimal number. eg RT_ANICURSOR would be '#21'Return ValueThe result is a list of string or integers, one for each resource enumerated.

        
    """
    pass
        

def EnumResourceTypes(hmodule:'int') -> 'List[str]':
    """
    Return name or integer id of all resource types contained in 

module

Args:

      hmodule(int):The handle to the module to enumerate.

Returns:

      List[str]
        
    """
    pass
        

def ExpandEnvironmentStrings(in:'str') -> 'str':
    """
    Expands environment-variable strings and replaces them with their 

defined values.

Args:

      in(str):String to expandWin32 API References

Returns:

      str
        
    """
    pass
        

def ExitWindows(reserved1:'int'=0,reserved2:'int'=0) -> 'None':
    """
    Logs off the current user

Args:

      reserved1(int):
      reserved2(int):Win32 API References

Returns:

      None
        
    """
    pass
        

def ExitWindowsEx(flags:'int',reserved:'int'=0) -> 'None':
    """
    either logs off the current user, shuts down the system, or shuts down and restarts 

the system.

Args:

      flags(int):The shutdown operation
      reserved(int):CommentsIt sends the WM_QUERYENDSESSION message to all applications to determine if they can be terminated.Win32 API References

Returns:

      None
        
    """
    pass
        

def FindFiles(fileSpec:'str') -> 'list':
    """
    Retrieves a list of matching filenames.  An interface to the API 

FindFirstFile/FindNextFile/Find close functions.

Args:

      fileSpec(str):A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).Win32 API References

Returns:

      list:Search for FindClose at msdn, google or google groups.
Return ValueReturns a sequence of WIN32_FIND_DATA tuples

        
    """
    pass
        

def FindFirstChangeNotification(pathName:'str',bSubDirs:'int',filter:'int') -> 'int':
    """
    Creates a change notification handle and sets up initial change 

notification filter conditions.

Args:

      pathName(str):Specifies the path of the directory to watch.
      bSubDirs(int):Specifies whether the function will monitor the directory or the directory tree. If this parameter is TRUE, the function monitors the directory tree rooted at the specified directory; if it is FALSE, it monitors only the specified directory
      filter(int):Specifies the filter conditions that satisfy a change notification wait. This parameter can be one or more of the following values:ValueMeaningFILE_NOTIFY_CHANGE_FILE_NAMEAny file name change in the watched directory or subtree causes a change notification wait operation to return. Changes include renaming, creating, or deleting a file name.FILE_NOTIFY_CHANGE_DIR_NAMEAny directory-name change in the watched directory or subtree causes a change notification wait operation to return. Changes include creating or deleting a directory.FILE_NOTIFY_CHANGE_ATTRIBUTESAny attribute change in the watched directory or subtree causes a change notification wait operation to return.FILE_NOTIFY_CHANGE_SIZEAny file-size change in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change in file size only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_LAST_WRITEAny change to the last write-time of files in the watched directory or subtree causes a change notification wait operation to return. The operating system detects a change to the last write-time only when the file is written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is sufficiently flushed.FILE_NOTIFY_CHANGE_SECURITYAny security-descriptor change in the watched directory or subtree causes a change notification wait operation to returnReturn ValueAlthough the result is a handle, the handle can not be closed via CloseHandle() - therefore a PyHandle object is not used.

Returns:

      int:Specifies the filter conditions that satisfy a change notification wait. This parameter can 

be one or more of the following values:


Value


Meaning



FILE_NOTIFY_CHANGE_FILE_NAMEAny file name change in the watched directory or subtree causes a change 

notification wait operation to return. Changes include renaming, creating, or deleting a file name.
FILE_NOTIFY_CHANGE_DIR_NAMEAny directory-name change in the watched directory or subtree causes a change 

notification wait operation to return. Changes include creating or deleting a directory.
FILE_NOTIFY_CHANGE_ATTRIBUTESAny attribute change in the watched directory or subtree causes a change 

notification wait operation to return.
FILE_NOTIFY_CHANGE_SIZEAny file-size change in the watched directory or subtree causes a change 

notification wait operation to return. The operating system detects a change in file size only when the file is 

written to the disk. For operating systems that use extensive caching, detection occurs only when the cache is 

sufficiently flushed.
FILE_NOTIFY_CHANGE_LAST_WRITEAny change to the last write-time of files in the watched directory or 

subtree causes a change notification wait operation to return. The operating system detects a change to the last 

write-time only when the file is written to the disk. For operating systems that use extensive caching, detection 

occurs only when the cache is sufficiently flushed.
FILE_NOTIFY_CHANGE_SECURITYAny security-descriptor change in the watched directory or subtree causes a 

change notification wait operation to return
Return ValueAlthough the result is a handle, the handle can not be closed via CloseHandle() - therefore a PyHandle object 

is not used.

        
    """
    pass
        

def FindNextChangeNotification(handle:'int') -> 'None':
    """
    Requests that the operating system signal a change notification handle 

the next time it detects an appropriate change.

Args:

      handle(int):The handle returned from win32api::FindFirstChangeNotification

Returns:

      None
        
    """
    pass
        

def FindCloseChangeNotification(handle:'int') -> 'None':
    """
    Closes the change notification handle.

Args:

      handle(int):The handle returned from win32api::FindFirstChangeNotification

Returns:

      None
        
    """
    pass
        

def FindExecutable(filename:'str',dir:'str') -> 'Tuple[int, str]':
    """
    Retrieves the name and handle of the executable (.EXE) file 

associated with the specified filename.

Args:

      filename(str):A file name.  This can be either a document or executable file.
      dir(str):The default directory.CommentsThe function will raise an exception if it fails.Win32 API References

Returns:

      Tuple[int, str]:Search for FindExecutable at msdn, google or google groups.
Return ValueThe return value is a tuple of (integer, string) 

The integer is the instance handle of the executable file associated 

with the specified filename. (This handle could also be the handle of 

a dynamic data exchange [DDE] server application.) 

The may contain the path to the DDE server started if no server responds to a request to initiate a DDE 

conversation.

        
    """
    pass
        

def FormatMessage(flags:'Any',source:'Any',messageId:'Any',languageID:'Any',inserts:'Any',errCode:'int'=0) -> 'str':
    """
    Returns an error message from the system error file.

Args:

      flags(Any):Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.
      source(Any):The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int; if flags contain FORMAT_MESSAGE_FROM_STRING it should be a string containing the error msg; otherwise it is ignored.
      messageId(Any):The message ID.
      languageID(Any):The language ID.
      inserts(Any):The string inserts to insert.Win32 API References
      errCode(int):The error code to return the message for,  If this value is 0, then GetLastError() is called to determine the error code.Alternative Parameters

Returns:

      str
        
    """
    pass
        

def FormatMessageW(flags:'Any',source:'Any',messageId:'Any',languageID:'Any',inserts:'Any',errCode:'int'=0) -> 'str':
    """
    Returns an error message from the system error file.

Args:

      flags(Any):Flags for the call.  Note that FORMAT_MESSAGE_ALLOCATE_BUFFER and FORMAT_MESSAGE_ARGUMENT_ARRAY will always be added.
      source(Any):The source object.  If flags contain FORMAT_MESSAGE_FROM_HMODULE it should be an int or PyHANDLE; if flags contain FORMAT_MESSAGE_FROM_STRING it should be a unicode string; otherwise it is ignored.
      messageId(Any):The message ID.
      languageID(Any):The language ID.
      inserts(Any):The string inserts to insert.Win32 API References
      errCode(int):The error code to return the message for,  If this value is 0, then GetLastError() is called to determine the error code.Alternative Parameters

Returns:

      str
        
    """
    pass
        

def FreeLibrary(hModule:'int') -> 'None':
    """
    Decrements the reference count of the loaded dynamic-link library (DLL) module.

Args:

      hModule(int):Specifies the handle to the module.Win32 API References

Returns:

      None
        
    """
    pass
        

def GenerateConsoleCtrlEvent(controlEvent:'int',processGroupId:'int') -> 'int':
    """
    Send a specified signal to a console process group that shares the 

console associated with the calling process.

Args:

      controlEvent(int):Signal to generate.
      processGroupId(int):Process group to get signal.Win32 API References

Returns:

      int
        
    """
    pass
        

def GetAsyncKeyState(key:'int') -> 'int':
    """
    Retrieves the status of the specified key.

Args:

      key(int):Specifies one of 256 possible virtual-key codes.CommentsAn application can use the virtual-key code constants win32con.VK_SHIFT, win32con.VK_CONTROL, and win32con.VK_MENU as values for the key parameter. This gives the state of the SHIFT, CTRL, or ALT keys without distinguishing between left and right. An application can also use the following virtual-key code constants as values for key to distinguish between the left and right instances of those keys: win32con.VK_LSHIFT win32con.VK_RSHIFT win32con.VK_LCONTROL win32con.VK_RCONTROL win32con.VK_LMENU win32con.VK_RMENU The GetAsyncKeyState method works with mouse buttons. However, it checks on the state of the physical mouse buttons, not on the logical mouse buttons that the physical buttons are mapped to.Win32 API References

Returns:

      int:Search for GetAsyncKeyState at msdn, google or google groups.
Return ValueThe return value specifies whether the key was pressed since the last 

call to GetAsyncKeyState, and whether the key is currently up or down. If 

the most significant bit is set, the key is down, and if the least significant 

bit is set, the key was pressed after the previous call to GetAsyncKeyState. 

The return value is zero if a window in another thread or process currently has the 

keyboard focus.

        
    """
    pass
        

def GetCommandLine() -> 'str':
    """
    Retrieves the current application's command line.

Args:



Returns:

      str
        
    """
    pass
        

def GetComputerName() -> 'str':
    """
    Returns the local computer name

Args:



Returns:

      str
        
    """
    pass
        

def GetComputerNameEx(NameType:'int') -> 'str':
    """
    Retrieves a NetBIOS or DNS name associated with the local computer

Args:

      NameType(int):Value from COMPUTER_NAME_FORMAT enum, win32con.ComputerName*Win32 API References

Returns:

      str
        
    """
    pass
        

def GetComputerObjectName(NameFormat:'int') -> 'str':
    """
    Retrieves the local computer's name in a specified format.

Args:

      NameFormat(int):EXTENDED_NAME_FORMAT value, win32con.Name*Win32 API References

Returns:

      str
        
    """
    pass
        

def GetMonitorInfo(hMonitor:'int') -> 'dict':
    """
    Retrieves information for a monitor by handle

Args:

      hMonitor(int):Handle to a monitorCommentsAccepts keyword argsReturn ValueReturns a dictionary representing a MONITORINFOEX structure

Returns:

      dict:Handle to a monitorComments

Accepts keyword args
Return ValueReturns a dictionary representing a MONITORINFOEX structure

        
    """
    pass
        

def GetUserName() -> 'str':
    """
    Returns the current user name

Args:



Returns:

      str
        
    """
    pass
        

def GetUserNameEx(NameFormat:'int') -> 'str':
    """
    Returns the current user name in format from EXTENDED_NAME_FORMAT enum

Args:

      NameFormat(int):EXTENDED_NAME_FORMAT value, win32con.Name*Win32 API References

Returns:

      str
        
    """
    pass
        

def GetCursorPos() -> 'Tuple[int, int]':
    """
    Returns the position of the cursor, in screen co-ordinates.

Args:



Returns:

      Tuple[int, int]
        
    """
    pass
        

def GetCurrentThread() -> 'int':
    """
    Returns a pseudohandle for the current thread.

Args:



Returns:

      int
        
    """
    pass
        

def GetCurrentThreadId() -> 'int':
    """
    Returns the thread ID for the current thread.

Args:



Returns:

      int
        
    """
    pass
        

def GetCurrentProcessId() -> 'int':
    """
    Returns the thread ID for the current process.

Args:



Returns:

      int
        
    """
    pass
        

def GetCurrentProcess() -> 'int':
    """
    Returns a pseudohandle for the current process.

Args:



Returns:

      int
        
    """
    pass
        

def GetConsoleTitle() -> 'str':
    """
    Returns the title for the current console.

Args:



Returns:

      str
        
    """
    pass
        

def GetDateFormat(locale:'int',flags:'int',time:'PyTime',format:'str') -> 'str':
    """
    Formats a date as a date string for a specified locale. The function formats 

either a specified date or the local system date.

Args:

      locale(int):
      flags(int):
      time(PyTime):The time to use, or None to use the current time.
      format(str):May be None

Returns:

      str
        
    """
    pass
        

def GetDiskFreeSpace(rootPath:'str') -> 'tuple':
    """
    Retrieves information about the specified disk, including the amount of 

free space available.

Args:

      rootPath(str):Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.Win32 API References

Returns:

      tuple:Search for GetDiskFreeSpace at msdn, google or google groups.
Return ValueThe return value is a tuple of 4 integers, containing 

the number of sectors per cluster, the number of bytes per sector, 

the total number of free clusters on the disk and the total number of clusters on the disk. 

If the function fails, an error is returned.

        
    """
    pass
        

def GetDiskFreeSpaceEx(rootPath:'str') -> 'tuple':
    """
    Retrieves information about the specified disk, including the amount of 

free space available.

Args:

      rootPath(str):Specifies the root directory of the disk to return information about. If rootPath is None, the method uses the root of the current directory.Win32 API References

Returns:

      tuple:Search for GetDiskFreeSpaceEx at msdn, google or google groups.
Return ValueThe return value is a tuple of 3 integers, containing 

the number of free bytes available 

the total number of bytes available on disk 

the total number of free bytes on disk 

the above values may be less, if user-quotas are in effect 

If the function fails, an error is returned.

        
    """
    pass
        

def GetDllDirectory() -> 'str':
    """
    Returns the DLL search path

Args:



Returns:

      str
        
    """
    pass
        

def GetDomainName() -> 'str':
    """
    Returns the current domain name

Args:



Returns:

      str
        
    """
    pass
        

def GetEnvironmentVariable(variable:'str') -> 'str':
    """
    Retrieves the value of an environment variable.

Args:

      variable(str):The variable to getWin32 API References

Returns:

      str:Search for GetEnvironmentVariable at msdn, google or google groups.
Return ValueReturns None if environment variable is not found

        
    """
    pass
        

def GetEnvironmentVariableW(Name:'str') -> 'str':
    """
    Retrieves the unicode value of an environment variable.

Args:

      Name(str):The variable to retrieveWin32 API References

Returns:

      str:Search for GetEnvironmentVariableW at msdn, google or google groups.
Return ValueReturns None if environment variable is not found

        
    """
    pass
        

def GetFileAttributes(pathName:'str') -> 'int':
    """
    Retrieves the attributes for the named file.

Args:

      pathName(str):The name of the file whose attributes are to be returned. If this param is a unicode object, GetFileAttributesW is called.Win32 API References

Returns:

      int:Search for GetFileAttributesW at msdn, google or google groups.
Return ValueThe return value is a combination of the win32con.FILE_ATTRIBUTE_* constants. 

An exception is raised on failure.

        
    """
    pass
        

def GetFileVersionInfo(Filename:'Union[str, Any]',SubBlock:'Union[str, Any]') -> 'None':
    """
    Retrieve version info for specified file

Args:

      Filename(Union[str, Any]):File to query for version info
      SubBlock(Union[str, Any]):Information to return: \\ for VS_FIXEDFILEINFO, \\VarFileInfo\\Translation for languages/codepages available

Returns:

      None
        
    """
    pass
        

def GetFocus() -> 'int':
    """
    Retrieves the handle of the keyboard focus window associated with the thread that 

called the method.

Args:



Returns:

      int:Search for GetFocus at msdn, google or google groups.
Return ValueThe method raises an exception if no window with the focus exists.

        
    """
    pass
        

def GetFullPathName(fileName:'str') -> 'str':
    """
    Returns the full path of a (possibly relative) path

Args:

      fileName(str):The file name.CommentsPlease use win32file::GetFullPathName instead - it has better Unicode semantics.

Returns:

      str
        
    """
    pass
        

def GetHandleInformation(Object:'int') -> 'int':
    """
    Retrieves a handle's flags.

Args:

      Object(int):Handle to an objectCommentsNot available on Win98/MeReturn ValueReturns a combination of HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

Returns:

      int:Handle to an objectComments

Not available on Win98/Me
Return ValueReturns a combination of HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSE

        
    """
    pass
        

def GetKeyboardLayout(threadId:'int'=0) -> 'int':
    """
    retrieves the active input locale identifier (formerly called the keyboard 

layout) for the specified thread.

Args:

      threadId(int):CommentsIf the idThread parameter is zero, the input locale identifier for the active thread is returned.

Returns:

      int
        
    """
    pass
        

def GetKeyboardLayoutList() -> 'Tuple[int, Any]':
    """
    Returns a sequence of all locale ids currently loaded

Args:



Returns:

      Tuple[int, Any]
        
    """
    pass
        

def GetKeyboardLayoutName() -> 'int':
    """
    Retrieves the name of the active input locale identifier (formerly 

called the keyboard layout).

Args:



Returns:

      int
        
    """
    pass
        

def GetKeyboardState() -> 'str':
    """
    Retrieves the status of the 256 virtual keys on the keyboard.

Args:



Returns:

      str:Search for GetKeyboardState at msdn, google or google groups.
Return ValueThe return value is a string of exactly 256 characters. 

Each character represents the bitmask for a key - see the Win32 

documentation for more details.

        
    """
    pass
        

def GetKeyState(key:'int') -> 'int':
    """
    Retrieves the status of the specified key.

Args:

      key(int):Specifies a virtual key. If the desired virtual key is a letter or digit (A through Z, a through z, or 0 through 9), key must be set to the ASCII value of that character. For other keys, it must be a virtual-key code.CommentsThe key status returned from this function changes as a given thread reads key messages from its message queue. The status does not reflect the interrupt-level state associated with the hardware. Use the win32api::GetAsyncKeyState method to retrieve that information.Win32 API References

Returns:

      int:Search for GetKeyState at msdn, google or google groups.
Return ValueThe return value specifies the status of 

the given virtual key. If the high-order bit is 1, the key is down; 

otherwise, it is up. If the low-order bit is 1, the key is toggled. 

A key, such as the CAPS LOCK key, is toggled if it is turned on. 

The key is off and untoggled if the low-order bit is 0. A toggle key's 

indicator light (if any) on the keyboard will be on when the key is 

toggled, and off when the key is untoggled.

        
    """
    pass
        

def GetLastError() -> 'int':
    """
    Retrieves the calling thread's last error code value.

Args:



Returns:

      int
        
    """
    pass
        

def GetLastInputInfo() -> 'int':
    """
    Returns time of last input event in tick count

Args:



Returns:

      int
        
    """
    pass
        

def GetLocalTime() -> 'tuple':
    """
    Returns the current local time

Args:



Returns:

      tuple
        
    """
    pass
        

def GetLongPathName(fileName:'str') -> 'str':
    """
    Converts the specified path to its long form.

Args:

      fileName(str):The file name.CommentsThis function may raise a NotImplementedError exception if the version of Windows does not support this function.

Returns:

      str
        
    """
    pass
        

def GetLongPathNameW(fileName:'str') -> 'str':
    """
    Converts the specified path to its long form.

Args:

      fileName(str):The file name.CommentsThis function may raise a NotImplementedError exception if the version of Windows does not support this function.

Returns:

      str
        
    """
    pass
        

def GetLogicalDrives() -> 'int':
    """
    Returns a bitmask representing the currently available disk drives.

Args:



Returns:

      int
        
    """
    pass
        

def GetLogicalDriveStrings() -> 'str':
    """
    Returns a string with all logical drives currently mapped.

Args:



Returns:

      str:Search for GetLogicalDriveStrings at msdn, google or google groups.
Return ValueThe return value is a single string, with each drive 

letter NULL terminated. 

Use "s.split('\\0')" to split into components.

        
    """
    pass
        

def GetModuleFileName(hModule:'int') -> 'str':
    """
    Retrieves the filename of the specified module.

Args:

      hModule(int):Specifies the handle to the module.Win32 API References

Returns:

      str
        
    """
    pass
        

def GetModuleFileNameW(hModule:'int') -> 'str':
    """
    Retrieves the unicode filename of the specified module.

Args:

      hModule(int):Specifies the handle to the module.Win32 API References

Returns:

      str
        
    """
    pass
        

def GetModuleHandle(fileName:'str'=None) -> 'int':
    """
    Returns the handle of an already loaded DLL.

Args:

      fileName(str):Specifies the file name of the module to load.Win32 API References

Returns:

      int
        
    """
    pass
        

def GetPwrCapabilities() -> 'dict':
    """
    Retrieves system's power capabilities

Args:



Returns:

      dict:Search for GetPwrCapabilities at msdn, google or google groups.
Return ValueReturns a dict representing a SYSTEM_POWER_CAPABILITIES struct

        
    """
    pass
        

def GetProfileSection(section:'str',iniName:'str'=None) -> 'list':
    """
    Retrieves all entries from a section in an INI file.

Args:

      section(str):The section in the INI file to retrieve a entries for.
      iniName(str):The name of the INI file.  If None, the system INI file is used.CommentsThis function is obsolete, applications should use the registry instead.Win32 API References

Returns:

      list:Search for GetProfileSection at msdn, google or google groups.
Return ValueThe return value is a list of strings.

        
    """
    pass
        

def GetProcAddress(hModule:'int',functionName:'PyResourceId') -> 'int':
    """
    Returns the address of the specified exported dynamic-link library (DLL) 

function.

Args:

      hModule(int):Specifies the handle to the module.
      functionName(PyResourceId):Specifies the name of the procedure, or its ordinal valueWin32 API References

Returns:

      int
        
    """
    pass
        

def GetProfileVal(section:'str',entry:'str',defValue:'Union[str, int]',iniName:'str'=None) -> 'Union[str, int]':
    """
    Retrieves entries from a windows INI file.  This method encapsulates 

GetProfileString, GetProfileInt, GetPrivateProfileString and GetPrivateProfileInt.

Args:

      section(str):The section in the INI file to retrieve a value for.
      entry(str):The entry within the section in the INI file to retrieve a value for.
      defValue(Union[str, int]):The default value.  The type of this parameter determines the methods return type.
      iniName(str):The name of the INI file.  If None, the system INI file is used.CommentsThis function is obsolete, applications should use the registry instead.Win32 API References

Returns:

      Union[str, int]:Search for GetPrivateProfileInt at msdn, google or google groups.
Return ValueThe return value is the same type as the default parameter.

        
    """
    pass
        

def GetShortPathName(path:'Union[str, Any]') -> 'str':
    """
    Obtains the short path form of the specified path.

Args:

      path(Union[str, Any]):If a unicode object is passed, GetShortPathNameW will be called and a unicode object returned.CommentsThe short path name is an 8.3 compatible file name.  As the input path does not need to be absolute, the returned name may be longer than the input path.Win32 API References

Returns:

      str
        
    """
    pass
        

def GetStdHandle(handle:'int') -> 'None':
    """
    Returns a handle for the standard input, standard output, or standard error device

Args:

      handle(int):input, output, or error device

Returns:

      None
        
    """
    pass
        

def GetSysColor(index:'int') -> 'int':
    """
    Returns the current system color for the specified element.

Args:

      index(int):The Id of the element to return.  See the API for full details.Win32 API References

Returns:

      int:Search for GetSysColor at msdn, google or google groups.
Return ValueThe return value is a windows RGB color representation.

        
    """
    pass
        

def GetSystemDefaultLangID() -> 'int':
    """
    Retrieves the system default language identifier.

Args:



Returns:

      int
        
    """
    pass
        

def GetSystemDefaultLCID() -> 'int':
    """
    Retrieves the system default locale identifier.

Args:



Returns:

      int
        
    """
    pass
        

def GetSystemDirectory() -> 'str':
    """
    Returns the path of the Windows system directory.

Args:



Returns:

      str
        
    """
    pass
        

def GetSystemFileCacheSize() -> 'tuple':
    """
    Returns the amount of memory reserved for file cache

Args:



Returns:

      tuple:win32api.GetSystemFileCacheSize

tuple = GetSystemFileCacheSize()Returns the amount of memory reserved for file cache
Return ValueReturns a tuple containing the minimum and maximum cache sizes, and flags (combination of 

win32con.MM_WORKING_SET_* flags)

        
    """
    pass
        

def SetSystemFileCacheSize(MinimumFileCacheSize:'Any',MaximumFileCacheSize:'Any',Flags:'int'=0) -> 'None':
    """
    Sets the amount of memory reserved for file cache

Args:

      MinimumFileCacheSize(Any):Minimum size in bytes.
      MaximumFileCacheSize(Any):Maximum size in bytes.
      Flags(int):Combination of win32con.MM_WORKING_SET_* flagsCommentsRequires SE_INCREASE_QUOTA_NAME privPass -1 for both min and max to flush file cache.Accepts keyword args.

Returns:

      None
        
    """
    pass
        

def GetSystemInfo() -> 'tuple':
    """
    Retrieves information about the current system.

Args:



Returns:

      tuple:Search for GetSystemInfo at msdn, google or google groups.
Return ValueThe return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are: 

wProcessorArchitecturedwPageSizelpMinimumApplicationAddresslpMaximumApplicationAddress 

dwActiveProcessorMaskdwNumberOfProcessors 

dwProcessorTypedwAllocationGranularity(wProcessorLevel,wProcessorRevision)

        
    """
    pass
        

def GetNativeSystemInfo() -> 'tuple':
    """
    Retrieves information about the current system for a Wow64 process.

Args:



Returns:

      tuple:Search for GetNativeSystemInfo at msdn, google or google groups.
Return ValueThe return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are: 

wProcessorArchitecturedwPageSizelpMinimumApplicationAddresslpMaximumApplicationAddress 

dwActiveProcessorMaskdwNumberOfProcessors 

dwProcessorTypedwAllocationGranularity(wProcessorLevel,wProcessorRevision)

        
    """
    pass
        

def GetSystemMetrics(index:'int') -> 'int':
    """
    Retrieves various system metrics and system configuration settings.

Args:

      index(int):Which metric is being requested.  See the API documentation for a full list.Win32 API References

Returns:

      int
        
    """
    pass
        

def GetSystemTime() -> 'tuple':
    """
    Returns the current system time

Args:



Returns:

      tuple
        
    """
    pass
        

def GetTempFileName(path:'str',prefix:'str',nUnique:'int') -> 'tuple':
    """
    Returns creates a temporary filename of the following form: 

path\\preuuuu.tmp.

Args:

      path(str):Specifies the path where the method creates the temporary filename. Applications typically specify a period (.) or the result of the GetTempPath function for this parameter.
      prefix(str):Specifies the temporary filename prefix.
      nUnique(int):Specifies an nteger used in creating the temporary filename. If this parameter is nonzero, it is appended to the temporary filename. If this parameter is zero, Windows uses the current system time to create a number to append to the filename.Win32 API References

Returns:

      tuple:Search for GetTempFileName at msdn, google or google groups.
Return ValueThe return value is a tuple of (string, int), where string is the 

filename, and rc is the unique number used to generate the filename.

        
    """
    pass
        

def GetTempPath() -> 'str':
    """
    Retrieves the path of the directory designated for temporary files.

Args:



Returns:

      str
        
    """
    pass
        

def GetThreadLocale() -> 'int':
    """
    Returns the current thread's locale.

Args:



Returns:

      int
        
    """
    pass
        

def GetTickCount() -> 'int':
    """
    Returns the number of milliseconds since windows started.

Args:



Returns:

      int
        
    """
    pass
        

def GetTimeFormat(locale:'int',flags:'int',time:'PyTime',format:'str') -> 'str':
    """
    Formats a time as a time string for a specified locale. The function formats 

either a specified time or the local system time.

Args:

      locale(int):
      flags(int):
      time(PyTime):The time to use, or None to use the current time.
      format(str):May be None

Returns:

      str
        
    """
    pass
        

def GetTimeZoneInformation(times_as_tuples:'bool'=False) -> 'tuple':
    """
    Retrieves the system time-zone information.

Args:

      times_as_tuples(bool):If true, the SYSTEMTIME elements are returned as tuples instead of a time object.Return ValueThe return value is a tuple of (rc, tzinfo), where rc is the integer return code from ::GetTimezoneInformation(), which may bevaluedescriptionTIME_ZONE_ID_STANDARDif in standard timeTIME_ZONE_ID_DAYLIGHTif in daylight savings timeTIME_ZONE_ID_UNKNOWNif the timezone in question doesn't use daylight savings time, (eg. indiana time).tzinfo is a tuple of:Items[0] int : biasSpecifies the current bias, in minutes, for local time translation on this computer. The bias is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. All translations between UTC and local time are based on the following formula:UTC = local time + bias [1] unicode : standardNameSpecifies a string associated with standard time on this operating system. For example, this member could contain "EST" to indicate Eastern Standard Time. This string is not used by the operating system, so anything stored there using the SetTimeZoneInformation function is returned unchanged by the GetTimeZoneInformation function. This string can be empty.[2] PyTime/tuple : standardTimeSpecifies a SYSTEMTIME object that contains a date and local time when the transition from daylight saving time to standard time occurs on this operating system. If this date is not specified, the wMonth member in the SYSTEMTIME structure must be zero. If this date is specified, the DaylightDate value in the TIME_ZONE_INFORMATION structure must also be specified. To select the correct day in the month, set the wYear member to zero, the wDayOfWeek member to an appropriate weekday, and the wDay member to a value in the range 1 through 5. Using this notation, the first Sunday in April can be specified, as can the last Thursday in October (5 is equal to "the last").[3] int : standardBiasSpecifies a bias value to be used during local time translations that occur during standard time. This member is ignored if a value for the StandardDate member is not supplied. This value is added to the value of the Bias member to form the bias used during standard time. In most time zones, the value of this member is zero.[4] unicode : daylightName[5] PyTime/tuple : daylightTime[6] int : daylightBiasSpecifies a bias value to be used during local time translations that occur during daylight saving time. This member is ignored if a value for the DaylightDate member is not supplied. This value is added to the value of the Bias member to form the bias used during daylight saving time. In most time zones, the value of this member is 60.

Returns:

      tuple:If true, the SYSTEMTIME elements are returned as tuples instead of a time 

object.
Return ValueThe return value is a tuple of (rc, tzinfo), where rc is 

the integer return code from ::GetTimezoneInformation(), which may be



value


description



TIME_ZONE_ID_STANDARDif in standard time
TIME_ZONE_ID_DAYLIGHTif in daylight savings time
TIME_ZONE_ID_UNKNOWNif the timezone in question doesn't use daylight savings time, (eg. indiana time).
tzinfo is a tuple of:
Items[0] int : bias
Specifies the current bias, in minutes, for local time translation on this computer. The 

bias is the difference, in minutes, between Coordinated Universal Time (UTC) and local time. All translations 

between UTC and local time are based on the following formula:UTC = local time + bias 
[1] unicode : standardName
Specifies a string associated with standard time on this operating system. For 

example, this member could contain "EST" to indicate Eastern Standard Time. This string is not used by the 

operating system, so anything stored there using the SetTimeZoneInformation function is returned unchanged by the 

GetTimeZoneInformation function. This string can be empty.
[2] PyTime/tuple : standardTime
Specifies a SYSTEMTIME object that contains a date and local time when 

the transition from daylight saving time to standard time occurs on this operating system. If this date is not 

specified, the wMonth member in the SYSTEMTIME structure must be zero. If this date is specified, the 

DaylightDate value in the TIME_ZONE_INFORMATION structure must also be specified. To select the correct day 

in the month, set the wYear member to zero, the wDayOfWeek member to an appropriate weekday, and the wDay member 

to a value in the range 1 through 5. Using this notation, the first Sunday in April can be specified, as can the 

last Thursday in October (5 is equal to "the last").
[3] int : standardBias
Specifies a bias value to be used during local time translations that occur during 

standard time. This member is ignored if a value for the StandardDate member is not supplied. This value is 

added to the value of the Bias member to form the bias used during standard time. In most time zones, the value 

of this member is zero.
[4] unicode : daylightName

[5] PyTime/tuple : daylightTime

[6] int : daylightBias
Specifies a bias value to be used during local time translations that occur during 

daylight saving time. This member is ignored if a value for the DaylightDate member is not supplied. This 

value is added to the value of the Bias member to form the bias used during daylight saving time. In most time 

zones, the value of this member is 60.

        
    """
    pass
        

def GetVersion() -> 'int':
    """
    Returns the current version of Windows, and information about the environment.

Args:



Returns:

      int:win32api.GetVersion

int = GetVersion()Returns the current version of Windows, and information about the environment.
Return ValueThe return value's low word is the major/minor version of Windows.  The high 

word is 0 if the platform is Windows NT, or 1 if Win32s on Windows 3.1

        
    """
    pass
        

def GetVersionEx(format:'int'=0) -> 'tuple':
    """
    Returns the current version of Windows, and information about the environment.

Args:

      format(int):The format of the version info to return. May be 0 (for OSVERSIONINFO) or 1 (for OSVERSIONINFOEX)Return ValueThe return value is a tuple with the following information.Items[0] int : majorVersionIdentifies the major version number of the operating system.[1] int : minorVersionIdentifies the minor version number of the operating system.[2] int : buildNumberIdentifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)[3] int : platformIdIdentifies the platform supported by the operating system. May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT[4] string : versionContains arbitrary additional information about the operating system.Return Valueor if the format param is 1, the return value is a tuple with:Items[0] int : majorVersionIdentifies the major version number of the operating system.[1] int : minorVersionIdentifies the minor version number of the operating system.[2] int : buildNumberIdentifies the build number of the operating system in the low-order word. (The high-order word contains the major and minor version numbers.)[3] int : platformIdIdentifies the platform supported by the operating system. May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or VER_PLATFORM_WIN32_NT[4] string : versionContains arbitrary additional information about the operating system.[5] int : wServicePackMajorMajor version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the major version number is 3. If no Service Pack has been installed, the value is zero.[6] int : wServicePackMinorMinor version number of the latest Service Pack installed on the system. For example, for Service Pack 3, the minor version number is 0.[7] int : wSuiteMaskBit flags that identify the product suites available on the system. This member can be a combination of the VER_SUITE_* values.[8] int : wProductTypeAdditional information about the system. This member can be one of the VER_NT_* values.[9] int : wReserved

Returns:

      tuple:The format of the version info to return. 

May be 0 (for OSVERSIONINFO) or 1 (for OSVERSIONINFOEX)
Return ValueThe return value is a tuple with the following information.
Items[0] int : majorVersion
Identifies the major version number of the operating 

system.
[1] int : minorVersion
Identifies the minor version number of the operating 

system.
[2] int : buildNumber
Identifies the build number of the operating system in 

the low-order word. (The high-order word contains the major and minor version 

numbers.)
[3] int : platformId
Identifies the platform supported by the operating system. 

May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or 

VER_PLATFORM_WIN32_NT
[4] string : version
Contains arbitrary additional 

information about the operating system.
Return Valueor if the format param is 1, the return value is a tuple with:
Items[0] int : majorVersion
Identifies the major version number of the operating 

system.
[1] int : minorVersion
Identifies the minor version number of the operating 

system.
[2] int : buildNumber
Identifies the build number of the operating system in 

the low-order word. (The high-order word contains the major and minor version 

numbers.)
[3] int : platformId
Identifies the platform supported by the operating system. 

May be one of VER_PLATFORM_WIN32s, VER_PLATFORM_WIN32_WINDOWS or 

VER_PLATFORM_WIN32_NT
[4] string : version
Contains arbitrary additional 

information about the operating system.
[5] int : wServicePackMajor
Major version number of the latest Service 

Pack installed on the system. For example, for Service Pack 3, the major version 

number is 3. If no Service Pack has been installed, the value is zero.
[6] int : wServicePackMinor
Minor version number of the latest Service 

Pack installed on the system. For example, for Service Pack 3, the minor version 

number is 0.
[7] int : wSuiteMask
Bit flags that identify the product suites available on the 

system. This member can be a combination of the VER_SUITE_* values.
[8] int : wProductType
Additional information about the system. This member can 

be one of the VER_NT_* values.
[9] int : wReserved


        
    """
    pass
        

def GetVolumeInformation(path:'str') -> 'tuple':
    """
    Returns information about a file system and colume whose root directory 

is specified.

Args:

      path(str):The root path of the volume on which information is being requested.Return ValueThe return is a tuple of: string - Volume Name long - Volume serial number. long - Maximum Component Length of a file name. long - Sys Flags - other flags specific to the file system.  See the api for details. string - File System Name

Returns:

      tuple:The root path of the volume on which information is being requested.Return ValueThe return is a tuple of: 

string - Volume Name 

long - Volume serial number. 

long - Maximum Component Length of a file name. 

long - Sys Flags - other flags specific to the file system.  See the api for details. 

string - File System Name

        
    """
    pass
        

def GetWindowsDirectory() -> 'str':
    """
    Returns the path of the Windows directory.

Args:



Returns:

      str
        
    """
    pass
        

def GetWindowLong(hwnd:'int',offset:'int') -> 'int':
    """
    Retrieves a long value at the specified offset into the extra window memory of 

the given window.

Args:

      hwnd(int):The handle to the window.
      offset(int):Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.CommentsThis function calls the GetWindowLongPtr Api function

Returns:

      int
        
    """
    pass
        

def GetUserDefaultLangID() -> 'int':
    """
    Retrieves the user default language identifier.

Args:



Returns:

      int
        
    """
    pass
        

def GetUserDefaultLCID() -> 'int':
    """
    Retrieves the user default locale identifier.

Args:



Returns:

      int
        
    """
    pass
        

def GlobalMemoryStatus() -> 'dict':
    """
    Returns systemwide memory usage

Args:



Returns:

      dict:win32api.GlobalMemoryStatus

dict = GlobalMemoryStatus()Returns systemwide memory usage
Return ValueReturns a dictionary representing a MEMORYSTATUS structure

        
    """
    pass
        

def GlobalMemoryStatusEx() -> 'dict':
    """
    Returns physical and virtual memory usage

Args:



Returns:

      dict:win32api.GlobalMemoryStatusEx

dict = GlobalMemoryStatusEx()Returns physical and virtual memory usage
Comments

Only available on Win2k and later.
Return ValueReturns a dictionary representing a MEMORYSTATUSEX structure

        
    """
    pass
        

def keybd_event(bVk:'Any',bScan:'Any',dwFlags:'Any'=0,dwExtraInfo:'Any'=0) -> 'None':
    """
    Simulate a keyboard event

Args:

      bVk(Any):Virtual-key code
      bScan(Any):Hardware scan code
      dwFlags(Any):Flags specifying various function options
      dwExtraInfo(Any):Additional data associated with keystrokeWin32 API References

Returns:

      None
        
    """
    pass
        

def mouse_event(dx:'Any',dy:'Any',dwData:'Any',dwFlags:'Any'=0,dwExtraInfo:'Any'=0) -> 'None':
    """
    Simulate a mouse event

Args:

      dx(Any):Horizontal position of mouse
      dy(Any):Vertical position of mouse
      dwData(Any):Flag specific parameter
      dwFlags(Any):Flags specifying various function options
      dwExtraInfo(Any):Additional data associated with mouse eventWin32 API References

Returns:

      None
        
    """
    pass
        

def LoadCursor(hInstance:'int',cursorid:'PyResourceId') -> 'int':
    """
    Loads a cursor.

Args:

      hInstance(int):Handle to the instance to load the resource from, or None to load a standard system cursor
      cursorid(PyResourceId):The ID of the cursor.  Can be a resource id or for system cursors, one of win32con.IDC_*Win32 API References

Returns:

      int
        
    """
    pass
        

def LoadKeyboardLayout(KLID:'str',Flags:'int'=0) -> 'int':
    """
    Loads a new locale id

Args:

      KLID(str):Hex string containing a locale id, eg "00000409"
      Flags(int):Combination of win32con.KLF_* constantsReturn ValueReturns the numeric locale id that was loaded

Returns:

      int:Combination of win32con.KLF_* constants
Return ValueReturns the numeric locale id that was loaded

        
    """
    pass
        

def LoadLibrary(fileName:'str') -> 'int':
    """
    Loads the specified DLL, and returns the handle.

Args:

      fileName(str):Specifies the file name of the module to load.Win32 API References

Returns:

      int
        
    """
    pass
        

def LoadLibraryEx(fileName:'str',handle:'int',handle1:'Any') -> 'int':
    """
    Loads the specified DLL, and returns the handle.

Args:

      fileName(str):Specifies the file name of the module to load.
      handle(int):Reserved - must be zero
      handle1(Any):Specifies the action to take when loading the module.Win32 API References

Returns:

      int
        
    """
    pass
        

def LoadResource(handle:'int',type:'PyResourceId',name:'PyResourceId',language:'int') -> 'str':
    """
    Finds and loads a resource from a PE file.

Args:

      handle(int):The handle of the module containing the resource. Use None for currrent process executable.
      type(PyResourceId):The type of resource to load.
      name(PyResourceId):The name or Id of the resource to load.
      language(int):Language to use, defaults to LANG_NEUTRAL.

Returns:

      str
        
    """
    pass
        

def LoadString(handle:'int',stringId:'int',numChars:'int'=1024) -> 'str':
    """
    Loads a string from a resource file.

Args:

      handle(int):The handle of the module containing the resource.
      stringId(int):The ID of the string to load.
      numChars(int):Number of characters to allocate for the return buffer.

Returns:

      str
        
    """
    pass
        

def MessageBeep(type:'int') -> 'int':
    """
    Plays a predefined waveform sound.

Args:

      type(int):Specifies the sound type, as identified by an entry in the [sounds] section of the registry. This parameter can be one of MB_ICONASTERISK, MB_ICONEXCLAMATION, MB_ICONHAND, MB_ICONQUESTION or MB_OK.CommentsThe waveform sound for each sound type is identified by an entry in the [sounds] section of the registry.

Returns:

      int
        
    """
    pass
        

def MessageBox(hwnd:'int',message:'str',title:'Union[str, None]',style:'int',language:'int') -> 'int':
    """
    Display a message box.

Args:

      hwnd(int):The handle of the parent window.  See the comments section.
      message(str):The message to be displayed in the message box.
      title(Union[str, None]):The title for the message box.  If None, the applications title will be used.
      style(int):The style of the message box.
      language(int):The language ID to use.CommentsNormally, a program in a GUI environment will use one of the MessageBox methods supplied by the GUI (eg, win32ui::MessageBox or PyCWnd::MessageBox)Return ValueAn integer identifying the button pressed to dismiss the dialog.

Returns:

      int:The language ID to use.
Comments

Normally, a program in a GUI environment will use one of the MessageBox 

methods supplied by the GUI (eg, win32ui::MessageBox or PyCWnd::MessageBox)
Return ValueAn integer identifying the button pressed to dismiss the dialog.

        
    """
    pass
        

def MonitorFromPoint(pt:'Tuple[int, int]',Flags:'int'=0) -> 'int':
    """
    Finds monitor that contains a point

Args:

      pt(Tuple[int, int]):Tuple of 2 ints (x,y) specifying screen coordinates
      Flags(int):Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARYCommentsAccepts keyword argumentsReturn ValueReturns None if no monitor was found

Returns:

      int:Flags that determine default behaviour, one of 

MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY
Comments

Accepts keyword arguments
Return ValueReturns None if no monitor was found

        
    """
    pass
        

def MonitorFromRect(rc:'PyRECT',Flags:'int'=0) -> 'int':
    """
    Finds monitor that has largest intersection with a rectangle

Args:

      rc(PyRECT):Rectangle to be examined
      Flags(int):Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARYCommentsAccepts keyword argumentsReturn ValueReturns None if no monitor was found

Returns:

      int:Flags that determine default behaviour, one of 

MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY
Comments

Accepts keyword arguments
Return ValueReturns None if no monitor was found

        
    """
    pass
        

def MonitorFromWindow(hwnd:'int',Flags:'int'=0) -> 'int':
    """
    Finds monitor that contains a window

Args:

      hwnd(int):Handle to a window
      Flags(int):Flags that determine default behaviour, one of MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARYCommentsAccepts keyword argumentsReturn ValueReturns None if no monitor was found

Returns:

      int:Flags that determine default behaviour, one of 

MONITOR_DEFAULTTONEAREST,MONITOR_DEFAULTTONULL,MONITOR_DEFAULTTOPRIMARY
Comments

Accepts keyword arguments
Return ValueReturns None if no monitor was found

        
    """
    pass
        

def MoveFile(srcName:'str',destName:'str') -> 'None':
    """
    Renames a file, or a directory (including its children).

Args:

      srcName(str):The name of the source file.
      destName(str):The name of the destination file.CommentsThis method can not move files across volumes.Win32 API References

Returns:

      None
        
    """
    pass
        

def MoveFileEx(srcName:'str',destName:'str',flag:'int') -> 'None':
    """
    Renames a file.

Args:

      srcName(str):The name of the source file.
      destName(str):The name of the destination file.  May be None.
      flag(int):Flags indicating how the move is to be performed.  See the API for full details.CommentsThis method can move files across volumes. If destName is None, and flags contains win32con.MOVEFILE_DELAY_UNTIL_REBOOT, the file will be deleted next reboot.Win32 API References

Returns:

      None
        
    """
    pass
        

def OpenProcess(reqdAccess:'int',bInherit:'int',pid:'int') -> 'int':
    """
    Retrieves a handle to an existing process

Args:

      reqdAccess(int):The required access.
      bInherit(int):Specifies whether the returned handle can be inherited by a new process created by the current process. If TRUE, the handle is inheritable.
      pid(int):The process ID

Returns:

      int
        
    """
    pass
        

def OutputDebugString(msg:'str') -> 'None':
    """
    Sends a string to the Windows debugging device.

Args:

      msg(str):The string to write.

Returns:

      None
        
    """
    pass
        

def PostMessage(hwnd:'int',idMessage:'int',wParam:'int'=None,lParam:'int'=None) -> 'None':
    """
    Post a message to a window.

Args:

      hwnd(int):The hWnd of the window to receive the message.
      idMessage(int):The ID of the message to post.
      wParam(int):The wParam for the message
      lParam(int):The lParam for the messageWin32 API References

Returns:

      None
        
    """
    pass
        

def PostQuitMessage(exitCode:'int'=0) -> 'None':
    """
    Post a quit message to an app.

Args:

      exitCode(int):The exit codeWin32 API References

Returns:

      None
        
    """
    pass
        

def PostThreadMessage(tid:'int',idMessage:'int',wParam:'Union[str, int]'=None,lParam:'Union[str, int]'=None) -> 'None':
    """
    Post a message to the specified thread.

Args:

      tid(int):Identifier of the thread to which the message will be posted.
      idMessage(int):The ID of the message to post.
      wParam(Union[str, int]):The wParam for the message
      lParam(Union[str, int]):The lParam for the messageWin32 API References

Returns:

      None
        
    """
    pass
        

def RegCloseKey(key:'Union[PyHKEY, int]') -> 'None':
    """
    Closes a previously opened registry key.

Args:

      key(Union[PyHKEY, int]):The key to be closed.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegConnectRegistry(computerName:'str',key:'int') -> 'int':
    """
    Establishes a connection to a predefined registry handle on another 

computer.

Args:

      computerName(str):The name of the remote computer, of the form \\\\computername.  If None, the local computer is used.
      key(int):The predefined handle.  May be win32con.HKEY_LOCAL_MACHINE or win32con.HKEY_USERS.Win32 API References

Returns:

      int:Search for RegConnectRegistry at msdn, google or google groups.
Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

        
    """
    pass
        

def RegCopyTree(KeySrc:'PyHKEY',SubKey:'str',KeyDest:'PyHKEY') -> 'None':
    """
    Copies an entire registry key to another location

Args:

      KeySrc(PyHKEY):Registry key to be copied
      SubKey(str):Subkey to be copied, can be None
      KeyDest(PyHKEY):The destination keyCommentsAccepts keyword args.Requires Vista or later.

Returns:

      None
        
    """
    pass
        

def RegCreateKey(key:'Union[PyHKEY, int]',subKey:'str') -> 'PyHKEY':
    """
    Creates the specified key, or opens the key if it already exists.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of a key that this method opens or creates. This key must be a subkey of the key identified by the key parameter. If key is one of the predefined keys, subKey may be None. In that case, the handle returned is the same hkey handle passed in to the function.Win32 API References

Returns:

      PyHKEY:Search for RegCreateKey at msdn, google or google groups.
Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

        
    """
    pass
        

def RegCreateKeyEx(Key:'Union[PyHKEY, int]',SubKey:'str',samDesired:'int',Options:'int',Class:'str'=None,SecurityAttributes:'PySECURITY_ATTRIBUTES'=None,Transaction:'int'=None) -> 'Tuple[PyHKEY, int]':
    """
    Extended version of RegCreateKey

Args:

      Key(Union[PyHKEY, int]):Registry key or one of win32con.HKEY_* values
      SubKey(str):Name of subkey to open or create.
      samDesired(int):Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain standard access rights such as DELETE, WRITE_OWNER, etc.
      Options(int):One of the winnt.REG_OPTION_* values
      Class(str):Name of registry key class
      SecurityAttributes(PySECURITY_ATTRIBUTES):Specifies security for key and handle inheritance
      Transaction(int):Handle to a transaction as returned by win32transaction::CreateTransactionCommentsImplemented only as Unicode (RegCreateKeyExW).  Accepts keyword arguments.If a transaction handle is passed in, RegCreateKeyTransacted will be called (requires Vista or later)Win32 API References

Returns:

      Tuple[PyHKEY, int]:Search for RegCreateKeyTransacted at msdn, google or google groups.
Return ValueReturns registry handle and flag indicating if key was opened or created (REG_CREATED_NEW_KEY or 

REG_OPENED_EXISTING_KEY)

        
    """
    pass
        

def RegDeleteKey(key:'Union[PyHKEY, int]',subKey:'str') -> 'None':
    """
    Deletes the specified key.  This method can not delete keys with subkeys.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of the key to delete. This key must be a subkey of the key identified by the key parameter. This value must not be None, and the key may not have subkeys.CommentsIf the method succeeds, the entire key, including all of its values, is removed. If the method fails, and exception is raised.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegDeleteKeyEx(Key:'Union[PyHKEY, int]',SubKey:'str',samDesired:'int'=0,Transaction:'int'=None) -> 'None':
    """
    Deletes a registry key from 32 or 64 bit registry view

Args:

      Key(Union[PyHKEY, int]):Registry key or one of win32con.HKEY_* values
      SubKey(str):Name of subkey to be deleted.
      samDesired(int):Can be KEY_WOW64_32KEY or KEY_WOW64_64KEY to specify alternate registry view
      Transaction(int):Handle to a transaction as returned by win32transaction::CreateTransactionCommentsAccepts keyword args.Requires 64-bit XP, Vista, or later.Key to be deleted cannot contain subkeysIf a transaction handle is specified, RegDeleteKeyTransacted is calledWin32 API References

Returns:

      None
        
    """
    pass
        

def RegDeleteTree(Key:'PyHKEY',SubKey:'str') -> 'None':
    """
    Recursively deletes a key's subkeys and values

Args:

      Key(PyHKEY):Handle to a registry key
      SubKey(str):Name of subkey to be deleted, or None for all subkeys and valuesCommentsAccepts keyword args.Requires Vista or later.

Returns:

      None
        
    """
    pass
        

def RegDeleteValue(key:'Union[PyHKEY, int]',value:'str') -> 'None':
    """
    Removes a named value from the specified registry key.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      value(str):The name of the value to remove.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegEnumKey(key:'Union[PyHKEY, int]',index:'int') -> 'str':
    """
    Enumerates subkeys of the specified open registry key. The function retrieves 

the name of one subkey each time it is called.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      index(int):The index of the key to retrieve.Win32 API References

Returns:

      str
        
    """
    pass
        

def RegEnumKeyEx(Key:'Union[PyHKEY, int]') -> 'tuple':
    """
    Lists subkeys of a registry key

Args:

      Key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS.Return ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

Returns:

      tuple:An already open key, or any one of the following win32con 

constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS.Return ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

        
    """
    pass
        

def RegEnumKeyExW(Key:'PyHKEY') -> 'tuple':
    """
    Unicode version of RegEnumKeyEx

Args:

      Key(PyHKEY):Registry handle opened with KEY_ENUMERATE_SUB_KEYS, or one of win32con.HKEY_* constantsReturn ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

Returns:

      tuple:Registry handle opened with KEY_ENUMERATE_SUB_KEYS, or one of win32con.HKEY_* constantsReturn ValueReturns subkeys as tuples of  (name, reserved, class, last write time). Reserved will always be 0.

        
    """
    pass
        

def RegEnumValue(key:'Union[PyHKEY, int]',index:'int') -> 'Tuple[str, Any, type]':
    """
    Enumerates values of the specified open registry key. The 

function retrieves the name of one subkey each time it is called.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      index(int):The index of the key to retrieve.CommentsThis function is typically called repeatedly, until an exception is raised, indicating no more values.Win32 API References

Returns:

      Tuple[str, Any, type]
        
    """
    pass
        

def RegFlushKey(key:'Union[PyHKEY, int]') -> 'None':
    """
    Writes all the attributes of the specified key to the registry.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERSCommentsIt is not necessary to call RegFlushKey to change a key. Registry changes are flushed to disk by the registry using its lazy flusher. Registry changes are also flushed to disk at system shutdown. Unlike win32api::RegCloseKey, the RegFlushKey method returns only when all the data has been written to the registry. An application should only call RegFlushKey if it requires absolute certainty that registry changes are on disk. If you don't know whether a RegFlushKey call is required, it probably isn't.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegGetKeySecurity(key:'Union[PyHKEY, int]',security_info:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Retrieves the security on the specified registry key.

Args:

      key(Union[PyHKEY, int]):Handle to an open key for which the security descriptor is set.
      security_info(int):Specifies the components of the security descriptor to retrieve. The value can be a combination of the *_SECURITY_INFORMATION constants.Win32 API References

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def RegLoadKey(key:'Union[PyHKEY, int]',subKey:'str',filename:'str') -> 'None':
    """
    The RegLoadKey method creates a subkey under HKEY_USER or HKEY_LOCAL_MACHINE 

and stores registration information from a specified file into that subkey.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of the key to delete. This key must be a subkey of the key identified by the key parameter. This value must not be None, and the key may not have subkeys.
      filename(str):The name of the file to load registry data from. This file must have been created with the win32api::RegSaveKey function. Under the file allocation table (FAT) file system, the filename may not have an extension.CommentsA call to RegLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege. If hkey is a handle returned by win32api::RegConnectRegistry, then the path specified in fileName is relative to the remote computer.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegOpenCurrentUser(samDesired:'int') -> 'PyHKEY':
    """
    Opens HKEY_CURRENT_USER for impersonated user

Args:

      samDesired(int):Desired access, combination of win32con.KEY_*Win32 API References

Returns:

      PyHKEY
        
    """
    pass
        

def RegOpenKey() -> 'PyHKEY':
    """
    Opens the specified key.

Args:



Returns:

      PyHKEY
        
    """
    pass
        

def RegOpenKeyEx(key:'Union[PyHKEY, int]',subKey:'str',sam:'int',reserved:'int'=0) -> 'PyHKEY':
    """
    Opens the specified key.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of a key that this method opens. This key must be a subkey of the key identified by the key parameter. If key is one of the predefined keys, subKey may be None. In that case, the handle returned is the same key handle passed in to the function.
      sam(int):Specifies an access mask that describes the desired security access for the new key. This parameter can be a combination of the following win32con constants: KEY_ALL_ACCESSKEY_CREATE_LINKKEY_CREATE_SUB_KEYKEY_ENUMERATE_SUB_KEYSKEY_EXECUTEKEY_NOTIFYKEY_QUERY_VALUEKEY_READKEY_SET_VALUEKEY_WRITEWin32 API References
      reserved(int):Reserved.  Must be zero.

Returns:

      PyHKEY:Search for RegOpenKeyEx at msdn, google or google groups.
Return ValueThe return value is the handle of the opened key. 

If the function fails, an exception is raised.

        
    """
    pass
        

def RegOpenKeyTransacted(Key:'Union[PyHKEY, int]',SubKey:'str',samDesired:'int',Transaction:'int',Options:'int'=0) -> 'PyHKEY':
    """
    Opens a registry key as part of a transaction

Args:

      Key(Union[PyHKEY, int]):Registry key or one of win32con.HKEY_* values
      SubKey(str):Name of subkey to open.  Can be None to reopen an existing key.
      samDesired(int):Access allowed to handle, combination of win32con.KEY_* constants.  Can also contain standard access rights such as DELETE, WRITE_OWNER, etc.
      Transaction(int):Handle to a transaction as returned by win32transaction::CreateTransaction
      Options(int):Reserved, use only 0CommentsAccepts keyword arguments.Requires Vista or later.Win32 API References

Returns:

      PyHKEY:Search for RegOpenKeyTransacted at msdn, google or google groups.
Return ValueReturns a transacted registry handle.  Note that operations on subkeys are not automatically transacted.

        
    """
    pass
        

def RegOverridePredefKey(Key:'PyHKEY',NewKey:'PyHKEY') -> 'None':
    """
    Redirects one of the predefined keys to different key

Args:

      Key(PyHKEY):One of the predefined registry keys (win32con.HKEY_*)
      NewKey(PyHKEY):Registry key to which it will be redirected.  Pass None to restore original key.CommentsRequires Windows 2000 or later.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegQueryValue(key:'Union[PyHKEY, int]',subKey:'str') -> 'str':
    """
    The RegQueryValue method retrieves the value associated with 

the unnamed value for a specified key in the registry.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of the subkey with which the value is associated. If this parameter is None or empty, the function retrieves the value set by the win32api::RegSetValue method for the key identified by key.CommentsValues in the registry have name, type, and data components. This method retrieves the data for a key's first value that has a NULL name. But the underlying API call doesn't return the type, Lame Lame Lame, DONT USE THIS!!!Win32 API References

Returns:

      str
        
    """
    pass
        

def RegQueryValueEx(key:'Union[PyHKEY, int]',valueName:'str') -> 'Tuple[Any, type]':
    """
    Retrieves the type and data for a specified value name associated 

with an open registry key.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      valueName(str):The name of the value to query.CommentsValues in the registry have name, type, and data components. This method retrieves the data for the given value.Win32 API References

Returns:

      Tuple[Any, type]
        
    """
    pass
        

def RegQueryInfoKey(key:'Union[PyHKEY, int]') -> 'Tuple[int, int, Any]':
    """
    Returns the number of 

subkeys, the number of values a key has, 

and if available the last time the key was modified as 

100's of nanoseconds since Jan 1, 1600.

Args:

      key(Union[PyHKEY, int]):An already open key, or or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERSWin32 API References

Returns:

      Tuple[int, int, Any]
        
    """
    pass
        

def RegQueryInfoKeyW(Key:'PyHKEY') -> 'dict':
    """
    Returns information about an open registry key

Args:

      Key(PyHKEY):Handle to a registry key, or one of win32con.HKEY_* constantsWin32 API References

Returns:

      dict
        
    """
    pass
        

def RegRestoreKey(Key:'PyHKEY',File:'str',Flags:'int'=0) -> 'None':
    """
    Restores a key and subkeys from a saved registry file

Args:

      Key(PyHKEY):Handle to registry key to be restored.  Can also be one of win32con.HKEY_* values.
      File(str):File from which to restore registry data
      Flags(int):One of REG_FORCE_RESTORE,REG_NO_LAZY_FLUSH,REG_REFRESH_HIVE,REG_WHOLE_HIVE_VOLATILE (from winnt)CommentsImplemented only as Unicode (RegRestoreKeyW).  Accepts keyword arguments.Requires SeBackupPrivilege and SeRestorePrivilegeWin32 API References

Returns:

      None
        
    """
    pass
        

def RegSaveKey(key:'Union[PyHKEY, int]',filename:'str',sa:'PySECURITY_ATTRIBUTES'=None) -> 'None':
    """
    The RegSaveKey method saves the specified key, and all its subkeys to the specified 

file.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      filename(str):The name of the file to save registry data to. This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the win32api::RegLoadKey, win32api::RegReplaceKey, or win32api::RegRestoreKey methods.
      sa(PySECURITY_ATTRIBUTES):The security attributes of the created file.CommentsIf key represents a key on a remote computer, the path described by fileName is relative to the remote computer. The caller of this method must possess the SeBackupPrivilege security privilege.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegSaveKeyEx(Key:'PyHKEY',File:'str',Flags:'int',SecurityAttributes:'PySECURITY_ATTRIBUTES'=None) -> 'None':
    """
    Extended version of RegSaveKey

Args:

      Key(PyHKEY):Handle to a registry key or one of HKEY_CURRENT_CONFIG, HKEY_CURRENT_USER
      File(str):Name of file in which to save data.  File must not already exist.
      Flags(int):One of REG_STANDARD_FORMAT,REG_LATEST_FORMAT,REG_NO_COMPRESSION (from winnt.py)CommentsImplemented only as Unicode (RegSaveKeyExW).  Accepts keyword arguments.SE_BACKUP_NAME privilege must be enabled.Win32 API References
      SecurityAttributes(PySECURITY_ATTRIBUTES):Specifies security for the file to be created

Returns:

      None
        
    """
    pass
        

def RegSetKeySecurity(key:'Union[PyHKEY, int]',security_info:'int',sd:'PySECURITY_DESCRIPTOR') -> 'None':
    """
    Sets the security on the specified registry key.

Args:

      key(Union[PyHKEY, int]):Handle to an open key for which the security descriptor is set.
      security_info(int):Specifies the components of the security descriptor to set. The value can be a combination of the *_SECURITY_INFORMATION constants.
      sd(PySECURITY_DESCRIPTOR):The new security descriptor for the keyCommentsIf key is one of the predefined keys, the predefined key should be closed with win32api::RegCloseKey. That ensures that the new security information is in effect the next time the predefined key is referenced.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegSetValue(key:'Union[PyHKEY, int]',subKey:'str',type:'int',value:'str') -> 'None':
    """
    Associates a value with a specified key.  Currently, only strings are supported.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      subKey(str):The name of the subkey with which the value is associated. This parameter can be None or empty, in which case the value will be added to the key identified by the key parameter.
      type(int):Type of data. Must be win32con.REG_SZ
      value(str):The value to associate with the key.CommentsIf the key specified by the lpszSubKey parameter does not exist, the RegSetValue function creates it. Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently. The key identified by the key parameter must have been opened with KEY_SET_VALUE access.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegSetValueEx(key:'Union[PyHKEY, int]',valueName:'str',reserved:'any',type:'int',value:'Any') -> 'None':
    """
    Stores data in the value field of an open registry key.

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_CLASSES_ROOTHKEY_CURRENT_USERHKEY_LOCAL_MACHINEHKEY_USERS
      valueName(str):The name of the value to set. If a value with this name is not already present in the key, the method adds it to the key. If this parameter is None or an empty string and the type parameter is the win32api.REG_SZ type, this function sets the same value the win32api::RegSetValue method would set.
      reserved(any):Place holder for reserved argument.  Zero will always be passed to the API function.
      type(int):Type of data.ValueMeaningREG_BINARYBinary data in any form.REG_DWORDA 32-bit number.REG_DWORD_LITTLE_ENDIANA 32-bit number in little-endian format. This is equivalent to REG_DWORD.In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format.REG_QWORDA 64-bit number.REG_QWORD_LITTLE_ENDIANA 64-bit number in little-endian format. This is equivalent to REG_QWORD.In little-endian format, a multi-byte value is stored in memory from the lowest byte (the little end) to the highest byte. For example, the value 0x12345678 is stored as (0x78 0x56 0x34 0x12) in little-endian format. Windows NT and Windows 95 are designed to run on little-endian computer architectures. A user may connect to computers that have big-endian architectures, such as some UNIX systems.REG_DWORD_BIG_ENDIANA 32-bit number in big-endian format. In big-endian format, a multi-byte value is stored in memory from the highest byte (the big end) to the lowest byte. For example, the value 0x12345678 is stored as (0x12 0x34 0x56 0x78) in big-endian format.REG_EXPAND_SZA null-terminated string that contains unexpanded references to environment variables (for example, %PATH%). It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions.REG_LINKA Unicode symbolic link.REG_MULTI_SZAn array of null-terminated strings, terminated by two null characters.REG_NONENo defined value type.REG_RESOURCE_LISTA device-driver resource list.REG_SZA null-terminated string. It will be a Unicode or ANSI string depending on whether you use the Unicode or ANSI functions
      value(Any):The value to be stored with the specified value name.CommentsThis method can also set additional value and type information for the specified key. The key identified by the key parameter must have been opened with KEY_SET_VALUE access. To open the key, use the win32api::RegCreateKeyEx or win32api::RegOpenKeyEx methods. Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently. The key identified by the key parameter must have been opened with KEY_SET_VALUE access.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegUnLoadKey(key:'Union[PyHKEY, int]',subKey:'str') -> 'None':
    """
    None

Args:

      key(Union[PyHKEY, int]):An already open key, or any one of the following win32con constants:HKEY_USERSHKEY_LOCAL_MACHINE
      subKey(str):The name of the key to unload. This key must be a subkey of the key identified by the key parameter. This value must not be None.CommentsA call to RegUnLoadKey fails if the calling process does not have the SE_RESTORE_PRIVILEGE privilege. If hkey is a handle returned by win32api::RegConnectRegistry, then the path specified in fileName is relative to the remote computer.Win32 API References

Returns:

      None
        
    """
    pass
        

def RegisterWindowMessage(msgString:'str') -> 'None':
    """
    The RegisterWindowMessage method, given a string, returns a system wide 

unique message ID, suitable for sending messages between applications who both register the same string.

Args:

      msgString(str):The name of the message to register. All applications that register this message string will get the same message. ID back.  It will be unique in the system and suitable for applications to use to exchange messages.CommentsOnly use RegisterWindowMessage when more than one application must process the  same message. For sending private messages within a window class, an application  can use any integer in the range WM_USER through 0x7FFF. (Messages in this range  are private to a window class, not to an application. For example, predefined  control classes such as BUTTON, EDIT, LISTBOX, and COMBOBOX may use values in  this range.)Win32 API References

Returns:

      None
        
    """
    pass
        

def RegNotifyChangeKeyValue(key:'Union[PyHKEY, int]',bWatchSubTree:'int',dwNotifyFilter:'int',hKey:'int',fAsynchronous:'int') -> 'None':
    """
    Receive notification of registry changes

Args:

      key(Union[PyHKEY, int]):Handle to an open registry key
      bWatchSubTree(int):Boolean, notify of changes to subkeys if True
      dwNotifyFilter(int):Combination of REG_NOTIFY_CHANGE_* constants
      hKey(int):Event handle to be signalled, use None if fAsynchronous is False
      fAsynchronous(int):Boolean, function returns immediately if True, waits for change if False

Returns:

      None
        
    """
    pass
        

def SearchPath(path:'str',fileName:'str',fileExt:'str'=None) -> 'int':
    """
    Searches a path for the specified file.

Args:

      path(str):The path to search.  If None, searches the standard paths.
      fileName(str):The name of the file to search for.
      fileExt(str):specifies an extension to be added to the filename when searching for the file. The first character of the filename extension must be a period (.). The extension is added only if the specified filename does not end with an extension. If a filename extension is not required or if the filename contains an extension, this parameter can be None.Win32 API References

Returns:

      int:Search for SearchPath at msdn, google or google groups.
Return ValueThe return value is a tuple of (string, int).  string is the full 

path name located.  int is the offset in the string of the base name 

of the file.

        
    """
    pass
        

def SendMessage(hwnd:'int',idMessage:'int',wParam:'Union[str, int]'=None,lParam:'Union[str, int]'=None) -> 'None':
    """
    Send a message to a window.

Args:

      hwnd(int):The hWnd of the window to receive the message.
      idMessage(int):The ID of the message to send.
      wParam(Union[str, int]):The wParam for the message
      lParam(Union[str, int]):The lParam for the messageWin32 API References

Returns:

      None
        
    """
    pass
        

def SetConsoleCtrlHandler(ctrlHandler:'callable',bAdd:'int') -> 'None':
    """
    Adds or removes an application-defined HandlerRoutine function from the 

list of handler functions for the calling process.

Args:

      ctrlHandler(callable):The function to call.  This function should accept one param - the type of signal.
      bAdd(int):True if the handler is being added, false if removed.CommentsNote that the implementation is a single CtrlHandler in C, which keeps a list of the handlers added by this function.  So although this function uses the same semantics as the Win32 function (ie, last registered first called, and first to return True stops the calls) the true order of all Python and C implemented CtrlHandlers may not match what would happen if all were implemented in C. This handler must acquire the Python lock before it can call any of the registered handlers.  This means the handler may not be called until the current Python thread yields the lock.  A console process can use the win32api::GenerateConsoleCtrlEvent function to send a CTRL+C or CTRL+BREAK signal to a console process group. The system generates CTRL_CLOSE_EVENT, CTRL_LOGOFF_EVENT, and CTRL_SHUTDOWN_EVENT signals when the user closes the console, logs off, or shuts down the system so that the process has an opportunity to clean up before termination.Win32 API References

Returns:

      None
        
    """
    pass
        

def SetConsoleTitle(title:'str') -> 'None':
    """
    Sets the title for the current console.

Args:

      title(str):The new titleWin32 API References

Returns:

      None
        
    """
    pass
        

def SetCursorPos(x,y:'Tuple[int, int]') -> 'None':
    """
    The SetCursorPos function moves the cursor to the specified screen coordinates.

Args:

      x,y(Tuple[int, int]):The new position.Win32 API References

Returns:

      None
        
    """
    pass
        

def SetDllDirectory(PathName:'str') -> 'None':
    """
    Modifies the application-specific DLL search path

Args:

      PathName(str):Directory to be added to search path, can be None to restore defaultsWin32 API References

Returns:

      None
        
    """
    pass
        

def SetErrorMode(errorMode:'int') -> 'int':
    """
    Controls whether the system will handle the specified types of serious errors, or 

whether the process will handle them.

Args:

      errorMode(int):A set of bit flags that specify the process error modeWin32 API References

Returns:

      int:Search for SetErrorMode at msdn, google or google groups.
Return ValueThe result is an integer containing the old error flags.

        
    """
    pass
        

def SetFileAttributes(pathName:'str',attrs:'int') -> 'int':
    """
    Sets the named file's attributes.

Args:

      pathName(str):The name of the file.
      attrs(int):The attributes to set.  Must be a combination of the win32con.FILE_ATTRIBUTE_* constants.

Returns:

      int
        
    """
    pass
        

def SetLastError() -> 'int':
    """
    Sets the calling thread's last error code value.

Args:



Returns:

      int
        
    """
    pass
        

def SetSysColors(Elements:'tuple',RgbValues:'tuple') -> 'None':
    """
    Changes color of various window elements

Args:

      Elements(tuple):A tuple of ints, COLOR_* constants indicating which window element to change
      RgbValues(tuple):An equal length tuple of ints representing RGB values (see win32api::RGB)

Returns:

      None
        
    """
    pass
        

def SetLocalTime(SystemTime:'PyTime') -> 'None':
    """
    Changes the system's local time

Args:

      SystemTime(PyTime):The local time to be set.  Can also be a time tuple.

Returns:

      None
        
    """
    pass
        

def SetSystemTime(year:'int',month:'int',dayOfWeek:'int',day:'int',hour:'int',minute:'int',second:'int',millseconds:'int') -> 'int':
    """
    Returns the current system time

Args:

      year(int):
      month(int):
      dayOfWeek(int):
      day(int):
      hour(int):
      minute(int):
      second(int):
      millseconds(int):

Returns:

      int
        
    """
    pass
        

def SetClassLong(hwnd:'int',offset:'int',val:'int') -> 'int':
    """
    Replaces the specified 32 or 64 bit value at the specified offset into the extra 

class memory for the window.

Args:

      hwnd(int):The handle to the window.
      offset(int):Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.
      val(int):Specifies the long value to place in the window's reserved memory.CommentsThis function calls the SetClassLongPtr Api function

Returns:

      int
        
    """
    pass
        

def SetClassWord(hwnd:'int',offset:'int',val:'int') -> 'int':
    """
    None

Args:

      hwnd(int):The handle to the window.
      offset(int):Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.
      val(int):Specifies the long value to place in the window's reserved memory.CommentsThis function is obsolete, use win32api::SetClassLong instead

Returns:

      int
        
    """
    pass
        

def SetWindowWord(hwnd:'int',offset:'int',val:'int') -> 'int':
    """
    None

Args:

      hwnd(int):The handle to the window.
      offset(int):Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.
      val(int):Specifies the long value to place in the window's reserved memory.CommentsThis function is obsolete, use win32api::SetWindowLong instead

Returns:

      int
        
    """
    pass
        

def SetCursor(hCursor:'int') -> 'int':
    """
    Set the cursor to the HCURSOR object.

Args:

      hCursor(int):The new cursor. Can be None to remove cursor.Win32 API References

Returns:

      int:Search for SetCursor at msdn, google or google groups.
Return ValueThe result is the previous cursor if there was one.

        
    """
    pass
        

def SetEnvironmentVariable(Name:'Union[str, Any]',Value:'Union[str, Any]') -> 'None':
    """
    Creates, deletes, or changes the value of an environment variable.

Args:

      Name(Union[str, Any]):Name of the environment variable
      Value(Union[str, Any]):Value to be set, use None to remove variableWin32 API References

Returns:

      None
        
    """
    pass
        

def SetEnvironmentVariable(Name:'Union[str, Any]',Value:'Union[str, Any]') -> 'None':
    """
    Creates, deletes, or changes the value of an environment variable.

Args:

      Name(Union[str, Any]):Name of the environment variable
      Value(Union[str, Any]):Value to be set, use None to remove variableWin32 API References

Returns:

      None
        
    """
    pass
        

def SetEnvironmentVariableW(Name:'str',Value:'str') -> 'None':
    """
    Creates, deletes, or changes the value of an environment variable.

Args:

      Name(str):Name of the environment variable
      Value(str):Value to be set, or None to remove variableWin32 API References

Returns:

      None
        
    """
    pass
        

def SetHandleInformation(Object:'int',Mask:'int',Flags:'int') -> 'None':
    """
    Sets a handles's flags

Args:

      Object(int):Handle to an object
      Mask(int):Bitmask specifying which flags should be set
      Flags(int):Bitmask of flag values to be set. Valid Flags are HANDLE_FLAG_INHERIT, HANDLE_FLAG_PROTECT_FROM_CLOSECommentsNot available on Win98/Me

Returns:

      None
        
    """
    pass
        

def SetStdHandle(handle:'int',handle1:'Union[int]') -> 'None':
    """
    Set the handle for the standard input, standard output, or standard error device

Args:

      handle(int):input, output, or error device
      handle1(Union[int]):A previously opened handle to be a standard handle

Returns:

      None
        
    """
    pass
        

def SetSystemPowerState(Suspend:'Any',Force:'Any') -> 'None':
    """
    Initiates low power mode to make system sleep or hibernate

Args:

      Suspend(Any):True - system is suspended. False - initiates hibernation.
      Force(Any):True - power state occurs unconditionally. False - applications are queried for permission.CommentsRequires Win2k or later.SE_SHUTDOWN_NAME privilege must be enabled.Win32 API References

Returns:

      None
        
    """
    pass
        

def SetThreadLocale(lcid:'int') -> 'None':
    """
    Sets the current thread's locale.

Args:

      lcid(int):The new LCID

Returns:

      None
        
    """
    pass
        

def SetTimeZoneInformation(tzi:'tuple') -> 'tuple':
    """
    Sets the system time-zone information.

Args:

      tzi(tuple):A tuple with the timezone infoCommentsThe tuple is of form:Items[0] int : Bias[1] string : StandardName[2] SYSTEMTIME tuple : StandardDate[3] int : StandardBias[4] string : DaylightName[5] SYSTEMTIME tuple : DaylightDate[6] int : DaylightBias

Returns:

      tuple
        
    """
    pass
        

def SetWindowLong(hwnd:'int',offset:'int',val:'int') -> 'int':
    """
    Places a long value at the specified offset into the extra window memory of the 

given window.

Args:

      hwnd(int):The handle to the window.
      offset(int):Specifies the zero-based byte offset of the value to change. Valid values are in the range zero through the number of bytes of extra window memory, minus four (for example, if 12 or more bytes of extra memory were specified, a value of 8 would be an index to the third long integer), or one of the GWL_ constants.
      val(int):Specifies the long value to place in the window's reserved memory.CommentsThis function calls the SetWindowLongPtr Api function

Returns:

      int
        
    """
    pass
        

def ShellExecute(hwnd:'int',op:'str',file:'str',params:'str',dir:'str',bShow:'int') -> 'int':
    """
    Opens or prints a file.

Args:

      hwnd(int):The handle of the parent window, or 0 for no parent.  This window receives any message boxes an application produces (for example, for error reporting).
      op(str):The operation to perform.  May be "open", "print", or None, which defaults to "open".
      file(str):The name of the file to open.
      params(str):The parameters to pass, if the file name contains an executable. Should be None for a document file.
      dir(str):The initial directory for the application.
      bShow(int):Specifies whether the application is shown when it is opened. If the lpszFile parameter specifies a document file, this parameter is zero.Win32 API References

Returns:

      int:Search for ShellExecute at msdn, google or google groups.
Return ValueThe instance handle of the application that was run. (This handle could also be the handle of a dynamic 

data exchange [DDE] server application.) If there is an error, the method raises an exception.

        
    """
    pass
        

def ShowCursor(show:'int') -> 'int':
    """
    The ShowCursor method displays or hides the cursor.

Args:

      show(int):Visiblilty flagCommentsThis function sets an internal display counter that determines whether the cursor should be displayed. The cursor is displayed only if the display count is greater than or equal to 0. If a mouse is installed, the initial display count is 0. If no mouse is installed, the display count is -1.Win32 API References

Returns:

      int:Search for ShowCursor at msdn, google or google groups.
Return ValueThe return value specifies the new display counter

        
    """
    pass
        

def Sleep(time:'int',bAlterable:'int'=0) -> 'int':
    """
    Suspends execution of the current thread for the specified time.

Args:

      time(int):The number of milli-seconds to sleep for,
      bAlterable(int):Specifies whether the function may terminate early due to an I/O completion callback function.Win32 API References

Returns:

      int:Search for SleepEx at msdn, google or google groups.
Return ValueThe return value is zero if the specified time interval expired.

        
    """
    pass
        

def TerminateProcess(handle:'int',exitCode:'int') -> 'None':
    """
    Kills a process

Args:

      handle(int):The handle of the process to terminate.
      exitCode(int):The exit code for the process.CommentsSee also win32api::OpenProcess

Returns:

      None
        
    """
    pass
        

def ToAsciiEx(vk:'int',scancode:'int',keyboardstate:'bytes',flags:'int'=0,hlayout:'Any'=None) -> 'bytes':
    """
    Translates the specified virtual-key code and keyboard state to the corresponding 

character or characters.

Args:

      vk(int):The virtual key code.
      scancode(int):The scan code.
      keyboardstate(bytes):A string of exactly 256 characters.
      flags(int):
      hlayout(Any):The keyboard layout to use

Returns:

      bytes
        
    """
    pass
        

def Unicode() -> 'str':
    """
    Creates a new Unicode object

Args:



Returns:

      str
        
    """
    pass
        

def UpdateResource(handle:'int',type:'PyResourceId',name:'PyResourceId',data:'str',language:'int') -> 'None':
    """
    Updates a resource in a PE file.

Args:

      handle(int):The update-file handle.
      type(PyResourceId):The type of resource to update
      name(PyResourceId):The id/name of the resource to update
      data(str):The data to place into the resource.
      language(int):Language to use, defaults to LANG_NEUTRAL.

Returns:

      None
        
    """
    pass
        

def VkKeyScan(char:'Any',char1:'chr') -> 'int':
    """
    Translates a character to the corresponding virtual-key code and shift state.

Args:

      char(Any):A byte or unicode string of length 1.  If a byte string is passed VkKeyScanA will be called, otherwise VkKeyScanW will be called.
      char1(chr):Specifies a characterWin32 API References

Returns:

      int
        
    """
    pass
        

def VkKeyScan(char:'Any',char1:'chr') -> 'int':
    """
    Translates a character to the corresponding virtual-key code and shift state.

Args:

      char(Any):A byte or unicode string of length 1.  If a byte string is passed VkKeyScanA will be called, otherwise VkKeyScanW will be called.
      char1(chr):Specifies a characterWin32 API References

Returns:

      int
        
    """
    pass
        

def WinExec(cmdLine:'str',show:'int') -> 'None':
    """
    Runs the specified application.

Args:

      cmdLine(str):The command line to execute.
      show(int):The initial state of the applications window.Win32 API References

Returns:

      None
        
    """
    pass
        

def WinHelp(hwnd:'int',hlpFile:'str',cmd:'int',data:'Union[str, int]'=0) -> 'None':
    """
    Invokes the Windows Help system.

Args:

      hwnd(int):The handle of the window requesting help.
      hlpFile(str):The name of the help file.
      cmd(int):The type of help.  See the api for full details.
      data(Union[str, int]):Additional data specific to the help call.Win32 API References

Returns:

      None:Search for WinHelp at msdn, google or google groups.
Return ValueThe method raises an exception if an error occurs.

        
    """
    pass
        

def WriteProfileSection(section:'str',data:'str',iniName:'str'=None) -> 'list':
    """
    Writes a complete section to an INI file or registry.

Args:

      section(str):The section in the INI file to be written.
      data(str):The data to write.  Can be None to delete the section.  Otherwise, must be string, with each entry terminated with '\\0', followed by another terminating '\\0'
      iniName(str):Name of INI file.  If specified, WritePrivateProfileSection will be called.CommentsThis function is obsolete, applications should use the registry instead.Win32 API References

Returns:

      list
        
    """
    pass
        

def WriteProfileVal(section:'str',entry:'str',value:'Union[str, int]',iniName:'str'=None) -> 'None':
    """
    Writes a value to a Windows INI file.

Args:

      section(str):The section in the INI file to write to.
      entry(str):The entry within the section in the INI file to write to.
      value(Union[str, int]):The value to write.
      iniName(str):The name of the INI file.  If None, the system INI file is used.CommentsThis function is obsolete, applications should use the registry instead.Win32 API References

Returns:

      None
        
    """
    pass
        

def HIBYTE(val:'int') -> 'int':
    """
    An interface to the win32api HIBYTE macro.

Args:

      val(int):The value to retrieve the HIBYTE from.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def LOBYTE(val:'int') -> 'int':
    """
    An interface to the win32api LOBYTE macro.

Args:

      val(int):The value to retrieve the LOBYTE from.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def HIWORD(val:'int') -> 'int':
    """
    An interface to the win32api HIWORD macro.

Args:

      val(int):The value to retrieve the HIWORD from.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def LOWORD(val:'int') -> 'int':
    """
    An interface to the win32api LOWORD macro.

Args:

      val(int):The value to retrieve the LOWORD from.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def RGB(red:'int',green:'int',blue:'int') -> 'int':
    """
    An interface to the win32api RGB macro.

Args:

      red(int):The red value
      green(int):The green value
      blue(int):The blue valueCommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def MAKELANGID(PrimaryLanguage:'int',SubLanguage:'int') -> 'int':
    """
    Creates a language identifier from a primary language identifier and a sublanguage 

identifier.

Args:

      PrimaryLanguage(int):Primary language identifier
      SubLanguage(int):The sublanguage identifierCommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def MAKEWORD(low:'int',high:'int') -> 'int':
    """
    creates a WORD value by concatenating the specified values.

Args:

      low(int):Specifies the low-order byte of the new value.
      high(int):Specifies the high-order byte of the new value.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        

def MAKELONG(low:'int',high:'int') -> 'int':
    """
    creates a LONG value by concatenating the specified values.

Args:

      low(int):Specifies the low-order byte of the new value.
      high(int):Specifies the high-order byte of the new value.CommentsThis is simply a wrapper to a C++ macro.

Returns:

      int
        
    """
    pass
        