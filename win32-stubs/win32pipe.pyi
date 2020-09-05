from pywintypes import *
__all__=['GetNamedPipeHandleState', 'SetNamedPipeHandleState', 'ConnectNamedPipe', 'TransactNamedPipe', 'CallNamedPipe', 'CreatePipe', 'FdCreatePipe', 'CreateNamedPipe', 'DisconnectNamedPipe', 'GetOverlappedResult', 'WaitNamedPipe', 'GetNamedPipeInfo', 'PeekNamedPipe', 'GetNamedPipeClientProcessId', 'GetNamedPipeServerProcessId', 'GetNamedPipeClientSessionId', 'GetNamedPipeServerSessionId', 'popen', 'NMPWAIT_NOWAIT', 'NMPWAIT_USE_DEFAULT_WAIT', 'NMPWAIT_WAIT_FOREVER', 'PIPE_ACCESS_DUPLEX', 'PIPE_ACCESS_INBOUND', 'PIPE_ACCESS_OUTBOUND', 'PIPE_NOWAIT', 'PIPE_READMODE_BYTE', 'PIPE_READMODE_MESSAGE', 'PIPE_TYPE_BYTE', 'PIPE_TYPE_MESSAGE', 'PIPE_UNLIMITED_INSTANCES', 'PIPE_WAIT']
import typing
"""An interface to the win32 pipe API's"""


def GetNamedPipeHandleState(hPipe:typing.Any,bGetCollectionData:int=0) -> typing.Any:
    """
    Determines the state of the named pipe.


Args:

      hPipe(typing.Any):The handle to the pipe.
      bGetCollectionData(int):Determines of the collection data should be returned.  If not, None is returned in their place.

Returns:

      typing.Any
        
    """
    pass


def SetNamedPipeHandleState(hPipe:typing.Any,Mode:Union[int,None],MaxCollectionCount:Union[int,None],CollectDataTimeout:Union[int,None]) -> None:
    """
    Sets the state of the named pipe.


Args:

      hPipe(typing.Any):The handle to the pipe.
      Mode(int,None):The pipe read mode.
      MaxCollectionCount(int,None):Maximum bytes collected before transmission to the server.
      CollectDataTimeout(int,None):Maximum time to wait, in milliseconds, before transmission to server.

Returns:

      None
        
    """
    pass


def ConnectNamedPipe(hPipe:typing.Any,overlapped:typing.Any=None) -> int:
    """
    Connects to a named pipe


Args:

      hPipe(typing.Any):The handle to the pipe.
      overlapped(typing.Any):An overlapped object to use, else NoneCommentsThe result is zero if the function succeeds.  If the function fails, GetLastError() is called, and if the result is ERROR_IO_PENDING or ERROR_PIPE_CONNECTED (common when passing an overlapped object), this value is returned.  All other error values raise a win32 exception (from which the error code can be extracted)

Returns:

      int
        
    """
    pass


def TransactNamedPipe(pipeName:typing.Any,writeData:Union[str,typing.Any],buffer/bufSize:typing.Any,overlapped:typing.Any=None) -> typing.Any:
    """
    Combines the functions that write a 

message to and read a message from the specified named pipe into a single 

network operation.


Args:

      pipeName(typing.Any):The name of the pipe.
      writeData(str,typing.Any):The data to write to the pipe.
      buffer/bufSize(typing.Any):Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.
      overlapped(typing.Any):An overlapped structure or NoneCommentsThis function is modelled on win32file::ReadFile - for overlapped operations you are expected to provide a buffer which will be filled asynchronously.

Returns:

      typing.Any
        
    """
    pass


def CallNamedPipe(pipeName:typing.Any,data:str,bufSize:int,timeOut:int) -> str:
    """
    Opens and performs a transaction on a named pipe.


Args:

      pipeName(typing.Any):The name of the pipe.
      data(str):The data to write.
      bufSize(int):The size of the result buffer to allocate for the read.
      timeOut(int):Specifies the number of milliseconds to wait for the named pipe to be available. In addition to numeric values, the following special values can be specified.ValueMeaningwin32pipe.NMPWAIT_NOWAITDoes not wait for the named pipe. If the named pipe is not available, the function returns an error.win32pipe.NMPWAIT_WAIT_FOREVERWaits indefinitely.win32pipe.NMPWAIT_USE_DEFAULT_WAITUses the default time-out specified in a call to the CreateNamedPipe function.

Returns:

      str
        
    """
    pass


def CreatePipe(sa:typing.Any,nSize:int) -> typing.Any:
    """
    Creates an anonymous pipe, and returns handles to the read and write ends of the pipe


Args:

      sa(typing.Any):
      nSize(int):

Returns:

      typing.Any
        
    """
    pass


def FdCreatePipe(sa:typing.Any,nSize:int,mode:int) -> typing.Any:
    """
    As CreatePipe but returns file descriptors


Args:

      sa(typing.Any):Specifies security and inheritance for the pipe
      nSize(int):Buffer size for pipe.  Use 0 for default size.
      mode(int):O_TEXT or O_BINARY

Returns:

      typing.Any
        
    """
    pass


def CreateNamedPipe(pipeName:typing.Any,openMode:int,pipeMode:int,nMaxInstances:int,nOutBufferSize:int,nInBufferSize:int,nDefaultTimeOut:int,sa:typing.Any) -> int:
    """
    Creates an instance of a named pipe and returns a handle for subsequent pipe operations


Args:

      pipeName(typing.Any):The name of the pipe
      openMode(int):OpenMode of the pipe
      pipeMode(int):
      nMaxInstances(int):
      nOutBufferSize(int):
      nInBufferSize(int):
      nDefaultTimeOut(int):
      sa(typing.Any):

Returns:

      int
        
    """
    pass


def DisconnectNamedPipe(hFile:typing.Any) -> None:
    """
    Disconnects the server end of a named pipe instance from a client process.


Args:

      hFile(typing.Any):The handle to the pipe to disconnect.

Returns:

      None
        
    """
    pass


def GetOverlappedResult(hFile:typing.Any,overlapped:typing.Any,bWait:int) -> int:
    """
    Determines the result of the most recent call with an OVERLAPPED object.


Args:

      hFile(typing.Any):The handle to the pipe or file
      overlapped(typing.Any):The overlapped object to check.
      bWait(int):Indicates if the function should wait for data to become available.CommentsThe result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

Returns:

      int
        
    """
    pass


def WaitNamedPipe(pipeName:typing.Any,timeout:int) -> None:
    """
    None


Args:

      pipeName(typing.Any):The name of the pipe
      timeout(int):The number of milliseconds the function will wait. instead of a literal value, you can specify one of the following values for the timeout:ValueMeaningNMPWAIT_USE_DEFAULT_WAITThe time-out interval is the default value specified by the server process in the CreateNamedPipe function.NMPWAIT_WAIT_FOREVERThe function does not return until an instance of the named pipe is available

Returns:

      None
        
    """
    pass


def GetNamedPipeInfo(hNamedPipe:typing.Any) -> typing.Any:
    """
    Returns pipe's flags, buffer sizes, and max instances


Args:

      hNamedPipe(typing.Any):Handle to a named pipe

Returns:

      typing.Any
        
    """
    pass


def PeekNamedPipe(hPipe:typing.Any,size:int) -> typing.Any:
    """
    Copies data from a named or anonymous pipe into a buffer without removing it from the pipe. It also returns information about data in the pipe.


Args:

      hPipe(typing.Any):The handle to the pipe.
      size(int):The size of the buffer.

Returns:

      typing.Any
        
    """
    pass


def GetNamedPipeClientProcessId(hPipe:typing.Any) -> int:
    """
    Returns the process id of client that is connected to a named pipe


Args:

      hPipe(typing.Any):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass


def GetNamedPipeServerProcessId(hPipe:typing.Any) -> int:
    """
    Returns pid of server process that created a named pipe


Args:

      hPipe(typing.Any):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass


def GetNamedPipeClientSessionId(hPipe:typing.Any) -> int:
    """
    Returns the session id of client that is connected to a named pipe


Args:

      hPipe(typing.Any):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass


def GetNamedPipeServerSessionId(hPipe:typing.Any) -> int:
    """
    Returns session id of server process that created a named pipe


Args:

      hPipe(typing.Any):The handle to the pipe.CommentsRequires Vista or later

Returns:

      int
        
    """
    pass


def popen(cmdstring:str,mode:str) -> typing.Any:
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