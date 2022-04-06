__all__=['', 'InternetSetCookie', 'InternetGetCookie', 'InternetAttemptConnect', 'InternetCheckConnection', 'InternetGoOnline', 'InternetCloseHandle', 'InternetConnect', 'InternetOpen', 'InternetOpenUrl', 'InternetCanonicalizeUrl', 'InternetGetLastResponseInfo', 'InternetReadFile', 'InternetWriteFile', 'FtpOpenFile', 'FtpCommand', 'InternetQueryOption', 'InternetSetOption', 'FindFirstUrlCacheEntry', 'FindNextUrlCacheEntry', 'FindFirstUrlCacheEntryEx', 'FindNextUrlCacheEntryEx', 'FindCloseUrlCache', 'FindFirstUrlCacheGroup', 'FindNextUrlCacheGroup', 'GetUrlCacheEntryInfo', 'DeleteUrlCacheGroup', 'CreateUrlCacheGroup', 'CreateUrlCacheEntry', 'CommitUrlCacheEntry', 'SetUrlCacheEntryGroup', 'GetUrlCacheGroupAttribute', 'SetUrlCacheGroupAttribute', 'DeleteUrlCacheEntry']
import typing
import win32typing
"""An interface to the Windows internet (wininet) API"""


def InternetSetCookie(url:'str',lpszCookieName:'str',data:'str') -> 'None':
    """
    Creates a cookie associated with the specified URL.

Args:

      url(str):
      lpszCookieName(str):
      data(str):

Returns:

      None
        
    """
    pass
        

def InternetGetCookie(Url:'str',CookieName:'str') -> 'str':
    """
    Retrieves the cookie for the specified URL

Args:

      Url(str):Site for which to retrieve cookie
      CookieName(str):Name of cookie (documented on MSDN as not implemented)

Returns:

      str
        
    """
    pass
        

def InternetAttemptConnect(Reserved:'typing.Any'=0) -> 'None':
    """
    Attempts to make a connection to the Internet.

Args:

      Reserved(typing.Any):Use only 0.

Returns:

      None
        
    """
    pass
        

def InternetCheckConnection(Url:'str',Flags:'typing.Any'=0,Reserved:'typing.Any'=0) -> 'None':
    """
    Allows an application to check if a connection to the Internet can be established

Args:

      Url(str):Url to attempt to connect to, can be None
      Flags(typing.Any):FLAG_ICC_FORCE_CONNECTION is only defined flag
      Reserved(typing.Any):Use only 0.

Returns:

      None
        
    """
    pass
        

def InternetGoOnline(Url:'str',Parent:'typing.Any'=None,Flags:'typing.Any'=0) -> 'None':
    """
    Prompts the user for permission to initiate connection to a URL.

Args:

      Url(str):Web site to connect to
      Parent(typing.Any):Handle to parent window
      Flags(typing.Any):INTERNET_GOONLINE_REFRESH is only available flag

Returns:

      None
        
    """
    pass
        

def InternetCloseHandle(handle:'win32typing.PyHINTERNET') -> 'None':
    """
    None

Args:

      handle(win32typing.PyHINTERNET):CommentsIt should not be necessary to call this function - all handles are PyHINTERNET objects, so can have their Close method called, and will otherwise be automatically closed.

Returns:

      None
        
    """
    pass
        

def InternetConnect(Internet:'win32typing.PyHINTERNET',ServerName:'str',ServerPort:'typing.Any',Username:'str',Password:'str',Service:'typing.Any',Flags:'typing.Any',Context:'typing.Any'=None) -> 'None':
    """
    Opens an FTP, Gopher, or HTTP session for a given site.

Args:

      Internet(win32typing.PyHINTERNET):Valid HINTERNET handle returned by a previous call to win32inet::InternetOpen.
      ServerName(str):A string that contains the host name of an Internet server. Alternately, the string can contain the IP number of the site, in ASCII dotted-decimal format (for example, 11.0.1.45).
      ServerPort(typing.Any):Number of the TCP/IP port on the server to connect to. These flags set only the port that will be used. The service is set by the value of dwService. This can be one of the INTERNET_DEFAULT_*_PORT constants or INTERNET_INVALID_PORT_NUMBER, which uses the default port for the service specified by dwService.
      Username(str):A string that contains the name of the user to log on. If this parameter is	None, the function uses	an appropriate default, except	for	HTTP; a	NULL parameter in HTTP causes the server to return an error.	For	the	FTP	protocol, the default is "anonymous".
      Password(str):Address	of a null-terminated string	that contains the password to use to	log	on.	If both	Password and	Username are None, the function	uses the default "anonymous"	password. In the case of FTP, the default password is the user's e-mail name. If lpszPassword is None,	but	lpszUsername is not None, the function uses a blank password.
      Service(typing.Any):Iinteger value that contains the type	of service to access.	This can be	one	of INTERNET_SERVICE_FTP, INTERNET_SERVICE_GOPHER, or INTERNET_SERVICE_HTTP.
      Flags(typing.Any):Integer value that contains the flags specific to the	service	used. When the value of	dwService is INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE causes the application to	use	passive	FTP	semantics.
      Context(typing.Any):Arbitrary object to be passed to callback functionCommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def InternetOpen(agent:'str',proxyName:'str',proxyBypass:'str',flags:'typing.Any') -> 'None':
    """
    Initializes an application's use of the Microsoft® Win32® Internet functions.

Args:

      agent(str):A string that contains the name of the application or entity calling the Internet functions. This name is used as the user agent in the HTTP protocol.
      proxyName(str):
      proxyBypass(str):
      flags(typing.Any):Combination of INTERNET_FLAG_ASYNC,INTERNET_FLAG_FROM_CACHE, or INTERNET_FLAG_OFFLINE

Returns:

      None
        
    """
    pass
        

def InternetOpenUrl(Internet:'win32typing.PyHINTERNET',Url:'str',Headers:'str'=None,Flags:'typing.Any'=0,Context:'typing.Any'=None) -> 'win32typing.PyHINTERNET':
    """
    Opens a resource specified by a 

complete FTP, Gopher, or HTTP URL.

Args:

      Internet(win32typing.PyHINTERNET):Internet handle as returned by win32inet::InternetOpen
      Url(str):A string that contains the URL to begin reading.  Only URLs beginning with ftp:, gopher:, http:, or https: are supported.
      Headers(str):a string	variable that contains the headers to be sent to the HTTP server.
      Flags(typing.Any):INTERNET_FLAG_*
      Context(typing.Any):An arbitrary object to be passed to the status callback functionCommentsAccepts keyword args.Return ValueReturns None in async mode (Internet handle created with INTERNET_FLAG_ASYNC). When handle is created, it will be passed to callback function of parent handle.

Returns:

      win32typing.PyHINTERNET:An arbitrary object to be passed to the status callback function
Comments

Accepts keyword args.
Return ValueReturns None in async mode (Internet handle created with INTERNET_FLAG_ASYNC). 

When handle is created, it will be passed to callback function of parent handle.

        
    """
    pass
        

def InternetCanonicalizeUrl(url:'str',flags:'typing.Any'=0) -> 'str':
    """
    Canonicalizes a URL, which includes 

converting unsafe characters and spaces into escape sequences.

Args:

      url(str):The URL to canonicalize.
      flags(typing.Any):integer value that contains the flags that control canonicalization. This can be one of the following values:ICU_BROWSER_MODEDoes not encode or decode characters after "#" or "?", and does not remove trailing white space after "?". If this value is not specified, the entire URL is encoded and trailing white space is removed.ICU_DECODEConverts all %XX sequences to characters, including escape sequences, before the URL is parsed.ICU_ENCODE_PERCENTEncodes any percent signs encountered. By default, percent signs are not encoded. This value is available in Microsoft® Internet Explorer 5 and later versions of the Win32® Internet functions.ICU_ENCODE_SPACES_ONLYEncodes spaces only.ICU_NO_ENCODEDoes not convert unsafe characters to escape sequences.ICU_NO_METADoes not remove meta sequences (such as "." and "..") from the URL. If no flags are specified (dwFlags = 0), the function converts all unsafe characters and meta sequences (such as .,\\ .., and ...) to escape sequences.

Returns:

      str
        
    """
    pass
        

def InternetGetLastResponseInfo() -> 'typing.Tuple[typing.Any, str]':
    """
    Retrieves the last Win32® Internet function error description or server response on the thread calling this function.

Args:



Returns:

      typing.Tuple[typing.Any, str]
        
    """
    pass
        

def InternetReadFile(hInternet:'win32typing.PyHINTERNET',size:'typing.Any') -> 'str':
    """
    None

Args:

      hInternet(win32typing.PyHINTERNET):
      size(typing.Any):Number of bytes to read.Return ValueThe result will be a string of zero bytes when the end is reached.

Returns:

      str:Number of bytes to read.Return ValueThe result will be a string of zero bytes when the end is reached.

        
    """
    pass
        

def InternetWriteFile(File:'win32typing.PyHINTERNET',Buffer:'str') -> 'typing.Any':
    """
    None

Args:

      File(win32typing.PyHINTERNET):Writeable internet	handle
      Buffer(str):String or	buffer containing data to be written

Returns:

      typing.Any
        
    """
    pass
        

def FtpOpenFile(hConnect:'win32typing.PyHINTERNET',FileName:'str',Access:'typing.Any',Flags:'typing.Any',Context:'typing.Any'=None) -> 'win32typing.PyHINTERNET':
    """
    Initiates access to a remote file on an FTP server for reading or writing.

Args:

      hConnect(win32typing.PyHINTERNET):Valid HINTERNET handle to an FTP session.
      FileName(str):The name of the file to access on the remote system.
      Access(typing.Any):Integer value that determines how the file will be accessed. This can be GENERIC_READ or GENERIC_WRITE, but not both.
      Flags(typing.Any):Integer value that contains the conditions under which the transfers occur. The application should select one transfer type and any of the flags that indicate how the caching of the file will be controlled.  The transfer type can be one of the FTP_TRANSFER_TYPE* values
      Context(typing.Any):Arbitrary object that will be passed to handle's callback functionCommentsAccepts keyword args

Returns:

      win32typing.PyHINTERNET
        
    """
    pass
        

def FtpCommand(Connect:'win32typing.PyHINTERNET',ExpectResponse:'typing.Any',Flags:'typing.Any',Command:'str',Context:'typing.Any'=None) -> 'win32typing.PyHINTERNET':
    """
    Allows an application to send commands directly to an FTP server.

Args:

      Connect(win32typing.PyHINTERNET):Valid HINTERNET	handle to an FTP session.
      ExpectResponse(typing.Any):Boolean value	that indicates whether or not the application expects a response	from the FTP server. This must be set to True if a response	is expected, or	False otherwise.
      Flags(typing.Any):Unsigned long integer value that contains the flags that control this function. This can be set to	either FTP_TRANSFER_TYPE_ASCII or FTP_TRANSFER_TYPE_BINARY
      Command(str):The command to send to the FTP server.
      Context(typing.Any):Arbitrary object	to be passed to	callbackCommentsThis function may cause a crash on 32-bit XP and Vista due to an internal error in win32inet.dll.Accepts keyword args

Returns:

      win32typing.PyHINTERNET
        
    """
    pass
        

def InternetQueryOption(hInternet:'win32typing.PyHINTERNET',Option:'typing.Any') -> 'typing.Any':
    """
    Retrieves an option for an internet handle

Args:

      hInternet(win32typing.PyHINTERNET):Internet handle, or None for global defaults
      Option(typing.Any):INTERNET_OPTION_* valueOptionReturned typeINTERNET_OPTION_CALLBACKPython callback functionINTERNET_OPTION_CONTEXT_VALUEContext objectINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHInt - Codepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_HANDLE_TYPEInt, INTERNET_HANDLE_TYPE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_EXTENDED_ERRORInt, ERROR_INTERNET_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_FLAGSInt, combination of INTERNET_REQFLAG_*INTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_SECURITY_FLAGSInt, SECURITY_FLAG_*INTERNET_OPTION_SECURITY_KEY_BITNESSIntINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_DATAFILE_NAMEString - Name of internet cache fileINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_SECURITY_CERTIFICATEStringINTERNET_OPTION_URLStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_CACHE_TIMESTAMPSdict - Expiration and last modified timesINTERNET_OPTION_HTTP_VERSIONdict - HTTP_VERSION_INFOINTERNET_OPTION_VERSIONdict - INTERNET_VERSION_INFOINTERNET_OPTION_PARENT_HANDLEPyHINTERNETINTERNET_OPTION_PROXYdict - INTERNET_PROXY_INFOINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFONot yet supported (INTERNET_DIAGNOSTIC_SOCKET_INFO)INTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTNot yet supported (INTERNET_CERTIFICATE_INFO)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_DATAFILE_EXTOnly valid for InternetSetOptionINTERNET_OPTION_DIGEST_AUTH_UNLOADOnly valid for InternetSetOptionINTERNET_OPTION_END_BROWSER_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_REFRESHOnly valid for InternetSetOptionINTERNET_OPTION_RESET_URLCACHE_SESSIONOnly valid for InternetSetOptionINTERNET_OPTION_SETTINGS_CHANGEDOnly valid for InternetSetOptionWin32 API References

Returns:

      typing.Any:Search for InternetQueryOption at msdn, google or google groups.
Return ValueThe type of object returned is dependent on the option requested

        
    """
    pass
        

def InternetSetOption(hInternet:'win32typing.PyHINTERNET',Option:'typing.Any',Buffer:'typing.Any') -> 'None':
    """
    Sets an option for an internet handle

Args:

      hInternet(win32typing.PyHINTERNET):Internet handle, or None for global defaults
      Option(typing.Any):The option to set, INTERNET_OPTION_*
      Buffer(typing.Any):Type is dependent on OptionOptionType of input objectINTERNET_OPTION_CALLBACKPython function called on status changeINTERNET_OPTION_CONTEXT_VALUEAny Python object to be passed to callback functionINTERNET_OPTION_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_SEND_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CONTROL_RECEIVE_TIMEOUTInt - timeout in millsecondsINTERNET_OPTION_CODEPAGEInt - Codepage of host part of URLINTERNET_OPTION_CODEPAGE_PATHCodepage for URLINTERNET_OPTION_CODEPAGE_EXTRAInt - Codepage for path part of URLINTERNET_OPTION_CONNECT_RETRIESInt - Number of time to try to reconnect to hostINTERNET_OPTION_CONNECT_TIMEOUTInt - Connection timeout in millisecondsINTERNET_OPTION_CONNECTED_STATEInt - Connection state, INTERNET_STATE_*INTERNET_OPTION_ERROR_MASKInt, combination of INTERNET_ERROR_MASK_*INTERNET_OPTION_FROM_CACHE_TIMEOUTInt - Timeout in ms before cached copy is usedINTERNET_OPTION_IDNInt, INTERNET_FLAG_IDN_*INTERNET_OPTION_MAX_CONNS_PER_1_0_SERVERIntINTERNET_OPTION_MAX_CONNS_PER_SERVERIntINTERNET_OPTION_READ_BUFFER_SIZEIntINTERNET_OPTION_WRITE_BUFFER_SIZEIntINTERNET_OPTION_REQUEST_PRIORITYIntINTERNET_OPTION_DIGEST_AUTH_UNLOADNoneINTERNET_OPTION_END_BROWSER_SESSIONNoneINTERNET_OPTION_REFRESHNoneINTERNET_OPTION_RESET_URLCACHE_SESSIONNoneINTERNET_OPTION_SETTINGS_CHANGEDNoneINTERNET_OPTION_BYPASS_EDITED_ENTRYBooleanINTERNET_OPTION_HTTP_DECODINGBooleanINTERNET_OPTION_IGNORE_OFFLINEBooleanINTERNET_OPTION_USERNAMEString - Username passed to InternetConnectINTERNET_OPTION_PASSWORDString - Password passed to InternetConnectINTERNET_OPTION_PROXY_PASSWORDStringINTERNET_OPTION_PROXY_USERNAMEStringINTERNET_OPTION_SECONDARY_CACHE_KEYStringINTERNET_OPTION_USER_AGENTStringINTERNET_OPTION_DATAFILE_EXTString - Extension to use for download cache fileINTERNET_OPTION_PROXYDict representing INTERNET_PROXY_INFO structINTERNET_OPTION_HTTP_VERSIONNot yet supported - HTTP_VERSION_INFOINTERNET_OPTION_PER_CONNECTION_OPTIONNot yet supported (INTERNET_PER_CONN_OPTION_LIST)INTERNET_OPTION_ALTER_IDENTITYNot supportedINTERNET_OPTION_ASYNCNot supportedINTERNET_OPTION_ASYNC_IDNot supportedINTERNET_OPTION_ASYNC_PRIORITYNot supportedINTERNET_OPTION_CACHE_STREAM_HANDLENot supportedINTERNET_OPTION_CALLBACK_FILTERNot supportedINTERNET_OPTION_CLIENT_CERT_CONTEXTNot supportedINTERNET_OPTION_DATA_RECEIVE_TIMEOUTNot supportedINTERNET_OPTION_DATA_SEND_TIMEOUTNot supportedINTERNET_OPTION_CONNECT_BACKOFFNot supportedINTERNET_OPTION_CONNECT_TIMENot supportedINTERNET_OPTION_DISABLE_AUTODIALNot supportedINTERNET_OPTION_DISCONNECTED_TIMEOUTNot supportedINTERNET_OPTION_IDENTITYNot supportedINTERNET_OPTION_IDLE_STATENot supportedINTERNET_OPTION_KEEP_CONNECTIONNot supportedINTERNET_OPTION_LISTEN_TIMEOUTNot supportedINTERNET_OPTION_OFFLINE_MODENot supportedINTERNET_OPTION_OFFLINE_SEMANTICSNot supportedINTERNET_OPTION_POLICYNot supportedINTERNET_OPTION_RECEIVE_THROUGHPUTNot supportedINTERNET_OPTION_REMOVE_IDENTITYNot supportedINTERNET_OPTION_SEND_THROUGHPUTNot supportedINTERNET_OPTION_CACHE_TIMESTAMPSOnly valid for InternetQueryOptionINTERNET_OPTION_HANDLE_TYPEOnly valid for InternetQueryOptionINTERNET_OPTION_DATAFILE_NAMEOnly valid for InternetQueryOptionINTERNET_OPTION_PARENT_HANDLEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATEOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_CERTIFICATE_STRUCTOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_SECURITY_KEY_BITNESSOnly valid for InternetQueryOptionINTERNET_OPTION_DIAGNOSTIC_SOCKET_INFOOnly valid for InternetQueryOptionINTERNET_OPTION_VERSIONOnly valid for InternetQueryOptionINTERNET_OPTION_EXTENDED_ERROROnly valid for InternetQueryOptionINTERNET_OPTION_REQUEST_FLAGSOnly valid for InternetQueryOptionINTERNET_OPTION_URLOnly valid for InternetQueryOptionWin32 API References

Returns:

      None
        
    """
    pass
        

def FindFirstUrlCacheEntry(SearchPattern:'typing.Any'=None) -> 'typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]':
    """
    Initiates an enumeration of the browser cache

Args:

      SearchPattern(typing.Any):Type of entry to find, can be 'visited:', 'cookie:', or NoneCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]:Search for FindFirstUrlCacheEntry at msdn, google or google groups.
Return ValueReturns a handle that can be passed to win32inet::FindNextUrlCacheEntry, and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

        
    """
    pass
        

def FindNextUrlCacheEntry(EnumHandle:'win32typing.PyUrlCacheHANDLE') -> 'typing.Any':
    """
    Continues enumeration of cached files

Args:

      EnumHandle(win32typing.PyUrlCacheHANDLE):Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntryCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any:Search for FindNextUrlCacheEntry at msdn, google or google groups.
Return ValueReturns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

        
    """
    pass
        

def FindFirstUrlCacheEntryEx(SearchPattern:'typing.Any'=None,Flags:'typing.Any'=0,Filter:'typing.Any'=0,GroupId:'typing.Any'=0) -> 'typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]':
    """
    Initiates an enumeration of the browser cache

Args:

      SearchPattern(typing.Any):Type of entry to find, can be 'visited:', 'cookie:', or None
      Flags(typing.Any):None currently defined
      Filter(typing.Any):Types of entries to return, combination of *_CACHE_ENTRY values
      GroupId(typing.Any):Cache group to enumerate, use 0 for allCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]:Search for FindFirstUrlCacheEntryEx at msdn, google or google groups.
Return ValueReturns a handle that can be passed to win32inet::FindNextUrlCacheEntry, and a dict 

containing information for the first entry found.  Throws error code ERROR_NO_MORE_ITEMS 

if no items are found.

        
    """
    pass
        

def FindNextUrlCacheEntryEx(EnumHandle:'win32typing.PyUrlCacheHANDLE') -> 'typing.Any':
    """
    Continues enumeration of cached files

Args:

      EnumHandle(win32typing.PyUrlCacheHANDLE):Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntryExCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any:Search for FindNextUrlCacheEntryEx at msdn, google or google groups.
Return ValueReturns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

        
    """
    pass
        

def FindCloseUrlCache(EnumHandle:'win32typing.PyUrlCacheHANDLE') -> 'None':
    """
    Closes a cache enumeration handle

Args:

      EnumHandle(win32typing.PyUrlCacheHANDLE):Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntryCommentsAccepts keyword argsWin32 API References

Returns:

      None
        
    """
    pass
        

def FindFirstUrlCacheGroup(Filter:'typing.Any') -> 'typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]':
    """
    Initiates enumeration of Url cache groups

Args:

      Filter(typing.Any):CACHEGROUP_SEARCH_*CommentsAccepts keyword argsWin32 API References

Returns:

      typing.Tuple[win32typing.PyUrlCacheHANDLE, typing.Any]:Search for FindFirstUrlCacheGroup at msdn, google or google groups.
Return ValueReturns a handle that can be passed to win32inet::FindNextUrlCacheGroup, and the id 

of the first group found.

        
    """
    pass
        

def FindNextUrlCacheGroup(Find:'int') -> 'typing.Any':
    """
    Continues enumeration of cache groups

Args:

      Find(int):Group enumeration handle as returned by win32inet::FindFirstUrlCacheGroupCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def GetUrlCacheEntryInfo(UrlName:'typing.Any') -> 'typing.Any':
    """
    Retrieves cache info for a URL

Args:

      UrlName(typing.Any):Cache enumeration handle as returned by win32inet::FindFirstUrlCacheEntryCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any:Search for GetUrlCacheEntryInfo at msdn, google or google groups.
Return ValueReturns a dict representing a INTERNET_CACHE_ENTRY_INFO strunct

        
    """
    pass
        

def DeleteUrlCacheGroup(GroupId:'typing.Any',Attributes:'typing.Any') -> 'None':
    """
    Deletes a cache group

Args:

      GroupId(typing.Any):Group id
      Attributes(typing.Any):Combination of CACHEGROUP_FLAG_* flagsCommentsAccepts keyword argsWin32 API References

Returns:

      None
        
    """
    pass
        

def CreateUrlCacheGroup(Flags:'typing.Any'=0) -> 'typing.Any':
    """
    Creates a new cache group

Args:

      Flags(typing.Any):Combination of CACHEGROUP_FLAG_* flagsCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def CreateUrlCacheEntry(UrlName:'typing.Any',ExpectedFileSize:'typing.Any',FileExtension:'typing.Any') -> 'typing.Any':
    """
    Creates a cache entry for a URL

Args:

      UrlName(typing.Any):The Url for which to create an entry
      ExpectedFileSize(typing.Any):Size of content, use 0 if unknown
      FileExtension(typing.Any):Extension to use for filenameCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any:Search for CreateUrlCacheEntry at msdn, google or google groups.
Return ValueReturns the filename to which content should be written

        
    """
    pass
        

def CommitUrlCacheEntry(UrlName:'typing.Any',LocalFileName:'typing.Any',CacheEntryType:'typing.Any',ExpireTime:'win32typing.PyTime'=None,LastModifiedTime:'win32typing.PyTime'=None,HeaderInfo:'typing.Any'=None,OriginalUrl:'typing.Any'=None) -> 'typing.Any':
    """
    Commits a cache entry

Args:

      UrlName(typing.Any):The Url for which to create an entry
      LocalFileName(typing.Any):Filename returned from win32inet::CreateUrlCacheEntry. Can be None when creating a history entry.
      CacheEntryType(typing.Any):Combination of *_CACHE_ENTRY flags
      ExpireTime(win32typing.PyTime):Time at which entry expires
      LastModifiedTime(win32typing.PyTime):Modification time of URL
      HeaderInfo(typing.Any):Header data used to request Url
      OriginalUrl(typing.Any):If redirected, original site requestedCommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def SetUrlCacheEntryGroup(UrlName:'typing.Any',Flags:'typing.Any',GroupId:'typing.Any') -> 'None':
    """
    Associates a cache entry with a group

Args:

      UrlName(typing.Any):Url whose cache is to be added to the group
      Flags(typing.Any):INTERNET_CACHE_GROUP_ADD or INTERNET_CACHE_GROUP_REMOVE
      GroupId(typing.Any):Id of a cache groupCommentsAccepts keyword argsWin32 API References

Returns:

      None
        
    """
    pass
        

def GetUrlCacheGroupAttribute(GroupId:'typing.Any',Attributes:'typing.Any') -> 'typing.Any':
    """
    Retrieves attributes for a cache group

Args:

      GroupId(typing.Any):Group id
      Attributes(typing.Any):Attributes to retrieve, CACHEGROUP_ATTRIBUTE_*CommentsAccepts keyword argsWin32 API References

Returns:

      typing.Any:Search for GetUrlCacheGroupAttribute at msdn, google or google groups.
Return ValueReturns a dict representing a INTERNET_CACHE_GROUP_INFO struct

        
    """
    pass
        

def SetUrlCacheGroupAttribute(GroupId:'typing.Any',Attributes:'typing.Any',GroupInfo:'typing.Any',Flags:'typing.Any'=0) -> 'None':
    """
    Changes the attributes of a cache group

Args:

      GroupId(typing.Any):Id of a cache group
      Attributes(typing.Any):Bitmask of CACHEGROUP_ATTRIBUTE_* flags indicating which attributes to set
      GroupInfo(typing.Any):INTERNET_CACHE_GROUP_INFO dict as returned by win32inet::GetUrlCacheGroupAttribute
      Flags(typing.Any):Reserved, use 0CommentsAccepts keyword argsWin32 API References

Returns:

      None
        
    """
    pass
        

def DeleteUrlCacheEntry(UrlName:'typing.Any') -> 'None':
    """
    Deletes the cache entry for a URL

Args:

      UrlName(typing.Any):Cached url to be deleted

Returns:

      None
        
    """
    pass
        