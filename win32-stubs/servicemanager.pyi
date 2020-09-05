from pywintypes import *
__all__=['CoInitializeEx', 'CoUninitialize', 'RegisterServiceCtrlHandler', 'LogMsg', 'LogInfoMsg', 'LogErrorMsg', 'LogWarningMsg', 'PumpWaitingMessages', 'Debugging', 'Initialize', 'Finalize', 'PrepareToHostSingle', 'PrepareToHostMultiple', 'RunningAsService', 'SetEventSourceName']
import typing
""""""


def CoInitializeEx() -> None:
    """
    Initialize OLE with additional options.


Args:



Returns:

      None
        
    """
    pass


def CoUninitialize() -> None:
    """
    Unitialize OLE


Args:



Returns:

      None
        
    """
    pass


def RegisterServiceCtrlHandler(serviceName:typing.Any,callback:typing.Any,extra_args:bool=False) -> typing.Any:
    """
    Registers the Python service control handler function.


Args:

      serviceName(typing.Any):The name of the service.  This is provided in args[0] of the service class __init__ method.
      callback(typing.Any):The Python function that performs as the control function.  This will be called with an integer status argument.
      extra_args(bool):Is this callback expecting the additional 2 args passed by HandlerEx?Return ValueIf the service manager is in debug mode, this returns None, indicating there is no service control manager handle, otherwise the handle to the Win32 service manager.

Returns:

      typing.Any:Is this callback expecting the additional 2 args passed by HandlerEx?
Return ValueIf the service manager is in debug mode, this returns None, indicating 

there is no service control manager handle, otherwise the handle to the Win32 service manager.

        
    """
    pass


def LogMsg(errorType:int,eventId:int,inserts:typing.Any=None) -> None:
    """
    Logs a specific message


Args:

      errorType(int):
      eventId(int):
      inserts(typing.Any):

Returns:

      None
        
    """
    pass


def LogInfoMsg(msg:typing.Any) -> None:
    """
    Logs a generic informational message to the event log


Args:

      msg(typing.Any):The message to write.

Returns:

      None
        
    """
    pass


def LogErrorMsg(msg:typing.Any) -> None:
    """
    Logs a generic error message to the event log


Args:

      msg(typing.Any):The message to write.

Returns:

      None
        
    """
    pass


def LogWarningMsg(msg:typing.Any) -> None:
    """
    Logs a generic warning message to the event log


Args:

      msg(typing.Any):The message to write.

Returns:

      None
        
    """
    pass


def PumpWaitingMessages() -> int:
    """
    Pumps all waiting messages.


Args:



Returns:

      int:servicemanager.PumpWaitingMessages

int = PumpWaitingMessages()Pumps all waiting messages.
Return ValueReturns 1 if a WM_QUIT message was received, else 0

        
    """
    pass


def Debugging(newVal:int=-1) -> typing.Any:
    """
    Indicates if the service is running in debug mode 

and optionally toggles the debug flag.


Args:

      newVal(int):If not -1, a new value for the debugging flag. The result is the value of the flag before it is changed.

Returns:

      typing.Any
        
    """
    pass


def Initialize(eventSourceName:typing.Any=None,eventSourceFile:typing.Any=None) -> None:
    """
    Initialize the module for hosting a service.  This is generally called 

automatically


Args:

      eventSourceName(typing.Any):The event source name
      eventSourceFile(typing.Any):The name of the file (generally a DLL) with the event source messages.

Returns:

      None
        
    """
    pass


def Finalize() -> None:
    """
    None


Args:



Returns:

      None
        
    """
    pass


def PrepareToHostSingle(klass:typing.Any=None) -> None:
    """
    Prepare for hosting a single service in this EXE


Args:

      klass(typing.Any):The Python class to host.  If not specified, the service name is looked up in the registry and the specified class instantiated.

Returns:

      None
        
    """
    pass


def PrepareToHostMultiple(service_name:Union[str,typing.Any],klass:typing.Any) -> None:
    """
    Prepare for hosting a multiple services in this EXE


Args:

      service_name(str,typing.Any):The name of the service hosted by the class
      klass(typing.Any):The Python class to host.

Returns:

      None
        
    """
    pass


def RunningAsService() -> typing.Any:
    """
    Indicates if the code is 

being executed as a service.


Args:



Returns:

      typing.Any
        
    """
    pass


def SetEventSourceName(sourceName:str,registerNow:bool=False) -> None:
    """
    Sets the event source name 

for event log entries written by the service.


Args:

      sourceName(str):The event source name
      registerNow(bool):If True, the event source name in the registry will be updated immediately. If False, the name will be registered the first time an event log entry is written via any pythonservice methods (or possibly never if no record if written). Note that in some cases, the service itself will not have permission to write the event source in the registry.  Therefore, it would be prudent for your installation program to call this function with registerNow=True, to ensure your services can write useful entries.

Returns:

      None
        
    """
    pass
