__all__=['', 'CeRapiInit', 'CeRapiUninit', 'CreateProcess', 'CeRapiInitEx', 'CeCopyFile', 'CeCheckPassword', 'CeCreateFile', 'CeDeleteFile', 'CeMoveFile', 'CeCreateDirectory', 'CeRemoveDirectory', 'CeGetTempPath', 'CeGetSystemInfo', 'CeGetDesktopDeviceCaps', 'CeGetSystemMetrics', 'CeGetSpecialFolderPath', 'CeGetStoreInformation', 'CeGetSystemPowerStatusEx', 'CeSHCreateShortcut', 'CeSHGetShortcutTarget', 'CeGetVersionEx', 'CeGlobalMemoryStatus', 'FindFiles', 'CeGetFileAttributes', 'CeSetFileAttributes', 'CeGetFileSize', 'CeReadFile', 'WriteFile', 'CSIDL_BITBUCKET', 'CSIDL_COMMON_DESKTOPDIRECTORY', 'CSIDL_COMMON_PROGRAMS', 'CSIDL_COMMON_STARTMENU', 'CSIDL_COMMON_STARTUP', 'CSIDL_CONTROLS', 'CSIDL_DESKTOP', 'CSIDL_DESKTOPDIRECTORY', 'CSIDL_DRIVES', 'CSIDL_FONTS', 'CSIDL_NETHOOD', 'CSIDL_NETWORK', 'CSIDL_PERSONAL', 'CSIDL_PRINTERS', 'CSIDL_PROGRAMS', 'CSIDL_RECENT', 'CSIDL_SENDTO', 'CSIDL_STARTMENU', 'CSIDL_STARTUP', 'CSIDL_TEMPLATES']
from typing import *
from win32helper.win32typing import *
"""A module which provides an interface to the win32 CE Remote API"""


def CeRapiInit() -> 'None':
    """
    Initializes the remote API.

Args:



Returns:

      None
        
    """
    pass
        

def CeRapiUninit() -> 'None':
    """
    UnInitializes the remote API.

Args:



Returns:

      None
        
    """
    pass
        

def CreateProcess(appName:'str',commandLine:'str',processAttributes:'PySECURITY_ATTRIBUTES',threadAttributes:'PySECURITY_ATTRIBUTES',bInheritHandles:'int',dwCreationFlags:'int',newEnvironment:'None',currentDirectory:'str',startupinfo:'PySTARTUPINFO') -> 'Tuple[int, int, int, int]':
    """
    Creates a new process and its primary thread. The new process executes the specified executable file.

Args:

      appName(str):name of executable module, or None
      commandLine(str):command line string, or None
      processAttributes(PySECURITY_ATTRIBUTES):process security attributes, or None
      threadAttributes(PySECURITY_ATTRIBUTES):thread security attributes, or None
      bInheritHandles(int):handle inheritance flag
      dwCreationFlags(int):creation flags
      newEnvironment(None):A dictionary of stringor Unicode pairs to define the environment for the process, or None to inherit the current environment.
      currentDirectory(str):current directory name, or None
      startupinfo(PySTARTUPINFO):a STARTUPINFO object that specifies how the main window for the new process should appear.CommentsThe result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

Returns:

      Tuple[int, int, int, int]
        
    """
    pass
        

def CeRapiInitEx() -> 'int':
    """
    Initializes the remote API asynchronously.

Args:



Returns:

      int
        
    """
    pass
        

def CeCopyFile(_from:'str',to:'str',bFailIfExists:'int') -> 'None':
    """
    Copies a file

Args:

      _from(str):The name of the file to copy from
      to(str):The name of the file to copy to
      bFailIfExists(int):Indicates if the operation should fail if the file exists.

Returns:

      None
        
    """
    pass
        

def CeCheckPassword(password:'str') -> 'None':
    """
    This function compares a specified string to the system password.

Args:

      password(str):The password to compare.

Returns:

      None
        
    """
    pass
        

def CeCreateFile(fileName:'str',desiredAccess:'int',shareMode:'int',attributes:'PySECURITY_ATTRIBUTES',creationDisposition:'int',flagsAndAttributes:'int',hTemplateFile:'int') -> 'PyCEHANDLE':
    """
    Creates or opens the a file or other object and returns a handle that can be used to access the object.

Args:

      fileName(str):The name of the file
      desiredAccess(int):access (read-write) mode Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.ValueMeaning0Specifies device query access to the object. An application can query device attributes without accessing the device.GENERIC_READSpecifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.GENERIC_WRITESpecifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
      shareMode(int):Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. To share the object, use a combination of one or more of the following values:ValueMeaningFILE_SHARE_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested.FILE_SHARE_READSubsequent open operations on the object will succeed only if read access is requested.FILE_SHARE_WRITESubsequent open operations on the object will succeed only if write access is requested.
      attributes(PySECURITY_ATTRIBUTES):The security attributes, or None
      creationDisposition(int):Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:ValueMeaningCREATE_NEWCreates a new file. The function fails if the specified file already exists.CREATE_ALWAYSCreates a new file. If the file exists, the function overwrites the file and clears the existing attributes.OPEN_EXISTINGOpens the file. The function fails if the file does not exist. See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.OPEN_ALWAYSOpens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.TRUNCATE_EXISTINGOpens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
      flagsAndAttributes(int):file attributes
      hTemplateFile(int):Specifies a handle with GENERIC_READ access to a template file. The template file supplies file attributes and extended attributes for the file being created.   Under Win95, this must be 0, else an exception will be raised.CommentsThe following objects can be opened:filespipesmailslotscommunications resourcesdisk devices (Windows NT only)consolesdirectories (open only)

Returns:

      PyCEHANDLE
        
    """
    pass
        

def CeDeleteFile(fileName:'str') -> 'None':
    """
    Deletes a file.

Args:

      fileName(str):The filename to delete

Returns:

      None
        
    """
    pass
        

def CeMoveFile(existingFileName:'str',newFileName:'str') -> 'None':
    """
    Renames an existing file or a directory (including all its children).

Args:

      existingFileName(str):Name of the existing file
      newFileName(str):New name for the file

Returns:

      None
        
    """
    pass
        

def CeCreateDirectory(name:'str',sa:'PySECURITY_ATTRIBUTES') -> 'None':
    """
    Creates a directory

Args:

      name(str):The name of the directory to create
      sa(PySECURITY_ATTRIBUTES):The security attributes, or None

Returns:

      None
        
    """
    pass
        

def CeRemoveDirectory(lpPathName:'str') -> 'None':
    """
    Removes an existing directory

Args:

      lpPathName(str):Name of the path to remove.

Returns:

      None
        
    """
    pass
        

def CeGetTempPath() -> 'str':
    """
    Obtains the temp path on the device.

Args:



Returns:

      str
        
    """
    pass
        

def CeGetSystemInfo() -> 'tuple':
    """
    Retrieves information about the CE device.

Args:



Returns:

      tuple:Search for GetSystemInfo at msdn, google or google groups.
Return ValueThe return value is a tuple of 9 values, which corresponds 

to the Win32 SYSTEM_INFO structure.  The element names are: 

dwOemIddwPageSizelpMinimumApplicationAddresslpMaximumApplicationAddress, 

dwActiveProcessorMaskdwNumberOfProcessors 

dwProcessorTypedwAllocationGranularity(wProcessorLevel,wProcessorRevision)

        
    """
    pass
        

def CeGetDesktopDeviceCaps() -> 'int':
    """
    Retrieves information about the CE desktop.

Args:



Returns:

      int
        
    """
    pass
        

def CeGetSystemMetrics() -> 'int':
    """
    Retrieves information about the CE system.

Args:



Returns:

      int
        
    """
    pass
        

def CeGetSpecialFolderPath() -> 'str':
    """
    Retrieves the location of special folders on the CE device.

Args:



Returns:

      str
        
    """
    pass
        

def CeGetStoreInformation() -> 'Tuple[int, int]':
    """
    Retrieves information about store on the CE system.

Args:



Returns:

      Tuple[int, int]:wincerapi.CeGetStoreInformation

int, int = CeGetStoreInformation()Retrieves information about store on the CE system.
Return ValueThe result is a tuple of (storeSize, freeSize)

        
    """
    pass
        

def CeGetSystemPowerStatusEx() -> 'tuple':
    """
    Retrieves the power status of the CE device.

Args:



Returns:

      tuple:wincerapi.CeGetSystemPowerStatusEx

tuple = CeGetSystemPowerStatusEx()Retrieves the power status of the CE device.
Return ValueThe result is a tuple of (ACLineStatus, BatteryFlag, BatteryLifePercent, BatteryLifeTime, BatteryFullLifeTime, BackupBatteryFlag, BackupBatteryLifePercent, BackupBatteryLifeTime, BackupBatteryLifeTime);

        
    """
    pass
        

def CeSHCreateShortcut() -> 'None':
    """
    Creates a shortcut on the remote device.

Args:



Returns:

      None
        
    """
    pass
        

def CeSHGetShortcutTarget() -> 'tuple':
    """
    Retrieves the target of a shortcut.

Args:



Returns:

      tuple
        
    """
    pass
        

def CeGetVersionEx() -> 'Tuple[int, int, int, int, str]':
    """
    Returns the current version of Windows, and information about the environment for the CE device.

Args:



Returns:

      Tuple[int, int, int, int, str]:wincerapi.CeGetVersionEx

(int,int,int,int,string) = CeGetVersionEx()Returns the current version of Windows, and information about the environment for the CE device.
Return ValueThe return value is a tuple with the following information.

        
    """
    pass
        

def CeGlobalMemoryStatus() -> 'tuple':
    """
    Returns information about current memory availability.

Args:



Returns:

      tuple:wincerapi.CeGlobalMemoryStatus

tuple = CeGlobalMemoryStatus()Returns information about current memory availability.
Return ValueThe return value is a tuple with the following information.

        
    """
    pass
        

def FindFiles(fileSpec:'str') -> 'list':
    """
    Retrieves a list of matching filenames on the CE device.  An interface to the API CeFindFirstFile/CeFindNextFile functions.

Args:

      fileSpec(str):A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).Win32 API References

Returns:

      list:Search for CloseHandle at msdn, google or google groups.
Return ValueThe return value is a list of tuples, in the same format as the WIN32_FIND_DATA structure:
Items
        
    """
    pass
        

def CeGetFileAttributes(fileName:'str') -> 'int':
    """
    Determines a files attributes.

Args:

      fileName(str):Name of the file to retrieve attributes for.

Returns:

      int
        
    """
    pass
        

def CeSetFileAttributes(filename:'str',newAttributes:'int') -> 'None':
    """
    Changes a file's attributes.

Args:

      filename(str):filename
      newAttributes(int):attributes to set

Returns:

      None
        
    """
    pass
        

def CeGetFileSize() -> 'Any':
    """
    Determines the size of a file.

Args:



Returns:

      Any
        
    """
    pass
        

def CeReadFile(hFile:'Union[int]',bufSize:'int') -> 'str':
    """
    Reads a file from the CE device.

Args:

      hFile(Union[int]):Handle to the file
      bufSize(int):Size of the buffer to create for the read.

Returns:

      str
        
    """
    pass
        

def WriteFile(hFile:'Union[int]',data:'str') -> 'Tuple[int, int]':
    """
    Writes a string to a file

Args:

      hFile(Union[int]):Handle to the file
      data(str):The data to write.Return ValueThe result is a tuple of (errCode, nBytesWritten). errCode will always be zero (until overlapped IO is supported!)

Returns:

      Tuple[int, int]:The data to write.Return ValueThe result is a tuple of (errCode, nBytesWritten). 

errCode will always be zero (until overlapped IO is supported!)

        
    """
    pass
        
CSIDL_BITBUCKET = ...
CSIDL_COMMON_DESKTOPDIRECTORY = ...
CSIDL_COMMON_PROGRAMS = ...
CSIDL_COMMON_STARTMENU = ...
CSIDL_COMMON_STARTUP = ...
CSIDL_CONTROLS = ...
CSIDL_DESKTOP = ...
CSIDL_DESKTOPDIRECTORY = ...
CSIDL_DRIVES = ...
CSIDL_FONTS = ...
CSIDL_NETHOOD = ...
CSIDL_NETWORK = ...
CSIDL_PERSONAL = ...
CSIDL_PRINTERS = ...
CSIDL_PROGRAMS = ...
CSIDL_RECENT = ...
CSIDL_SENDTO = ...
CSIDL_STARTMENU = ...
CSIDL_STARTUP = ...
CSIDL_TEMPLATES = ...