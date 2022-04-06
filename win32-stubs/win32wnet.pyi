__all__=['', 'NCBBuffer', 'Netbios', 'WNetAddConnection2', 'WNetAddConnection3', 'WNetCancelConnection2', 'WNetOpenEnum', 'WNetCloseEnum', 'WNetEnumResource', 'WNetGetUser', 'WNetGetUniversalName', 'WNetGetResourceInformation', 'WNetGetLastError', 'WNetGetResourceParent', 'WNetGetConnection']
import typing
import win32typing
"""A module that exposes the Windows Networking API."""


def NCBBuffer(size:'typing.Any') -> 'typing.Any':
    """
    Creates an NCB buffer of the relevant size.

Args:

      size(typing.Any):The number of bytes to allocate.

Returns:

      typing.Any
        
    """
    pass
        

def Netbios(ncb:'win32typing.NCB') -> 'typing.Any':
    """
    Executes a Netbios call.

Args:

      ncb(win32typing.NCB):The NCB object to use for the call.

Returns:

      typing.Any
        
    """
    pass
        

def WNetAddConnection2(NetResource:'win32typing.PyNETRESOURCE',Password:'typing.Any'=None,UserName:'typing.Any'=None,Flags:'typing.Any'=0) -> 'None':
    """
    Creates a connection to a network resource. The function can redirect 

a local device to the network resource.

Args:

      NetResource(win32typing.PyNETRESOURCE):Describes the network resource for the connection.
      Password(typing.Any):The password to use.  Use None for default credentials.
      UserName(typing.Any):The user name to connect as.  Use None for default credentials.
      Flags(typing.Any):Combination win32netcon.CONNECT_* flagsCommentsThis function also accepts backwards-compatible, positional-only arguments of (dwType, lpLocalName, lpRemoteName[, lpProviderName, Username, Password, flags])Accepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass
        

def WNetAddConnection3(hwnd:'int',NetResource:'win32typing.PyNETRESOURCE',Password:'typing.Any'=None,UserName:'typing.Any'=None,Flags:'typing.Any'=0) -> 'None':
    """
    Creates a connection to a network resource.

Args:

      hwnd(typing.Any):Handle to a parent window.
      NetResource(win32typing.PyNETRESOURCE):Describes the network resource for the connection.
      Password(typing.Any):The password to use.  Use None for default credentials.
      UserName(typing.Any):The user name to connect as.  Use None for default credentials.
      Flags(typing.Any):Combination win32netcon.CONNECT_* flagsCommentsAccepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass
        

def WNetCancelConnection2(name:'str',flags:'typing.Any',force:'typing.Any') -> 'None':
    """
    Closes network connections made by WNetAddConnection2 or 3

Args:

      name(str):Name of existing connection to be closed
      flags(typing.Any):Currently determines if the persisent connection information will be updated as a result of this call.
      force(typing.Any):indicates if the close operation should be forced. (i.e. ignore open files and connections)

Returns:

      None
        
    """
    pass
        

def WNetOpenEnum(scope:'typing.Any',_type:'typing.Any',usage:'typing.Any',resource:'win32typing.PyNETRESOURCE') -> 'int':
    """
    None

Args:

      scope(typing.Any):Specifies the scope of the enumeration.
      _type(typing.Any):Specifies the resource types to enumerate.
      usage(typing.Any):Specifies the resource usage to be enumerated.
      resource(win32typing.PyNETRESOURCE):Python NETRESOURCE object.CommentsSee the Microsoft SDK  for complete information on WNetOpenEnum.Return ValuePyHANDLE representing the Win32 HANDLE for the open resource. This handle will be automatically be closed via win32wnet::WNetCloseEnum, but good style dictates it still be closed manually.

Returns:

      int:Python NETRESOURCE object.Comments

See the Microsoft SDK  for complete information on WNetOpenEnum.
Return ValuePyHANDLE representing the Win32 HANDLE for the open resource. 

This handle will be automatically be closed via win32wnet::WNetCloseEnum, but 

good style dictates it still be closed manually.

        
    """
    pass
        

def WNetCloseEnum(handle:'int') -> 'None':
    """
    None

Args:

      handle(int):The handle to close, as obtained from win32wnet::WNetOpenEnumCommentsYou should perform a WNetClose for each handle returned from win32wnet::WNetOpenEnum.

Returns:

      None
        
    """
    pass
        

def WNetEnumResource(handle:'int',maxExtries:'typing.Any'=64) -> 'typing.List[win32typing.PyNETRESOURCE]':
    """
    Enumerates a list of resources

Args:

      handle(int):A handle to an open Enumeration Object (from win32wnet::WNetOpenEnum)
      maxExtries(typing.Any):The maximum number of entries to return.CommentsSuccessive calls to win32wnet.WNetEnumResource will enumerate starting where the previous call stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is closed and reopened.  This lets you process an enumeration in small chunks (as small as 1 item at a time) and still fully enumerate a network object!Return ValueThe list contains PyNETRESOURCE entries. The total number of PyNETRESOURCE entries will be &lt= number requested (excepting the default behavior of requesting 0, which returns up to 64)

Returns:

      typing.List[win32typing.PyNETRESOURCE]:The maximum number of entries to return.
Comments

Successive calls to win32wnet.WNetEnumResource will enumerate starting where the previous call 

stopped. That is, the enumeration is not reset on successive calls UNLESS the enumeration handle is 

closed and reopened.  This lets you process an enumeration in small chunks (as small as 1 item at a time) 

and still fully enumerate a network object!
Return ValueThe list contains PyNETRESOURCE entries. The total number of PyNETRESOURCE entries will be &lt= number 

requested (excepting the default behavior of requesting 0, which returns up to 64)

        
    """
    pass
        

def WNetGetUser(connection:'str'=None) -> 'str':
    """
    Retrieves the current default user name, or the user name used to establish a 

network connection.

Args:

      connection(str):A string that specifies either the name of a local device that has been redirected to a network resource, or the remote name of a network resource to which a connection has been made without redirecting a local device. If this parameter is None, the system returns the name of the current user for the process.

Returns:

      str
        
    """
    pass
        

def WNetGetUniversalName(localPath:'str',infoLevel:'typing.Any') -> 'typing.Union[str, typing.Any]':
    """
    Takes a drive-based path for a network resource and returns an 

information structure that contains a more universal form of the name.

Args:

      localPath(str):A string that is a drive-based path for a network resource. For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named SAMPLE.DOC in the directory \\WIN32\\EXAMPLES on that share, the drive-based path is H:\\WIN32\\EXAMPLES\\SAMPLE.DOC.
      infoLevel(typing.Any):Specifies the type of structure that the function stores in the buffer pointed to by the lpBuffer parameter. This parameter can be one of the following values.ValueMeaningUNIVERSAL_NAME_INFO_LEVEL (=1)The function returns a simple string with the UNC name.REMOTE_NAME_INFO_LEVEL (=2)The function returns a tuple based in the Win32 REMOTE_NAME_INFO data structure.Return ValueIf the infoLevel parameter is REMOTE_NAME_INFO_LEVEL, the result is a tuple of 3 strings: (UNCName, connectionName, remainingPath)

Returns:

      typing.Union[str, typing.Any]:Specifies the type of structure that the function stores in the 

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
        

def WNetGetResourceInformation(NetResource:'win32typing.PyNETRESOURCE') -> 'typing.Tuple[win32typing.PyNETRESOURCE, typing.Any]':
    """
    Finds the type and provider of a network 

resource

Args:

      NetResource(win32typing.PyNETRESOURCE):Describes a network resource.  lpRemoteName is required, dwType and lpProvider can be supplied if knownReturn ValueReturns a NETRESOURCE and a string containing the trailing part of the remote path

Returns:

      typing.Tuple[win32typing.PyNETRESOURCE, typing.Any]:Describes a network resource.  lpRemoteName 

is required, dwType and lpProvider can be supplied if knownReturn ValueReturns a NETRESOURCE and a string containing the trailing part of the remote path

        
    """
    pass
        

def WNetGetLastError() -> 'typing.Tuple[typing.Any, typing.Any, typing.Any]':
    """
    Retrieves extended error information set by a network provider 

when one of the WNet* functions fails

Args:



Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any]:win32wnet.WNetGetLastError

(int,str,str) = WNetGetLastError()Retrieves extended error information set by a network provider 

when one of the WNet* functions fails
Comments

The error description or the network provider name may be truncated if they exceed 1024 and 256 characters, 

respectively
Return ValueReturns the error code, a text description of the error, and the name of the network provider

        
    """
    pass
        

def WNetGetResourceParent(NetResource:'win32typing.PyNETRESOURCE') -> 'win32typing.PyNETRESOURCE':
    """
    Finds the parent resource of a network resource

Args:

      NetResource(win32typing.PyNETRESOURCE):Describes a network resource.  lpRemoteName and lpProvider are required, dwType is recommended for efficiency

Returns:

      win32typing.PyNETRESOURCE
        
    """
    pass
        

def WNetGetConnection(connection:'str'=None) -> 'str':
    """
    Retrieves the name of the network resource associated with a local 

device.

Args:

      connection(str):A string that is a drive-based path for a network resource. For example, if drive H has been mapped to a network drive share, and the network resource of interest is a file named Sample.doc in the directory \\Win32\\Examples on that share, the drive-based path is H:\\Win32\\Examples\\Sample.doc.

Returns:

      str
        
    """
    pass
        