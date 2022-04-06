__all__=['', 'CreatePhonebookEntry', 'Dial', 'EditPhonebookEntry', 'EnumConnections', 'EnumEntries', 'GetConnectStatus', 'GetEntryDialParams', 'GetErrorString', 'HangUp', 'IsHandleValid', 'SetEntryDialParams', 'RASCS_AllDevicesConnected', 'RASCS_AuthAck', 'RASCS_AuthCallback', 'RASCS_AuthChangePassword', 'RASCS_Authenticate', 'RASCS_Authenticated', 'RASCS_AuthLinkSpeed', 'RASCS_AuthNotify', 'RASCS_AuthProject', 'RASCS_AuthRetry', 'RASCS_CallbackComplete', 'RASCS_CallbackSetByCaller', 'RASCS_ConnectDevice', 'RASCS_Connected', 'RASCS_DeviceConnected', 'RASCS_Disconnected', 'RASCS_Interactive', 'RASCS_LogonNetwork', 'RASCS_OpenPort', 'RASCS_PasswordExpired', 'RASCS_PortOpened', 'RASCS_PrepareForCallback', 'RASCS_Projected', 'RASCS_ReAuthenticate', 'RASCS_RetryAuthentication', 'RASCS_StartAuthentication', 'RASCS_WaitForCallback', 'RASCS_WaitForModemReset']
import typing
import win32typing
"""A module encapsulating the Windows Remote Access Service (RAS) API."""


def CreatePhonebookEntry(hWnd:'typing.Any',fileName:'str'=None) -> 'None':
    """
    Creates a new phonebook entry.  The function displays a dialog box into 

which the user can enter information about the entry

Args:

      hWnd(typing.Any):Handle to the parent window of the dialog box.
      fileName(str):Specifies the filename of the phonebook entry. Currently this is ignored.Win32 API References

Returns:

      None
        
    """
    pass
        

def Dial(dialExtensions:'typing.Any',fileName:'str',RasDialParams:'win32typing.RASDIALPARAMS',callback:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Establishes a RAS connection to a RAS server.

Args:

      dialExtensions(typing.Any):An object providing the RASDIALEXTENSIONS information, or None
      fileName(str):Specifies the filename of the phonebook entry, or None.  Ignored on Win95.
      RasDialParams(win32typing.RASDIALPARAMS):A tuple describing a RASDIALPARAMS structure.
      callback(typing.Any):The method to be called when RAS events occur, or None. If not None, the function must have the signature of win32ras::RasDialFunc1CommentsNote - this handle must be closed using win32ras::HangUp, or else the RAS port will remain open, even after the program has terminated. Your operating system may need rebooting to clean up otherwise!Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any]:Search for RasDial at msdn, google or google groups.
Return ValueThe return value is (handle, retCode). 

It is possible for a valid handle to be returned even on failure. 

If the returned handle is = 0, then it can be assumed invalid.

        
    """
    pass
        

def EditPhonebookEntry(hWnd:'typing.Any',fileName:'str',entryName:'str'=None) -> 'None':
    """
    Creates a new phonebook entry.  The function displays a dialog box into which 

the user can enter information about the entry

Args:

      hWnd(typing.Any):Handle to the parent window of the dialog box.
      fileName(str):Specifies the filename of the phonebook entry, or None.  Currently this is ignored.
      entryName(str):Specifies the name of the phonebook entry to editWin32 API References

Returns:

      None
        
    """
    pass
        

def EnumConnections() -> 'typing.Any':
    """
    Returns a list of tuples, one for each active connection.

Args:



Returns:

      typing.Any:Search for RasEnumConnections at msdn, google or google groups.
Return ValueEach tuple is of format (handle, entryName, deviceType, deviceName)

        
    """
    pass
        

def EnumEntries(reserved:'str'=None,fileName:'str'=None) -> 'None':
    """
    Returns a list of tuples, one for each phonebook entry.

Args:

      reserved(str):Reserved - must be None
      fileName(str):The name of the phonebook file, or None.

Returns:

      None
        
    """
    pass
        

def GetConnectStatus(hrasconn:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any, str, str]':
    """
    Returns a tuple with connection information.

Args:

      hrasconn(typing.Any):Handle to the RAS session.Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any, str, str]
        
    """
    pass
        

def GetEntryDialParams(fileName:'str',entryName:'str') -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Returns a tuple with the most recently set dial parameters for 

the specified entry.

Args:

      fileName(str):The filename of the phonebook, or None.
      entryName(str):The name of the entry to retrieve the params for.Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any, typing.Any]:Search for RasGetConnectStatus at msdn, google or google groups.
Return ValueThe return value is a tuple describing the params retrieved, plus a BOOL integer 

indicating if the password was also retrieved.

        
    """
    pass
        

def GetErrorString(error:'typing.Any') -> 'str':
    """
    Returns an error string for a RAS error code.

Args:

      error(typing.Any):The error value being queried.Win32 API References

Returns:

      str
        
    """
    pass
        

def HangUp(hras:'typing.Any') -> 'None':
    """
    Terminates a remote access session.

Args:

      hras(typing.Any):The handle to the RAS connection to be terminated.Win32 API References

Returns:

      None
        
    """
    pass
        

def IsHandleValid(hras:'typing.Any') -> 'None':
    """
    Indicates if the given RAS handle is valid.

Args:

      hras(typing.Any):The handle to the RAS connection being checked.

Returns:

      None
        
    """
    pass
        

def SetEntryDialParams(fileName:'str',RasDialParams:'typing.Any',bSavePassword:'typing.Any') -> 'None':
    """
    Sets the dial parameters for the specified entry.

Args:

      fileName(str):The filename of the phonebook, or None.
      RasDialParams(typing.Any):A tuple describing a RASDIALPARAMS structure.
      bSavePassword(typing.Any):Indicates whether to remove password from entry's parameters.Win32 API References

Returns:

      None
        
    """
    pass
        
RASCS_AllDevicesConnected = ...
RASCS_AuthAck = ...
RASCS_AuthCallback = ...
RASCS_AuthChangePassword = ...
RASCS_Authenticate = ...
RASCS_Authenticated = ...
RASCS_AuthLinkSpeed = ...
RASCS_AuthNotify = ...
RASCS_AuthProject = ...
RASCS_AuthRetry = ...
RASCS_CallbackComplete = ...
RASCS_CallbackSetByCaller = ...
RASCS_ConnectDevice = ...
RASCS_Connected = ...
RASCS_DeviceConnected = ...
RASCS_Disconnected = ...
RASCS_Interactive = ...
RASCS_LogonNetwork = ...
RASCS_OpenPort = ...
RASCS_PasswordExpired = ...
RASCS_PortOpened = ...
RASCS_PrepareForCallback = ...
RASCS_Projected = ...
RASCS_ReAuthenticate = ...
RASCS_RetryAuthentication = ...
RASCS_StartAuthentication = ...
RASCS_WaitForCallback = ...
RASCS_WaitForModemReset = ...
