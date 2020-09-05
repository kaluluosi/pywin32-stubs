from pywintypes import *
__all__=['DosDateTimeToTime', 'Unicode', 'UnicodeFromRaw', 'IsTextUnicode', 'OVERLAPPED', 'IID', 'Time', 'Time', 'CreateGuid', 'ACL', 'SID', 'SECURITY_ATTRIBUTES', 'SECURITY_DESCRIPTOR', 'HANDLE', 'HKEY', 'WAVEFORMATEX']
import typing
"""A module which supports common Windows types."""


def DosDateTimeToTime() -> typing.Any:
    """
    Converts an MS-DOS Date/Time to a standard Time object.


Args:



Returns:

      typing.Any
        
    """
    pass


def Unicode() -> str:
    """
    Creates a new Unicode object


Args:



Returns:

      str
        
    """
    pass


def UnicodeFromRaw(str:Union[str,typing.Any]) -> str:
    """
    Creates a new Unicode object from raw binary data


Args:

      str(str,typing.Any):The string containing the binary data.

Returns:

      str
        
    """
    pass


def IsTextUnicode(str:str,flags:int) -> typing.Any:
    """
    Determines whether a buffer probably contains a form of Unicode text.


Args:

      str(str):The string containing the binary data.
      flags(int):Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. result is nonzero if the data in the buffer passes the specified tests. result is zero if the data in the buffer does not pass the specified tests. In either case, flags contains the results of the specific tests the function applied to make its determination.

Returns:

      typing.Any:Determines the specific tests to makeReturn ValueThe function returns (result, flags), both integers. 

result is nonzero if the data in the buffer passes the specified tests. 

result is zero if the data in the buffer does not pass the specified tests. 

In either case, flags contains the results of the specific tests the function applied to make its 

determination.

        
    """
    pass


def OVERLAPPED() -> typing.Any:
    """
    Creates a new OVERLAPPED object


Args:



Returns:

      typing.Any
        
    """
    pass


def IID(iidString:Union[str,typing.Any],is_bytes:bool=False) -> typing.Any:
    """
    Creates a new IID object


Args:

      iidString(str,typing.Any):A string representation of an IID, or a ProgID.
      is_bytes(bool):Indicates if the first param is actually the bytes of an IID structure.

Returns:

      typing.Any
        
    """
    pass


def Time(timeRepr:typing.Any) -> typing.Any:
    """
    Creates a new time object.


Args:

      timeRepr(typing.Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      typing.Any
        
    """
    pass


def Time(timeRepr:typing.Any) -> typing.Any:
    """
    Creates a new time object.


Args:

      timeRepr(typing.Any):An integer/float/tuple time representation.CommentsNote that the parameter can be any object that supports int(object) - for example , another PyTime object. The integer should be as defined by the Python time module. See the description of the PyTime object for more information.

Returns:

      typing.Any
        
    """
    pass


def CreateGuid() -> typing.Any:
    """
    Creates a new, unique GUIID.


Args:



Returns:

      typing.Any
        
    """
    pass


def ACL(bufSize:int=64) -> typing.Any:
    """
    Creates a new ACL object


Args:

      bufSize(int):The size for the ACL.

Returns:

      typing.Any
        
    """
    pass


def SID(buffer:typing.Any,idAuthority:typing.Any,subAuthorities:typing.Any,bufSize:int=32) -> typing.Any:
    """
    Creates a new SID object


Args:

      buffer(typing.Any):A raw data buffer, assumed to hold the SID data.Alternative Parameters
      idAuthority(typing.Any):The identifier authority.
      subAuthorities(typing.Any):A list of sub authorities.
      bufSize(int):Size for the SID bufferAlternative Parameters

Returns:

      typing.Any
        
    """
    pass


def SECURITY_ATTRIBUTES() -> typing.Any:
    """
    Creates a new SECURITY_ATTRIBUTES object


Args:



Returns:

      typing.Any
        
    """
    pass


def SECURITY_DESCRIPTOR() -> typing.Any:
    """
    Creates a new SECURITY_DESCRIPTOR object


Args:



Returns:

      typing.Any
        
    """
    pass


def HANDLE() -> int:
    """
    Creates a new HANDLE object


Args:



Returns:

      int
        
    """
    pass


def HKEY() -> typing.Any:
    """
    Creates a new HKEY object


Args:



Returns:

      typing.Any
        
    """
    pass


def WAVEFORMATEX() -> typing.Any:
    """
    Creates a new WAVEFORMATEX object


Args:



Returns:

      typing.Any
        
    """
    pass
