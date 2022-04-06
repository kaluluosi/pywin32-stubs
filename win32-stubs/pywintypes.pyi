__all__=['', 'DosDateTimeToTime', 'Unicode', 'UnicodeFromRaw', 'IsTextUnicode', 'OVERLAPPED', 'IID', 'Time', 'Time', 'CreateGuid', 'ACL', 'SID', 'SECURITY_ATTRIBUTES', 'SECURITY_DESCRIPTOR', 'HANDLE', 'HKEY', 'WAVEFORMATEX']
import typing
import win32typing
"""A module which supports common Windows types."""


def DosDateTimeToTime() -> 'win32typing.PyTime':
    """
    Converts an MS-DOS Date/Time to a standard Time object.

Args:



Returns:

      win32typing.PyTime
        
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
        

def UnicodeFromRaw(_str:'typing.Union[str, typing.Any]') -> 'str':
    """
    Creates a new Unicode object from raw binary data

Args:

      _str(typing.Union[str, typing.Any]):The string containing the binary data.

Returns:

      str
        
    """
    pass
        

def IsTextUnicode(_str:'str',flags:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Determines whether a buffer probably contains a form of Unicode text.

Args:

      _str(str):The string containing the binary data.
      flags(typing.Any):Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. result is nonzero if the data in the buffer passes the specified tests. result is zero if the data in the buffer does not pass the specified tests. In either case, flags contains the results of the specific tests the function applied to make its determination.

Returns:

      typing.Tuple[typing.Any, typing.Any]:Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. 

result is nonzero if the data in the buffer passes the specified tests. 

result is zero if the data in the buffer does not pass the specified tests. 

In either case, flags contains the results of the specific tests the function applied to make its 

determination.

        
    """
    pass
        

def OVERLAPPED() -> 'win32typing.PyOVERLAPPED':
    """
    Creates a new OVERLAPPED object

Args:



Returns:

      win32typing.PyOVERLAPPED
        
    """
    pass
        

def IID(iidString:'typing.Union[str, typing.Any]',is_bytes:'typing.Any'=False) -> 'win32typing.PyIID':
    """
    Creates a new IID object

Args:

      iidString(typing.Union[str, typing.Any]):A string representation of an IID, or a ProgID.
      is_bytes(typing.Any):Indicates if the first param is actually the bytes of an IID structure.

Returns:

      win32typing.PyIID
        
    """
    pass
        

def Time(timeRepr:'typing.Any') -> 'win32typing.PyTime':
    """
    Creates a new time object.

Args:

      timeRepr(typing.Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      win32typing.PyTime
        
    """
    pass
        

def Time(timeRepr:'typing.Any') -> 'win32typing.PyTime':
    """
    Creates a new time object.

Args:

      timeRepr(typing.Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      win32typing.PyTime
        
    """
    pass
        

def CreateGuid() -> 'win32typing.PyIID':
    """
    Creates a new, unique GUIID.

Args:



Returns:

      win32typing.PyIID
        
    """
    pass
        

def ACL(bufSize:'typing.Any'=64) -> 'win32typing.PyACL':
    """
    Creates a new ACL object

Args:

      bufSize(typing.Any):The size for the ACL.

Returns:

      win32typing.PyACL
        
    """
    pass
        

def SID(buffer:'typing.Any',idAuthority:'typing.Any',subAuthorities:'typing.Any',bufSize:'typing.Any'=32) -> 'win32typing.PySID':
    """
    Creates a new SID object

Args:

      buffer(typing.Any):A raw data buffer, assumed to hold the SID data.Alternative Parameters
      idAuthority(typing.Any):The identifier authority.
      subAuthorities(typing.Any):A list of sub authorities.
      bufSize(typing.Any):Size for the SID bufferAlternative Parameters

Returns:

      win32typing.PySID
        
    """
    pass
        

def SECURITY_ATTRIBUTES() -> 'win32typing.PySECURITY_ATTRIBUTES':
    """
    Creates a new SECURITY_ATTRIBUTES object

Args:



Returns:

      win32typing.PySECURITY_ATTRIBUTES
        
    """
    pass
        

def SECURITY_DESCRIPTOR() -> 'win32typing.PySECURITY_DESCRIPTOR':
    """
    Creates a new SECURITY_DESCRIPTOR object

Args:



Returns:

      win32typing.PySECURITY_DESCRIPTOR
        
    """
    pass
        

def HANDLE() -> 'int':
    """
    Creates a new HANDLE object

Args:



Returns:

      int
        
    """
    pass
        

def HKEY() -> 'win32typing.PyHKEY':
    """
    Creates a new HKEY object

Args:



Returns:

      win32typing.PyHKEY
        
    """
    pass
        

def WAVEFORMATEX() -> 'win32typing.PyWAVEFORMATEX':
    """
    Creates a new WAVEFORMATEX object

Args:



Returns:

      win32typing.PyWAVEFORMATEX
        
    """
    pass
        