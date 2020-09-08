__all__=['', 'DsGetSpn', 'DsWriteAccountSpn', 'DsBind', 'DsUnBind', 'DsGetDcName', 'DsCrackNames', 'DsListInfoForServer', 'DsListServersInSite', 'DsListServersInSite', 'DsListServersInSite', 'DsListRoles', 'DsListDomainsInSite', 'ACL', 'SID', 'SECURITY_ATTRIBUTES', 'SECURITY_DESCRIPTOR', 'ImpersonateNamedPipeClient', 'ImpersonateLoggedOnUser', 'ImpersonateAnonymousToken', 'IsTokenRestricted', 'RevertToSelf', 'LogonUser', 'LogonUserEx', 'LookupAccountName', 'LookupAccountSid', 'GetBinarySid', 'SetSecurityInfo', 'GetSecurityInfo', 'SetNamedSecurityInfo', 'GetNamedSecurityInfo', 'OpenProcessToken', 'LookupPrivilegeValue', 'LookupPrivilegeName', 'LookupPrivilegeDisplayName', 'AdjustTokenPrivileges', 'AdjustTokenGroups', 'GetTokenInformation', 'OpenThreadToken', 'SetThreadToken', 'GetFileSecurity', 'SetFileSecurity', 'GetUserObjectSecurity', 'SetUserObjectSecurity', 'GetKernelObjectSecurity', 'SetKernelObjectSecurity', 'SetTokenInformation', 'LsaOpenPolicy', 'LsaClose', 'LsaQueryInformationPolicy', 'LsaSetInformationPolicy', 'LsaAddAccountRights', 'LsaRemoveAccountRights', 'LsaEnumerateAccountRights', 'LsaEnumerateAccountsWithUserRight', 'ConvertSidToStringSid', 'ConvertStringSidToSid', 'ConvertSecurityDescriptorToStringSecurityDescriptor', 'ConvertStringSecurityDescriptorToSecurityDescriptor', 'LsaStorePrivateData', 'LsaRetrievePrivateData', 'LsaRegisterPolicyChangeNotification', 'LsaUnregisterPolicyChangeNotification', 'CryptEnumProviders', 'EnumerateSecurityPackages', 'AllocateLocallyUniqueId', 'ImpersonateSelf', 'DuplicateToken', 'DuplicateTokenEx', 'CheckTokenMembership', 'CreateRestrictedToken', 'LsaRegisterLogonProcess', 'LsaConnectUntrusted', 'LsaDeregisterLogonProcess', 'LsaLookupAuthenticationPackage', 'LsaEnumerateLogonSessions', 'LsaGetLogonSessionData', 'AcquireCredentialsHandle', 'InitializeSecurityContext', 'AcceptSecurityContext', 'QuerySecurityPackageInfo', 'LsaCallAuthenticationPackage', 'TranslateName', 'CreateWellKnownSid', 'MapGenericMask', 'ACCESS_ALLOWED_ACE_TYPE', 'ACCESS_ALLOWED_OBJECT_ACE_TYPE', 'ACCESS_DENIED_ACE_TYPE', 'ACCESS_DENIED_OBJECT_ACE_TYPE', 'ACL_REVISION', 'ACL_REVISION_DS', 'AuditCategoryAccountLogon', 'AuditCategoryAccountManagement', 'AuditCategoryDetailedTracking', 'AuditCategoryDirectoryServiceAccess', 'AuditCategoryLogon', 'AuditCategoryObjectAccess', 'AuditCategoryPolicyChange', 'AuditCategoryPrivilegeUse', 'AuditCategorySystem', 'CONTAINER_INHERIT_ACE', 'DACL_SECURITY_INFORMATION', 'DENY_ACCESS', 'DISABLE_MAX_PRIVILEGE', 'DS_SPN_ADD_SPN_OP', 'DS_SPN_DELETE_SPN_OP', 'DS_SPN_DN_HOST', 'DS_SPN_DNS_HOST', 'DS_SPN_DOMAIN', 'DS_SPN_NB_DOMAIN', 'DS_SPN_NB_HOST', 'DS_SPN_REPLACE_SPN_OP', 'DS_SPN_SERVICE', 'FAILED_ACCESS_ACE_FLAG', 'GRANT_ACCESS', 'GROUP_SECURITY_INFORMATION', 'INHERIT_ONLY_ACE', 'INHERITED_ACE', 'LABEL_SECURITY_INFORMATION', 'LOGON32_LOGON_BATCH', 'LOGON32_LOGON_INTERACTIVE', 'LOGON32_LOGON_NETWORK', 'LOGON32_LOGON_NETWORK_CLEARTEXT', 'LOGON32_LOGON_NEW_CREDENTIALS', 'LOGON32_LOGON_SERVICE', 'LOGON32_LOGON_UNLOCK', 'LOGON32_PROVIDER_DEFAULT', 'LOGON32_PROVIDER_WINNT35', 'LOGON32_PROVIDER_WINNT40', 'LOGON32_PROVIDER_WINNT50', 'NO_INHERITANCE', 'NO_PROPAGATE_INHERIT_ACE', 'NOT_USED_ACCESS', 'OBJECT_INHERIT_ACE', 'OWNER_SECURITY_INFORMATION', 'POLICY_ALL_ACCESS', 'POLICY_AUDIT_EVENT_FAILURE', 'POLICY_AUDIT_EVENT_NONE', 'POLICY_AUDIT_EVENT_SUCCESS', 'POLICY_AUDIT_EVENT_UNCHANGED', 'POLICY_AUDIT_LOG_ADMIN', 'POLICY_CREATE_ACCOUNT', 'POLICY_CREATE_PRIVILEGE', 'POLICY_CREATE_SECRET', 'POLICY_EXECUTE', 'POLICY_GET_PRIVATE_INFORMATION', 'POLICY_LOOKUP_NAMES', 'POLICY_NOTIFICATION', 'POLICY_READ', 'POLICY_SERVER_ADMIN', 'POLICY_SET_AUDIT_REQUIREMENTS', 'POLICY_SET_DEFAULT_QUOTA_LIMITS', 'POLICY_TRUST_ADMIN', 'POLICY_VIEW_AUDIT_INFORMATION', 'POLICY_VIEW_LOCAL_INFORMATION', 'POLICY_WRITE', 'PolicyAccountDomainInformation', 'PolicyAuditEventsInformation', 'PolicyAuditFullQueryInformation', 'PolicyAuditFullSetInformation', 'PolicyAuditLogInformation', 'PolicyDefaultQuotaInformation', 'PolicyDnsDomainInformation', 'PolicyLsaServerRoleInformation', 'PolicyModificationInformation', 'PolicyNotifyAccountDomainInformation', 'PolicyNotifyAuditEventsInformation', 'PolicyNotifyDnsDomainInformation', 'PolicyNotifyDomainEfsInformation', 'PolicyNotifyDomainKerberosTicketInformation', 'PolicyNotifyMachineAccountPasswordInformation', 'PolicyNotifyServerRoleInformation', 'PolicyPdAccountInformation', 'PolicyPrimaryDomainInformation', 'PolicyReplicaSourceInformation', 'PolicyServerDisabled', 'PolicyServerDisabled', 'PolicyServerEnabled', 'PolicyServerEnabled', 'PolicyServerRoleBackup', 'PolicyServerRolePrimary', 'PROTECTED_DACL_SECURITY_INFORMATION', 'PROTECTED_SACL_SECURITY_INFORMATION', 'REVOKE_ACCESS', 'SACL_SECURITY_INFORMATION', 'SANDBOX_INERT', 'SDDL_REVISION_1', 'SE_DACL_AUTO_INHERITED', 'SE_DACL_DEFAULTED', 'SE_DACL_PRESENT', 'SE_DACL_PROTECTED', 'SE_DS_OBJECT', 'SE_DS_OBJECT_ALL', 'SE_FILE_OBJECT', 'SE_GROUP_DEFAULTED', 'SE_GROUP_ENABLED', 'SE_GROUP_ENABLED_BY_DEFAULT', 'SE_GROUP_LOGON_ID', 'SE_GROUP_MANDATORY', 'SE_GROUP_OWNER', 'SE_GROUP_RESOURCE', 'SE_GROUP_USE_FOR_DENY_ONLY', 'SE_KERNEL_OBJECT', 'SE_LMSHARE', 'SE_OWNER_DEFAULTED', 'SE_PRINTER', 'SE_PRIVILEGE_ENABLED', 'SE_PRIVILEGE_ENABLED_BY_DEFAULT', 'SE_PRIVILEGE_REMOVED', 'SE_PRIVILEGE_USED_FOR_ACCESS', 'SE_PROVIDER_DEFINED_OBJECT', 'SE_REGISTRY_KEY', 'SE_REGISTRY_WOW64_32KEY', 'SE_SACL_AUTO_INHERITED', 'SE_SACL_DEFAULTED', 'SE_SACL_PRESENT', 'SE_SACL_PROTECTED', 'SE_SELF_RELATIVE', 'SE_SERVICE', 'SE_UNKNOWN_OBJECT_TYPE', 'SE_WINDOW_OBJECT', 'SE_WMIGUID_OBJECT', 'SECPKG_CRED_BOTH', 'SECPKG_CRED_INBOUND', 'SECPKG_CRED_OUTBOUND', 'SECPKG_FLAG_ACCEPT_WIN32_NAME', 'SECPKG_FLAG_CLIENT_ONLY', 'SECPKG_FLAG_CONNECTION', 'SECPKG_FLAG_DATAGRAM', 'SECPKG_FLAG_EXTENDED_ERROR', 'SECPKG_FLAG_IMPERSONATION', 'SECPKG_FLAG_INTEGRITY', 'SECPKG_FLAG_MULTI_REQUIRED', 'SECPKG_FLAG_PRIVACY', 'SECPKG_FLAG_STREAM', 'SECPKG_FLAG_TOKEN_ONLY', 'SECURITY_CREATOR_SID_AUTHORITY', 'SECURITY_LOCAL_SID_AUTHORITY', 'SECURITY_NON_UNIQUE_AUTHORITY', 'SECURITY_NT_AUTHORITY', 'SECURITY_NULL_SID_AUTHORITY', 'SECURITY_RESOURCE_MANAGER_AUTHORITY', 'SECURITY_WORLD_SID_AUTHORITY', 'SecurityAnonymous', 'SecurityDelegation', 'SecurityIdentification', 'SecurityImpersonation', 'SET_ACCESS', 'SET_AUDIT_FAILURE', 'SET_AUDIT_SUCCESS', 'SidTypeAlias', 'SidTypeComputer', 'SidTypeDeletedAccount', 'SidTypeDomain', 'SidTypeGroup', 'SidTypeInvalid', 'SidTypeUnknown', 'SidTypeUser', 'SidTypeWellKnownGroup', 'STYPE_DEVICE', 'STYPE_DISKTREE', 'STYPE_IPC', 'STYPE_PRINTQ', 'STYPE_SPECIAL', 'STYPE_TEMPORARY', 'SUB_CONTAINERS_AND_OBJECTS_INHERIT', 'SUB_CONTAINERS_ONLY_INHERIT', 'SUB_OBJECTS_ONLY_INHERIT', 'SUCCESSFUL_ACCESS_ACE_FLAG', 'SYSTEM_AUDIT_ACE_TYPE', 'SYSTEM_AUDIT_OBJECT_ACE_TYPE', 'TOKEN_ADJUST_DEFAULT', 'TOKEN_ADJUST_GROUPS', 'TOKEN_ADJUST_PRIVILEGES', 'TOKEN_ALL_ACCESS', 'TOKEN_ASSIGN_PRIMARY', 'TOKEN_DUPLICATE', 'TOKEN_EXECUTE', 'TOKEN_IMPERSONATE', 'TOKEN_QUERY', 'TOKEN_QUERY_SOURCE', 'TOKEN_READ', 'TOKEN_WRITE', 'TokenImpersonation', 'TokenPrimary', 'TrustedControllersInformation', 'TrustedDomainAuthInformation', 'TrustedDomainAuthInformationInternal', 'TrustedDomainFullInformation', 'TrustedDomainFullInformation2Internal', 'TrustedDomainFullInformationInternal', 'TrustedDomainInformationBasic', 'TrustedDomainInformationEx', 'TrustedDomainInformationEx2Internal', 'TrustedDomainNameInformation', 'TrustedPasswordInformation', 'TrustedPosixOffsetInformation', 'TRUSTEE_BAD_FORM', 'TRUSTEE_IS_ALIAS', 'TRUSTEE_IS_COMPUTER', 'TRUSTEE_IS_DELETED', 'TRUSTEE_IS_DOMAIN', 'TRUSTEE_IS_GROUP', 'TRUSTEE_IS_INVALID', 'TRUSTEE_IS_NAME', 'TRUSTEE_IS_OBJECTS_AND_NAME', 'TRUSTEE_IS_OBJECTS_AND_SID', 'TRUSTEE_IS_SID', 'TRUSTEE_IS_UNKNOWN', 'TRUSTEE_IS_USER', 'TRUSTEE_IS_WELL_KNOWN_GROUP', 'UNPROTECTED_DACL_SECURITY_INFORMATION', 'UNPROTECTED_SACL_SECURITY_INFORMATION']
from typing import *
from win32helper.win32typing import *
"""An interface to the win32 security API's"""


def DsGetSpn(ServiceType:'int',ServiceClass:'str',ServiceName:'str',InstancePort:'int'=0,InstanceNames:'Tuple[str, ...]'=None,InstancePorts:'Tuple[int, ...]'=None) -> 'Tuple[str, ...]':
    """
    None

Args:

      ServiceType(int):Type of Spn to create, one of the DS_SPN_* constants
      ServiceClass(str):Arbitrary string that describes type of service, eg http
      ServiceName(str):Name of service, can be None (not required for DS_SPN_*_HOST Spn's)
      InstancePort(int):Port nbr for service instance, use 0 for no port
      InstanceNames(Tuple[str, ...]):A sequence of service instance names, can be None - not required for for host Spn's
      InstancePorts(Tuple[int, ...]):A sequence of extra instance ports.  If specified, must be same length as InstanceNames.

Returns:

      Tuple[str, ...]
        
    """
    pass
        

def DsWriteAccountSpn(hDS:'PyDS_HANDLE',Operation:'int',Account:'str',Spns:'Tuple[str, ...]') -> 'None':
    """
    Associates a set of service principal names with an account

Args:

      hDS(PyDS_HANDLE):Directory service handle as returned from win32security::DsBind
      Operation(int):Constant from DS_SPN_WRITE_OP enum
      Account(str):Distinguished name of account whose Spn's will be modified
      Spns(Tuple[str, ...]):A sequence of target Spn's as returned by win32security::DsGetSpn

Returns:

      None
        
    """
    pass
        

def DsBind(DomainController:'str',DnsDomainName:'str') -> 'PyDS_HANDLE':
    """
    Creates a connection to a directory service

Args:

      DomainController(str):Name of domain controller to contact, can be None
      DnsDomainName(str):Dotted name of domain to bind to, can be None

Returns:

      PyDS_HANDLE
        
    """
    pass
        

def DsUnBind(hDS:'PyDS_HANDLE') -> 'None':
    """
    None

Args:

      hDS(PyDS_HANDLE):A handle to a directory service as returned by win32security::DsBind

Returns:

      None
        
    """
    pass
        

def DsGetDcName(computerName:'str'=None,domainName:'str'=None,domainGUID:'PyIID'=None,siteName:'str'=None,flags:'int'=0) -> 'dict':
    """
    Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.

Args:

      computerName(str):
      domainName(str):
      domainGUID(PyIID):
      siteName(str):
      flags(int):CommentsThis function supports keyword arguments.

Returns:

      dict
        
    """
    pass
        

def DsCrackNames(hds:'PyDS_HANDLE',flags:'int',formatOffered:'int',formatDesired:'int',names:'List[Any]') -> 'Tuple[Any, Any, Any]':
    """
    Converts an array of directory service object names from one format to another.

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind
      flags(int):
      formatOffered(int):
      formatDesired(int):
      names(List[Any]):

Returns:

      Tuple[Any, Any, Any]
        
    """
    pass
        

def DsListInfoForServer(hds:'PyDS_HANDLE',server:'str') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    Lists miscellaneous information for a server.

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind
      server(str):

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def DsListServersInSite(hds:'PyDS_HANDLE',site:'str') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    None

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind
      site(str):

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def DsListServersInSite(hds:'PyDS_HANDLE',site:'str') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    None

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind
      site(str):

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def DsListServersInSite(hds:'PyDS_HANDLE',site:'str') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    None

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind
      site(str):

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def DsListRoles(hds:'PyDS_HANDLE') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    None

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def DsListDomainsInSite(hds:'PyDS_HANDLE') -> 'List[PyDS_NAME_RESULT_ITEM]':
    """
    None

Args:

      hds(PyDS_HANDLE):Directory service handle as returned by win32security::DsBind

Returns:

      List[PyDS_NAME_RESULT_ITEM]
        
    """
    pass
        

def ACL(bufSize:'int'=64) -> 'PyACL':
    """
    None

Args:

      bufSize(int):The size of the buffer for the ACL.

Returns:

      PyACL
        
    """
    pass
        

def SID() -> 'PySID':
    """
    None

Args:



Returns:

      PySID
        
    """
    pass
        

def SECURITY_ATTRIBUTES() -> 'PySECURITY_ATTRIBUTES':
    """
    None

Args:



Returns:

      PySECURITY_ATTRIBUTES
        
    """
    pass
        

def SECURITY_DESCRIPTOR() -> 'PySECURITY_DESCRIPTOR':
    """
    None

Args:



Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def ImpersonateNamedPipeClient(handle:'int') -> 'None':
    """
    Impersonates a named-pipe client application.

Args:

      handle(int):handle of a named pipe.

Returns:

      None
        
    """
    pass
        

def ImpersonateLoggedOnUser(handle:'int') -> 'None':
    """
    Impersonates a logged on user.

Args:

      handle(int):Handle to a token that represents a logged-on user

Returns:

      None
        
    """
    pass
        

def ImpersonateAnonymousToken(ThreadHandle:'int') -> 'None':
    """
    Cause a thread to act in the security context of an anonymous token

Args:

      ThreadHandle(int):Handle to thread that will

Returns:

      None
        
    """
    pass
        

def IsTokenRestricted(TokenHandle:'int') -> 'bool':
    """
    Checks if a token contains restricted sids

Args:

      TokenHandle(int):Handle to an access token

Returns:

      bool
        
    """
    pass
        

def RevertToSelf() -> 'None':
    """
    Terminates the impersonation of a client application.

Args:



Returns:

      None
        
    """
    pass
        

def LogonUser(Username:'str',Domain:'str',Password:'str',LogonType:'int',LogonProvider:'int') -> 'int':
    """
    Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.

Args:

      Username(str):The name of the user account to log on to. This may also be a marshalled credential (see win32cred::CredMarshalCredential).
      Domain(str):The name of the domain, or None for the current domain
      Password(str):User's password.  Use a blank string if Username contains a marshalled credential.
      LogonType(int):One of LOGON32_LOGON_* values
      LogonProvider(int):One of LOGON32_PROVIDER_* valuesCommentsAccepts keyword argsOn Windows 2000 and earlier, the calling process must have SE_TCB_NAME privilege.

Returns:

      int
        
    """
    pass
        

def LogonUserEx(Username:'str',Domain:'str',Password:'str',LogonType:'int',LogonProvider:'int') -> 'Tuple[int, PySID, str, dict]':
    """
    Log a user onto the local machine,

Args:

      Username(str):User account, may be specified as a UPN (user@domain.com). This may also be a marshalled credential (see win32cred::CredMarshalCredential).
      Domain(str):User's domain. Can be None if Username is a full UPN.
      Password(str):User's password.  Use a blank string if Username contains a marshalled credential.
      LogonType(int):One of LOGON32_LOGON_* values
      LogonProvider(int):One of LOGON32_PROVIDER_* valuesCommentsRequires Windows XP or laterAccepts keyword argsReturn ValueReturns access token, logon sid, profile buffer, and process quotas. Format of the profile buffer is not known, so returned object is subject to change.

Returns:

      Tuple[int, PySID, str, dict]:One of LOGON32_PROVIDER_* valuesComments

Requires Windows XP or later

Accepts keyword args
Return ValueReturns access token, logon sid, profile buffer, and process quotas. 

Format of the profile buffer is not known, so returned object is subject to change.

        
    """
    pass
        

def LookupAccountName(systemName:'str',accountName:'str') -> 'Tuple[PySID, str, int]':
    """
    Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.

Args:

      systemName(str):The system name, or None
      accountName(str):The account nameReturn ValueThe result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

Returns:

      Tuple[PySID, str, int]:The account nameReturn ValueThe result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

        
    """
    pass
        

def LookupAccountSid(systemName:'str',sid:'PySID') -> 'Tuple[str, str, int]':
    """
    Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.

Args:

      systemName(str):The system name, or None
      sid(PySID):The SIDReturn ValueThe result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

Returns:

      Tuple[str, str, int]:The SIDReturn ValueThe result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

        
    """
    pass
        

def GetBinarySid(SID:'str') -> 'PySID':
    """
    Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.

Args:

      SID(str):Textual representation of a SID. Textual SID example: S-1-5-32-544

Returns:

      PySID
        
    """
    pass
        

def SetSecurityInfo(handle:'Union[int]',ObjectType:'int',SecurityInfo:'int',Owner:'PySID',Group:'PySID',Dacl:'PyACL',Sacl:'PyACL') -> 'None':
    """
    Sets security info for an object by handle

Args:

      handle(Union[int]):Handle to object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constants
      Owner(PySID):Sid to set as owner of object, can be None
      Group(PySID):Group Sid, can be None
      Dacl(PyACL):Discretionary ACL to set for object, can be None
      Sacl(PyACL):System Audit ACL to set for object, can be None

Returns:

      None
        
    """
    pass
        

def GetSecurityInfo(handle:'Union[int]',ObjectType:'int',SecurityInfo:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Retrieve security info for an object by handle

Args:

      handle(Union[int]):Handle to object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constantsCommentsSeparate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def SetNamedSecurityInfo(ObjectName:'Union[Any, str]',ObjectType:'int',SecurityInfo:'int',Owner:'PySID',Group:'PySID',Dacl:'PyACL',Sacl:'PyACL') -> 'None':
    """
    Sets security info for an object by name

Args:

      ObjectName(Union[Any, str]):Name of object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constants
      Owner(PySID):Sid to set as owner of object, can be None
      Group(PySID):Group Sid, can be None
      Dacl(PyACL):Discretionary ACL to set for object, can be None
      Sacl(PyACL):System Audit ACL to set for object, can be None

Returns:

      None
        
    """
    pass
        

def GetNamedSecurityInfo(ObjectName:'Union[Any, str]',ObjectType:'int',SecurityInfo:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Retrieve security info for an object by name

Args:

      ObjectName(Union[Any, str]):Name of object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constantsCommentsSeparate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def OpenProcessToken(processHandle:'int',desiredAccess:'int') -> 'int':
    """
    Opens the access token associated with a process.

Args:

      processHandle(int):The handle of the process to open.
      desiredAccess(int):Desired access to process

Returns:

      int
        
    """
    pass
        

def LookupPrivilegeValue(systemName:'str',privilegeName:'str') -> 'LARGE_INTEGER':
    """
    Retrieves the locally unique id for a privilege name

Args:

      systemName(str):String specifying the system, use None for local machine
      privilegeName(str):String specifying the privilege (win32security.SE_*_NAME)

Returns:

      LARGE_INTEGER
        
    """
    pass
        

def LookupPrivilegeName(SystemName:'Union[str]',luid:'LARGE_INTEGER') -> 'str':
    """
    return the text name for a privilege LUID

Args:

      SystemName(Union[str]):System name, local system assumed if not specified
      luid(LARGE_INTEGER):64 bit value representing a privilege

Returns:

      str
        
    """
    pass
        

def LookupPrivilegeDisplayName(SystemName:'Union[str]',Name:'Union[str]') -> 'str':
    """
    Returns long description for a privilege name

Args:

      SystemName(Union[str]):System name, local system assumed if not specified
      Name(Union[str]):Name of privilege, Se...Privilege string constants (win32security.SE_*_NAME)

Returns:

      str
        
    """
    pass
        

def AdjustTokenPrivileges(TokenHandle:'int',bDisableAllPrivileges:'int',NewState:'PyTOKEN_PRIVILEGES') -> 'PyTOKEN_PRIVILEGES':
    """
    Enables or disables privileges for an access token.

Args:

      TokenHandle(int):Handle to an access token
      bDisableAllPrivileges(int):Flag for disabling all privileges
      NewState(PyTOKEN_PRIVILEGES):The new state, can be None if bDisableAllPrivileges is TrueCommentsAccepts keyword args.Return ValueReturns modified privileges for later restoral.  Privileges deleted from the token using SE_PRIVILEGE_REMOVED are not returned.

Returns:

      PyTOKEN_PRIVILEGES:The new state, can be None if bDisableAllPrivileges is TrueComments

Accepts keyword args.
Return ValueReturns modified privileges for later restoral.  Privileges deleted from the token using 

SE_PRIVILEGE_REMOVED are not returned.

        
    """
    pass
        

def AdjustTokenGroups(TokenHandle:'int',ResetToDefault:'Any',NewState:'PyTOKEN_GROUPS') -> 'PyTOKEN_GROUPS':
    """
    Sets the groups associated to an access token.

Args:

      TokenHandle(int):The handle to access token to be modified
      ResetToDefault(Any):Sets groups to default enabled/disabled states,
      NewState(PyTOKEN_GROUPS):Groups and attributes to be set for tokenCommentsAccepts keyword args.Return ValueReturns previous state of groups modified

Returns:

      PyTOKEN_GROUPS:Groups and attributes to be set for tokenComments

Accepts keyword args.
Return ValueReturns previous state of groups modified

        
    """
    pass
        

def GetTokenInformation(TokenHandle:'int',TokenInformationClass:'int') -> 'Any':
    """
    Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.

Args:

      TokenHandle(int):Handle to an access token.
      TokenInformationClass(int):Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.Return ValueThe following types are supportedTokenInformationClassReturn typeTokenSessionIdint - Terminal Services session idTokenSandBoxInertBooleanTokenTypeValue from TOKEN_TYPE enum (TokenPrimary,TokenImpersonation)TokenImpersonationLevelValue from SECURITY_IMPERSONATION_LEVEL enumTokenVirtualizationEnabledBooleanTokenVirtualizationAllowedBooleanTokenHasRestrictionsBooleanTokenElevationTypeint - TokenElevation* value indicating what type of token is linked toTokenUIAccessBooleanTokenUser(PySID,int)TokenOwnerPySIDTokenGroups((PySID,int),) returns a list of tuples containing (group Sid, attribute flags)TokenRestrictedSids((PySID,int),)TokenPrivileges((int,int),) returns PyTOKEN_PRIVILEGES (tuple of LUID and attribute flags for each privilege) attributes are combination of SE_PRIVILEGE_ENABLED,SE_PRIVILEGE_ENABLED_BY_DEFAULT,SE_PRIVILEGE_USED_FOR_ACCESSTokenPrimaryGroupPySIDTokenSource(string,LUID)TokenDefaultDaclPyACLTokenStatisticsdict Returns a dictionary representing a TOKEN_STATISTICS structureTokenOriginLUID identifying the logon sessionTokenLinkedTokenPyHANDLE - Returns handle to the access token to which token is linkedTokenLogonSidPySIDTokenElevationBooleanTokenIntegrityLevel(PySID, int)TokenMandatoryPolicyint (TOKEN_MANDATORY_POLICY_* flag)

Returns:

      Any:Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.Return ValueThe following types are supported



TokenInformationClass


Return type



TokenSessionIdint - Terminal Services session id
TokenSandBoxInertBoolean
TokenTypeValue from TOKEN_TYPE enum (TokenPrimary,TokenImpersonation)
TokenImpersonationLevelValue from SECURITY_IMPERSONATION_LEVEL enum
TokenVirtualizationEnabledBoolean
TokenVirtualizationAllowedBoolean
TokenHasRestrictionsBoolean
TokenElevationTypeint - TokenElevation* value indicating what type of token is linked to
TokenUIAccessBoolean
TokenUser(PySID,int)
TokenOwnerPySID
TokenGroups((PySID,int),) 

returns a list of tuples containing (group Sid, attribute flags)
TokenRestrictedSids((PySID,int),)
TokenPrivileges((int,int),) 

returns PyTOKEN_PRIVILEGES (tuple of LUID and attribute flags for each privilege) 

attributes are combination of SE_PRIVILEGE_ENABLED,SE_PRIVILEGE_ENABLED_BY_DEFAULT,SE_PRIVILEGE_USED_FOR_ACCESS
TokenPrimaryGroupPySID
TokenSource(string,LUID)
TokenDefaultDaclPyACL
TokenStatisticsdict 

Returns a dictionary representing a TOKEN_STATISTICS structure
TokenOriginLUID identifying the logon session
TokenLinkedTokenPyHANDLE - Returns handle to the access token to which token is linked
TokenLogonSidPySID
TokenElevationBoolean
TokenIntegrityLevel(PySID, int)
TokenMandatoryPolicyint (TOKEN_MANDATORY_POLICY_* flag)

        
    """
    pass
        

def OpenThreadToken(handle:'int',desiredAccess:'int',openAsSelf:'int') -> 'Any':
    """
    Opens the access token associated with a thread.

Args:

      handle(int):handle to thread
      desiredAccess(int):access to process
      openAsSelf(int):Flag for process or thread security

Returns:

      Any
        
    """
    pass
        

def SetThreadToken(Thread:'int',Token:'int') -> 'None':
    """
    Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.

Args:

      Thread(int):Handle to a thread.  Use None to indicate calling thread.
      Token(int):Handle to an impersonation token.  Use None to end impersonation.

Returns:

      None
        
    """
    pass
        

def GetFileSecurity(filename:'str',info:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

Args:

      filename(str):The name of the file
      info(int):Flags that specify the information requested.CommentsThis function reportedly will not return the INHERITED_ACE flag on some Windows XP SP1 systems Use GetNamedSecurityInfo if you encounter this problem.

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def SetFileSecurity(filename:'str',info:'int',security:'PySECURITY_DESCRIPTOR') -> 'None':
    """
    Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.

Args:

      filename(str):The name of the file
      info(int):The type of information to set.
      security(PySECURITY_DESCRIPTOR):The security information

Returns:

      None
        
    """
    pass
        

def GetUserObjectSecurity(handle:'int',info:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

Args:

      handle(int):The handle to the object
      info(int):Flags that specify the information requested.

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def SetUserObjectSecurity(handle:'int',info:'int',security:'PySECURITY_DESCRIPTOR') -> 'None':
    """
    Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.

Args:

      handle(int):The handle to an object for which security information will be set.
      info(int):The type of information to set - combination of SECURITY_INFORMATION values
      security(PySECURITY_DESCRIPTOR):The security information

Returns:

      None
        
    """
    pass
        

def GetKernelObjectSecurity(handle:'int',info:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

Args:

      handle(int):The handle to the object
      info(int):Flags that specify the information requested.

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def SetKernelObjectSecurity(handle:'int',info:'int',security:'PySECURITY_DESCRIPTOR') -> 'None':
    """
    Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.

Args:

      handle(int):The handle to an object for which security information will be set.
      info(int):The type of information to set - combination of SECURITY_INFORMATION values
      security(PySECURITY_DESCRIPTOR):The security information

Returns:

      None
        
    """
    pass
        

def SetTokenInformation(TokenHandle:'int',TokenInformationClass:'int',TokenInformation:'Any') -> 'None':
    """
    Set a specified type of information in an access token

Args:

      TokenHandle(int):Handle to an access token to be modified
      TokenInformationClass(int):Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information to be modfied
      TokenInformation(Any):Type is dependent on TokenInformationClassTokenInformationClassType of input expectedTokenOwnerPySID to be used as owner of created objectsTokenPrimaryGroupPySIDTokenDefaultDaclPyACL - Default permissions for created objectsTokenSessionIdInt - Terminal services session idTokenVirtualizationEnabledBooleanTokenVirtualizationAllowedBooleanTokenIntegrityLevelPySID_AND_ATTRIBUTES containing an integrity SID and SE_GROUP_INTEGRITY flagTokenMandatoryPolicyInt. one of TOKEN_MANDATORY_POLICY_* values

Returns:

      None
        
    """
    pass
        

def LsaOpenPolicy(system_name:'Union[str]',access_mask:'int') -> 'PyLSA_HANDLE':
    """
    Opens a policy handle for the specified system

Args:

      system_name(Union[str]):System name, local system assumed if not specified
      access_mask(int):Bitmask of requested access types

Returns:

      PyLSA_HANDLE
        
    """
    pass
        

def LsaClose(PolicyHandle:'int') -> 'None':
    """
    None

Args:

      PolicyHandle(int):An LSA policy handle as returned by win32security::LsaOpenPolicy

Returns:

      None
        
    """
    pass
        

def LsaQueryInformationPolicy(PolicyHandle:'PyLSA_HANDLE',InformationClass:'int') -> 'None':
    """
    Retrieves information from the policy handle

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      InformationClass(int):POLICY_INFORMATION_CLASS valuePOLICY_INFORMATION_CLASS valueReturn typePolicyAuditEventsInformationreturns tuple of (boolean,(int,...)) Tuple consists of a boolean indicating if auditing is enabled, and a tuple of ints, indexed by POLICY_AUDIT_EVENT_TYPE values, containing a combination of POLICY_AUDIT_EVENT_UNCHANGED, POLICY_AUDIT_EVENT_SUCCESS, POLICY_AUDIT_EVENT_FAILURE, POLICY_AUDIT_EVENT_NONEPolicyDnsDomainInformationReturns a tuple representing a POLICY_DNS_DOMAIN_INFO structPolicyPrimaryDomainInformationReturns name and SID of primary domainPolicyAccountDomainInformationReturns name and SID of account domainPolicyLsaServerRoleInformationReturns an int, one of PolicyServerRoleBackup, PolicyServerRolePrimaryPolicyModificationInformationReturns modification serial nbr and modified time of Lsa database

Returns:

      None
        
    """
    pass
        

def LsaSetInformationPolicy(PolicyHandle:'PyLSA_HANDLE',InformationClass:'int',Information:'Any') -> 'None':
    """
    Sets policy options

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      InformationClass(int):POLICY_INFORMATION_CLASS value
      Information(Any):Type is dependent on InformationClassInformationClassType of input expectedPolicyAuditEventsInformation(boolean, (int, ...)) First member imdicates whether auditing is enabled or not. Seconed member is a sequence of POLICY_AUDIT_EVENT_* flags specifying which events should be audited.  See AuditCategory* values for positions of each event type.

Returns:

      None
        
    """
    pass
        

def LsaAddAccountRights(PolicyHandle:'PyLSA_HANDLE',AccountSid:'PySID',UserRights:'Tuple[Union[Any, str], ...]') -> 'None':
    """
    Adds a list of privileges to an account

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(PySID):Account to which privs will be added
      UserRights(Tuple[Union[Any, str], ...]):Sequence of privilege names (SE_*_NAME unicode constants)CommentsAccount is created if it doesn't already exist.Accepts keyword args.

Returns:

      None
        
    """
    pass
        

def LsaRemoveAccountRights(PolicyHandle:'PyLSA_HANDLE',AccountSid:'PySID',AllRights:'int',UserRights:'Tuple[Union[Any, str], ...]') -> 'None':
    """
    Removes privs from an account

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(PySID):Account whose privileges will be removed
      AllRights(int):Boolean value indicating if all privs should be removed from account
      UserRights(Tuple[Union[Any, str], ...]):List of privilege names to be removed (SE_*_NAME unicode constants)CommentsIf AllRights parm is true, account is *deleted*Accepts keyword args.

Returns:

      None
        
    """
    pass
        

def LsaEnumerateAccountRights(PolicyHandle:'PyLSA_HANDLE',AccountSid:'PySID') -> 'List[str]':
    """
    Lists privileges held by SID

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(PySID):Security identifier of account for which to list privs

Returns:

      List[str]
        
    """
    pass
        

def LsaEnumerateAccountsWithUserRight(PolicyHandle:'PyLSA_HANDLE',UserRight:'Union[Any, str]') -> 'Tuple[PySID, ...]':
    """
    Return SIDs that hold specified priv

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      UserRight(Union[Any, str]):Name of privilege (SE_*_NAME unicode constant)

Returns:

      Tuple[PySID, ...]
        
    """
    pass
        

def ConvertSidToStringSid(Sid:'PySID') -> 'str':
    """
    Return string representation of a SID

Args:

      Sid(PySID):PySID object

Returns:

      str
        
    """
    pass
        

def ConvertStringSidToSid(StringSid:'str') -> 'PySID':
    """
    Creates a SID from a string representation

Args:

      StringSid(str):String representation of a SID

Returns:

      PySID
        
    """
    pass
        

def ConvertSecurityDescriptorToStringSecurityDescriptor(SecurityDescriptor:'PySECURITY_DESCRIPTOR',RequestedStringSDRevision:'int',SecurityInformation:'int') -> 'str':
    """
    Return string representation of a SECURITY_DESCRIPTOR

Args:

      SecurityDescriptor(PySECURITY_DESCRIPTOR):PySECURITY_DESCRIPTOR object
      RequestedStringSDRevision(int):Only SDDL_REVISION_1 currently valid
      SecurityInformation(int):Combination of bit flags from SECURITY_INFORMATION enum

Returns:

      str
        
    """
    pass
        

def ConvertStringSecurityDescriptorToSecurityDescriptor(StringSecurityDescriptor:'str',StringSDRevision:'int') -> 'PySECURITY_DESCRIPTOR':
    """
    Turns string representation of a SECURITY_DESCRIPTOR into the real thing

Args:

      StringSecurityDescriptor(str):String representation of a SECURITY_DESCRIPTOR
      StringSDRevision(int):Only SDDL_REVISION_1 currently valid

Returns:

      PySECURITY_DESCRIPTOR
        
    """
    pass
        

def LsaStorePrivateData(PolicyHandle:'PyLSA_HANDLE',KeyName:'str',PrivateData:'Any') -> 'None':
    """
    Stores encrypted unicode data under specified Lsa registry key. Returns None on success

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      KeyName(str):Registry key in which to store data
      PrivateData(Any):Unicode string to be encrypted and stored

Returns:

      None
        
    """
    pass
        

def LsaRetrievePrivateData(PolicyHandle:'PyLSA_HANDLE',KeyName:'str') -> 'str':
    """
    Retreives encrypted unicode data from Lsa registry key.

Args:

      PolicyHandle(PyLSA_HANDLE):An LSA policy handle as returned by win32security::LsaOpenPolicy
      KeyName(str):Registry key to read

Returns:

      str
        
    """
    pass
        

def LsaRegisterPolicyChangeNotification(InformationClass:'int',NotificationEventHandle:'int') -> 'None':
    """
    Register an event handle to receive policy change events

Args:

      InformationClass(int):One of POLICY_NOTIFICATION_INFORMATION_CLASS contants
      NotificationEventHandle(int):Event handle to receives notification

Returns:

      None
        
    """
    pass
        

def LsaUnregisterPolicyChangeNotification(InformationClass:'int',NotificationEventHandle:'int') -> 'None':
    """
    Stop receiving policy change notification

Args:

      InformationClass(int):POLICY_NOTIFICATION_INFORMATION_CLASS constant
      NotificationEventHandle(int):Event handle previously registered to receive policy change events

Returns:

      None
        
    """
    pass
        

def CryptEnumProviders() -> 'List[Tuple[str, int]]':
    """
    List cryptography providers

Args:



Returns:

      List[Tuple[str, int]]:win32security.CryptEnumProviders

[(PyUnicode,int),...] = CryptEnumProviders()List cryptography providers
Return ValueReturns a sequence of tuples containing provider name and type

        
    """
    pass
        

def EnumerateSecurityPackages() -> 'Tuple[dict, ...]':
    """
    List available security packages as a sequence of dictionaries representing SecPkgInfo structures

Args:



Returns:

      Tuple[dict, ...]
        
    """
    pass
        

def AllocateLocallyUniqueId() -> 'None':
    """
    Creates a new LUID

Args:



Returns:

      None
        
    """
    pass
        

def ImpersonateSelf(ImpersonationLevel:'int') -> 'None':
    """
    Assigns an impersonation token for current security context to current process

Args:

      ImpersonationLevel(int):A value from SECURITY_IMPERSONATION_LEVEL enum

Returns:

      None
        
    """
    pass
        

def DuplicateToken(ExistingTokenHandle:'int',ImpersonationLevel:'int') -> 'int':
    """
    Creates a copy of an access token with specified impersonation level

Args:

      ExistingTokenHandle(int):Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken)
      ImpersonationLevel(int):A value from SECURITY_IMPERSONATION_LEVEL enum

Returns:

      int
        
    """
    pass
        

def DuplicateTokenEx(ExistingToken:'int',ImpersonationLevel:'int',DesiredAccess:'int',TokenType:'int',TokenAttributes:'PySECURITY_ATTRIBUTES'=None) -> 'int':
    """
    Extended version of DuplicateToken.

Args:

      ExistingToken(int):Logon token opened with TOKEN_DUPLICATE access
      ImpersonationLevel(int):One of win32security.Security* values
      DesiredAccess(int):Type of access required for the handle, combination of win32security.TOKEN_* flags
      TokenType(int):Type of token to be created, TokenPrimary or TokenImpersonation
      TokenAttributes(PySECURITY_ATTRIBUTES):Specifies security and inheritance for the new handle.  None results in default DACL and no inheritance,CommentsAccepts keyword arguments

Returns:

      int
        
    """
    pass
        

def CheckTokenMembership(TokenHandle:'int',SidToCheck:'PySID') -> 'bool':
    """
    Checks if a SID is enabled in a token

Args:

      TokenHandle(int):Handle to an access token, current process token used if None
      SidToCheck(PySID):Sid to be checked for presence in token

Returns:

      bool
        
    """
    pass
        

def CreateRestrictedToken(ExistingTokenHandle:'int',Flags:'int',SidsToDisable:'Tuple[PySID_AND_ATTRIBUTES, ...]',PrivilegesToDelete:'Tuple[PyLUID_AND_ATTRIBUTES, ...]',SidsToRestrict:'Tuple[PySID_AND_ATTRIBUTES, ...]') -> 'int':
    """
    Creates a restricted copy of an access token with reduced privs - requires win2K or higher

Args:

      ExistingTokenHandle(int):Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken
      Flags(int):Valid values are zero or a combination of DISABLE_MAX_PRIVILEGE and SANDBOX_INERT
      SidsToDisable(Tuple[PySID_AND_ATTRIBUTES, ...]):Ssequence of PySID_AND_ATTRIBUTES tuples, or None
      PrivilegesToDelete(Tuple[PyLUID_AND_ATTRIBUTES, ...]):Privilege LUIDS to remove from token (attributes are ignored), or None
      SidsToRestrict(Tuple[PySID_AND_ATTRIBUTES, ...]):Sequence of PySID_AND_ATTRIBUTES tuples (attributes must be 0).  Can be None.

Returns:

      int
        
    """
    pass
        

def LsaRegisterLogonProcess(LogonProcessName:'str') -> 'PyLsaLogon_HANDLE':
    """
    Creates a trusted connection to LSA

Args:

      LogonProcessName(str):Name to use for this logon processCommentsRequires SeTcbPrivilege (and must be enabled)

Returns:

      PyLsaLogon_HANDLE
        
    """
    pass
        

def LsaConnectUntrusted() -> 'PyLsaLogon_HANDLE':
    """
    Creates untrusted connection to LSA

Args:



Returns:

      PyLsaLogon_HANDLE
        
    """
    pass
        

def LsaDeregisterLogonProcess(LsaHandle:'PyLsaLogon_HANDLE') -> 'None':
    """
    Closes connection to LSA server

Args:

      LsaHandle(PyLsaLogon_HANDLE):An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess

Returns:

      None
        
    """
    pass
        

def LsaLookupAuthenticationPackage(LsaHandle:'PyLsaLogon_HANDLE',PackageName:'str') -> 'int':
    """
    Retrieves the unique id for an authentication package

Args:

      LsaHandle(PyLsaLogon_HANDLE):An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess
      PackageName(str):Name of security package to be identified

Returns:

      int
        
    """
    pass
        

def LsaEnumerateLogonSessions() -> 'Tuple[Any, ...]':
    """
    Lists all current logon ids

Args:



Returns:

      Tuple[Any, ...]
        
    """
    pass
        

def LsaGetLogonSessionData(LogonId:'Any') -> 'Tuple[dict, ...]':
    """
    Returns information about a logon session

Args:

      LogonId(Any):An LUID identifying a logon sessionReturn ValueReturns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

Returns:

      Tuple[dict, ...]:An LUID identifying a logon sessionReturn ValueReturns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

        
    """
    pass
        

def AcquireCredentialsHandle(Principal:'Union[Any, str]',Package:'Union[Any, str]',CredentialUse:'int',LogonID:'Any',AuthData:'tuple') -> 'Tuple[PyCredHandle, PyTime]':
    """
    Creates a handle to credentials for use with SSPI

Args:

      Principal(Union[Any, str]):Use None for current security context
      Package(Union[Any, str]):Name of security package that credentials will be used with
      CredentialUse(int):Intended use of requested credentials, SECPKG_CRED_INBOUND, SECPKG_CRED_OUTBOUND, or SECPKG_CRED_BOTH
      LogonID(Any):LUID representing a logon session, can be None
      AuthData(tuple):Sequence of 3 strings: (User, Domain, Password) - use none for existing credentialsReturn ValueReturns credential handle and credential's expiration time

Returns:

      Tuple[PyCredHandle, PyTime]:Sequence of 3 strings: (User, Domain, Password) - use none for existing credentialsReturn ValueReturns credential handle and credential's expiration time

        
    """
    pass
        

def InitializeSecurityContext(Credential:'PyCredHandle',Context:'PyCtxtHandle',TargetName:'Union[Any, str]',ContextReq:'int',TargetDataRep:'int',pInput:'PySecBufferDesc',NewContext:'PyCtxtHandle',pOutput:'PySecBufferDesc') -> 'Tuple[int, int, PyTime]':
    """
    Creates a security context based on credentials created by AcquireCredentialsHandle

Args:

      Credential(PyCredHandle):A credentials handle as returned by win32security::AcquireCredentialsHandle
      Context(PyCtxtHandle):Use None on initial call, then handle returned in NewContext thereafter
      TargetName(Union[Any, str]):Target of context, security package specific - Use None with NTLM
      ContextReq(int):Combination of ISC_REQ_* flags
      TargetDataRep(int):One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP
      pInput(PySecBufferDesc):Data buffer - use None initially
      NewContext(PyCtxtHandle):Uninitialized context handle to receive output
      pOutput(PySecBufferDesc):Buffer that receives output data for subsequent callsReturn ValueReturn value is a tuple of (return code, attribute flags, expiration time)

Returns:

      Tuple[int, int, PyTime]:Buffer that receives output data for subsequent callsReturn ValueReturn value is a tuple of (return code, attribute flags, expiration time)

        
    """
    pass
        

def AcceptSecurityContext(Credential:'PyCredHandle',Context:'PyCtxtHandle',pInput:'PySecBufferDesc',ContextReq:'int',TargetDataRep:'int',NewContext:'PyCtxtHandle',pOutput:'PySecBufferDesc') -> 'Tuple[int, Any, int]':
    """
    Builds security context between server and client

Args:

      Credential(PyCredHandle):Handle to server's credentials (see AcquireCredentialsHandle)
      Context(PyCtxtHandle):Use None on initial call, then handle returned in NewContext thereafter
      pInput(PySecBufferDesc):Data buffer received from client
      ContextReq(int):Combination of ASC_REQ_* flags
      TargetDataRep(int):One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP
      NewContext(PyCtxtHandle):Uninitialized context handle to receive output
      pOutput(PySecBufferDesc):Buffer that receives output data, to be passed back as pInput on subsequent callsReturn ValueReturns a tuple of (return code, context attributes, context expiration time)

Returns:

      Tuple[int, Any, int]:Buffer that receives output data, to be passed back as pInput on subsequent callsReturn ValueReturns a tuple of (return code, context attributes, context expiration time)

        
    """
    pass
        

def QuerySecurityPackageInfo(PackageName:'Any') -> 'dict':
    """
    Retrieves parameters for a security package

Args:

      PackageName(Any):Name of the security package to queryReturn ValueReturns a dictionary representing a SecPkgInfo struct

Returns:

      dict:Name of the security package to queryReturn ValueReturns a dictionary representing a SecPkgInfo struct

        
    """
    pass
        

def LsaCallAuthenticationPackage(LsaHandle:'PyLsaLogon_HANDLE',AuthenticationPackage:'int',MessageType:'int',ProtocolSubmitBuffer:'Any') -> 'None':
    """
    Requests the services of an authentication package

Args:

      LsaHandle(PyLsaLogon_HANDLE):Lsa handle as returned by win32security::LsaRegisterLogonProcess or win32security::LsaConnectUntrusted
      AuthenticationPackage(int):Id of authentication package to call, as returned by win32security::LsaLookupAuthenticationPackage
      MessageType(int):Type of request that is being made, Kerb*Message or MsV1_0* constant
      ProtocolSubmitBuffer(Any):Type is dependent on MessageTypeCommentsMessage type is embedded in different types of submit buffers in the API call, but passed separately from python for simplicity of parsing inputMessageTypeInput typeKerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon sessionKerbRetrieveTicketMessagelong - a logon id, use 0 for current logon sessionKerbPurgeTicketCacheMessage(long, PyUnicode, PyUnicode) - tuple containing (LogonId, ServerName, RealmName)KerbRetrieveEncodedTicketMessage(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) (int, PyUnicode, int, int, int, PyCredHandle)MessageTypeReturn typeKerbQueryTicketCacheMessage(dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)KerbPurgeTicketCacheMessageNoneKerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKETKerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB_EXTERNAL_TICKETReturn ValueType of returned object is dependent on MessageType

Returns:

      None:Type is dependent on MessageTypeComments

Message type is embedded in different types of submit buffers in the API call, but passed separately 

from python for simplicity of parsing input



MessageType


Input type



KerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon session
KerbRetrieveTicketMessagelong - a logon id, use 0 for current logon session
KerbPurgeTicketCacheMessage(long, PyUnicode, PyUnicode) - tuple containing (LogonId, ServerName, RealmName)
KerbRetrieveEncodedTicketMessage(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) 

(int, PyUnicode, int, int, int, PyCredHandle)



MessageType


Return type



KerbQueryTicketCacheMessage(dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)
KerbPurgeTicketCacheMessageNone
KerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKET
KerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB_EXTERNAL_TICKET
Return ValueType of returned object is dependent on MessageType

        
    """
    pass
        

def TranslateName(accountName:'str',accountNameFormat:'int',accountNameFormat1:'int',numChars:'int'=1024) -> 'str':
    """
    Converts a directory service object name from one format to another.

Args:

      accountName(str):object name
      accountNameFormat(int):A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the accountName name.
      accountNameFormat1(int):A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the desired name.
      numChars(int):Number of Unicode characters to allocate for the return buffer.

Returns:

      str
        
    """
    pass
        

def CreateWellKnownSid(WellKnownSidType:'int',DomainSid:'PySID'=None) -> 'PySID':
    """
    Returns one of the predefined well known sids

Args:

      WellKnownSidType(int):One of the Win*Sid constants
      DomainSid(PySID):Domain for the new SID, or None for local machine

Returns:

      PySID
        
    """
    pass
        

def MapGenericMask(AccessMask:'int',GenericMapping:'Tuple[int, int, int, int]') -> 'int':
    """
    Translates generic access rights into specific rights

Args:

      AccessMask(int):A bitmask of generic rights to be interpreted according to GenericMapping
      GenericMapping(Tuple[int, int, int, int]):A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) containing the standard and specific rights that correspond to the generic rights.Return ValueThe input AccessMask will be returned with any generic access rights translated into specific equivalents

Returns:

      int:A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) 

containing the standard and specific rights that correspond to the generic rights.Return ValueThe input AccessMask will be returned with any generic access rights translated into specific equivalents

        
    """
    pass
        
ACCESS_ALLOWED_ACE_TYPE = ...
ACCESS_ALLOWED_OBJECT_ACE_TYPE = ...
ACCESS_DENIED_ACE_TYPE = ...
ACCESS_DENIED_OBJECT_ACE_TYPE = ...
ACL_REVISION = ...
ACL_REVISION_DS = ...
AuditCategoryAccountLogon = ...
AuditCategoryAccountManagement = ...
AuditCategoryDetailedTracking = ...
AuditCategoryDirectoryServiceAccess = ...
AuditCategoryLogon = ...
AuditCategoryObjectAccess = ...
AuditCategoryPolicyChange = ...
AuditCategoryPrivilegeUse = ...
AuditCategorySystem = ...
CONTAINER_INHERIT_ACE = ...
DACL_SECURITY_INFORMATION = ...
DENY_ACCESS = ...
DISABLE_MAX_PRIVILEGE = ...
DS_SPN_ADD_SPN_OP = ...
DS_SPN_DELETE_SPN_OP = ...
DS_SPN_DN_HOST = ...
DS_SPN_DNS_HOST = ...
DS_SPN_DOMAIN = ...
DS_SPN_NB_DOMAIN = ...
DS_SPN_NB_HOST = ...
DS_SPN_REPLACE_SPN_OP = ...
DS_SPN_SERVICE = ...
FAILED_ACCESS_ACE_FLAG = ...
GRANT_ACCESS = ...
GROUP_SECURITY_INFORMATION = ...
INHERIT_ONLY_ACE = ...
INHERITED_ACE = ...
LABEL_SECURITY_INFORMATION = ...
LOGON32_LOGON_BATCH = ...
LOGON32_LOGON_INTERACTIVE = ...
LOGON32_LOGON_NETWORK = ...
LOGON32_LOGON_NETWORK_CLEARTEXT = ...
LOGON32_LOGON_NEW_CREDENTIALS = ...
LOGON32_LOGON_SERVICE = ...
LOGON32_LOGON_UNLOCK = ...
LOGON32_PROVIDER_DEFAULT = ...
LOGON32_PROVIDER_WINNT35 = ...
LOGON32_PROVIDER_WINNT40 = ...
LOGON32_PROVIDER_WINNT50 = ...
NO_INHERITANCE = ...
NO_PROPAGATE_INHERIT_ACE = ...
NOT_USED_ACCESS = ...
OBJECT_INHERIT_ACE = ...
OWNER_SECURITY_INFORMATION = ...
POLICY_ALL_ACCESS = ...
POLICY_AUDIT_EVENT_FAILURE = ...
POLICY_AUDIT_EVENT_NONE = ...
POLICY_AUDIT_EVENT_SUCCESS = ...
POLICY_AUDIT_EVENT_UNCHANGED = ...
POLICY_AUDIT_LOG_ADMIN = ...
POLICY_CREATE_ACCOUNT = ...
POLICY_CREATE_PRIVILEGE = ...
POLICY_CREATE_SECRET = ...
POLICY_EXECUTE = ...
POLICY_GET_PRIVATE_INFORMATION = ...
POLICY_LOOKUP_NAMES = ...
POLICY_NOTIFICATION = ...
POLICY_READ = ...
POLICY_SERVER_ADMIN = ...
POLICY_SET_AUDIT_REQUIREMENTS = ...
POLICY_SET_DEFAULT_QUOTA_LIMITS = ...
POLICY_TRUST_ADMIN = ...
POLICY_VIEW_AUDIT_INFORMATION = ...
POLICY_VIEW_LOCAL_INFORMATION = ...
POLICY_WRITE = ...
PolicyAccountDomainInformation = ...
PolicyAuditEventsInformation = ...
PolicyAuditFullQueryInformation = ...
PolicyAuditFullSetInformation = ...
PolicyAuditLogInformation = ...
PolicyDefaultQuotaInformation = ...
PolicyDnsDomainInformation = ...
PolicyLsaServerRoleInformation = ...
PolicyModificationInformation = ...
PolicyNotifyAccountDomainInformation = ...
PolicyNotifyAuditEventsInformation = ...
PolicyNotifyDnsDomainInformation = ...
PolicyNotifyDomainEfsInformation = ...
PolicyNotifyDomainKerberosTicketInformation = ...
PolicyNotifyMachineAccountPasswordInformation = ...
PolicyNotifyServerRoleInformation = ...
PolicyPdAccountInformation = ...
PolicyPrimaryDomainInformation = ...
PolicyReplicaSourceInformation = ...
PolicyServerDisabled = ...
PolicyServerDisabled = ...
PolicyServerEnabled = ...
PolicyServerEnabled = ...
PolicyServerRoleBackup = ...
PolicyServerRolePrimary = ...
PROTECTED_DACL_SECURITY_INFORMATION = ...
PROTECTED_SACL_SECURITY_INFORMATION = ...
REVOKE_ACCESS = ...
SACL_SECURITY_INFORMATION = ...
SANDBOX_INERT = ...
SDDL_REVISION_1 = ...
SE_DACL_AUTO_INHERITED = ...
SE_DACL_DEFAULTED = ...
SE_DACL_PRESENT = ...
SE_DACL_PROTECTED = ...
SE_DS_OBJECT = ...
SE_DS_OBJECT_ALL = ...
SE_FILE_OBJECT = ...
SE_GROUP_DEFAULTED = ...
SE_GROUP_ENABLED = ...
SE_GROUP_ENABLED_BY_DEFAULT = ...
SE_GROUP_LOGON_ID = ...
SE_GROUP_MANDATORY = ...
SE_GROUP_OWNER = ...
SE_GROUP_RESOURCE = ...
SE_GROUP_USE_FOR_DENY_ONLY = ...
SE_KERNEL_OBJECT = ...
SE_LMSHARE = ...
SE_OWNER_DEFAULTED = ...
SE_PRINTER = ...
SE_PRIVILEGE_ENABLED = ...
SE_PRIVILEGE_ENABLED_BY_DEFAULT = ...
SE_PRIVILEGE_REMOVED = ...
SE_PRIVILEGE_USED_FOR_ACCESS = ...
SE_PROVIDER_DEFINED_OBJECT = ...
SE_REGISTRY_KEY = ...
SE_REGISTRY_WOW64_32KEY = ...
SE_SACL_AUTO_INHERITED = ...
SE_SACL_DEFAULTED = ...
SE_SACL_PRESENT = ...
SE_SACL_PROTECTED = ...
SE_SELF_RELATIVE = ...
SE_SERVICE = ...
SE_UNKNOWN_OBJECT_TYPE = ...
SE_WINDOW_OBJECT = ...
SE_WMIGUID_OBJECT = ...
SECPKG_CRED_BOTH = ...
SECPKG_CRED_INBOUND = ...
SECPKG_CRED_OUTBOUND = ...
SECPKG_FLAG_ACCEPT_WIN32_NAME = ...
SECPKG_FLAG_CLIENT_ONLY = ...
SECPKG_FLAG_CONNECTION = ...
SECPKG_FLAG_DATAGRAM = ...
SECPKG_FLAG_EXTENDED_ERROR = ...
SECPKG_FLAG_IMPERSONATION = ...
SECPKG_FLAG_INTEGRITY = ...
SECPKG_FLAG_MULTI_REQUIRED = ...
SECPKG_FLAG_PRIVACY = ...
SECPKG_FLAG_STREAM = ...
SECPKG_FLAG_TOKEN_ONLY = ...
SECURITY_CREATOR_SID_AUTHORITY = ...
SECURITY_LOCAL_SID_AUTHORITY = ...
SECURITY_NON_UNIQUE_AUTHORITY = ...
SECURITY_NT_AUTHORITY = ...
SECURITY_NULL_SID_AUTHORITY = ...
SECURITY_RESOURCE_MANAGER_AUTHORITY = ...
SECURITY_WORLD_SID_AUTHORITY = ...
SecurityAnonymous = ...
SecurityDelegation = ...
SecurityIdentification = ...
SecurityImpersonation = ...
SET_ACCESS = ...
SET_AUDIT_FAILURE = ...
SET_AUDIT_SUCCESS = ...
SidTypeAlias = ...
SidTypeComputer = ...
SidTypeDeletedAccount = ...
SidTypeDomain = ...
SidTypeGroup = ...
SidTypeInvalid = ...
SidTypeUnknown = ...
SidTypeUser = ...
SidTypeWellKnownGroup = ...
STYPE_DEVICE = ...
STYPE_DISKTREE = ...
STYPE_IPC = ...
STYPE_PRINTQ = ...
STYPE_SPECIAL = ...
STYPE_TEMPORARY = ...
SUB_CONTAINERS_AND_OBJECTS_INHERIT = ...
SUB_CONTAINERS_ONLY_INHERIT = ...
SUB_OBJECTS_ONLY_INHERIT = ...
SUCCESSFUL_ACCESS_ACE_FLAG = ...
SYSTEM_AUDIT_ACE_TYPE = ...
SYSTEM_AUDIT_OBJECT_ACE_TYPE = ...
TOKEN_ADJUST_DEFAULT = ...
TOKEN_ADJUST_GROUPS = ...
TOKEN_ADJUST_PRIVILEGES = ...
TOKEN_ALL_ACCESS = ...
TOKEN_ASSIGN_PRIMARY = ...
TOKEN_DUPLICATE = ...
TOKEN_EXECUTE = ...
TOKEN_IMPERSONATE = ...
TOKEN_QUERY = ...
TOKEN_QUERY_SOURCE = ...
TOKEN_READ = ...
TOKEN_WRITE = ...
TokenImpersonation = ...
TokenPrimary = ...
TrustedControllersInformation = ...
TrustedDomainAuthInformation = ...
TrustedDomainAuthInformationInternal = ...
TrustedDomainFullInformation = ...
TrustedDomainFullInformation2Internal = ...
TrustedDomainFullInformationInternal = ...
TrustedDomainInformationBasic = ...
TrustedDomainInformationEx = ...
TrustedDomainInformationEx2Internal = ...
TrustedDomainNameInformation = ...
TrustedPasswordInformation = ...
TrustedPosixOffsetInformation = ...
TRUSTEE_BAD_FORM = ...
TRUSTEE_IS_ALIAS = ...
TRUSTEE_IS_COMPUTER = ...
TRUSTEE_IS_DELETED = ...
TRUSTEE_IS_DOMAIN = ...
TRUSTEE_IS_GROUP = ...
TRUSTEE_IS_INVALID = ...
TRUSTEE_IS_NAME = ...
TRUSTEE_IS_OBJECTS_AND_NAME = ...
TRUSTEE_IS_OBJECTS_AND_SID = ...
TRUSTEE_IS_SID = ...
TRUSTEE_IS_UNKNOWN = ...
TRUSTEE_IS_USER = ...
TRUSTEE_IS_WELL_KNOWN_GROUP = ...
UNPROTECTED_DACL_SECURITY_INFORMATION = ...
UNPROTECTED_SACL_SECURITY_INFORMATION = ...