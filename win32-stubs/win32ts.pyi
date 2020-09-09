__all__=['', 'WTSOpenServer', 'WTSCloseServer', 'WTSQueryUserConfig', 'WTSSetUserConfig', 'WTSEnumerateServers', 'WTSEnumerateSessions', 'WTSLogoffSession', 'WTSDisconnectSession', 'WTSQuerySessionInformation', 'WTSEnumerateProcesses', 'WTSQueryUserToken', 'WTSShutdownSystem', 'WTSTerminateProcess', 'ProcessIdToSessionId', 'WTSGetActiveConsoleSessionId', 'WTSRegisterSessionNotification', 'WTSUnRegisterSessionNotification', 'WTSWaitSystemEvent', 'WTSSendMessage']
import typing
from win32helper import win32typing
"""Interface to the Terminal Services Api 

All functions in this module accept keyword arguments"""


def WTSOpenServer(ServerName:'str') -> 'int':
    """
    Opens a handle to a terminal server

Args:

      ServerName(str):Name ot terminal server to be opened

Returns:

      int
        
    """
    pass
        

def WTSCloseServer(Server:'int') -> 'None':
    """
    Closes a terminal server handle

Args:

      Server(int):Terminal Server handle

Returns:

      None
        
    """
    pass
        

def WTSQueryUserConfig(ServerName:'str',UserName:'str',ConfigClass:'typing.Any') -> 'typing.Any':
    """
    Returns user configuration

Args:

      ServerName(str):Name ot terminal server
      UserName(str):Name of user
      ConfigClass(typing.Any):Type of information to be returned, win32ts.WTSUserConfig*ConfigClassReturned valueWTSUserConfigInitialProgramUnicode string, program to be run when user logs onWTSUserConfigWorkingDirectoryUnicode string, working dir for initial programWTSUserConfigModemCallbackPhoneNumberUnicode stringWTSUserConfigTerminalServerProfilePathUnicode stringWTSUserConfigTerminalServerHomeDirUnicode stringWTSUserConfigTerminalServerHomeDirDriveUnicode stringWTSUserConfigfInheritInitialProgramIntWTSUserConfigfAllowLogonTerminalServerInt, 1 if user can log on thru Terminal ServiceWTSUserConfigTimeoutSettingsConnectionsInt, max connection time (ms)WTSUserConfigTimeoutSettingsDisconnectionsIntWTSUserConfigTimeoutSettingsIdleInt, max idle time (ms)WTSUserConfigfDeviceClientDrivesIntWTSUserConfigfDeviceClientPrintersIntWTSUserConfigfDeviceClientDefaultPrinterIntWTSUserConfigBrokenTimeoutSettingsIntWTSUserConfigReconnectSettingsIntWTSUserConfigModemCallbackSettingsIntWTSUserConfigShadowingSettingsInt, indicates if user's session my be monitoredWTSUserConfigfTerminalServerRemoteHomeDirInt,Return ValueThe type of the returned value is dependent on the config class requested

Returns:

      typing.Any:Type of information to be returned, win32ts.WTSUserConfig*


ConfigClass


Returned value



WTSUserConfigInitialProgramUnicode string, program to be 

run when user logs on
WTSUserConfigWorkingDirectoryUnicode string, working dir 

for initial program
WTSUserConfigModemCallbackPhoneNumberUnicode 

string
WTSUserConfigTerminalServerProfilePathUnicode 

string
WTSUserConfigTerminalServerHomeDirUnicode string
WTSUserConfigTerminalServerHomeDirDriveUnicode 

string
WTSUserConfigfInheritInitialProgramInt
WTSUserConfigfAllowLogonTerminalServerInt, 1 if 

user can log on thru Terminal Service
WTSUserConfigTimeoutSettingsConnectionsInt, 

max connection time (ms)
WTSUserConfigTimeoutSettingsDisconnectionsInt
WTSUserConfigTimeoutSettingsIdleInt, max idle time 

(ms)
WTSUserConfigfDeviceClientDrivesInt
WTSUserConfigfDeviceClientPrintersInt
WTSUserConfigfDeviceClientDefaultPrinterInt
WTSUserConfigBrokenTimeoutSettingsInt
WTSUserConfigReconnectSettingsInt
WTSUserConfigModemCallbackSettingsInt
WTSUserConfigShadowingSettingsInt, indicates if user's 

session my be monitored
WTSUserConfigfTerminalServerRemoteHomeDirInt,
Return ValueThe type of the returned value is dependent on the config class requested

        
    """
    pass
        

def WTSSetUserConfig(ServerName:'str',UserName:'str',ConfigClass:'typing.Any') -> 'None':
    """
    Changes user configuration

Args:

      ServerName(str):Name ot terminal server
      UserName(str):Name of user
      ConfigClass(typing.Any):Type of information to be set, win32ts.WTSUserConfig*ConfigClassType of data requiredWTSUserConfigInitialProgramUnicode string, program to be run when user logs onWTSUserConfigWorkingDirectoryUnicode string, working dir for initial programWTSUserConfigModemCallbackPhoneNumberUnicode stringWTSUserConfigTerminalServerProfilePathUnicode stringWTSUserConfigTerminalServerHomeDirUnicode stringWTSUserConfigTerminalServerHomeDirDriveUnicode stringWTSUserConfigfInheritInitialProgramIntWTSUserConfigfAllowLogonTerminalServerInt, 1 if user can log on thru Terminal ServiceWTSUserConfigTimeoutSettingsConnectionsInt, max connection time (ms)WTSUserConfigTimeoutSettingsDisconnectionsIntWTSUserConfigTimeoutSettingsIdleInt, max idle time (ms)WTSUserConfigfDeviceClientDrivesIntWTSUserConfigfDeviceClientPrintersIntWTSUserConfigfDeviceClientDefaultPrinterIntWTSUserConfigBrokenTimeoutSettingsIntWTSUserConfigReconnectSettingsIntWTSUserConfigModemCallbackSettingsIntWTSUserConfigShadowingSettingsInt, indicates if user's session my be monitoredWTSUserConfigfTerminalServerRemoteHomeDirInt,

Returns:

      None
        
    """
    pass
        

def WTSEnumerateServers(DomainName:'str'=None,Version:'typing.Any'=1,Reserved:'typing.Any'=0) -> 'typing.Tuple[str, ...]':
    """
    Lists terminal servers in a domain

Args:

      DomainName(str):Use None for current domain
      Version(typing.Any):Version of request, currently 1 is only valid value
      Reserved(typing.Any):Reserved, use 0 if passed in

Returns:

      typing.Tuple[str, ...]
        
    """
    pass
        

def WTSEnumerateSessions(Server:'int',Version:'typing.Any'=1,Reserved:'typing.Any'=0) -> 'typing.Tuple[typing.Any, ...]':
    """
    Lists sessions on a server

Args:

      Server(int):Handle to a terminal server
      Version(typing.Any):Version of request, currently 1 is only valid value
      Reserved(typing.Any):Reserved, use 0 if passed inReturn ValueReturns a sequence of dictionaries representing WTS_SESSION_INFO structs, containing {SessionId:int, WinStationName:str, State:int}

Returns:

      typing.Tuple[typing.Any, ...]:Reserved, use 0 if passed in
Return ValueReturns a sequence of dictionaries representing WTS_SESSION_INFO structs, containing {SessionId:int, 

WinStationName:str, State:int}

        
    """
    pass
        

def WTSLogoffSession(Server:'int',SessionId:'typing.Any',Wait:'typing.Any') -> 'None':
    """
    Logs off a user logged in through Terminal Services

Args:

      Server(int):Handle to a terminal server
      SessionId(typing.Any):Terminal services session id as returned by win32ts::WTSEnumerateSessions
      Wait(typing.Any):Indicates whether operation should be performed asynchronously

Returns:

      None
        
    """
    pass
        

def WTSDisconnectSession(Server:'int',SessionId:'typing.Any',Wait:'typing.Any') -> 'None':
    """
    Disconnects a session without logging it off

Args:

      Server(int):Handle to a terminal server
      SessionId(typing.Any):Terminal services session id as returned by win32ts::WTSEnumerateSessions
      Wait(typing.Any):Indicates whether operation should be performed asynchronously

Returns:

      None
        
    """
    pass
        

def WTSQuerySessionInformation(Server:'int',SessionId:'typing.Any',WTSInfoClass:'typing.Any') -> 'None':
    """
    Returns information about a terminal services session

Args:

      Server(int):Handle to a terminal server as returned by win32ts::WTSOpenServer
      SessionId(typing.Any):Terminal services session id as returned by win32ts::WTSEnumerateSessions
      WTSInfoClass(typing.Any):Type of information requested, from WTS_INFO_CLASS enumInfoClassReturned valueWTSApplicationNameUnicode stringWTSClientDirectoryUnicode stringWTSClientNameUnicode stringWTSDomainNameUnicode stringWTSInitialProgramUnicode stringWTSOEMIdUnicode stringWTSUserNameUnicode stringWTSWinStationNameUnicode stringWTSWorkingDirectoryUnicode stringWTSClientProtocolTypeInt, one of WTS_PROTOCOL_TYPE_CONSOLE,WTS_PROTOCOL_TYPE_ICA,WTS_PROTOCOL_TYPE_RDPWTSClientProductIdIntWTSClientBuildNumberIntWTSClientHardwareIdIntWTSSessionIdIntWTSConnectStateInt, from WTS_CONNECTSTATE_CLASSWTSClientDisplayDict containing client's display settingsWTSClientAddressDict containing type and value of client's IP address (None if console session) IPV6 addresses may not be returned correctly on Windows versions earlier than Windows Server 2012 (see http://sourceforge.net/p/pywin32/bugs/664/ for details)

Returns:

      None
        
    """
    pass
        

def WTSEnumerateProcesses(Server:'int',Version:'typing.Any'=1,Reserved:'typing.Any'=0) -> 'typing.Tuple[str, ...]':
    """
    Lists processes on a terminal server

Args:

      Server(int):Handle to a terminal server
      Version(typing.Any):Version of request, currently 1 is only valid value
      Reserved(typing.Any):Reserved, use 0 if passed in

Returns:

      typing.Tuple[str, ...]
        
    """
    pass
        

def WTSQueryUserToken(SessionId:'typing.Any') -> 'int':
    """
    Retrieves the access token for a session

Args:

      SessionId(typing.Any):Terminal services session idCommentsThis function is intended only for use by trusted processes that have SE_TCB_PRIVILEGE enabled

Returns:

      int
        
    """
    pass
        

def WTSShutdownSystem(Server:'int',ShutdownFlag:'typing.Any') -> 'None':
    """
    Issues a shutdown request to a terminal server

Args:

      Server(int):Handle to a terminal server
      ShutdownFlag(typing.Any):One of the win32ts.WTS_WSD_* values

Returns:

      None
        
    """
    pass
        

def WTSTerminateProcess(Server:'int',ProcessId:'typing.Any',ExitCode:'typing.Any') -> 'None':
    """
    Kills a process on a terminal server

Args:

      Server(int):Handle to a terminal server
      ProcessId(typing.Any):Id of a process as returned by win32ts::WTSEnumerateProcesses
      ExitCode(typing.Any):Exit code for the process

Returns:

      None
        
    """
    pass
        

def ProcessIdToSessionId(ProcessId:'typing.Any') -> 'typing.Any':
    """
    Finds the session under which a process is running

Args:

      ProcessId(typing.Any):Id of a process as returned by win32ts::WTSEnumerateProcesses

Returns:

      typing.Any
        
    """
    pass
        

def WTSGetActiveConsoleSessionId() -> 'typing.Any':
    """
    Returns the id of the console session

Args:



Returns:

      typing.Any
        
    """
    pass
        

def WTSRegisterSessionNotification(Wnd:'int',Flags:'typing.Any') -> 'None':
    """
    Registers a window to receive terminal service notifications

Args:

      Wnd(int):Window handle to receive terminal service messages
      Flags(typing.Any):NOTIFY_FOR_THIS_SESSION or NOTIFY_FOR_ALL_SESSIONS

Returns:

      None
        
    """
    pass
        

def WTSUnRegisterSessionNotification(Wnd:'int') -> 'None':
    """
    Disables terminal service window messages

Args:

      Wnd(int):Window previously registered to receive session notifications

Returns:

      None
        
    """
    pass
        

def WTSWaitSystemEvent(Server:'int',EventMask:'typing.Any') -> 'typing.Any':
    """
    Waits for an event to occur

Args:

      Server(int):Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE
      EventMask(typing.Any):Combination of WTS_EVENT_* valuesReturn ValueReturns a bitmask of WTS_EVENT_* flags indication which event(s) occurred

Returns:

      typing.Any:Combination of WTS_EVENT_* values
Return ValueReturns a bitmask of WTS_EVENT_* flags indication which event(s) occurred

        
    """
    pass
        

def WTSSendMessage(Server:'int',SessionId:'typing.Any',Title:'str',Message:'str',Style:'typing.Any',Timeout:'typing.Any',Wait:'typing.Any') -> 'typing.Any':
    """
    Sends a popup message to a terminal services session

Args:

      Server(int):Handle to a terminal server, or WTS_CURRENT_SERVER_HANDLE
      SessionId(typing.Any):Terminal services session id
      Title(str):Title of dialog
      Message(str):Message to be displayed
      Style(typing.Any):Usually MB_OK
      Timeout(typing.Any):Seconds to wait before returning (only used if Wait is True)
      Wait(typing.Any):Specifies if function should wait for user input before returningReturn ValueReturns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,

Returns:

      typing.Any:Specifies if function should wait for user input before returningReturn ValueReturns one of IDABORT,IDCANCEL,IDIGNORE,IDNO,IDOK,IDRETRY,IDYES,IDASYNC,IDTIMEOUT,

        
    """
    pass
        