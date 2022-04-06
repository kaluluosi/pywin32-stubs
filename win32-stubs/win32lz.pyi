__all__=['', 'GetExpandedName', 'Close', 'Copy', 'Init', 'OpenFile']
import typing
import win32typing
"""A module encapsulating the Windows LZ compression routines."""


def GetExpandedName(Source:'typing.Any') -> 'str':
    """
    Retrieves the original name of an expanded file,

Args:

      Source(typing.Any):Name of a compressed fileWin32 API References

Returns:

      str
        
    """
    pass
        

def Close(handle:'typing.Any') -> 'None':
    """
    Closes a handle to an LZ file.

Args:

      handle(typing.Any):The handle of the LZ file to close.Win32 API References

Returns:

      None
        
    """
    pass
        

def Copy(hSrc:'typing.Any',hDest:'typing.Any') -> 'typing.Any':
    """
    Copies a source file to a destination file.

Args:

      hSrc(typing.Any):The handle of the source file to copy.
      hDest(typing.Any):The handle of the destination file.CommentsIf the source file is compressed with the Microsoft File Compression Utility (COMPRESS.EXE), this function creates a decompressed destination file. If the source file is not compressed, this function duplicates the original file.Win32 API References

Returns:

      typing.Any
        
    """
    pass
        

def Init(handle:'typing.Any') -> 'None':
    """
    Allocates memory for the internal data structures required to decompress files, and then 

creates and initializes them.

Args:

      handle(typing.Any):handle of source fileWin32 API References

Returns:

      None
        
    """
    pass
        

def OpenFile(fileName:'str',action:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Creates, opens, reopens, or deletes the specified file.

Args:

      fileName(str):Name of file to open
      action(typing.Any):Can be one of the wi32con.OF_ constants (OF_CREATE, OF_DELETE, etc)Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        