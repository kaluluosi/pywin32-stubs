from pywintypes import *
__all__=['AddCounter', 'AddEnglishCounter', 'RemoveCounter', 'EnumObjectItems', 'EnumObjects', 'OpenQuery', 'CloseQuery', 'MakeCounterPath', 'GetCounterInfo', 'GetFormattedCounterValue', 'CollectQueryData', 'ValidatePath', 'ExpandCounterPath', 'ParseCounterPath', 'ParseInstanceName', 'SetCounterScaleFactor', 'BrowseCounters', 'ConnectMachine', 'LookupPerfIndexByName', 'LookupPerfNameByIndex']
import typing
"""A module, encapsulating the Windows Performance Data Helpers API"""


def AddCounter(hQuery:int,path:str,userData:int=0) -> int:
    """
    Adds a new counter


Args:

      hQuery(int):Handle to an open query.
      path(str):Full path to the performance data
      userData(int):User data associated with the counter.CommentsSee also win32pdh::RemoveCounter

Returns:

      int
        
    """
    pass


def AddEnglishCounter(hQuery:int,path:str,userData:int=0) -> int:
    """
    Adds a counter to a query by its English name


Args:

      hQuery(int):Handle to an open query.
      path(str):Full counter path with standard English names.
      userData(int):User data associated with the counter.CommentsAvailable on Vista and laterSee also win32pdh::RemoveCounterReturn ValueReturns a handle to the counter

Returns:

      int:User data associated with the counter.
Comments

Available on Vista and later

See also win32pdh::RemoveCounter
Return ValueReturns a handle to the counter

        
    """
    pass


def RemoveCounter(handle:int) -> None:
    """
    Removes a previously opened counter


Args:

      handle(int):Handle to an open counter.CommentsSee also win32pdh::AddCounter

Returns:

      None
        
    """
    pass


def EnumObjectItems(DataSource:str,machine:str,object:str,detailLevel:int,flags:int=0) -> tuple:
    """
    Enumerates an object's items


Args:

      DataSource(str):Path of a performance log file, or None for machine counters
      machine(str):The machine to use, or None
      object(str):The type of object
      detailLevel(int):The level of data required, win32pdh.PERF_DETAIL_*
      flags(int):Flags - must be zero

Returns:

      tuple
        
    """
    pass


def EnumObjects(DataSource:str,machine:str,detailLevel:int,refresh:int=1) -> list:
    """
    Enumerates objects


Args:

      DataSource(str):Path to a performance log file, or None for machine counters
      machine(str):The machine to use, or None
      detailLevel(int):The level of data required.
      refresh(int):Should the list be refreshed.

Returns:

      list
        
    """
    pass


def OpenQuery(DataSource:str=None,userData:int=0) -> int:
    """
    Opens a new query


Args:

      DataSource(str):Name of a performaance log file, or None for live data
      userData(int):User data associated with the query.CommentsSee also win32pdh::CloseQuery

Returns:

      int
        
    """
    pass


def CloseQuery(handle:int) -> None:
    """
    Closes a query


Args:

      handle(int):Handle to an open query.CommentsSee also win32pdh::OpenQuery

Returns:

      None
        
    """
    pass


def MakeCounterPath(elements:typing.Any,flags:int=0) -> None:
    """
    Makes a fully resolved counter path


Args:

      elements(typing.Any):The elements to use to create the path.
      flags(int):PDH_PATH_WBEM_RESULT, PDH_PATH_WBEM_INPUT, or 0

Returns:

      None
        
    """
    pass


def GetCounterInfo(handle:int,bRetrieveExplainText:int) -> None:
    """
    Retrieves information about a counter, such as data size, counter type, path, and 

user-supplied data values.


Args:

      handle(int):The handle of the item to query
      bRetrieveExplainText(int):Should explain text be retrieved?

Returns:

      None
        
    """
    pass


def GetFormattedCounterValue(handle:int,format:int) -> typing.Any:
    """
    Retrieves a formatted counter value


Args:

      handle(int):Handle to the counter
      format(int):Format of result.  Can be PDH_FMT_DOUBLE, PDH_FMT_LARGE, PDH_FMT_LONG and or'd with PDH_FMT_NOSCALE, PDH_FMT_1000

Returns:

      typing.Any
        
    """
    pass


def CollectQueryData(hQuery:int) -> None:
    """
    Collects the current raw data value for all counters in the specified query and 

updates the status code of each counter.


Args:

      hQuery(int):Handle to an open query.

Returns:

      None
        
    """
    pass


def ValidatePath(path:str) -> int:
    """
    Validates that the specified counter is present on the machine specified in the 

counter path.


Args:

      path(str):The counter path to validate.CommentsThis method returns an integer result code.  No exception is ever thrown.  Zero result indicates success.

Returns:

      int
        
    """
    pass


def ExpandCounterPath(wildCardPath:str) -> typing.Any:
    """
    Examines the specified machine (or local machine if none is specified) 

for counters and instances of counters that match the wild card strings in the counter path.


Args:

      wildCardPath(str):The counter path to expand.CommentsThe counter path format is assumed to be: \\machine\\object(parent/instance#index)\\countername and the parent, instance, index, and countername elements may contain either a valid name or a wild card character.The API function leaks memory on Windows XP.

Returns:

      typing.Any
        
    """
    pass


def ParseCounterPath(path:str,flags:int=0) -> typing.Any:
    """
    Parses the elements of the counter path.


Args:

      path(str):The counter path to parse.
      flags(int):Reserved - must be zero.

Returns:

      typing.Any
        
    """
    pass


def ParseInstanceName(instanceName:str) -> typing.Any:
    """
    Parses the elements of the instance name


Args:

      instanceName(str):The instance name to parse.

Returns:

      typing.Any
        
    """
    pass


def SetCounterScaleFactor(hCounter:int,factor:int) -> None:
    """
    Sets the scale factor that is applied to the calculated value of the 

specified counter when you request the formatted counter value.


Args:

      hCounter(int):Handle to the counter.
      factor(int):power of ten used to multiply value.

Returns:

      None
        
    """
    pass


def BrowseCounters(Flags:typing.Any,hWndOwner:typing.Any,CallBack:typing.Any,DefaultDetailLevel:int,DialogBoxCaption:str=None,InitialPath:str=None,DataSource:str=None,ReturnMultiple:typing.Any=False,CallBackArg:typing.Any=None) -> str:
    """
    Displays the counter browsing dialog box so that the user can select the 

counters to be returned to the caller.


Args:

      Flags(typing.Any):Sequence of boolean flags, or None. All default to False. (bIncludeInstanceIndex, bSingleCounterPerAdd, bSingleCounterPerDialog, bLocalCountersOnly, bWildCardInstances, bHideDetailBox, bInitializePath, bDisableMachineSelection, bIncludeCostlyObjects, bShowObjectBrowser)
      hWndOwner(typing.Any):Parent for the dialog.
      CallBack(typing.Any):A callable object to function as the callback.
      DefaultDetailLevel(int):The default detail level to show on startup in the Detail Level combo box. If the Detail Level combo box is not shown, this is the detail level to use in filtering the displayed performance counters and objects.
      DialogBoxCaption(str):The dialog caption, or None for default.
      InitialPath(str):Counter to be selected initially, or None for default
      DataSource(str):Name of a performance log file, or None for live counters
      ReturnMultiple(typing.Any):Return all selected counter paths as a sequence of strings. Previously, this function only returned a single path even when multiple counters were selected.
      CallBackArg(typing.Any):Extra argument to be passed to callback function. For backward compatibility, the callback will only receive a single argument if this is not given.

Returns:

      str
        
    """
    pass


def ConnectMachine(machineName:str) -> str:
    """
    connects to the specified machine, and creates and initializes a machine 

entry in the PDH DLL.


Args:

      machineName(str):The machine name.

Returns:

      str
        
    """
    pass


def LookupPerfIndexByName(machineName:str,instanceName:str) -> int:
    """
    Returns the counter index corresponding to the specified counter name.


Args:

      machineName(str):The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.
      instanceName(str):The full name of the counter.

Returns:

      int
        
    """
    pass


def LookupPerfNameByIndex(machineName:str,index:int) -> str:
    """
    Returns the performance object name corresponding to the specified 

index.


Args:

      machineName(str):The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.
      index(int):The index of the performance object.

Returns:

      str
        
    """
    pass
