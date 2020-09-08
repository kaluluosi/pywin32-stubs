__all__=['', 'DosDateTimeToTime', 'Unicode', 'UnicodeFromRaw', 'IsTextUnicode', 'OVERLAPPED', 'IID', 'Time', 'Time', 'CreateGuid', 'ACL', 'SID', 'SECURITY_ATTRIBUTES', 'SECURITY_DESCRIPTOR', 'HANDLE', 'HKEY', 'WAVEFORMATEX']
from typing import *
from win32helper.win32typing import *
"""A module which supports common Windows types."""


def DosDateTimeToTime() -> 'PyTime':
    """
    Converts an MS-DOS Date/Time to a standard Time object.

Args:



Returns:

      PyTime
        
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
        

def UnicodeFromRaw(_str:'Union[Any, str]') -> 'str':
    """
    Creates a new Unicode object from raw binary data

Args:

      _str(Union[Any, str]):The string containing the binary data.

Returns:

      str
        
    """
    pass
        

def IsTextUnicode(_str:'str',flags:'int') -> 'Tuple[int, int]':
    """
    Determines whether a buffer probably contains a form of Unicode text.

Args:

      _str(str):The string containing the binary data.
      flags(int):Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. result is nonzero if the data in the buffer passes the specified tests. result is zero if the data in the buffer does not pass the specified tests. In either case, flags contains the results of the specific tests the function applied to make its determination.

Returns:

      Tuple[int, int]:Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. 

result is nonzero if the data in the buffer passes the specified tests. 

result is zero if the data in the buffer does not pass the specified tests. 

In either case, flags contains the results of the specific tests the function applied to make its 

determination.

        
    """
    pass
        

def OVERLAPPED() -> 'PyOVERLAPPED':
    """
    Creates a new OVERLAPPED object

Args:



Returns:

      PyOVERLAPPED
        
    """
    pass
        

def IID(iidString:'Union[Any, str]',is_bytes:'bool'=False) -> 'PyIID':
    """
    Creates a new IID object

Args:

      iidString(Union[Any, str]):A string representation of an IID, or a ProgID.
      is_bytes(bool):Indicates if the first param is actually the bytes of an IID structure.

Returns:

      PyIID
        
    """
    pass
        

def Time(timeRepr:'Any') -> 'PyTime':
    """
    Creates a new time object.

Args:

      timeRepr(Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      PyTime
        
    """
    pass
        

def Time(timeRepr:'Any') -> 'PyTime':
    """
    Creates a new time object.

Args:

      timeRepr(Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      PyTime
        
    """
    pass
        

def CreateGuid() -> 'PyIID':
    """
    Creates a new, unique GUIID.

Args:



Returns:

      PyIID
        
    """
    pass
        

def ACL(bufSize:'int'=64) -> 'PyACL':
    """
    Creates a new ACL object

Args:

      bufSize(int):The size for the ACL.

Returns:

      PyACL
        
    """
    pass
        

def SID(buffer:'Any',idAuthority:'Any',subAuthorities:'Any',bufSize:'int'=32) -> 'PySID':
    """
    Creates a new SID object

Args:

      buffer(Any):A raw data buffer, assumed to hold the SID data.Alternative Parameters
      idAuthority(Any):The identifier authority.
      subAuthorities(Any):A list of sub authorities.
      bufSize(int):Size for the SID bufferAlternative Parameters

Returns:

      PySID
        
    """
    pass
        

def SECURITY_ATTRIBUTES() -> 'PySECURITY_ATTRIBUTES':
    """
    Creates a new SECURITY_ATTRIBUTES object

Args:



Returns:

      PySECURITY_ATTRIBUTES
        
    """
    pass
        

def SECURITY_DESCRIPTOR() -> 'PySECURITY_DESCRIPTOR':
    """
    Creates a new SECURITY_DESCRIPTOR object

Args:



Returns:

      PySECURITY_DESCRIPTOR
        
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
        

def HKEY() -> 'PyHKEY':
    """
    Creates a new HKEY object

Args:



Returns:

      PyHKEY
        
    """
    pass
        

def WAVEFORMATEX() -> 'PyWAVEFORMATEX':
    """
    Creates a new WAVEFORMATEX object

Args:



Returns:

      PyWAVEFORMATEX
        
    """
    pass
        