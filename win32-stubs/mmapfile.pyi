__all__=['', 'mmapfile']
import typing
from win32helper import win32typing
"""Compiled extension module that provides access to the memory mapped file API"""


def mmapfile(File:'typing.Any',Name:'typing.Any',MaximumSize:'typing.Any'=0,FileOffset:'typing.Any'=0,NumberOfBytesToMap:'typing.Any'=0) -> 'win32typing.Pymmapfile':
    """
    Creates or opens a memory mapped file. 

This method uses the following API functions: CreateFileMapping, MapViewOfFile, VirtualQuery

Args:

      File(typing.Any):Name of file.  Use None or '' when opening an existing named mapping, or to use system pagefile.
      Name(typing.Any):Name of mapping object to create or open, can be None
      MaximumSize(typing.Any):Size of file mapping to create, should be specified as a multiple of system page size (see win32api::GetSystemInfo).  Defaults to size of existing file if 0. If an existing named mapping is opened, the returned object will have the same size as the original mapping.
      FileOffset(typing.Any):Offset into the file at which to create view.  This should be specified as a multiple of system allocation granularity. (see win32api::GetSystemInfo)
      NumberOfBytesToMap(typing.Any):Size of view to create, also a multiple of system page size. If 0, view will span from offset to end of file mapping.CommentsAccepts keyword args.Win32 API References

Returns:

      win32typing.Pymmapfile
        
    """
    pass
        