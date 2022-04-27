__all__=['', 'ADsOpenObject', 'ADsGetObject', 'ADsBuildEnumerator', 'ADsEnumerateNext', 'ADsGetLastError', 'StringAsDS_SELECTION_LIST', 'DSOP_SCOPE_INIT_INFOs']
import typing
import win32typing
"""A COM interface to ADSI"""


def ADsOpenObject(path:'typing.Any',username:'typing.Any',password:'typing.Any',iid:'win32typing.PyIID',reserved:'typing.Any'=0) -> 'typing.Any':
    """
    Binds to an ADSI object using explicit username and password credentials.

Args:

      path(typing.Any):
      username(typing.Any):
      password(typing.Any):
      iid(win32typing.PyIID):The requested interface
      reserved(typing.Any):

Returns:

      typing.Any
        
    """
    pass
        

def ADsGetObject(path:'typing.Any',iid:'win32typing.PyIID') -> 'typing.Any':
    """
    Binds to an object given its path and a specified interface identifier (IID).

Args:

      path(typing.Any):
      iid(win32typing.PyIID):The requested interface

Returns:

      typing.Any
        
    """
    pass
        

def ADsBuildEnumerator(container:'win32typing.PyIADsContainer') -> 'typing.Any':
    """
    Builds an enumerator object for the specified ADSI container object.

Args:

      container(win32typing.PyIADsContainer):

Returns:

      typing.Any
        
    """
    pass
        

def ADsEnumerateNext(enum:'typing.Any',num:'typing.Any'=1) -> 'typing.Any':
    """
    None

Args:

      enum(typing.Any):The enumerator.
      num(typing.Any):Number of items to retrieve.Return ValueThe result is a tuple of Python objects converted from Variants, one for each element returned.  Note that if zero elements are returned, it is not considered an error condition - an empty tuple is simply returned.

Returns:

      typing.Any:Number of items to retrieve.
Return ValueThe result is a tuple of Python objects converted from Variants, 

one for each element returned.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned.

        
    """
    pass
        

def ADsGetLastError() -> 'typing.Tuple[typing.Any, typing.Any, typing.Any]':
    """
    None

Args:



Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any]
        
    """
    pass
        

def StringAsDS_SELECTION_LIST(buf:'typing.Any') -> 'typing.Any':
    """
    None

Args:

      buf(typing.Any):The raw buffer

Returns:

      typing.Any
        
    """
    pass
        

def DSOP_SCOPE_INIT_INFOs(size:'typing.Any') -> 'typing.Any':
    """
    None

Args:

      size(typing.Any):The number of PyDSOP_SCOPE_INIT_INFO objects to create in the array.

Returns:

      typing.Any
        
    """
    pass
        