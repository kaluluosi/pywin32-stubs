__all__=['', 'AddCounter', 'AddEnglishCounter', 'RemoveCounter', 'EnumObjectItems', 'EnumObjects', 'OpenQuery', 'CloseQuery', 'MakeCounterPath', 'GetCounterInfo', 'GetFormattedCounterValue', 'CollectQueryData', 'ValidatePath', 'ExpandCounterPath', 'ParseCounterPath', 'ParseInstanceName', 'SetCounterScaleFactor', 'BrowseCounters', 'ConnectMachine', 'LookupPerfIndexByName', 'LookupPerfNameByIndex']
import typing
import win32typing
"""A module, encapsulating the Windows Performance Data Helpers API"""


def AddCounter(hQuery:'typing.Any',path:'str',userData:'typing.Any'=0) -> 'typing.Any':
    """
    Adds a new counter

Args:

      hQuery(typing.Any):Handle to an open query.
      path(str):Full path to the performance data
      userData(typing.Any):User data associated with the counter.CommentsSee also win32pdh::RemoveCounter

Returns:

      typing.Any
        
    """
    pass
        

def AddEnglishCounter(hQuery:'typing.Any',path:'str',userData:'typing.Any'=0) -> 'typing.Any':
    """
    Adds a counter to a query by its English name

Args:

      hQuery(typing.Any):Handle to an open query.
      path(str):Full counter path with standard English names.
      userData(typing.Any):User data associated with the counter.CommentsAvailable on Vista and laterSee also win32pdh::RemoveCounterReturn ValueReturns a handle to the counter

Returns:

      typing.Any:User data associated with the counter.
Comments

Available on Vista and later

See also win32pdh::RemoveCounter
Return ValueReturns a handle to the counter

        
    """
    pass
        

def RemoveCounter(handle:'typing.Any') -> 'None':
    """
    Removes a previously opened counter

Args:

      handle(typing.Any):Handle to an open counter.CommentsSee also win32pdh::AddCounter

Returns:

      None
        
    """
    pass
        

def EnumObjectItems(DataSource:'str',machine:'str',_object:'str',detailLevel:'typing.Any',flags:'typing.Any'=0) -> 'typing.Any':
    """
    Enumerates an object's items

Args:

      DataSource(str):Path of a performance log file, or None for machine counters
      machine(str):The machine to use, or None
      _object(str):The type of object
      detailLevel(typing.Any):The level of data required, win32pdh.PERF_DETAIL_*
      flags(typing.Any):Flags - must be zero

Returns:

      typing.Any
        
    """
    pass
        

def EnumObjects(DataSource:'str',machine:'str',detailLevel:'typing.Any',refresh:'typing.Any'=1) -> 'typing.Any':
    """
    Enumerates objects

Args:

      DataSource(str):Path to a performance log file, or None for machine counters
      machine(str):The machine to use, or None
      detailLevel(typing.Any):The level of data required.
      refresh(typing.Any):Should the list be refreshed.

Returns:

      typing.Any
        
    """
    pass
        

def OpenQuery(DataSource:'typing.Any'=None,userData:'typing.Any'=0) -> 'typing.Any':
    """
    Opens a new query

Args:

      DataSource(typing.Any):Name of a performaance log file, or None for live data
      userData(typing.Any):User data associated with the query.CommentsSee also win32pdh::CloseQuery

Returns:

      typing.Any
        
    """
    pass
        

def CloseQuery(handle:'typing.Any') -> 'None':
    """
    Closes a query

Args:

      handle(typing.Any):Handle to an open query.CommentsSee also win32pdh::OpenQuery

Returns:

      None
        
    """
    pass
        

def MakeCounterPath(elements:'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]',flags:'typing.Any'=0) -> 'None':
    """
    Makes a fully resolved counter path

Args:

      elements(typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]):The elements to use to create the path.
      flags(typing.Any):PDH_PATH_WBEM_RESULT, PDH_PATH_WBEM_INPUT, or 0

Returns:

      None
        
    """
    pass
        

def GetCounterInfo(handle:'typing.Any',bRetrieveExplainText:'typing.Any') -> 'None':
    """
    Retrieves information about a counter, such as data size, counter type, path, and 

user-supplied data values.

Args:

      handle(typing.Any):The handle of the item to query
      bRetrieveExplainText(typing.Any):Should explain text be retrieved?

Returns:

      None
        
    """
    pass
        

def GetFormattedCounterValue(handle:'typing.Any',_format:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves a formatted counter value

Args:

      handle(typing.Any):Handle to the counter
      _format(typing.Any):Format of result.  Can be PDH_FMT_DOUBLE, PDH_FMT_LARGE, PDH_FMT_LONG and or'd with PDH_FMT_NOSCALE, PDH_FMT_1000

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def CollectQueryData(hQuery:'typing.Any') -> 'None':
    """
    Collects the current raw data value for all counters in the specified query and 

updates the status code of each counter.

Args:

      hQuery(typing.Any):Handle to an open query.

Returns:

      None
        
    """
    pass
        

def ValidatePath(path:'str') -> 'typing.Any':
    """
    Validates that the specified counter is present on the machine specified in the 

counter path.

Args:

      path(str):The counter path to validate.CommentsThis method returns an integer result code.  No exception is ever thrown.  Zero result indicates success.

Returns:

      typing.Any
        
    """
    pass
        

def ExpandCounterPath(wildCardPath:'str') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Examines the specified machine (or local machine if none is specified) 

for counters and instances of counters that match the wild card strings in the counter path.

Args:

      wildCardPath(str):The counter path to expand.CommentsThe counter path format is assumed to be: \\machine\\object(parent/instance#index)\\countername and the parent, instance, index, and countername elements may contain either a valid name or a wild card character.The API function leaks memory on Windows XP.

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def ParseCounterPath(path:'str',flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Parses the elements of the counter path.

Args:

      path(str):The counter path to parse.
      flags(typing.Any):Reserved - must be zero.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]
        
    """
    pass
        

def ParseInstanceName(instanceName:'str') -> 'typing.Tuple[typing.Any, typing.Any, typing.Any]':
    """
    Parses the elements of the instance name

Args:

      instanceName(str):The instance name to parse.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any]
        
    """
    pass
        

def SetCounterScaleFactor(hCounter:'typing.Any',factor:'typing.Any') -> 'None':
    """
    Sets the scale factor that is applied to the calculated value of the 

specified counter when you request the formatted counter value.

Args:

      hCounter(typing.Any):Handle to the counter.
      factor(typing.Any):power of ten used to multiply value.

Returns:

      None
        
    """
    pass
        

def BrowseCounters(Flags:'typing.Tuple[typing.Any, ...]',hWndOwner:'int',CallBack:'typing.Any',DefaultDetailLevel:'typing.Any',DialogBoxCaption:'str'=None,InitialPath:'typing.Any'=None,DataSource:'typing.Any'=None,ReturnMultiple:'typing.Any'=False,CallBackArg:'typing.Any'=None) -> 'str':
    """
    Displays the counter browsing dialog box so that the user can select the 

counters to be returned to the caller.

Args:

      Flags(typing.Tuple[typing.Any, ...]):Sequence of boolean flags, or None. All default to False. (bIncludeInstanceIndex, bSingleCounterPerAdd, bSingleCounterPerDialog, bLocalCountersOnly, bWildCardInstances, bHideDetailBox, bInitializePath, bDisableMachineSelection, bIncludeCostlyObjects, bShowObjectBrowser)
      hWndOwner(int):Parent for the dialog.
      CallBack(typing.Any):A callable object to function as the callback.
      DefaultDetailLevel(typing.Any):The default detail level to show on startup in the Detail Level combo box. If the Detail Level combo box is not shown, this is the detail level to use in filtering the displayed performance counters and objects.
      DialogBoxCaption(str):The dialog caption, or None for default.
      InitialPath(typing.Any):Counter to be selected initially, or None for default
      DataSource(typing.Any):Name of a performance log file, or None for live counters
      ReturnMultiple(typing.Any):Return all selected counter paths as a sequence of strings. Previously, this function only returned a single path even when multiple counters were selected.
      CallBackArg(typing.Any):Extra argument to be passed to callback function. For backward compatibility, the callback will only receive a single argument if this is not given.

Returns:

      str
        
    """
    pass
        

def ConnectMachine(machineName:'str') -> 'str':
    """
    connects to the specified machine, and creates and initializes a machine 

entry in the PDH DLL.

Args:

      machineName(str):The machine name.

Returns:

      str
        
    """
    pass
        

def LookupPerfIndexByName(machineName:'str',instanceName:'str') -> 'typing.Any':
    """
    Returns the counter index corresponding to the specified counter name.

Args:

      machineName(str):The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.
      instanceName(str):The full name of the counter.

Returns:

      typing.Any
        
    """
    pass
        

def LookupPerfNameByIndex(machineName:'str',index:'typing.Any') -> 'str':
    """
    Returns the performance object name corresponding to the specified 

index.

Args:

      machineName(str):The name of the machine where the specified counter is located. The machine name can be specified by the DNS name or the IP address.
      index(typing.Any):The index of the performance object.

Returns:

      str
        
    """
    pass
        