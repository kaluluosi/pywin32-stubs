from pywintypes import *
__all__=['NCBBuffer', 'Netbios', 'WNetAddConnection2', 'WNetAddConnection3', 'WNetCancelConnection2', 'WNetOpenEnum', 'WNetCloseEnum', 'WNetEnumResource', 'WNetGetUser', 'WNetGetUniversalName', 'WNetGetResourceInformation', 'WNetGetLastError', 'WNetGetResourceParent', 'WNetGetConnection']
import typing
"""A module that exposes the Windows Networking API."""


def NCBBuffer(size:int) -> typing.Any:
    """
    Creates an NCB buffer of the relevant size.


Args:

      size(int):The number of bytes to allocate.

Returns:

      typing.Any
        
    """
    pass


def Netbios(ncb:typing.Any) -> int:
    """
    Executes a Netbios call.


Args:

      ncb(typing.Any):The NCB object to use for the call.

Returns:

      int
        
    """
    pass


def WNetAddConnection2(NetResource:typing.Any,Password:str=None,UserName:str=None,Flags:int=0) -> None:
    """
    Creates a connection to a network resource. The function can redirect 

a local device to the network resource.


Args:

      NetResource(typing.Any):Describes the network resource for the connection.
      Password(str):The password to use.  Use None for default credentials.
      UserName(str):The user name to connect as.  Use None for default credentials.
      Flags(int):Combination win32netcon.CONNECT_* flagsCommentsThis function also accepts backwards-compatible, positional-only arguments of (dwType, lpLocalName, lpRemoteName[, lpProviderName, Username, Password, flags])Accepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def WNetAddConnection3(hwnd:int,NetResource:typing.Any,Password:str=None,UserName:str=None,Flags:int=0) -> None:
    """
    Creates a connection to a network resource.


Args:

      hwnd(int):Handle to a parent window.
      NetResource(typing.Any):Describes the network resource for the connection.
      Password(str):The password to use.  Use None for default credentials.
      UserName(str):The user name to connect as.  Use None for default credentials.
      Flags(int):Combination win32netcon.CONNECT_* flagsCommentsAccepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def WNetCancelConnection2(name:str,flags:int,force:int) -> None:
    """
    Closes network connections made by WNetAddConnection2 or 3


Args:

      name(str):Name of existing connection to be closed
      flags(int):Currently determines if the persisent connection information will be updated as a result of this call.
      force(int):indicates if the close operation should be forced. (i.e. ignore open files and connections)

Returns:

      None
        
    """
    pass


def WNetOpenEnum(scope:int,type:int,usage:int,resource:typing.Any) -> int:
    """
    None


Args:

      scope(int):Specifies the scope of the enumeration.
      type(int):Specifies the resource types to enumerate.
      usage(int):Specifies the resource usage to be enumerated.
      resource(typing.Any):Python NETRESOURCE object.CommentsSee the Microsoft SDK  for complete information on WNetOpenEnum.Return ValuePyHANDLE representing the Win32 HANDLE for the open resource. This handle will be automatically be closed via win32wnet::WNetCloseEnum, but good style dictates it still be closed manually.

Returns:

      int:Python NETRESOURCE object.Comments

See the Microsoft SDK  for complete information on WNetOpenEnum.
Return ValuePyHANDLE representing the Win32 HANDLE for the open resource. 

This handle will be automatically be closed via win32wnet::WNetCloseEnum, but 

good style dictates it still be closed manually.

        
    """
    pass


def WNetCloseEnum(handle:typing.Any) -> None:
    """
    None


Args:

      handle(typing.Any):The handle to close, as obtained from win32wnet::WNetOpenEnumCommentsYou should perform a WNetClose for each handle returned from win32wnet::WNetOpenEnum.

Returns:

      None
        
    """
    pass


def WNetEnumResource(handle:typing.Any,maxExtries:int=64) -> typing.Any:
    """
    Enumerates a list of resources


Args:

      handle(typing.Any):A handle to an open Enumeration Object (from win32wnet::WNetOpenEnum)
      maxExtries(int):The maximum number of entries to return.CommentsSuccessive calls to win32wnet.WNetEnumResource will enumerate starting where the previous call stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is closed and reopened.  This lets you process an enumeration in small chunks (as small as 1 item at a time) and still fully enumerate a network object!Return ValueThe list contains PyNETRESOURCE entries. The total number of PyNETRESOURCE entries will be &lt= number requested (excepting the default behavior of requesting 0, which returns up to 64)

Returns:

      typing.Any:The maximum number of entries to return.
Comments

Successive calls to win32wnet.WNetEnumResource will enumerate starting where the previous call 

stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is 

closed and reopened.  This lets you process an enumeration in small chunks (as small as 1 item at a time) 

and still fully enumerate a network object!
Return ValueThe list contains PyNETRESOURCE entries. The total number of PyNETRESOURCE entries will be &lt= number 

requested (excepting the default behavior of requesting 0, which returns up to 64)

        
    """
    pass


def WNetGetUser(connection:str=None) -> str:
    """
    Retrieves the current default user name, or the user name used to establish a 

network connection.


Args:

      connection(str):A string that specifies either the name of a local device that has been redirected to a network resource, or the remote name of a network resource to which a connection has been made without redirecting a local device. If this parameter is None, the system returns the name of the current user for the process.

Returns:

      str
        
    """
    pass


def WNetGetUniversalName(localPath:str,infoLevel:int) -> typing.Any:
    """
    Takes a drive-based path for a network resource and returns an 

information structure that contains a more universal form of the name.


Args:

      localPath(str):A string that is a drive-based path for a network resource. For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named SAMPLE.DOC in the directory \\WIN32\\EXAMPLES on that share, the drive-based path is H:\\WIN32\\EXAMPLES\\SAMPLE.DOC.
      infoLevel(int):Specifies the type of structure that the function stores in the buffer pointed to by the lpBuffer parameter. This parameter can be one of the following values.ValueMeaningUNIVERSAL_NAME_INFO_LEVEL (=1)The function returns a simple string with the UNC name.REMOTE_NAME_INFO_LEVEL (=2)The function returns a tuple based in the Win32 REMOTE_NAME_INFO data structure.Return ValueIf the infoLevel parameter is REMOTE_NAME_INFO_LEVEL, the result is a tuple of 3 strings: (UNCName, connectionName, remainingPath)

Returns:

      typing.Any:Specifies the type of structure that the function stores in the 

buffer pointed to by the lpBuffer parameter. This parameter can be one of the following values.



Value


Meaning



UNIVERSAL_NAME_INFO_LEVEL (=1)The function returns a simple string with the UNC name.
REMOTE_NAME_INFO_LEVEL (=2)The function returns a tuple based in the Win32 REMOTE_NAME_INFO data 

structure.
Return ValueIf the infoLevel parameter is REMOTE_NAME_INFO_LEVEL, the result is a tuple of 3 strings: (UNCName, 

connectionName, remainingPath)

        
    """
    pass


def WNetGetResourceInformation(NetResource:typing.Any) -> typing.Any:
    """
    Finds the type and provider of a network 

resource


Args:

      NetResource(typing.Any):Describes a network resource.  lpRemoteName is required, dwType and lpProvider can be supplied if knownReturn ValueReturns a NETRESOURCE and a string containing the trailing part of the remote path

Returns:

      typing.Any:Describes a network resource.  lpRemoteName 

is required, dwType and lpProvider can be supplied if knownReturn ValueReturns a NETRESOURCE and a string containing the trailing part of the remote path

        
    """
    pass


def WNetGetLastError() -> typing.Any:
    """
    Retrieves extended error information set by a network provider 

when one of the WNet* functions fails


Args:



Returns:

      typing.Any:win32wnet.WNetGetLastError

(int,str,str) = WNetGetLastError()Retrieves extended error information set by a network provider 

when one of the WNet* functions fails
Comments

The error description or the network provider name may be truncated if they exceed 1024 and 256 characters, 

respectively
Return ValueReturns the error code, a text description of the error, and the name of the network provider

        
    """
    pass


def WNetGetResourceParent(NetResource:typing.Any) -> typing.Any:
    """
    Finds the parent resource of a network resource


Args:

      NetResource(typing.Any):Describes a network resource.  lpRemoteName and lpProvider are required, dwType is recommended for efficiency

Returns:

      typing.Any
        
    """
    pass


def WNetGetConnection(connection:str=None) -> str:
    """
    Retrieves the name of the network resource associated with a local 

device.


Args:

      connection(str):A string that is a drive-based path for a network resource. For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named Sample.doc in the directory \\Win32\\Examples on that share, the drive-based path is H:\\Win32\\Examples\\Sample.doc.

Returns:

      str
        
    """
    pass
