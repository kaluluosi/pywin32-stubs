__all__=['GetNamedPipeHandleState', 'SetNamedPipeHandleState', 'ConnectNamedPipe', 'TransactNamedPipe', 'CallNamedPipe', 'CreatePipe', 'FdCreatePipe', 'CreateNamedPipe', 'DisconnectNamedPipe', 'GetOverlappedResult', 'WaitNamedPipe', 'GetNamedPipeInfo', 'PeekNamedPipe', 'GetNamedPipeClientProcessId', 'GetNamedPipeServerProcessId', 'GetNamedPipeClientSessionId', 'GetNamedPipeServerSessionId', 'popen', 'NMPWAIT_NOWAIT', 'NMPWAIT_USE_DEFAULT_WAIT', 'NMPWAIT_WAIT_FOREVER', 'PIPE_ACCESS_DUPLEX', 'PIPE_ACCESS_INBOUND', 'PIPE_ACCESS_OUTBOUND', 'PIPE_NOWAIT', 'PIPE_READMODE_BYTE', 'PIPE_READMODE_MESSAGE', 'PIPE_TYPE_BYTE', 'PIPE_TYPE_MESSAGE', 'PIPE_UNLIMITED_INSTANCES', 'PIPE_WAIT']
from typing import *
from .win32typing import *
"""An interface to the win32 pipe API's"""


def GetNamedPipeHandleState(hPipe:'int',bGetCollectionData:'int'=0) -> 'Tuple[int, int, Union[None, int], Union[None, int], str]':
    """
    Determines the state of the named pipe.

Args:

      hPipe(int):The handle to the pipe.
      bGetCollectionData(int):Determines of the collection data should be returned.  If not, None is returned in their place.

Returns:

      Tuple[int, int, Union[None, int], Union[None, int], str]
        
    """
    pass
        

def SetNamedPipeHandleState(hPipe:'int',Mode:'Union[None, int]',MaxCollectionCount:'Union[None, int]',CollectDataTimeout:'Union[None, int]') -> 'None':
    """
    Sets the state of the named pipe.

Args:

      hPipe(int):The handle to the pipe.
      Mode(Union[None, int]):The pipe read mode.
      MaxCollectionCount(Union[None, int]):Maximum bytes collected before transmission to the server.
      CollectDataTimeout(Union[None, int]):Maximum time to wait, in milliseconds, before transmission to server.

Returns:

      None
        
    """
    pass
        

def ConnectNamedPipe(hPipe:'int',overlapped:'PyOVERLAPPED'=None) -> 'int':
    """
    Connects to a named pipe

Args:

      hPipe(int):The handle to the pipe.
      overlapped(PyOVERLAPPED):An overlapped object to use, else NoneCommentsThe result is zero if the function succeeds.  If the function fails, GetLastError() is called, and if the result is ERROR_IO_PENDING or ERROR_PIPE_CONNECTED (common when passing an overlapped object), this value is returned.  All other error values raise a win32 exception (from which the error code can be extracted)

Returns:

      int
        
    """
    pass
        

def TransactNamedPipe(pipeName:'Any',writeData:'Union[str, Any]',buffer_bufSize:'Union[int, PyOVERLAPPEDReadBuffer]',overlapped:'PyOVERLAPPED'=None) -> 'Union[str, Any]':
    """
    Combines the functions that write a 

message to and read a message from the specified named pipe into a single 

network operation.

Args:

      pipeName(Any):The name of the pipe.
      writeData(Union[str, Any]):The data to write to the pipe.
      buffer_bufSize(Union[int, PyOVERLAPPEDReadBuffer]):Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.
      overlapped(PyOVERLAPPED):An overlapped structure or NoneCommentsThis function is modelled on win32file::ReadFile - for overlapped operations you are expected to provide a buffer which will be filled asynchronously.

Returns:

      Union[str, Any]
        
    """
    pass
        

def CallNamedPipe(pipeName:'Any',data:'str',bufSize:'int',timeOut:'int') -> 'str':
    """
    Opens and performs a transaction on a named pipe.

Args:

      pipeName(Any):The name of the pipe.
      data(str):The data to write.
      bufSize(int):The size of the result buffer to allocate for the read.
      timeOut(int):Specifies the number of milliseconds to wait for the named pipe to be available. In addition to numeric values, the following special values can be specified.ValueMeaningwin32pipe.NMPWAIT_NOWAITDoes not wait for the named pipe. If the named pipe is not available, the function returns an error.win32pipe.NMPWAIT_WAIT_FOREVERWaits indefinitely.win32pipe.NMPWAIT_USE_DEFAULT_WAITUses the default time-out specified in a call to the CreateNamedPipe function.

Returns:

      str
        
    """
    pass
        

def CreatePipe(sa:'PySECURITY_ATTRIBUTES',nSize:'int') -> 'Tuple[int, int]':
    """
    Creates an anonymous pipe, and returns handles to the read and write ends of the pipe

Args:

      sa(PySECURITY_ATTRIBUTES):
      nSize(int):

Returns:

      Tuple[int, int]
        
    """
    pass
        

def FdCreatePipe(sa:'PySECURITY_ATTRIBUTES',nSize:'int',mode:'int') -> 'Tuple[int, int]':
    """
    As CreatePipe but returns file descriptors

Args:

      sa(PySECURITY_ATTRIBUTES):Specifies security and inheritance for the pipe
      nSize(int):Buffer size for pipe.  Use 0 for default size.
      mode(int):O_TEXT or O_BINARY

Returns:

      Tuple[int, int]
        
    """
    pass
        

def CreateNamedPipe(pipeName:'str',openMode:'int',pipeMode:'int',nMaxInstances:'int',nOutBufferSize:'int',nInBufferSize:'int',nDefaultTimeOut:'int',sa:'PySECURITY_ATTRIBUTES') -> 'int':
    """
    Creates an instance of a named pipe and returns a handle for subsequent pipe operations

Args:

      pipeName(str):The name of the pipe
      openMode(int):OpenMode of the pipe
      pipeMode(int):
      nMaxInstances(int):
      nOutBufferSize(int):
      nInBufferSize(int):
      nDefaultTimeOut(int):
      sa(PySECURITY_ATTRIBUTES):

Returns:

      int
        
    """
    pass
        

def DisconnectNamedPipe(hFile:'int') -> 'None':
    """
    Disconnects the server end of a named pipe instance from a client process.

Args:

      hFile(int):The handle to the pipe to disconnect.

Returns:

      None
        
    """
    pass
        

def GetOverlappedResult(hFile:'int',overlapped:'PyOVERLAPPED',bWait:'int') -> 'int':
    """
    Determines the result of the most recent call with an OVERLAPPED object.

Args:

      hFile(int):The handle to the pipe or file
      overlapped(PyOVERLAPPED):The overlapped object to check.
      bWait(int):Indicates if the function should wait for data to become available.CommentsThe result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

Returns:

      int
        
    """
    pass
        

def WaitNamedPipe(pipeName:'str',timeout:'int') -> 'None':
    """
    None

Args:

      pipeName(str):The name of the pipe
      timeout(int):The number of milliseconds the function will wait. instead of a literal value, you can specify one of the following values for the timeout:ValueMeaningNMPWAIT_USE_DEFAULT_WAITThe time-out interval is the default value specified by the server process in the CreateNamedPipe function.NMPWAIT_WAIT_FOREVERThe function does not return until an instance of the named pipe is available

Returns:

      None
        
    """
    pass
        

def GetNamedPipeInfo(hNamedPipe:'int') -> 'Tuple[int, int, int, int]':
    """
    Returns pipe's flags, buffer sizes, and max instances

Args:

      hNamedPipe(int):Handle to a named pipe

Returns:

      Tuple[int, int, int, int]
        
    """
    pass
        

def PeekNamedPipe(hPipe:'int',size:'int') -> 'Tuple[str, int, int]':
    """
    Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.

Args:

      hPipe(int):The handle to the pipe.
      size(int):The size of the buffer.

Returns:

      Tuple[str, int, int]
        
    """
    pass
        

def GetNamedPipeClientProcessId(hPipe:'int') -> 'int':
    """
    Returns the process id of client that is connected to a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass
        

def GetNamedPipeServerProcessId(hPipe:'int') -> 'int':
    """
    Returns pid of server process that created a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass
        

def GetNamedPipeClientSessionId(hPipe:'int') -> 'int':
    """
    Returns the session id of client that is connected to a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass
        

def GetNamedPipeServerSessionId(hPipe:'int') -> 'int':
    """
    Returns session id of server process that created a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass
        

def popen(cmdstring:'str',mode:'str') -> 'Any':
    """
    Popen that works from a GUI.

Args:

      cmdstring(str):The cmdstring to pass to the shell
      mode(str):Either 'r' or 'w'Return ValueThe result of this function is a pipe (file) connected to the processes stdin or stdout, depending on the requested mode.

Returns:

      Any:Either 'r' or 'w'Return ValueThe result of this function is a pipe (file) connected to the 

processes stdin or stdout, depending on the requested mode.

        
    """
    pass
        
NMPWAIT_NOWAIT = ...
NMPWAIT_USE_DEFAULT_WAIT = ...
NMPWAIT_WAIT_FOREVER = ...
PIPE_ACCESS_DUPLEX = ...
PIPE_ACCESS_INBOUND = ...
PIPE_ACCESS_OUTBOUND = ...
PIPE_NOWAIT = ...
PIPE_READMODE_BYTE = ...
PIPE_READMODE_MESSAGE = ...
PIPE_TYPE_BYTE = ...
PIPE_TYPE_MESSAGE = ...
PIPE_UNLIMITED_INSTANCES = ...
PIPE_WAIT = ...