__all__=['', 'GetNamedPipeHandleState', 'SetNamedPipeHandleState', 'ConnectNamedPipe', 'TransactNamedPipe', 'CallNamedPipe', 'CreatePipe', 'FdCreatePipe', 'CreateNamedPipe', 'DisconnectNamedPipe', 'GetOverlappedResult', 'WaitNamedPipe', 'GetNamedPipeInfo', 'PeekNamedPipe', 'GetNamedPipeClientProcessId', 'GetNamedPipeServerProcessId', 'GetNamedPipeClientSessionId', 'GetNamedPipeServerSessionId', 'popen', 'NMPWAIT_NOWAIT', 'NMPWAIT_USE_DEFAULT_WAIT', 'NMPWAIT_WAIT_FOREVER', 'PIPE_ACCESS_DUPLEX', 'PIPE_ACCESS_INBOUND', 'PIPE_ACCESS_OUTBOUND', 'PIPE_NOWAIT', 'PIPE_READMODE_BYTE', 'PIPE_READMODE_MESSAGE', 'PIPE_TYPE_BYTE', 'PIPE_TYPE_MESSAGE', 'PIPE_UNLIMITED_INSTANCES', 'PIPE_WAIT']
import typing
import win32typing
"""An interface to the win32 pipe API's"""


def GetNamedPipeHandleState(hPipe:'int',bGetCollectionData:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Union[typing.Any], typing.Union[typing.Any], str]':
    """
    Determines the state of the named pipe.

Args:

      hPipe(int):The handle to the pipe.
      bGetCollectionData(typing.Any):Determines of the collection data should be returned.  If not, None is returned in their place.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Union[typing.Any], typing.Union[typing.Any], str]
        
    """
    pass
        

def SetNamedPipeHandleState(hPipe:'int',Mode:'typing.Union[typing.Any]',MaxCollectionCount:'typing.Union[typing.Any]',CollectDataTimeout:'typing.Union[typing.Any]') -> 'None':
    """
    Sets the state of the named pipe.

Args:

      hPipe(int):The handle to the pipe.
      Mode(typing.Union[typing.Any]):The pipe read mode.
      MaxCollectionCount(typing.Union[typing.Any]):Maximum bytes collected before transmission to the server.
      CollectDataTimeout(typing.Union[typing.Any]):Maximum time to wait, in milliseconds, before transmission to server.

Returns:

      None
        
    """
    pass
        

def ConnectNamedPipe(hPipe:'int',overlapped:'win32typing.PyOVERLAPPED'=None) -> 'typing.Any':
    """
    Connects to a named pipe

Args:

      hPipe(int):The handle to the pipe.
      overlapped(win32typing.PyOVERLAPPED):An overlapped object to use, else NoneCommentsThe result is zero if the function succeeds.  If the function fails, GetLastError() is called, and if the result is ERROR_IO_PENDING or ERROR_PIPE_CONNECTED (common when passing an overlapped object), this value is returned.  All other error values raise a win32 exception (from which the error code can be extracted)

Returns:

      typing.Any
        
    """
    pass
        

def TransactNamedPipe(pipeName:'typing.Any',writeData:'typing.Union[str, typing.Any]',buffer_bufSize:'typing.Union[win32typing.PyOVERLAPPEDReadBuffer, typing.Any]',overlapped:'win32typing.PyOVERLAPPED'=None) -> 'typing.Union[str, typing.Any]':
    """
    Combines the functions that write a 

message to and read a message from the specified named pipe into a single 

network operation.

Args:

      pipeName(typing.Any):The name of the pipe.
      writeData(typing.Union[str, typing.Any]):The data to write to the pipe.
      buffer_bufSize(typing.Union[win32typing.PyOVERLAPPEDReadBuffer, typing.Any]):Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.
      overlapped(win32typing.PyOVERLAPPED):An overlapped structure or NoneCommentsThis function is modelled on win32file::ReadFile - for overlapped operations you are expected to provide a buffer which will be filled asynchronously.

Returns:

      typing.Union[str, typing.Any]
        
    """
    pass
        

def CallNamedPipe(pipeName:'typing.Any',data:'str',bufSize:'typing.Any',timeOut:'typing.Any') -> 'str':
    """
    Opens and performs a transaction on a named pipe.

Args:

      pipeName(typing.Any):The name of the pipe.
      data(str):The data to write.
      bufSize(typing.Any):The size of the result buffer to allocate for the read.
      timeOut(typing.Any):Specifies the number of milliseconds to wait for the named pipe to be available. In addition to numeric values, the following special values can be specified.ValueMeaningwin32pipe.NMPWAIT_NOWAITDoes not wait for the named pipe. If the named pipe is not available, the function returns an error.win32pipe.NMPWAIT_WAIT_FOREVERWaits indefinitely.win32pipe.NMPWAIT_USE_DEFAULT_WAITUses the default time-out specified in a call to the CreateNamedPipe function.

Returns:

      str
        
    """
    pass
        

def CreatePipe(sa:'win32typing.PySECURITY_ATTRIBUTES',nSize:'typing.Any') -> 'typing.Tuple[int, int]':
    """
    Creates an anonymous pipe, and returns handles to the read and write ends of the pipe

Args:

      sa(win32typing.PySECURITY_ATTRIBUTES):
      nSize(typing.Any):

Returns:

      typing.Tuple[int, int]
        
    """
    pass
        

def FdCreatePipe(sa:'win32typing.PySECURITY_ATTRIBUTES',nSize:'typing.Any',mode:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    As CreatePipe but returns file descriptors

Args:

      sa(win32typing.PySECURITY_ATTRIBUTES):Specifies security and inheritance for the pipe
      nSize(typing.Any):Buffer size for pipe.  Use 0 for default size.
      mode(typing.Any):O_TEXT or O_BINARY

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def CreateNamedPipe(pipeName:'str',openMode:'typing.Any',pipeMode:'typing.Any',nMaxInstances:'typing.Any',nOutBufferSize:'typing.Any',nInBufferSize:'typing.Any',nDefaultTimeOut:'typing.Any',sa:'win32typing.PySECURITY_ATTRIBUTES') -> 'int':
    """
    Creates an instance of a named pipe and returns a handle for subsequent pipe operations

Args:

      pipeName(str):The name of the pipe
      openMode(typing.Any):OpenMode of the pipe
      pipeMode(typing.Any):
      nMaxInstances(typing.Any):
      nOutBufferSize(typing.Any):
      nInBufferSize(typing.Any):
      nDefaultTimeOut(typing.Any):
      sa(win32typing.PySECURITY_ATTRIBUTES):

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
        

def GetOverlappedResult(hFile:'int',overlapped:'win32typing.PyOVERLAPPED',bWait:'typing.Any') -> 'typing.Any':
    """
    Determines the result of the most recent call with an OVERLAPPED object.

Args:

      hFile(int):The handle to the pipe or file
      overlapped(win32typing.PyOVERLAPPED):The overlapped object to check.
      bWait(typing.Any):Indicates if the function should wait for data to become available.CommentsThe result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

Returns:

      typing.Any
        
    """
    pass
        

def WaitNamedPipe(pipeName:'str',timeout:'typing.Any') -> 'None':
    """
    None

Args:

      pipeName(str):The name of the pipe
      timeout(typing.Any):The number of milliseconds the function will wait. instead of a literal value, you can specify one of the following values for the timeout:ValueMeaningNMPWAIT_USE_DEFAULT_WAITThe time-out interval is the default value specified by the server process in the CreateNamedPipe function.NMPWAIT_WAIT_FOREVERThe function does not return until an instance of the named pipe is available

Returns:

      None
        
    """
    pass
        

def GetNamedPipeInfo(hNamedPipe:'int') -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Returns pipe's flags, buffer sizes, and max instances

Args:

      hNamedPipe(int):Handle to a named pipe

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]
        
    """
    pass
        

def PeekNamedPipe(hPipe:'int',size:'typing.Any') -> 'typing.Tuple[str, typing.Any, typing.Any]':
    """
    Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.

Args:

      hPipe(int):The handle to the pipe.
      size(typing.Any):The size of the buffer.

Returns:

      typing.Tuple[str, typing.Any, typing.Any]
        
    """
    pass
        

def GetNamedPipeClientProcessId(hPipe:'int') -> 'typing.Any':
    """
    Returns the process id of client that is connected to a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      typing.Any
        
    """
    pass
        

def GetNamedPipeServerProcessId(hPipe:'int') -> 'typing.Any':
    """
    Returns pid of server process that created a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      typing.Any
        
    """
    pass
        

def GetNamedPipeClientSessionId(hPipe:'int') -> 'typing.Any':
    """
    Returns the session id of client that is connected to a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      typing.Any
        
    """
    pass
        

def GetNamedPipeServerSessionId(hPipe:'int') -> 'typing.Any':
    """
    Returns session id of server process that created a named pipe

Args:

      hPipe(int):The handle to the pipe.CommentsRequires Vista or later

Returns:

      typing.Any
        
    """
    pass
        

def popen(cmdstring:'str',mode:'str') -> 'typing.Any':
    """
    Popen that works from a GUI.

Args:

      cmdstring(str):The cmdstring to pass to the shell
      mode(str):Either 'r' or 'w'Return ValueThe result of this function is a pipe (file) connected to the processes stdin or stdout, depending on the requested mode.

Returns:

      typing.Any:Either 'r' or 'w'Return ValueThe result of this function is a pipe (file) connected to the 

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
