__all__=['', 'ADsOpenObject', 'ADsGetObject', 'ADsBuildEnumerator', 'ADsEnumerateNext', 'ADsGetLastError', 'StringAsDS_SELECTION_LIST', 'DSOP_SCOPE_INIT_INFOs']
from typing import *
from win32helper.win32typing import *
"""A COM interface to ADSI"""


def ADsOpenObject(path:'Any',username:'Any',password:'Any',iid:'PyIID',reserved:'int'=0) -> 'Any':
    """
    Binds to an ADSI object using explicit username and password credentials.

Args:

      path(Any):
      username(Any):
      password(Any):
      iid(PyIID):The requested interface
      reserved(int):

Returns:

      Any
        
    """
    pass
        

def ADsGetObject(path:'Any',iid:'PyIID') -> 'Any':
    """
    Binds to an object given its path and a specified interface identifier (IID).

Args:

      path(Any):
      iid(PyIID):The requested interface

Returns:

      Any
        
    """
    pass
        

def ADsBuildEnumerator(container:'PyIADsContainer') -> 'Any':
    """
    Builds an enumerator object for the specified ADSI container object.

Args:

      container(PyIADsContainer):

Returns:

      Any
        
    """
    pass
        

def ADsEnumerateNext(enum:'Any',num:'int'=1) -> 'Any':
    """
    None

Args:

      enum(Any):The enumerator.
      num(int):Number of items to retrieve.Return ValueThe result is a tuple of Python objects converted from Variants, one for each element returned.  Note that if zero elements are returned, it is not considered an error condition - an empty tuple is simply returned.

Returns:

      Any:Number of items to retrieve.
Return ValueThe result is a tuple of Python objects converted from Variants, 

one for each element returned.  Note that if zero elements are returned, it is not considered 

an error condition - an empty tuple is simply returned.

        
    """
    pass
        

def ADsGetLastError() -> 'Tuple[int, Any, Any]':
    """
    None

Args:



Returns:

      Tuple[int, Any, Any]
        
    """
    pass
        

def StringAsDS_SELECTION_LIST(buf:'str') -> 'Any':
    """
    None

Args:

      buf(str):The raw buffer

Returns:

      Any
        
    """
    pass
        

def DSOP_SCOPE_INIT_INFOs(size:'int') -> 'Any':
    """
    None

Args:

      size(int):The number of PyDSOP_SCOPE_INIT_INFO objects to create in the array.

Returns:

      Any
        
    """
    pass
        