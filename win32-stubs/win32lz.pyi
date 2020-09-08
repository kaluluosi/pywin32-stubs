__all__=['', 'GetExpandedName', 'Close', 'Copy', 'Init', 'OpenFile']
from typing import *
from win32helper.win32typing import *
"""A module encapsulating the Windows LZ compression routines."""


def GetExpandedName(Source:'str') -> 'str':
    """
    Retrieves the original name of an expanded file,

Args:

      Source(str):Name of a compressed fileWin32 API References

Returns:

      str
        
    """
    pass
        

def Close(handle:'int') -> 'None':
    """
    Closes a handle to an LZ file.

Args:

      handle(int):The handle of the LZ file to close.Win32 API References

Returns:

      None
        
    """
    pass
        

def Copy(hSrc:'int',hDest:'int') -> 'int':
    """
    Copies a source file to a destination file.

Args:

      hSrc(int):The handle of the source file to copy.
      hDest(int):The handle of the destination file.CommentsIf the source file is compressed with the Microsoft File Compression Utility (COMPRESS.EXE), this function creates a decompressed destination file. If the source file is not compressed, this function duplicates the original file.Win32 API References

Returns:

      int
        
    """
    pass
        

def Init(handle:'int') -> 'None':
    """
    Allocates memory for the internal data structures required to decompress files, and then 

creates and initializes them.

Args:

      handle(int):handle of source fileWin32 API References

Returns:

      None
        
    """
    pass
        

def OpenFile(fileName:'str',action:'int') -> 'Tuple[int, tuple]':
    """
    Creates, opens, reopens, or deletes the specified file.

Args:

      fileName(str):Name of file to open
      action(int):Can be one of the wi32con.OF_ constants (OF_CREATE, OF_DELETE, etc)Win32 API References

Returns:

      Tuple[int, tuple]
        
    """
    pass
        