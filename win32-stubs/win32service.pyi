from pywintypes import *
__all__=['GetThreadDesktop', 'EnumWindowStations', 'GetUserObjectInformation', 'SetUserObjectInformation', 'OpenWindowStation', 'OpenDesktop', 'CreateDesktop', 'OpenInputDesktop', 'GetProcessWindowStation', 'CreateWindowStation', 'EnumServicesStatus', 'EnumServicesStatusEx', 'EnumDependentServices', 'QueryServiceConfig', 'StartService', 'OpenService', 'OpenSCManager', 'CloseServiceHandle', 'QueryServiceStatus', 'QueryServiceStatusEx', 'SetServiceObjectSecurity', 'QueryServiceObjectSecurity', 'GetServiceKeyName', 'GetServiceDisplayName', 'SetServiceStatus', 'ControlService', 'DeleteService', 'CreateService', 'ChangeServiceConfig', 'LockServiceDatabase', 'UnlockServiceDatabase', 'QueryServiceLockStatus', 'ChangeServiceConfig2', 'QueryServiceConfig2', 'DBT_CONFIGCHANGECANCELED', 'DBT_CONFIGCHANGED', 'DBT_CUSTOMEVENT', 'DBT_DEVICEARRIVAL', 'DBT_DEVICEQUERYREMOVE', 'DBT_DEVICEQUERYREMOVEFAILED', 'DBT_DEVICEREMOVECOMPLETE', 'DBT_DEVICEREMOVEPENDING', 'DBT_DEVICETYPESPECIFIC', 'DBT_QUERYCHANGECONFIG', 'DF_ALLOWOTHERACCOUNTHOOK', 'SC_ACTION_NONE', 'SC_ACTION_REBOOT', 'SC_ACTION_RESTART', 'SC_ACTION_RUN_COMMAND', 'SC_ENUM_PROCESS_INFO', 'SC_GROUP_IDENTIFIER', 'SC_MANAGER_ALL_ACCESS', 'SC_MANAGER_CONNECT', 'SC_MANAGER_CREATE_SERVICE', 'SC_MANAGER_ENUMERATE_SERVICE', 'SC_MANAGER_LOCK', 'SC_MANAGER_MODIFY_BOOT_CONFIG', 'SC_MANAGER_QUERY_LOCK_STATUS', 'SERVICE_ACCEPT_HARDWAREPROFILECHANGE', 'SERVICE_ACCEPT_NETBINDCHANGE', 'SERVICE_ACCEPT_PARAMCHANGE', 'SERVICE_ACCEPT_PAUSE_CONTINUE', 'SERVICE_ACCEPT_POWEREVENT', 'SERVICE_ACCEPT_PRESHUTDOWN', 'SERVICE_ACCEPT_SESSIONCHANGE', 'SERVICE_ACCEPT_SHUTDOWN', 'SERVICE_ACCEPT_STOP', 'SERVICE_ACTIVE', 'SERVICE_ALL_ACCESS', 'SERVICE_AUTO_START', 'SERVICE_BOOT_START', 'SERVICE_CHANGE_CONFIG', 'SERVICE_CONFIG_DELAYED_AUTO_START_INFO', 'SERVICE_CONFIG_DESCRIPTION', 'SERVICE_CONFIG_FAILURE_ACTIONS', 'SERVICE_CONFIG_FAILURE_ACTIONS_FLAG', 'SERVICE_CONFIG_PRESHUTDOWN_INFO', 'SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFO', 'SERVICE_CONFIG_SERVICE_SID_INFO', 'SERVICE_CONTINUE_PENDING', 'SERVICE_CONTROL_CONTINUE', 'SERVICE_CONTROL_DEVICEEVENT', 'SERVICE_CONTROL_HARDWAREPROFILECHANGE', 'SERVICE_CONTROL_INTERROGATE', 'SERVICE_CONTROL_NETBINDADD', 'SERVICE_CONTROL_NETBINDDISABLE', 'SERVICE_CONTROL_NETBINDENABLE', 'SERVICE_CONTROL_NETBINDREMOVE', 'SERVICE_CONTROL_PARAMCHANGE', 'SERVICE_CONTROL_PAUSE', 'SERVICE_CONTROL_POWEREVENT', 'SERVICE_CONTROL_PRESHUTDOWN', 'SERVICE_CONTROL_SESSIONCHANGE', 'SERVICE_CONTROL_SHUTDOWN', 'SERVICE_CONTROL_STOP', 'SERVICE_DEMAND_START', 'SERVICE_DISABLED', 'SERVICE_DRIVER', 'SERVICE_ENUMERATE_DEPENDENTS', 'SERVICE_ERROR_CRITICAL', 'SERVICE_ERROR_IGNORE', 'SERVICE_ERROR_NORMAL', 'SERVICE_ERROR_SEVERE', 'SERVICE_FILE_SYSTEM_DRIVER', 'SERVICE_INACTIVE', 'SERVICE_INTERACTIVE_PROCESS', 'SERVICE_INTERROGATE', 'SERVICE_KERNEL_DRIVER', 'SERVICE_NO_CHANGE', 'SERVICE_PAUSE_CONTINUE', 'SERVICE_PAUSE_PENDING', 'SERVICE_PAUSED', 'SERVICE_QUERY_CONFIG', 'SERVICE_QUERY_STATUS', 'SERVICE_RUNNING', 'SERVICE_SID_TYPE_NONE', 'SERVICE_SID_TYPE_RESTRICTED', 'SERVICE_SID_TYPE_UNRESTRICTED', 'SERVICE_SPECIFIC_ERROR', 'SERVICE_START', 'SERVICE_START_PENDING', 'SERVICE_STATE_ALL', 'SERVICE_STOP', 'SERVICE_STOP_PENDING', 'SERVICE_STOPPED', 'SERVICE_SYSTEM_START', 'SERVICE_USER_DEFINED_CONTROL', 'SERVICE_WIN32', 'SERVICE_WIN32_OWN_PROCESS', 'SERVICE_WIN32_SHARE_PROCESS', 'UOI_FLAGS', 'UOI_NAME', 'UOI_TYPE', 'UOI_USER_SID', 'WSF_VISIBLE']
import typing
"""An interface to the Windows NT Service API"""


def GetThreadDesktop(ThreadId:int) -> typing.Any:
    """
    Retrieves a handle to the desktop for a thread


Args:

      ThreadId(int):Id of thread

Returns:

      typing.Any
        
    """
    pass


def EnumWindowStations() -> typing.Any:
    """
    Lists names of window stations


Args:



Returns:

      typing.Any
        
    """
    pass


def GetUserObjectInformation(Handle:typing.Any,type:int) -> None:
    """
    Returns specified type of info about a window station or desktop


Args:

      Handle(typing.Any):Handle to window station or desktop
      type(int):Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SIDReturn ValueReturn type is dependent on UOI_* constant passed in

Returns:

      None:Type of info to return, one of UOI_FLAGS,UOI_NAME, UOI_TYPE, or UOI_USER_SIDReturn ValueReturn type is dependent on UOI_* constant passed in

        
    """
    pass


def SetUserObjectInformation(Handle:typing.Any,info:typing.Any,type:int) -> None:
    """
    Set specified type of info for a window station or desktop object


Args:

      Handle(typing.Any):Handle to window station or desktop
      info(typing.Any):Information to set for handle, currently only a dictionary representing USEROBJECTFLAGS struct
      type(int):Type of info to set, currently only accepts UOI_FLAGSCommentsCurrently only UOI_FLAGS supported

Returns:

      None
        
    """
    pass


def OpenWindowStation(szWinSta:Union[str,typing.Any],Inherit:typing.Any,DesiredAccess:int) -> typing.Any:
    """
    Returns a handle to the specified window station


Args:

      szWinSta(str,typing.Any):Name of window station
      Inherit(typing.Any):Allow handle to be inherited by subprocesses
      DesiredAccess(int):Bitmask of access types

Returns:

      typing.Any
        
    """
    pass


def OpenDesktop(szDesktop:Union[str,typing.Any],Flags:int,Inherit:bool,DesiredAccess:int) -> typing.Any:
    """
    Opens a handle to a desktop


Args:

      szDesktop(str,typing.Any):Name of desktop to open
      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      Inherit(bool):Allow handle to be inherited
      DesiredAccess(int):ACCESS_MASK specifying level of access for handle

Returns:

      typing.Any
        
    """
    pass


def CreateDesktop(Desktop:Union[str,typing.Any],Flags:int,DesiredAccess:int,SecurityAttributes:typing.Any) -> typing.Any:
    """
    Creates a new desktop in calling process's current window station


Args:

      Desktop(str,typing.Any):Name of desktop to create
      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      DesiredAccess(int):An ACCESS_MASK determining level of access available thru returned handle
      SecurityAttributes(typing.Any):Specifies inheritance and controls access to desktop

Returns:

      typing.Any
        
    """
    pass


def OpenInputDesktop(Flags:int,Inherit:bool,DesiredAccess:int) -> typing.Any:
    """
    Returns a handle to desktop for logged-in user


Args:

      Flags(int):DF_ALLOWOTHERACCOUNTHOOK or 0
      Inherit(bool):Specifies if handle will be inheritable
      DesiredAccess(int):ACCESS_MASK specifying access available to returned handle

Returns:

      typing.Any
        
    """
    pass


def GetProcessWindowStation() -> typing.Any:
    """
    Returns a handle to calling process's current window station


Args:



Returns:

      typing.Any
        
    """
    pass


def CreateWindowStation(WindowStation:Union[str,typing.Any],Flags:int,DesiredAccess:int,SecurityAttributes:typing.Any) -> typing.Any:
    """
    Creates a new window station


Args:

      WindowStation(str,typing.Any):Name of window station to create, or None
      Flags(int):CWF_CREATE_ONLY or 0
      DesiredAccess(int):Bitmask of access types available to returned handle
      SecurityAttributes(typing.Any):Specifies security for window station, and whether handle is inheritableCommentsIf name is None or empty string, name is formatteded from logon id

Returns:

      typing.Any
        
    """
    pass


def EnumServicesStatus(hSCManager:typing.Any,ServiceType:int,ServiceState:int) -> typing.Any:
    """
    Returns a tuple of status info for each service that meets specified criteria


Args:

      hSCManager(typing.Any):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceType(int):Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)
      ServiceState(int):Limits to services in specified stateReturn ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

Returns:

      typing.Any:Limits to services in specified state
Return ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

        
    """
    pass


def EnumServicesStatusEx(SCManager:typing.Any,ServiceType:int,ServiceState:int,InfoLevel:int,GroupName:str=None) -> typing.Any:
    """
    Lists the status of services that meet the specified criteria


Args:

      SCManager(typing.Any):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceType(int):Types of services to enumerate (SERVICE_DRIVER and/or SERVICE_WIN32)
      ServiceState(int):Limits to services in specified state
      InfoLevel(int):Currently SC_ENUM_PROCESS_INFO is only level definedWin32 API References
      GroupName(str):Name of group - use None for all, or '' for services that don't belong to a group

Returns:

      typing.Any:Search for EnumServicesStatusEx at msdn, google or google groups.
Return ValueReturns a sequence of dicts, whose contents depend on information level requested. 

Currently, only information level supported is SC_ENUM_PROCESS_INFO (returns ENUM_SERVICE_STATUS_PROCESS).

        
    """
    pass


def EnumDependentServices(hService:typing.Any,ServiceState:int) -> typing.Any:
    """
    Lists services that depend on a service


Args:

      hService(typing.Any):Handle to service for which to list dependent services (as returned by win32service::OpenService)
      ServiceState(int):Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVEReturn ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

Returns:

      typing.Any:Limits to services in specified state - One of SERVICE_STATE_ALL, SERVICE_ACTIVE, SERVICE_INACTIVE
Return ValueReturns a sequence of tuples representing ENUM_SERVICE_STATUS structs: (ServiceName, DisplayName, SERVICE_STATUS)

        
    """
    pass


def QueryServiceConfig(hService:typing.Any) -> tuple:
    """
    Retrieves configuration parameters for a service


Args:

      hService(typing.Any):Service handle as returned by win32service::OpenServiceReturn ValueReturns a tuple representing a QUERY_SERVICE_CONFIG struct:Items[0] int : ServiceTypeCombination of SERVICE_*_DRIVER or SERVICE_*_PROCESS constants[1] int : StartTypeOne of SERVICE_*_START constants[2] int : ErrorControlOne of SERVICE_ERROR_* constants[3] PyUnicode : BinaryPathNameService's binary executable, can also contain command line args[4] PyUnicode : LoadOrderGroupLoading group that service is a member of[5] int : TagIdOrder of service within its load order group[6] [PyUnicode,...] : DependenciesSequence of names of services on which this service depends[7] PyUnicode : ServiceStartNameAccount name under which service will run[8] PyUnicode : DisplayNameName of service

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


def StartService(hService:typing.Any,args:typing.Any) -> None:
    """
    Starts the specified service


Args:

      hService(typing.Any):Handle to the service to be started
      args(typing.Any):Arguments to the service.

Returns:

      None
        
    """
    pass


def OpenService(scHandle:typing.Any,name:typing.Any,desiredAccess:int) -> typing.Any:
    """
    Returns a handle to the specified service.


Args:

      scHandle(typing.Any):Handle to the Service Control Mananger
      name(typing.Any):The name of the service to open.
      desiredAccess(int):The access desired.

Returns:

      typing.Any
        
    """
    pass


def OpenSCManager(machineName:typing.Any,dbName:typing.Any,desiredAccess:int) -> typing.Any:
    """
    Returns a handle to the service control manager


Args:

      machineName(typing.Any):The name of the computer, or None
      dbName(typing.Any):The name of the service database, or None
      desiredAccess(int):The access desired. (combination of win32service.SC_MANAGER_* flags)

Returns:

      typing.Any
        
    """
    pass


def CloseServiceHandle(scHandle:typing.Any) -> None:
    """
    Closes a service or SCM handle


Args:

      scHandle(typing.Any):Handle to close

Returns:

      None
        
    """
    pass


def QueryServiceStatus(hService:typing.Any) -> typing.Any:
    """
    Queries a service status


Args:

      hService(typing.Any):Handle to service to be queried

Returns:

      typing.Any
        
    """
    pass


def QueryServiceStatusEx(hService:typing.Any) -> typing.Any:
    """
    Queries a service status


Args:

      hService(typing.Any):Handle to service to be queried

Returns:

      typing.Any
        
    """
    pass


def SetServiceObjectSecurity(Handle:typing.Any,SecurityInformation:int,SecurityDescriptor:typing.Any) -> None:
    """
    Set the security descriptor for a service


Args:

      Handle(typing.Any):Service handle
      SecurityInformation(int):Type of infomation to set, combination of values from SECURITY_INFORMATION enum
      SecurityDescriptor(typing.Any):PySECURITY_DESCRIPTOR containing infomation to set

Returns:

      None
        
    """
    pass


def QueryServiceObjectSecurity(Handle:typing.Any,SecurityInformation:int) -> typing.Any:
    """
    Retrieves information from the security descriptor for a service


Args:

      Handle(typing.Any):Service handle
      SecurityInformation(int):Type of infomation to retrieve, combination of values from SECURITY_INFORMATION enum

Returns:

      typing.Any
        
    """
    pass


def GetServiceKeyName(hSCManager:typing.Any,DisplayName:typing.Any) -> typing.Any:
    """
    Translates a service display name into its registry key name


Args:

      hSCManager(typing.Any):Handle to service control manager as returned by win32service::OpenSCManager
      DisplayName(typing.Any):Display name of a service

Returns:

      typing.Any
        
    """
    pass


def GetServiceDisplayName(hSCManager:typing.Any,ServiceName:typing.Any) -> typing.Any:
    """
    Translates an internal service name into its display name


Args:

      hSCManager(typing.Any):Handle to service control manager as returned by win32service::OpenSCManager
      ServiceName(typing.Any):Name of service

Returns:

      typing.Any
        
    """
    pass


def SetServiceStatus(scHandle:int,serviceStatus:typing.Any) -> None:
    """
    Sets a service status


Args:

      scHandle(int):Handle to set
      serviceStatus(typing.Any):The new status

Returns:

      None
        
    """
    pass


def ControlService(scHandle:typing.Any,code:int) -> typing.Any:
    """
    Sends a control message to a service.


Args:

      scHandle(typing.Any):Handle to control
      code(int):The service control code.Return ValueThe result is the new service status.

Returns:

      typing.Any:The service control code.Return ValueThe result is the new service status.

        
    """
    pass


def DeleteService(scHandle:typing.Any) -> None:
    """
    Deletes the specified service


Args:

      scHandle(typing.Any):Handle to service to be deleted

Returns:

      None
        
    """
    pass


def CreateService(scHandle:typing.Any,name:typing.Any,displayName:typing.Any,desiredAccess:int,serviceType:int,startType:int,errorControl:int,binaryFile:typing.Any,loadOrderGroup:typing.Any,bFetchTag:int,serviceDeps:typing.Any,acctName:typing.Any,password:typing.Any) -> typing.Any:
    """
    Creates a new service.


Args:

      scHandle(typing.Any):handle to service control manager database
      name(typing.Any):Name of service
      displayName(typing.Any):Display name
      desiredAccess(int):type of access to service
      serviceType(int):type of service
      startType(int):When/how to start service
      errorControl(int):severity if service fails to start
      binaryFile(typing.Any):name of binary file
      loadOrderGroup(typing.Any):name of load ordering group , or None
      bFetchTag(int):Should the tag be fetched and returned?  If TRUE, the result is a tuple of (handle, tag), otherwise just handle.
      serviceDeps(typing.Any):sequence of dependency names
      acctName(typing.Any):account name of service, or None
      password(typing.Any):password for service account , or None

Returns:

      typing.Any
        
    """
    pass


def ChangeServiceConfig(hService:typing.Any,serviceType:int,startType:int,errorControl:int,binaryFile:typing.Any,loadOrderGroup:typing.Any,bFetchTag:int,serviceDeps:typing.Any,acctName:typing.Any,password:typing.Any,displayName:typing.Any) -> typing.Any:
    """
    Changes the configuration of an existing service.


Args:

      hService(typing.Any):handle to service to be modified
      serviceType(int):type of service, or SERVICE_NO_CHANGE
      startType(int):When/how to start service, or SERVICE_NO_CHANGE
      errorControl(int):severity if service fails to start, or SERVICE_NO_CHANGE
      binaryFile(typing.Any):name of binary file, or None
      loadOrderGroup(typing.Any):name of load ordering group , or None
      bFetchTag(int):Should the tag be fetched and returned?  If TRUE, the result is the tag, else None.
      serviceDeps(typing.Any):sequence of dependency names
      acctName(typing.Any):account name of service, or None
      password(typing.Any):password for service account , or None
      displayName(typing.Any):Display name

Returns:

      typing.Any
        
    """
    pass


def LockServiceDatabase(sc_handle:typing.Any) -> int:
    """
    Locks the service database.


Args:

      sc_handle(typing.Any):A handle to the SCM.

Returns:

      int
        
    """
    pass


def UnlockServiceDatabase(lock:int) -> int:
    """
    Unlocks the service database.


Args:

      lock(int):A lock provided by win32service::LockServiceDatabase

Returns:

      int
        
    """
    pass


def QueryServiceLockStatus(hSCManager:typing.Any) -> typing.Any:
    """
    Retrieves the lock status of the specified service control manager database.


Args:

      hSCManager(typing.Any):Handle to the SCM.Return ValueThe result is a tuple of (bIsLocked, userName, lockDuration)

Returns:

      typing.Any:Handle to the SCM.Return ValueThe result is a tuple of (bIsLocked, userName, lockDuration)

        
    """
    pass


def ChangeServiceConfig2(hService:typing.Any,InfoLevel:int,info:typing.Any) -> None:
    """
    Modifies advanced service parameters


Args:

      hService(typing.Any):Service handle as returned by win32service::OpenService
      InfoLevel(int):One of win32service.SERVICE_CONFIG_* values
      info(typing.Any):Type depends on InfoLevelInfoLevelInput valueSERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOSequence of unicode strings

Returns:

      None
        
    """
    pass


def QueryServiceConfig2(hService:typing.Any,InfoLevel:int) -> typing.Any:
    """
    Retrieves advanced service configuration options


Args:

      hService(typing.Any):Service handle as returned by win32service::OpenService
      InfoLevel(int):One of win32service.SERVICE_CONFIG_* valuesInfoLevelType of value returnedSERVICE_CONFIG_DESCRIPTIONUnicode stringSERVICE_CONFIG_FAILURE_ACTIONSDict representing a SERVICE_FAILURE_ACTIONS structSERVICE_CONFIG_DELAYED_AUTO_START_INFOBooleanSERVICE_CONFIG_FAILURE_ACTIONS_FLAGBooleanSERVICE_CONFIG_PRESHUTDOWN_INFOint (shutdown timeout in milliseconds)SERVICE_CONFIG_SERVICE_SID_INFOint (SERVICE_SID_TYPE_*)SERVICE_CONFIG_REQUIRED_PRIVILEGES_INFOList of unicode stringsReturn ValueType of returned object depends on InfoLevel

Returns:

      typing.Any:One of win32service.SERVICE_CONFIG_* values


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