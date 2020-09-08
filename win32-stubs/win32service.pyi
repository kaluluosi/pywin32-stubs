__all__=['GetThreadDesktop', 'EnumWindowStations', 'GetUserObjectInformation', 'SetUserObjectInformation', 'OpenWindowStation', 'OpenDesktop', 'CreateDesktop', 'OpenInputDesktop', 'GetProcessWindowStation', 'CreateWindowStation', 'EnumServicesStatus', 'EnumServicesStatusEx', 'EnumDependentServices', 'QueryServiceConfig', 'StartService', 'OpenService', 'OpenSCManager', 'CloseServiceHandle', 'QueryServiceStatus', 'QueryServiceStatusEx', 'SetServiceObjectSecurity', 'QueryServiceObjectSecurity', 'GetServiceKeyName', 'GetServiceDisplayName', 'SetServiceStatus', 'ControlService', 'DeleteService', 'CreateService', 'ChangeServiceConfig', 'LockServiceDatabase', 'UnlockServiceDatabase', 'QueryServiceLockStatus', 'ChangeServiceConfig2', 'QueryServiceConfig2', 'DBT_CONFIGCHANGECANCELED', 'DBT_CONFIGCHANGED', 'DBT_CUSTOMEVENT', 'DBT_DEVICEARRIVAL', 'DBT_DEVICEQUERYREMOVE', 'DBT_DEVICEQUERYREMOVEFAILED', 'DBT_DEVICEREMOVECOMPLETE', 'DBT_DEVICEREMOVEPENDING', 'DBT_DEVICETYPESPECIFIC', 'DBT_QUERYCHANGECONFIG', 'DF_ALLOWOTHERACCOUNTHOOK', 'SC_ACTION_NONE', 'SC_ACTION_REBOOT', 'SC_ACTION_RESTART', 'SC_ACTION_RUN_COMMAND', 'SC_ENUM_PROCESS_INFO', 'SC_GROUP_IDENTIFIER', 'SC_MANAGER_ALL_ACCESS', 'SC_MANAGER_CONNECT', 'SC_MANAGER_CREATE_SERVICE', 'SC_MANAGER_ENUMERATE_SERVICE', 'SC_MANAGER_LOCK', 'SC_MANAGER_MODIFY_BOOT_CONFIG', 'SC_MANAGER_QUERY_LOCK_STATUS', 'SERVICE_ACCEPT_HARDWAREPROFILECHANGE', 'SERVICE_ACCEPT_NETBINDCHANGE', 'SERVICE_ACCEPT_PARAMCHANGE', 'SERVICE_ACCEPT_PAUSE_CONTINUE', 'SERVICE_ACCEPT_POWEREVENT', 'SERVICE_ACCEPT_PRESHUTDOWN', 'SERVICE_ACCEPT_SESSIONCHANGE', 'SERVICE_ACCEPT_SHUTDOWN', 'SERVICE_ACCEPT_STOP', 'SERVICE_ACTIVE', 'SERVICE_ALL_ACCESS', 'SERVICE_AUTO_START', 'SERVICE_BOOT_START', 'SERVICE_CHANGE_CONFIG', 'SERVICE_CONFIG_DELAYED_AUTO_START_INFO', 'SERVICE_CONFIG_DESCRIPTION', 'SERVICE_CONFIG_FAILURE_ACTIONS', 'SERVICE_CONFIG_FAILURE_ACTIONS_FLAG', 'SERVICE_CONFIG_PRESHUTDOWN_INFO', 'SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO', 'SERVICE_CONFIG_SERVICE_SID_INFO', 'SERVICE_CONTINUE_PENDING', 'SERVICE_CONTROL_CONTINUE', 'SERVICE_CONTROL_DEVICEEVENT', 'SERVICE_CONTROL_HARDWAREPROFILECHANGE', 'SERVICE_CONTROL_INTERROGATE', 'SERVICE_CONTROL_NETBINDADD', 'SERVICE_CONTROL_NETBINDDISABLE', 'SERVICE_CONTROL_NETBINDENABLE', 'SERVICE_CONTROL_NETBINDREMOVE', 'SERVICE_CONTROL_PARAMCHANGE', 'SERVICE_CONTROL_PAUSE', 'SERVICE_CONTROL_POWEREVENT', 'SERVICE_CONTROL_PRESHUTDOWN', 'SERVICE_CONTROL_SESSIONCHANGE', 'SERVICE_CONTROL_SHUTDOWN', 'SERVICE_CONTROL_STOP', 'SERVICE_DEMAND_START', 'SERVICE_DISABLED', 'SERVICE_DRIVER', 'SERVICE_ENUMERATE_DEPENDENTS', 'SERVICE_ERROR_CRITICAL', 'SERVICE_ERROR_IGNORE', 'SERVICE_ERROR_NORMAL', 'SERVICE_ERROR_SEVERE', 'SERVICE_FILE_SYSTEM_DRIVER', 'SERVICE_INACTIVE', 'SERVICE_INTERACTIVE_PROCESS', 'SERVICE_INTERROGATE', 'SERVICE_KERNEL_DRIVER', 'SERVICE_NO_CHANGE', 'SERVICE_PAUSE_CONTINUE', 'SERVICE_PAUSE_PENDING', 'SERVICE_PAUSED', 'SERVICE_QUERY_CONFIG', 'SERVICE_QUERY_STATUS', 'SERVICE_RUNNING', 'SERVICE_SID_TYPE_NONE', 'SERVICE_SID_TYPE_RESTRICTED', 'SERVICE_SID_TYPE_UNRESTRICTED', 'SERVICE_SPECIFIC_ERROR', 'SERVICE_START', 'SERVICE_START_PENDING', 'SERVICE_STATE_ALL', 'SERVICE_STOP', 'SERVICE_STOP_PENDING', 'SERVICE_STOPPED', 'SERVICE_SYSTEM_START', 'SERVICE_USER_DEFINED_CONTROL', 'SERVICE_WIN32', 'SERVICE_WIN32_OWN_PROCESS', 'SERVICE_WIN32_SHARE_PROCESS', 'UOI_FLAGS', 'UOI_NAME', 'UOI_TYPE', 'UOI_USER_SID', 'WSF_VISIBLE']
from typing import *
from .win32typing import *
"""An interface to the Windows NT Service API"""


def GetThreadDesktop(ThreadId:'int') -> 'PyHDESK':
    """
    Retrieves a handle to the desktop for a thread

Args:

      ThreadId(int):Id of thread

Returns:

      PyHDESK
        
    """
    pass
        

def EnumWindowStations() -> 'Tuple[Tuple[str, Any], ...]':
    """
    Lists names of window stations

Args:



Returns:

      Tuple[Tuple[str, Any], ...]
        
    """
    pass
        

def GetUserObjectInformation(Handle:'int',type:'int') -> 'None':
    """
    Returns specified type of info about a window station or desktop

Args:

      Handle(int):Handle to window station or desktop
      type(int):Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SIDReturn ValueReturn type is dependent on UOI_* constant passed in

Returns:

      None:Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SIDReturn ValueReturn type is dependent on UOI_* constant passed in

        
    """
    pass
        

def SetUserObjectInformation(Handle:'int',info:'Any',type:'int') -> 'None':
    """
    Set specified type of info for a window station or desktop object

Args:

      Handle(int):Handle to window station or desktop
      info(Any):Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct
      type(int):Type of info to set, currently only accepts UOI_FLAGSCommentsCurrently only UOI_FLAGS supported

Returns:

      None
        
    """
    pass
        

def OpenWindowStation(szWinSta:'Union[str, Any]',Inherit:'Any',DesiredAccess:'int') -> 'PyHWINSTA':
    """
    Returns a handle to the specified window station

Args:

      szWinSta(Union[str, Any]):Name of window station
      Inherit(Any):Allow handle to be inherited by subprocesses
      DesiredAccess(int):Bitmask of access types

Returns:

      PyHWINSTA
        
    """
    pass
        

def OpenDesktop(szDesktop:'Union[str, Any]',Flags:'int',Inherit:'bool',DesiredAccess:'int') -> 'PyHDESK':
    """
    Opens a handle to a desktop

Args:

      szDesktop(Union[str, Any]):Name of desktop to open
      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      Inherit(bool):Allow handle to be inherited
      DesiredAccess(int):ACCESS_MASK specifying level of access for handle

Returns:

      PyHDESK
        
    """
    pass
        

def CreateDesktop(Desktop:'Union[str, Any]',Flags:'int',DesiredAccess:'int',SecurityAttributes:'PySECURITY_ATTRIBUTES') -> 'PyHDESK':
    """
    Creates a new desktop in calling process's current window station

Args:

      Desktop(Union[str, Any]):Name of desktop to create
      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      DesiredAccess(int):An ACCESS_MASK determining level of access available thru returned handle
      SecurityAttributes(PySECURITY_ATTRIBUTES):Specifies inheritance and controls access to desktop

Returns:

      PyHDESK
        
    """
    pass
        

def OpenInputDesktop(Flags:'int',Inherit:'bool',DesiredAccess:'int') -> 'PyHDESK':
    """
    Returns a handle to desktop for logged-in user

Args:

      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      Inherit(bool):Specifies if handle will be inheritable
      DesiredAccess(int):ACCESS_MASK specifying access available to returned handle

Returns:

      PyHDESK
        
    """
    pass
        

def GetProcessWindowStation() -> 'PyHWINSTA':
    """
    Returns a handle to calling process's current window station

Args:



Returns:

      PyHWINSTA
        
    """
    pass
        

def CreateWindowStation(WindowStation:'Union[str, Any]',Flags:'int',DesiredAccess:'int',SecurityAttributes:'PySECURITY_ATTRIBUTES') -> 'PyHWINSTA':
    """
    Creates a new window station

Args:

      WindowStation(Union[str, Any]):Name of window station to create, or None
      Flags(int):CWF_CREATE_ONLY or 0
      DesiredAccess(int):Bitmask of access types available to returned handle
      SecurityAttributes(PySECURITY_ATTRIBUTES):Specifies security for window station, and whether handle is inheritableCommentsIf name is None or empty string, name is formatteded from logon id

Returns:

      PyHWINSTA
        
    """
    pass
        

def EnumServicesStatus(hSCManager:'PySC_HANDLE',ServiceType:'int',ServiceState:'int') -> 'Tuple[tuple, ...]':
    """
    Returns a tuple of status info for each service that meets specified criteria

Args:

      hSCManager(PySC_HANDLE):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceType(int):Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)
      ServiceState(int):Limits to services in specified stateReturn ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

Returns:

      Tuple[tuple, ...]:Limits to services in specified state
Return ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

        
    """
    pass
        

def EnumServicesStatusEx(SCManager:'PySC_HANDLE',ServiceType:'int',ServiceState:'int',InfoLevel:'int',GroupName:'str'=None) -> 'Tuple[dict, ...]':
    """
    Lists the status of services that meet the specified criteria

Args:

      SCManager(PySC_HANDLE):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceType(int):Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)
      ServiceState(int):Limits to services in specified state
      InfoLevel(int):Currently SC_ENUM_PROCESS_INFO is only level definedWin32 API References
      GroupName(str):Name of group - use None for all, or '' for services that don't belong to a group

Returns:

      Tuple[dict, ...]:Search for EnumServicesStatusEx at msdn, google or google groups.
Return ValueReturns a sequence of dicts, whose contents depend on information level requested. 

Currently, only information level supported is SC_ENUM_PROCESS_INFO (returns ENUM_SERVICE_STATUS_PROCESS).

        
    """
    pass
        

def EnumDependentServices(hService:'PySC_HANDLE',ServiceState:'int') -> 'Tuple[tuple, ...]':
    """
    Lists services that depend on a service

Args:

      hService(PySC_HANDLE):Handle to service for which to list dependent services (as returned by win32service::OpenService)
      ServiceState(int):Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVEReturn ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

Returns:

      Tuple[tuple, ...]:Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVE
Return ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

        
    """
    pass
        

def QueryServiceConfig(hService:'PySC_HANDLE') -> 'tuple':
    """
    Retrieves configuration parameters for a service

Args:

      hService(PySC_HANDLE):Service handle as returned by win32service::OpenServiceReturn ValueReturns a tuple representing a QUERY_SERVICE_CONFIG struct:Items[0] int : ServiceTypeCombination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants[1] int : StartTypeOne of SERVICE_*_START constants[2] int : ErrorControlOne of SERVICE_ERROR_* constants[3] PyUnicode : BinaryPathNameService's binary executable, can also contain command line args[4] PyUnicode : LoadOrderGroupLoading group that service is a member of[5] int : TagIdOrder of service within its load order group[6] [PyUnicode,...] : DependenciesSequence of names of services on which this service depends[7] PyUnicode : ServiceStartNameAccount name under which service will run[8] PyUnicode : DisplayNameName of service

Returns:

      tuple:Service handle as returned by win32service::OpenServiceReturn ValueReturns a tuple representing a QUERY_SERVICE_CONFIG struct:
Items[0] int : ServiceType
Combination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants
[1] int : StartType
One of SERVICE_*_START constants
[2] int : ErrorControl
One of SERVICE_ERROR_* constants
[3] PyUnicode : BinaryPathName
Service's binary executable, can also contain command line args
[4] PyUnicode : LoadOrderGroup
Loading group that service is a member of
[5] int : TagId
Order of service within its load order group
[6] [PyUnicode,...] : Dependencies
Sequence of names of services on which this service depends
[7] PyUnicode : ServiceStartName
Account name under which service will run
[8] PyUnicode : DisplayName
Name of service

        
    """
    pass
        

def StartService(hService:'PySC_HANDLE',args:'List[str]') -> 'None':
    """
    Starts the specified service

Args:

      hService(PySC_HANDLE):Handle to the service to be started
      args(List[str]):Arguments to the service.

Returns:

      None
        
    """
    pass
        

def OpenService(scHandle:'PySC_HANDLE',name:'str',desiredAccess:'int') -> 'PySC_HANDLE':
    """
    Returns a handle to the specified service.

Args:

      scHandle(PySC_HANDLE):Handle to the Service Control Mananger
      name(str):The name of the service to open.
      desiredAccess(int):The access desired.

Returns:

      PySC_HANDLE
        
    """
    pass
        

def OpenSCManager(machineName:'str',dbName:'str',desiredAccess:'int') -> 'PySC_HANDLE':
    """
    Returns a handle to the service control manager

Args:

      machineName(str):The name of the computer, or None
      dbName(str):The name of the service database, or None
      desiredAccess(int):The access desired. (combination of win32service.SC_MANAGER_* flags)

Returns:

      PySC_HANDLE
        
    """
    pass
        

def CloseServiceHandle(scHandle:'PySC_HANDLE') -> 'None':
    """
    Closes a service or SCM handle

Args:

      scHandle(PySC_HANDLE):Handle to close

Returns:

      None
        
    """
    pass
        

def QueryServiceStatus(hService:'PySC_HANDLE') -> 'SERVICE_STATUS':
    """
    Queries a service status

Args:

      hService(PySC_HANDLE):Handle to service to be queried

Returns:

      SERVICE_STATUS
        
    """
    pass
        

def QueryServiceStatusEx(hService:'PySC_HANDLE') -> 'SERVICE_STATUS':
    """
    Queries a service status

Args:

      hService(PySC_HANDLE):Handle to service to be queried

Returns:

      SERVICE_STATUS
        
    """
    pass
        

def SetServiceObjectSecurity(Handle:'PySC_HANDLE',SecurityInformation:'int',SecurityDescriptor:'PySECURITY_DESCRIPTOR') -> 'None':
    """
    Set the security descriptor for a service

Args:

      Handle(PySC_HANDLE):Service handle
      SecurityInformation(int):Type of infomation to set, combination of values from SECURITY_INFORMATION enum
      SecurityDescriptor(PySECURITY_DESCRIPTOR):PySECURITY_DESCRIPTOR containing infomation to set

Returns:

      None
        
    """
    pass
        

def QueryServiceObjectSecurity(Handle:'PySC_HANDLE',SecurityInformation:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Retrieves information from the security descriptor for a service

Args:

      Handle(PySC_HANDLE):Service handle
      SecurityInformation(int):Type of infomation to retrieve, combination of values from SECURITY_INFORMATION enum

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def GetServiceKeyName(hSCManager:'PySC_HANDLE',DisplayName:'Any') -> 'Any':
    """
    Translates a service display name into its registry key name

Args:

      hSCManager(PySC_HANDLE):Handle to service control manager as returned by win32service::OpenSCManager
      DisplayName(Any):Display name of a service

Returns:

      Any
        
    """
    pass
        

def GetServiceDisplayName(hSCManager:'PySC_HANDLE',ServiceName:'Any') -> 'Any':
    """
    Translates an internal service name into its display name

Args:

      hSCManager(PySC_HANDLE):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceName(Any):Name of service

Returns:

      Any
        
    """
    pass
        

def SetServiceStatus(scHandle:'int',serviceStatus:'SERVICE_STATUS') -> 'None':
    """
    Sets a service status

Args:

      scHandle(int):Handle to set
      serviceStatus(SERVICE_STATUS):The new status

Returns:

      None
        
    """
    pass
        

def ControlService(scHandle:'PySC_HANDLE',code:'int') -> 'SERVICE_STATUS':
    """
    Sends a control message to a service.

Args:

      scHandle(PySC_HANDLE):Handle to control
      code(int):The service control code.Return ValueThe result is the new service status.

Returns:

      SERVICE_STATUS:The service control code.Return ValueThe result is the new service status.

        
    """
    pass
        

def DeleteService(scHandle:'PySC_HANDLE') -> 'None':
    """
    Deletes the specified service

Args:

      scHandle(PySC_HANDLE):Handle to service to be deleted

Returns:

      None
        
    """
    pass
        

def CreateService(scHandle:'PySC_HANDLE',name:'str',displayName:'str',desiredAccess:'int',serviceType:'int',startType:'int',errorControl:'int',binaryFile:'str',loadOrderGroup:'str',bFetchTag:'int',serviceDeps:'List[str]',acctName:'str',password:'str') -> 'Tuple[Union[PySC_HANDLE], int]':
    """
    Creates a new service.

Args:

      scHandle(PySC_HANDLE):handle to service control manager database
      name(str):Name of service
      displayName(str):Display name
      desiredAccess(int):type of access to service
      serviceType(int):type of service
      startType(int):When/how to start service
      errorControl(int):severity if service fails to start
      binaryFile(str):name of binary file
      loadOrderGroup(str):name of load ordering group , or None
      bFetchTag(int):Should the tag be fetched and returned?  If TRUE, the result is a tuple of (handle, tag), otherwise just handle.
      serviceDeps(List[str]):sequence of dependency names
      acctName(str):account name of service, or None
      password(str):password for service account , or None

Returns:

      Tuple[Union[PySC_HANDLE], int]
        
    """
    pass
        

def ChangeServiceConfig(hService:'PySC_HANDLE',serviceType:'int',startType:'int',errorControl:'int',binaryFile:'str',loadOrderGroup:'str',bFetchTag:'int',serviceDeps:'List[str]',acctName:'str',password:'str',displayName:'str') -> 'Union[None, int]':
    """
    Changes the configuration of an existing service.

Args:

      hService(PySC_HANDLE):handle to service to be modified
      serviceType(int):type of service, or SERVICE_NO_CHANGE
      startType(int):When/how to start service, or SERVICE_NO_CHANGE
      errorControl(int):severity if service fails to start, or SERVICE_NO_CHANGE
      binaryFile(str):name of binary file, or None
      loadOrderGroup(str):name of load ordering group , or None
      bFetchTag(int):Should the tag be fetched and returned?  If TRUE, the result is the tag, else None.
      serviceDeps(List[str]):sequence of dependency names
      acctName(str):account name of service, or None
      password(str):password for service account , or None
      displayName(str):Display name

Returns:

      Union[None, int]
        
    """
    pass
        

def LockServiceDatabase(sc_handle:'PySC_HANDLE') -> 'int':
    """
    Locks the service database.

Args:

      sc_handle(PySC_HANDLE):A handle to the SCM.

Returns:

      int
        
    """
    pass
        

def UnlockServiceDatabase(lock:'int') -> 'int':
    """
    Unlocks the service database.

Args:

      lock(int):A lock provided by win32service::LockServiceDatabase

Returns:

      int
        
    """
    pass
        

def QueryServiceLockStatus(hSCManager:'PySC_HANDLE') -> 'Tuple[int, str, int]':
    """
    Retrieves the lock status of the specified service control manager database.

Args:

      hSCManager(PySC_HANDLE):Handle to the SCM.Return ValueThe result is a tuple of (bIsLocked, userName, lockDuration)

Returns:

      Tuple[int, str, int]:Handle to the SCM.Return ValueThe result is a tuple of (bIsLocked, userName, lockDuration)

        
    """
    pass
        

def ChangeServiceConfig2(hService:'PySC_HANDLE',InfoLevel:'int',info:'Any') -> 'None':
    """
    Modifies advanced service parameters

Args:

      hService(PySC_HANDLE):Service handle as returned by win32service::OpenService
      InfoLevel(int):One of win32service.SERVICE_CONFIG_* values
      info(Any):Type depends on InfoLevelInfoLevelInput valueSERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOSequence of unicode strings

Returns:

      None
        
    """
    pass
        

def QueryServiceConfig2(hService:'PySC_HANDLE',InfoLevel:'int') -> 'Any':
    """
    Retrieves advanced service configuration options

Args:

      hService(PySC_HANDLE):Service handle as returned by win32service::OpenService
      InfoLevel(int):One of win32service.SERVICE_CONFIG_* valuesInfoLevelType of value returnedSERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOList of unicode stringsReturn ValueType of returned object depends on InfoLevel

Returns:

      Any:One of win32service.SERVICE_CONFIG_* values


InfoLevel


Type of value returned



SERVICE_CONFIG_DESCRIPTIONUnicode string
SERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS struct
SERVICE_CONFIG_DELAYED_AUTO_START_INFOBoolean
SERVICE_CONFIG_FAILURE_ACTIONS_FLAGBoolean
SERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)
SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOList of unicode strings
Return ValueType of returned object depends on InfoLevel

        
    """
    pass
        
DBT_CONFIGCHANGECANCELED = ...
DBT_CONFIGCHANGED = ...
DBT_CUSTOMEVENT = ...
DBT_DEVICEARRIVAL = ...
DBT_DEVICEQUERYREMOVE = ...
DBT_DEVICEQUERYREMOVEFAILED = ...
DBT_DEVICEREMOVECOMPLETE = ...
DBT_DEVICEREMOVEPENDING = ...
DBT_DEVICETYPESPECIFIC = ...
DBT_QUERYCHANGECONFIG = ...
DF_ALLOWOTHERACCOUNTHOOK = ...
SC_ACTION_NONE = ...
SC_ACTION_REBOOT = ...
SC_ACTION_RESTART = ...
SC_ACTION_RUN_COMMAND = ...
SC_ENUM_PROCESS_INFO = ...
SC_GROUP_IDENTIFIER = ...
SC_MANAGER_ALL_ACCESS = ...
SC_MANAGER_CONNECT = ...
SC_MANAGER_CREATE_SERVICE = ...
SC_MANAGER_ENUMERATE_SERVICE = ...
SC_MANAGER_LOCK = ...
SC_MANAGER_MODIFY_BOOT_CONFIG = ...
SC_MANAGER_QUERY_LOCK_STATUS = ...
SERVICE_ACCEPT_HARDWAREPROFILECHANGE = ...
SERVICE_ACCEPT_NETBINDCHANGE = ...
SERVICE_ACCEPT_PARAMCHANGE = ...
SERVICE_ACCEPT_PAUSE_CONTINUE = ...
SERVICE_ACCEPT_POWEREVENT = ...
SERVICE_ACCEPT_PRESHUTDOWN = ...
SERVICE_ACCEPT_SESSIONCHANGE = ...
SERVICE_ACCEPT_SHUTDOWN = ...
SERVICE_ACCEPT_STOP = ...
SERVICE_ACTIVE = ...
SERVICE_ALL_ACCESS = ...
SERVICE_AUTO_START = ...
SERVICE_BOOT_START = ...
SERVICE_CHANGE_CONFIG = ...
SERVICE_CONFIG_DELAYED_AUTO_START_INFO = ...
SERVICE_CONFIG_DESCRIPTION = ...
SERVICE_CONFIG_FAILURE_ACTIONS = ...
SERVICE_CONFIG_FAILURE_ACTIONS_FLAG = ...
SERVICE_CONFIG_PRESHUTDOWN_INFO = ...
SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO = ...
SERVICE_CONFIG_SERVICE_SID_INFO = ...
SERVICE_CONTINUE_PENDING = ...
SERVICE_CONTROL_CONTINUE = ...
SERVICE_CONTROL_DEVICEEVENT = ...
SERVICE_CONTROL_HARDWAREPROFILECHANGE = ...
SERVICE_CONTROL_INTERROGATE = ...
SERVICE_CONTROL_NETBINDADD = ...
SERVICE_CONTROL_NETBINDDISABLE = ...
SERVICE_CONTROL_NETBINDENABLE = ...
SERVICE_CONTROL_NETBINDREMOVE = ...
SERVICE_CONTROL_PARAMCHANGE = ...
SERVICE_CONTROL_PAUSE = ...
SERVICE_CONTROL_POWEREVENT = ...
SERVICE_CONTROL_PRESHUTDOWN = ...
SERVICE_CONTROL_SESSIONCHANGE = ...
SERVICE_CONTROL_SHUTDOWN = ...
SERVICE_CONTROL_STOP = ...
SERVICE_DEMAND_START = ...
SERVICE_DISABLED = ...
SERVICE_DRIVER = ...
SERVICE_ENUMERATE_DEPENDENTS = ...
SERVICE_ERROR_CRITICAL = ...
SERVICE_ERROR_IGNORE = ...
SERVICE_ERROR_NORMAL = ...
SERVICE_ERROR_SEVERE = ...
SERVICE_FILE_SYSTEM_DRIVER = ...
SERVICE_INACTIVE = ...
SERVICE_INTERACTIVE_PROCESS = ...
SERVICE_INTERROGATE = ...
SERVICE_KERNEL_DRIVER = ...
SERVICE_NO_CHANGE = ...
SERVICE_PAUSE_CONTINUE = ...
SERVICE_PAUSE_PENDING = ...
SERVICE_PAUSED = ...
SERVICE_QUERY_CONFIG = ...
SERVICE_QUERY_STATUS = ...
SERVICE_RUNNING = ...
SERVICE_SID_TYPE_NONE = ...
SERVICE_SID_TYPE_RESTRICTED = ...
SERVICE_SID_TYPE_UNRESTRICTED = ...
SERVICE_SPECIFIC_ERROR = ...
SERVICE_START = ...
SERVICE_START_PENDING = ...
SERVICE_STATE_ALL = ...
SERVICE_STOP = ...
SERVICE_STOP_PENDING = ...
SERVICE_STOPPED = ...
SERVICE_SYSTEM_START = ...
SERVICE_USER_DEFINED_CONTROL = ...
SERVICE_WIN32 = ...
SERVICE_WIN32_OWN_PROCESS = ...
SERVICE_WIN32_SHARE_PROCESS = ...
UOI_FLAGS = ...
UOI_NAME = ...
UOI_TYPE = ...
UOI_USER_SID = ...
WSF_VISIBLE = ...