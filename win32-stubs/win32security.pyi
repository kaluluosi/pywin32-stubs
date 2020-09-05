from pywintypes import *
__all__=['DsGetSpn', 'DsWriteAccountSpn', 'DsBind', 'DsUnBind', 'DsGetDcName', 'DsCrackNames', 'DsListInfoForServer', 'DsListServersInSite', 'DsListServersInSite', 'DsListServersInSite', 'DsListRoles', 'DsListDomainsInSite', 'ACL', 'SID', 'SECURITY_ATTRIBUTES', 'SECURITY_DESCRIPTOR', 'ImpersonateNamedPipeClient', 'ImpersonateLoggedOnUser', 'ImpersonateAnonymousToken', 'IsTokenRestricted', 'RevertToSelf', 'LogonUser', 'LogonUserEx', 'LookupAccountName', 'LookupAccountSid', 'GetBinarySid', 'SetSecurityInfo', 'GetSecurityInfo', 'SetNamedSecurityInfo', 'GetNamedSecurityInfo', 'OpenProcessToken', 'LookupPrivilegeValue', 'LookupPrivilegeName', 'LookupPrivilegeDisplayName', 'AdjustTokenPrivileges', 'AdjustTokenGroups', 'GetTokenInformation', 'OpenThreadToken', 'SetThreadToken', 'GetFileSecurity', 'SetFileSecurity', 'GetUserObjectSecurity', 'SetUserObjectSecurity', 'GetKernelObjectSecurity', 'SetKernelObjectSecurity', 'SetTokenInformation', 'LsaOpenPolicy', 'LsaClose', 'LsaQueryInformationPolicy', 'LsaSetInformationPolicy', 'LsaAddAccountRights', 'LsaRemoveAccountRights', 'LsaEnumerateAccountRights', 'LsaEnumerateAccountsWithUserRight', 'ConvertSidToStringSid', 'ConvertStringSidToSid', 'ConvertSecurityDescriptorToStringSecurityDescriptor', 'ConvertStringSecurityDescriptorToSecurityDescriptor', 'LsaStorePrivateData', 'LsaRetrievePrivateData', 'LsaRegisterPolicyChangeNotification', 'LsaUnregisterPolicyChangeNotification', 'CryptEnumProviders', 'EnumerateSecurityPackages', 'AllocateLocallyUniqueId', 'ImpersonateSelf', 'DuplicateToken', 'DuplicateTokenEx', 'CheckTokenMembership', 'CreateRestrictedToken', 'LsaRegisterLogonProcess', 'LsaConnectUntrusted', 'LsaDeregisterLogonProcess', 'LsaLookupAuthenticationPackage', 'LsaEnumerateLogonSessions', 'LsaGetLogonSessionData', 'AcquireCredentialsHandle', 'InitializeSecurityContext', 'AcceptSecurityContext', 'QuerySecurityPackageInfo', 'LsaCallAuthenticationPackage', 'TranslateName', 'CreateWellKnownSid', 'MapGenericMask', 'ACCESS_ALLOWED_ACE_TYPE', 'ACCESS_ALLOWED_OBJECT_ACE_TYPE', 'ACCESS_DENIED_ACE_TYPE', 'ACCESS_DENIED_OBJECT_ACE_TYPE', 'ACL_REVISION', 'ACL_REVISION_DS', 'AuditCategoryAccountLogon', 'AuditCategoryAccountManagement', 'AuditCategoryDetailedTracking', 'AuditCategoryDirectoryServiceAccess', 'AuditCategoryLogon', 'AuditCategoryObjectAccess', 'AuditCategoryPolicyChange', 'AuditCategoryPrivilegeUse', 'AuditCategorySystem', 'CONTAINER_INHERIT_ACE', 'DACL_SECURITY_INFORMATION', 'DENY_ACCESS', 'DISABLE_MAX_PRIVILEGE', 'DS_SPN_ADD_SPN_OP', 'DS_SPN_DELETE_SPN_OP', 'DS_SPN_DN_HOST', 'DS_SPN_DNS_HOST', 'DS_SPN_DOMAIN', 'DS_SPN_NB_DOMAIN', 'DS_SPN_NB_HOST', 'DS_SPN_REPLACE_SPN_OP', 'DS_SPN_SERVICE', 'FAILED_ACCESS_ACE_FLAG', 'GRANT_ACCESS', 'GROUP_SECURITY_INFORMATION', 'INHERIT_ONLY_ACE', 'INHERITED_ACE', 'LABEL_SECURITY_INFORMATION', 'LOGON32_LOGON_BATCH', 'LOGON32_LOGON_INTERACTIVE', 'LOGON32_LOGON_NETWORK', 'LOGON32_LOGON_NETWORK_CLEARTEXT', 'LOGON32_LOGON_NEW_CREDENTIALS', 'LOGON32_LOGON_SERVICE', 'LOGON32_LOGON_UNLOCK', 'LOGON32_PROVIDER_DEFAULT', 'LOGON32_PROVIDER_WINNT35', 'LOGON32_PROVIDER_WINNT40', 'LOGON32_PROVIDER_WINNT50', 'NO_INHERITANCE', 'NO_PROPAGATE_INHERIT_ACE', 'NOT_USED_ACCESS', 'OBJECT_INHERIT_ACE', 'OWNER_SECURITY_INFORMATION', 'POLICY_ALL_ACCESS', 'POLICY_AUDIT_EVENT_FAILURE', 'POLICY_AUDIT_EVENT_NONE', 'POLICY_AUDIT_EVENT_SUCCESS', 'POLICY_AUDIT_EVENT_UNCHANGED', 'POLICY_AUDIT_LOG_ADMIN', 'POLICY_CREATE_ACCOUNT', 'POLICY_CREATE_PRIVILEGE', 'POLICY_CREATE_SECRET', 'POLICY_EXECUTE', 'POLICY_GET_PRIVATE_INFORMATION', 'POLICY_LOOKUP_NAMES', 'POLICY_NOTIFICATION', 'POLICY_READ', 'POLICY_SERVER_ADMIN', 'POLICY_SET_AUDIT_REQUIREMENTS', 'POLICY_SET_DEFAULT_QUOTA_LIMITS', 'POLICY_TRUST_ADMIN', 'POLICY_VIEW_AUDIT_INFORMATION', 'POLICY_VIEW_LOCAL_INFORMATION', 'POLICY_WRITE', 'PolicyAccountDomainInformation', 'PolicyAuditEventsInformation', 'PolicyAuditFullQueryInformation', 'PolicyAuditFullSetInformation', 'PolicyAuditLogInformation', 'PolicyDefaultQuotaInformation', 'PolicyDnsDomainInformation', 'PolicyLsaServerRoleInformation', 'PolicyModificationInformation', 'PolicyNotifyAccountDomainInformation', 'PolicyNotifyAuditEventsInformation', 'PolicyNotifyDnsDomainInformation', 'PolicyNotifyDomainEfsInformation', 'PolicyNotifyDomainKerberosTicketInformation', 'PolicyNotifyMachineAccountPasswordInformation', 'PolicyNotifyServerRoleInformation', 'PolicyPdAccountInformation', 'PolicyPrimaryDomainInformation', 'PolicyReplicaSourceInformation', 'PolicyServerDisabled', 'PolicyServerDisabled', 'PolicyServerEnabled', 'PolicyServerEnabled', 'PolicyServerRoleBackup', 'PolicyServerRolePrimary', 'PROTECTED_DACL_SECURITY_INFORMATION', 'PROTECTED_SACL_SECURITY_INFORMATION', 'REVOKE_ACCESS', 'SACL_SECURITY_INFORMATION', 'SANDBOX_INERT', 'SDDL_REVISION_1', 'SE_DACL_AUTO_INHERITED', 'SE_DACL_DEFAULTED', 'SE_DACL_PRESENT', 'SE_DACL_PROTECTED', 'SE_DS_OBJECT', 'SE_DS_OBJECT_ALL', 'SE_FILE_OBJECT', 'SE_GROUP_DEFAULTED', 'SE_GROUP_ENABLED', 'SE_GROUP_ENABLED_BY_DEFAULT', 'SE_GROUP_LOGON_ID', 'SE_GROUP_MANDATORY', 'SE_GROUP_OWNER', 'SE_GROUP_RESOURCE', 'SE_GROUP_USE_FOR_DENY_ONLY', 'SE_KERNEL_OBJECT', 'SE_LMSHARE', 'SE_OWNER_DEFAULTED', 'SE_PRINTER', 'SE_PRIVILEGE_ENABLED', 'SE_PRIVILEGE_ENABLED_BY_DEFAULT', 'SE_PRIVILEGE_REMOVED', 'SE_PRIVILEGE_USED_FOR_ACCESS', 'SE_PROVIDER_DEFINED_OBJECT', 'SE_REGISTRY_KEY', 'SE_REGISTRY_WOW64_32KEY', 'SE_SACL_AUTO_INHERITED', 'SE_SACL_DEFAULTED', 'SE_SACL_PRESENT', 'SE_SACL_PROTECTED', 'SE_SELF_RELATIVE', 'SE_SERVICE', 'SE_UNKNOWN_OBJECT_TYPE', 'SE_WINDOW_OBJECT', 'SE_WMIGUID_OBJECT', 'SECPKG_CRED_BOTH', 'SECPKG_CRED_INBOUND', 'SECPKG_CRED_OUTBOUND', 'SECPKG_FLAG_ACCEPT_WIN32_NAME', 'SECPKG_FLAG_CLIENT_ONLY', 'SECPKG_FLAG_CONNECTION', 'SECPKG_FLAG_DATAGRAM', 'SECPKG_FLAG_EXTENDED_ERROR', 'SECPKG_FLAG_IMPERSONATION', 'SECPKG_FLAG_INTEGRITY', 'SECPKG_FLAG_MULTI_REQUIRED', 'SECPKG_FLAG_PRIVACY', 'SECPKG_FLAG_STREAM', 'SECPKG_FLAG_TOKEN_ONLY', 'SECURITY_CREATOR_SID_AUTHORITY', 'SECURITY_LOCAL_SID_AUTHORITY', 'SECURITY_NON_UNIQUE_AUTHORITY', 'SECURITY_NT_AUTHORITY', 'SECURITY_NULL_SID_AUTHORITY', 'SECURITY_RESOURCE_MANAGER_AUTHORITY', 'SECURITY_WORLD_SID_AUTHORITY', 'SecurityAnonymous', 'SecurityDelegation', 'SecurityIdentification', 'SecurityImpersonation', 'SET_ACCESS', 'SET_AUDIT_FAILURE', 'SET_AUDIT_SUCCESS', 'SidTypeAlias', 'SidTypeComputer', 'SidTypeDeletedAccount', 'SidTypeDomain', 'SidTypeGroup', 'SidTypeInvalid', 'SidTypeUnknown', 'SidTypeUser', 'SidTypeWellKnownGroup', 'STYPE_DEVICE', 'STYPE_DISKTREE', 'STYPE_IPC', 'STYPE_PRINTQ', 'STYPE_SPECIAL', 'STYPE_TEMPORARY', 'SUB_CONTAINERS_AND_OBJECTS_INHERIT', 'SUB_CONTAINERS_ONLY_INHERIT', 'SUB_OBJECTS_ONLY_INHERIT', 'SUCCESSFUL_ACCESS_ACE_FLAG', 'SYSTEM_AUDIT_ACE_TYPE', 'SYSTEM_AUDIT_OBJECT_ACE_TYPE', 'TOKEN_ADJUST_DEFAULT', 'TOKEN_ADJUST_GROUPS', 'TOKEN_ADJUST_PRIVILEGES', 'TOKEN_ALL_ACCESS', 'TOKEN_ASSIGN_PRIMARY', 'TOKEN_DUPLICATE', 'TOKEN_EXECUTE', 'TOKEN_IMPERSONATE', 'TOKEN_QUERY', 'TOKEN_QUERY_SOURCE', 'TOKEN_READ', 'TOKEN_WRITE', 'TokenImpersonation', 'TokenPrimary', 'TrustedControllersInformation', 'TrustedDomainAuthInformation', 'TrustedDomainAuthInformationInternal', 'TrustedDomainFullInformation', 'TrustedDomainFullInformation2Internal', 'TrustedDomainFullInformationInternal', 'TrustedDomainInformationBasic', 'TrustedDomainInformationEx', 'TrustedDomainInformationEx2Internal', 'TrustedDomainNameInformation', 'TrustedPasswordInformation', 'TrustedPosixOffsetInformation', 'TRUSTEE_BAD_FORM', 'TRUSTEE_IS_ALIAS', 'TRUSTEE_IS_COMPUTER', 'TRUSTEE_IS_DELETED', 'TRUSTEE_IS_DOMAIN', 'TRUSTEE_IS_GROUP', 'TRUSTEE_IS_INVALID', 'TRUSTEE_IS_NAME', 'TRUSTEE_IS_OBJECTS_AND_NAME', 'TRUSTEE_IS_OBJECTS_AND_SID', 'TRUSTEE_IS_SID', 'TRUSTEE_IS_UNKNOWN', 'TRUSTEE_IS_USER', 'TRUSTEE_IS_WELL_KNOWN_GROUP', 'UNPROTECTED_DACL_SECURITY_INFORMATION', 'UNPROTECTED_SACL_SECURITY_INFORMATION']
import typing
"""An interface to the win32 security API's"""


def DsGetSpn(ServiceType:int,ServiceClass:typing.Any,ServiceName:typing.Any,InstancePort:int=0,InstanceNames:typing.Any=None,InstancePorts:typing.Any=None) -> typing.Any:
    """
    None


Args:

      ServiceType(int):Type of Spn to create, one of the DS_SPN_* constants
      ServiceClass(typing.Any):Arbitrary string that describes type of service, eg http
      ServiceName(typing.Any):Name of service, can be None (not required for DS_SPN_*_HOST Spn's)
      InstancePort(int):Port nbr for service instance, use 0 for no port
      InstanceNames(typing.Any):A sequence of service instance names, can be None - not required for for host Spn's
      InstancePorts(typing.Any):A sequence of extra instance ports.  If specified, must be same length as InstanceNames.

Returns:

      typing.Any
        
    """
    pass


def DsWriteAccountSpn(hDS:typing.Any,Operation:int,Account:typing.Any,Spns:typing.Any) -> None:
    """
    Associates a set of service principal names with an account


Args:

      hDS(typing.Any):Directory service handle as returned from win32security::DsBind
      Operation(int):Constant from DS_SPN_WRITE_OP enum
      Account(typing.Any):Distinguished name of account whose Spn's will be modified
      Spns(typing.Any):A sequence of target Spn's as returned by win32security::DsGetSpn

Returns:

      None
        
    """
    pass


def DsBind(DomainController:typing.Any,DnsDomainName:typing.Any) -> typing.Any:
    """
    Creates a connection to a directory service


Args:

      DomainController(typing.Any):Name of domain controller to contact, can be None
      DnsDomainName(typing.Any):Dotted name of domain to bind to, can be None

Returns:

      typing.Any
        
    """
    pass


def DsUnBind(hDS:typing.Any) -> None:
    """
    None


Args:

      hDS(typing.Any):A handle to a directory service as returned by win32security::DsBind

Returns:

      None
        
    """
    pass


def DsGetDcName(computerName:typing.Any=None,domainName:typing.Any=None,domainGUID:typing.Any=None,siteName:typing.Any=None,flags:int=0) -> dict:
    """
    Returns the name of a domain controller (DC) in a specified domain. 

You can supply DC selection criteria to this function to indicate preference for a DC with particular characteristics.


Args:

      computerName(typing.Any):
      domainName(typing.Any):
      domainGUID(typing.Any):
      siteName(typing.Any):
      flags(int):CommentsThis function supports keyword arguments.

Returns:

      dict
        
    """
    pass


def DsCrackNames(hds:typing.Any,flags:int,formatOffered:int,formatDesired:int,names:typing.Any) -> typing.Any:
    """
    Converts an array of directory service object names from one format to another.


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind
      flags(int):
      formatOffered(int):
      formatDesired(int):
      names(typing.Any):

Returns:

      typing.Any
        
    """
    pass


def DsListInfoForServer(hds:typing.Any,server:typing.Any) -> typing.Any:
    """
    Lists miscellaneous information for a server.


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind
      server(typing.Any):

Returns:

      typing.Any
        
    """
    pass


def DsListServersInSite(hds:typing.Any,site:typing.Any) -> typing.Any:
    """
    None


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind
      site(typing.Any):

Returns:

      typing.Any
        
    """
    pass


def DsListServersInSite(hds:typing.Any,site:typing.Any) -> typing.Any:
    """
    None


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind
      site(typing.Any):

Returns:

      typing.Any
        
    """
    pass


def DsListServersInSite(hds:typing.Any,site:typing.Any) -> typing.Any:
    """
    None


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind
      site(typing.Any):

Returns:

      typing.Any
        
    """
    pass


def DsListRoles(hds:typing.Any) -> typing.Any:
    """
    None


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind

Returns:

      typing.Any
        
    """
    pass


def DsListDomainsInSite(hds:typing.Any) -> typing.Any:
    """
    None


Args:

      hds(typing.Any):Directory service handle as returned by win32security::DsBind

Returns:

      typing.Any
        
    """
    pass


def ACL(bufSize:int=64) -> typing.Any:
    """
    None


Args:

      bufSize(int):The size of the buffer for the ACL.

Returns:

      typing.Any
        
    """
    pass


def SID() -> typing.Any:
    """
    None


Args:



Returns:

      typing.Any
        
    """
    pass


def SECURITY_ATTRIBUTES() -> typing.Any:
    """
    None


Args:



Returns:

      typing.Any
        
    """
    pass


def SECURITY_DESCRIPTOR() -> typing.Any:
    """
    None


Args:



Returns:

      typing.Any
        
    """
    pass


def ImpersonateNamedPipeClient(handle:int) -> None:
    """
    Impersonates a named-pipe client application.


Args:

      handle(int):handle of a named pipe.

Returns:

      None
        
    """
    pass


def ImpersonateLoggedOnUser(handle:typing.Any) -> None:
    """
    Impersonates a logged on user.


Args:

      handle(typing.Any):Handle to a token that represents a logged-on user

Returns:

      None
        
    """
    pass


def ImpersonateAnonymousToken(ThreadHandle:typing.Any) -> None:
    """
    Cause a thread to act in the security context of an anonymous token


Args:

      ThreadHandle(typing.Any):Handle to thread that will

Returns:

      None
        
    """
    pass


def IsTokenRestricted(TokenHandle:typing.Any) -> bool:
    """
    Checks if a token contains restricted sids


Args:

      TokenHandle(typing.Any):Handle to an access token

Returns:

      bool
        
    """
    pass


def RevertToSelf() -> None:
    """
    Terminates the impersonation of a client application.


Args:



Returns:

      None
        
    """
    pass


def LogonUser(Username:typing.Any,Domain:typing.Any,Password:typing.Any,LogonType:int,LogonProvider:int) -> int:
    """
    Attempts to log a user on to the local computer, that is, to the computer from which LogonUser was called. You cannot use LogonUser to log on to a remote computer.


Args:

      Username(typing.Any):The name of the user account to log on to. This may also be a marshalled credential (see win32cred::CredMarshalCredential).
      Domain(typing.Any):The name of the domain, or None for the current domain
      Password(typing.Any):User's password.  Use a blank string if Username contains a marshalled credential.
      LogonType(int):One of LOGON32_LOGON_* values
      LogonProvider(int):One of LOGON32_PROVIDER_* valuesCommentsAccepts keyword argsOn Windows 2000 and earlier, the calling process must have SE_TCB_NAME privilege.

Returns:

      int
        
    """
    pass


def LogonUserEx(Username:typing.Any,Domain:typing.Any,Password:typing.Any,LogonType:int,LogonProvider:int) -> typing.Any:
    """
    Log a user onto the local machine,


Args:

      Username(typing.Any):User account, may be specified as a UPN (user@domain.com). This may also be a marshalled credential (see win32cred::CredMarshalCredential).
      Domain(typing.Any):User's domain. Can be None if Username is a full UPN.
      Password(typing.Any):User's password.  Use a blank string if Username contains a marshalled credential.
      LogonType(int):One of LOGON32_LOGON_* values
      LogonProvider(int):One of LOGON32_PROVIDER_* valuesCommentsRequires Windows XP or laterAccepts keyword argsReturn ValueReturns access token, logon sid, profile buffer, and process quotas. Format of the profile buffer is not known, so returned object is subject to change.

Returns:

      typing.Any:One of LOGON32_PROVIDER_* valuesComments

Requires Windows XP or later

Accepts keyword args
Return ValueReturns access token, logon sid, profile buffer, and process quotas. 

Format of the profile buffer is not known, so returned object is subject to change.

        
    """
    pass


def LookupAccountName(systemName:str,accountName:str) -> typing.Any:
    """
    Accepts the name of a system and an account as input. It retrieves a security identifier (SID) for the account and the name of the domain on which the account was found.


Args:

      systemName(str):The system name, or None
      accountName(str):The account nameReturn ValueThe result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

Returns:

      typing.Any:The account nameReturn ValueThe result is a tuple of new SID object, the domain name where the account was found, and the type of account the SID is for.

        
    """
    pass


def LookupAccountSid(systemName:str,sid:typing.Any) -> typing.Any:
    """
    Accepts a security identifier (SID) as input. It retrieves the name of the account for this SID and the name of the first domain on which this SID is found.


Args:

      systemName(str):The system name, or None
      sid(typing.Any):The SIDReturn ValueThe result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

Returns:

      typing.Any:The SIDReturn ValueThe result is a tuple of the name, the domain name where the account was found, and the type of account the SID is for.

        
    """
    pass


def GetBinarySid(SID:str) -> typing.Any:
    """
    Accepts a SID string (eg: S-1-5-32-544) and returns the SID as a PySID object.


Args:

      SID(str):Textual representation of a SID. Textual SID example: S-1-5-32-544

Returns:

      typing.Any
        
    """
    pass


def SetSecurityInfo(handle:Union[int,typing.Any],ObjectType:int,SecurityInfo:int,Owner:typing.Any,Group:typing.Any,Dacl:typing.Any,Sacl:typing.Any) -> None:
    """
    Sets security info for an object by handle


Args:

      handle(int,typing.Any):Handle to object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constants
      Owner(typing.Any):Sid to set as owner of object, can be None
      Group(typing.Any):Group Sid, can be None
      Dacl(typing.Any):Discretionary ACL to set for object, can be None
      Sacl(typing.Any):System Audit ACL to set for object, can be None

Returns:

      None
        
    """
    pass


def GetSecurityInfo(handle:Union[int,typing.Any],ObjectType:int,SecurityInfo:int) -> typing.Any:
    """
    Retrieve security info for an object by handle


Args:

      handle(int,typing.Any):Handle to object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constantsCommentsSeparate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR

Returns:

      typing.Any
        
    """
    pass


def SetNamedSecurityInfo(ObjectName:Union[str,typing.Any],ObjectType:int,SecurityInfo:int,Owner:typing.Any,Group:typing.Any,Dacl:typing.Any,Sacl:typing.Any) -> None:
    """
    Sets security info for an object by name


Args:

      ObjectName(str,typing.Any):Name of object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constants
      Owner(typing.Any):Sid to set as owner of object, can be None
      Group(typing.Any):Group Sid, can be None
      Dacl(typing.Any):Discretionary ACL to set for object, can be None
      Sacl(typing.Any):System Audit ACL to set for object, can be None

Returns:

      None
        
    """
    pass


def GetNamedSecurityInfo(ObjectName:Union[str,typing.Any],ObjectType:int,SecurityInfo:int) -> typing.Any:
    """
    Retrieve security info for an object by name


Args:

      ObjectName(str,typing.Any):Name of object
      ObjectType(int):Value from SE_OBJECT_TYPE enum
      SecurityInfo(int):Combination of SECURITY_INFORMATION constantsCommentsSeparate owner, group, dacl, and sacl are not returned as they can be easily retrieved from the returned PySECURITY_DESCRIPTOR

Returns:

      typing.Any
        
    """
    pass


def OpenProcessToken(processHandle:int,desiredAccess:int) -> int:
    """
    Opens the access token associated with a process.


Args:

      processHandle(int):The handle of the process to open.
      desiredAccess(int):Desired access to process

Returns:

      int
        
    """
    pass


def LookupPrivilegeValue(systemName:str,privilegeName:str) -> typing.Any:
    """
    Retrieves the locally unique id for a privilege name


Args:

      systemName(str):String specifying the system, use None for local machine
      privilegeName(str):String specifying the privilege (win32security.SE_*_NAME)

Returns:

      typing.Any
        
    """
    pass


def LookupPrivilegeName(SystemName:Union[str,typing.Any],luid:typing.Any) -> str:
    """
    return the text name for a privilege LUID


Args:

      SystemName(str,typing.Any):System name, local system assumed if not specified
      luid(typing.Any):64 bit value representing a privilege

Returns:

      str
        
    """
    pass


def LookupPrivilegeDisplayName(SystemName:Union[str,typing.Any],Name:Union[str,typing.Any]) -> str:
    """
    Returns long description for a privilege name


Args:

      SystemName(str,typing.Any):System name, local system assumed if not specified
      Name(str,typing.Any):Name of privilege, Se...Privilege string constants (win32security.SE_*_NAME)

Returns:

      str
        
    """
    pass


def AdjustTokenPrivileges(TokenHandle:typing.Any,bDisableAllPrivileges:int,NewState:typing.Any) -> typing.Any:
    """
    Enables or disables privileges for an access token.


Args:

      TokenHandle(typing.Any):Handle to an access token
      bDisableAllPrivileges(int):Flag for disabling all privileges
      NewState(typing.Any):The new state, can be None if bDisableAllPrivileges is TrueCommentsAccepts keyword args.Return ValueReturns modified privileges for later restoral.  Privileges deleted from the token using SE_PRIVILEGE_REMOVED are not returned.

Returns:

      typing.Any:The new state, can be None if bDisableAllPrivileges is TrueComments

Accepts keyword args.
Return ValueReturns modified privileges for later restoral.  Privileges deleted from the token using 

SE_PRIVILEGE_REMOVED are not returned.

        
    """
    pass


def AdjustTokenGroups(TokenHandle:typing.Any,ResetToDefault:typing.Any,NewState:typing.Any) -> typing.Any:
    """
    Sets the groups associated to an access token.


Args:

      TokenHandle(typing.Any):The handle to access token to be modified
      ResetToDefault(typing.Any):Sets groups to default enabled/disabled states,
      NewState(typing.Any):Groups and attributes to be set for tokenCommentsAccepts keyword args.Return ValueReturns previous state of groups modified

Returns:

      typing.Any:Groups and attributes to be set for tokenComments

Accepts keyword args.
Return ValueReturns previous state of groups modified

        
    """
    pass


def GetTokenInformation(TokenHandle:typing.Any,TokenInformationClass:int) -> typing.Any:
    """
    Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information.


Args:

      TokenHandle(typing.Any):Handle to an access token.
      TokenInformationClass(int):Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.Return ValueThe following types are supportedTokenInformationClassReturn typeTokenSessionIdint - Terminal Services session idTokenSandBoxInertBooleanTokenTypeValue from TOKEN_TYPE enum (TokenPrimary,TokenImpersonation)TokenImpersonationLevelValue from SECURITY_IMPERSONATION_LEVEL enumTokenVirtualizationEnabledBooleanTokenVirtualizationAllowedBooleanTokenHasRestrictionsBooleanTokenElevationTypeint - TokenElevation* value indicating what type of token is linked toTokenUIAccessBooleanTokenUser(PySID,int)TokenOwnerPySIDTokenGroups((PySID,int),) returns a list of tuples containing (group Sid, attribute flags)TokenRestrictedSids((PySID,int),)TokenPrivileges((int,int),) returns PyTOKEN_PRIVILEGES (tuple of LUID and attribute flags for each privilege) attributes are combination of SE_PRIVILEGE_ENABLED,SE_PRIVILEGE_ENABLED_BY_DEFAULT,SE_PRIVILEGE_USED_FOR_ACCESSTokenPrimaryGroupPySIDTokenSource(string,LUID)TokenDefaultDaclPyACLTokenStatisticsdict Returns a dictionary representing a TOKEN_STATISTICS structureTokenOriginLUID identifying the logon sessionTokenLinkedTokenPyHANDLE - Returns handle to the access token to which token is linkedTokenLogonSidPySIDTokenElevationBooleanTokenIntegrityLevel(PySID, int)TokenMandatoryPolicyint (TOKEN_MANDATORY_POLICY_* flag)

Returns:

      typing.Any:Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information the function retrieves.Return ValueThe following types are supported



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


def OpenThreadToken(handle:typing.Any,desiredAccess:int,openAsSelf:int) -> typing.Any:
    """
    Opens the access token associated with a thread.


Args:

      handle(typing.Any):handle to thread
      desiredAccess(int):access to process
      openAsSelf(int):Flag for process or thread security

Returns:

      typing.Any
        
    """
    pass


def SetThreadToken(Thread:typing.Any,Token:typing.Any) -> None:
    """
    Assigns an impersonation token to a thread. The function 

can also cause a thread to stop using an impersonation token.


Args:

      Thread(typing.Any):Handle to a thread.  Use None to indicate calling thread.
      Token(typing.Any):Handle to an impersonation token.  Use None to end impersonation.

Returns:

      None
        
    """
    pass


def GetFileSecurity(filename:str,info:int) -> typing.Any:
    """
    Obtains specified information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.


Args:

      filename(str):The name of the file
      info(int):Flags that specify the information requested.CommentsThis function reportedly will not return the INHERITED_ACE flag on some Windows XP SP1 systems Use GetNamedSecurityInfo if you encounter this problem.

Returns:

      typing.Any
        
    """
    pass


def SetFileSecurity(filename:str,info:int,security:typing.Any) -> None:
    """
    Sets information about the security of a file or directory. The information obtained is constrained by the caller's access rights and privileges.


Args:

      filename(str):The name of the file
      info(int):The type of information to set.
      security(typing.Any):The security information

Returns:

      None
        
    """
    pass


def GetUserObjectSecurity(handle:typing.Any,info:int) -> typing.Any:
    """
    Obtains specified information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.


Args:

      handle(typing.Any):The handle to the object
      info(int):Flags that specify the information requested.

Returns:

      typing.Any
        
    """
    pass


def SetUserObjectSecurity(handle:typing.Any,info:int,security:typing.Any) -> None:
    """
    Sets information about the security of a user object. The information obtained is constrained by the caller's access rights and privileges.


Args:

      handle(typing.Any):The handle to an object for which security information will be set.
      info(int):The type of information to set - combination of SECURITY_INFORMATION values
      security(typing.Any):The security information

Returns:

      None
        
    """
    pass


def GetKernelObjectSecurity(handle:typing.Any,info:int) -> typing.Any:
    """
    Obtains specified information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.


Args:

      handle(typing.Any):The handle to the object
      info(int):Flags that specify the information requested.

Returns:

      typing.Any
        
    """
    pass


def SetKernelObjectSecurity(handle:typing.Any,info:int,security:typing.Any) -> None:
    """
    Sets information about the security of a kernel object. The information obtained is constrained by the caller's access rights and privileges.


Args:

      handle(typing.Any):The handle to an object for which security information will be set.
      info(int):The type of information to set - combination of SECURITY_INFORMATION values
      security(typing.Any):The security information

Returns:

      None
        
    """
    pass


def SetTokenInformation(TokenHandle:typing.Any,TokenInformationClass:int,TokenInformation:typing.Any) -> None:
    """
    Set a specified type of information in an access token


Args:

      TokenHandle(typing.Any):Handle to an access token to be modified
      TokenInformationClass(int):Specifies a value from the TOKEN_INFORMATION_CLASS enumerated type identifying the type of information to be modfied
      TokenInformation(typing.Any):Type is dependent on TokenInformationClassTokenInformationClassType of input expectedTokenOwnerPySID to be used as owner of created objectsTokenPrimaryGroupPySIDTokenDefaultDaclPyACL - Default permissions for created objectsTokenSessionIdInt - Terminal services session idTokenVirtualizationEnabledBooleanTokenVirtualizationAllowedBooleanTokenIntegrityLevelPySID_AND_ATTRIBUTES containing an integrity SID and SE_GROUP_INTEGRITY flagTokenMandatoryPolicyInt. one of TOKEN_MANDATORY_POLICY_* values

Returns:

      None
        
    """
    pass


def LsaOpenPolicy(system_name:Union[str,typing.Any],access_mask:int) -> typing.Any:
    """
    Opens a policy handle for the specified system


Args:

      system_name(str,typing.Any):System name, local system assumed if not specified
      access_mask(int):Bitmask of requested access types

Returns:

      typing.Any
        
    """
    pass


def LsaClose(PolicyHandle:typing.Any) -> None:
    """
    None


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy

Returns:

      None
        
    """
    pass


def LsaQueryInformationPolicy(PolicyHandle:typing.Any,InformationClass:int) -> None:
    """
    Retrieves information from the policy handle


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      InformationClass(int):POLICY_INFORMATION_CLASS valuePOLICY_INFORMATION_CLASS valueReturn typePolicyAuditEventsInformationreturns tuple of (boolean,(int,...)) Tuple consists of a boolean indicating if auditing is enabled, and a tuple of ints, indexed by POLICY_AUDIT_EVENT_TYPE values, containing a combination of POLICY_AUDIT_EVENT_UNCHANGED, POLICY_AUDIT_EVENT_SUCCESS, POLICY_AUDIT_EVENT_FAILURE, POLICY_AUDIT_EVENT_NONEPolicyDnsDomainInformationReturns a tuple representing a POLICY_DNS_DOMAIN_INFO structPolicyPrimaryDomainInformationReturns name and SID of primary domainPolicyAccountDomainInformationReturns name and SID of account domainPolicyLsaServerRoleInformationReturns an int, one of PolicyServerRoleBackup, PolicyServerRolePrimaryPolicyModificationInformationReturns modification serial nbr and modified time of Lsa database

Returns:

      None
        
    """
    pass


def LsaSetInformationPolicy(PolicyHandle:typing.Any,InformationClass:int,Information:typing.Any) -> None:
    """
    Sets policy options


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      InformationClass(int):POLICY_INFORMATION_CLASS value
      Information(typing.Any):Type is dependent on InformationClassInformationClassType of input expectedPolicyAuditEventsInformation(boolean, (int, ...)) First member imdicates whether auditing is enabled or not. Seconed member is a sequence of POLICY_AUDIT_EVENT_* flags specifying which events should be audited.  See AuditCategory* values for positions of each event type.

Returns:

      None
        
    """
    pass


def LsaAddAccountRights(PolicyHandle:typing.Any,AccountSid:typing.Any,UserRights:typing.Any) -> None:
    """
    Adds a list of privileges to an account


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(typing.Any):Account to which privs will be added
      UserRights(typing.Any):Sequence of privilege names (SE_*_NAME unicode constants)CommentsAccount is created if it doesn't already exist.Accepts keyword args.

Returns:

      None
        
    """
    pass


def LsaRemoveAccountRights(PolicyHandle:typing.Any,AccountSid:typing.Any,AllRights:int,UserRights:typing.Any) -> None:
    """
    Removes privs from an account


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(typing.Any):Account whose privileges will be removed
      AllRights(int):Boolean value indicating if all privs should be removed from account
      UserRights(typing.Any):List of privilege names to be removed (SE_*_NAME unicode constants)CommentsIf AllRights parm is true, account is *deleted*Accepts keyword args.

Returns:

      None
        
    """
    pass


def LsaEnumerateAccountRights(PolicyHandle:typing.Any,AccountSid:typing.Any) -> typing.Any:
    """
    Lists privileges held by SID


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      AccountSid(typing.Any):Security identifier of account for which to list privs

Returns:

      typing.Any
        
    """
    pass


def LsaEnumerateAccountsWithUserRight(PolicyHandle:typing.Any,UserRight:Union[str,typing.Any]) -> typing.Any:
    """
    Return SIDs that hold specified priv


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      UserRight(str,typing.Any):Name of privilege (SE_*_NAME unicode constant)

Returns:

      typing.Any
        
    """
    pass


def ConvertSidToStringSid(Sid:typing.Any) -> str:
    """
    Return string representation of a SID


Args:

      Sid(typing.Any):PySID object

Returns:

      str
        
    """
    pass


def ConvertStringSidToSid(StringSid:str) -> typing.Any:
    """
    Creates a SID from a string representation


Args:

      StringSid(str):String representation of a SID

Returns:

      typing.Any
        
    """
    pass


def ConvertSecurityDescriptorToStringSecurityDescriptor(SecurityDescriptor:typing.Any,RequestedStringSDRevision:int,SecurityInformation:int) -> str:
    """
    Return string representation of a SECURITY_DESCRIPTOR


Args:

      SecurityDescriptor(typing.Any):PySECURITY_DESCRIPTOR object
      RequestedStringSDRevision(int):Only SDDL_REVISION_1 currently valid
      SecurityInformation(int):Combination of bit flags from SECURITY_INFORMATION enum

Returns:

      str
        
    """
    pass


def ConvertStringSecurityDescriptorToSecurityDescriptor(StringSecurityDescriptor:str,StringSDRevision:int) -> typing.Any:
    """
    Turns string representation of a SECURITY_DESCRIPTOR into the real thing


Args:

      StringSecurityDescriptor(str):String representation of a SECURITY_DESCRIPTOR
      StringSDRevision(int):Only SDDL_REVISION_1 currently valid

Returns:

      typing.Any
        
    """
    pass


def LsaStorePrivateData(PolicyHandle:typing.Any,KeyName:str,PrivateData:typing.Any) -> None:
    """
    Stores encrypted unicode data under specified Lsa registry key. Returns None on success


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      KeyName(str):Registry key in which to store data
      PrivateData(typing.Any):Unicode string to be encrypted and stored

Returns:

      None
        
    """
    pass


def LsaRetrievePrivateData(PolicyHandle:typing.Any,KeyName:str) -> str:
    """
    Retreives encrypted unicode data from Lsa registry key.


Args:

      PolicyHandle(typing.Any):An LSA policy handle as returned by win32security::LsaOpenPolicy
      KeyName(str):Registry key to read

Returns:

      str
        
    """
    pass


def LsaRegisterPolicyChangeNotification(InformationClass:int,NotificationEventHandle:typing.Any) -> None:
    """
    Register an event handle to receive policy change events


Args:

      InformationClass(int):One of POLICY_NOTIFICATION_INFORMATION_CLASS contants
      NotificationEventHandle(typing.Any):Event handle to receives notification

Returns:

      None
        
    """
    pass


def LsaUnregisterPolicyChangeNotification(InformationClass:int,NotificationEventHandle:typing.Any) -> None:
    """
    Stop receiving policy change notification


Args:

      InformationClass(int):POLICY_NOTIFICATION_INFORMATION_CLASS constant
      NotificationEventHandle(typing.Any):Event handle previously registered to receive policy change events

Returns:

      None
        
    """
    pass


def CryptEnumProviders() -> typing.Any:
    """
    List cryptography providers


Args:



Returns:

      typing.Any:win32security.CryptEnumProviders

[(PyUnicode,int),...] = CryptEnumProviders()List cryptography providers
Return ValueReturns a sequence of tuples containing provider name and type

        
    """
    pass


def EnumerateSecurityPackages() -> typing.Any:
    """
    List available security packages as a sequence of dictionaries representing SecPkgInfo structures


Args:



Returns:

      typing.Any
        
    """
    pass


def AllocateLocallyUniqueId() -> None:
    """
    Creates a new LUID


Args:



Returns:

      None
        
    """
    pass


def ImpersonateSelf(ImpersonationLevel:int) -> None:
    """
    Assigns an impersonation token for current security context to current process


Args:

      ImpersonationLevel(int):A value from SECURITY_IMPERSONATION_LEVEL enum

Returns:

      None
        
    """
    pass


def DuplicateToken(ExistingTokenHandle:typing.Any,ImpersonationLevel:int) -> int:
    """
    Creates a copy of an access token with specified impersonation level


Args:

      ExistingTokenHandle(typing.Any):Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken)
      ImpersonationLevel(int):A value from SECURITY_IMPERSONATION_LEVEL enum

Returns:

      int
        
    """
    pass


def DuplicateTokenEx(ExistingToken:typing.Any,ImpersonationLevel:int,DesiredAccess:int,TokenType:int,TokenAttributes:typing.Any=None) -> int:
    """
    Extended version of DuplicateToken.


Args:

      ExistingToken(typing.Any):Logon token opened with TOKEN_DUPLICATE access
      ImpersonationLevel(int):One of win32security.Security* values
      DesiredAccess(int):Type of access required for the handle, combination of win32security.TOKEN_* flags
      TokenType(int):Type of token to be created, TokenPrimary or TokenImpersonation
      TokenAttributes(typing.Any):Specifies security and inheritance for the new handle.  None results in default DACL and no inheritance,CommentsAccepts keyword arguments

Returns:

      int
        
    """
    pass


def CheckTokenMembership(TokenHandle:typing.Any,SidToCheck:typing.Any) -> bool:
    """
    Checks if a SID is enabled in a token


Args:

      TokenHandle(typing.Any):Handle to an access token, current process token used if None
      SidToCheck(typing.Any):Sid to be checked for presence in token

Returns:

      bool
        
    """
    pass


def CreateRestrictedToken(ExistingTokenHandle:typing.Any,Flags:int,SidsToDisable:typing.Any,PrivilegesToDelete:typing.Any,SidsToRestrict:typing.Any) -> int:
    """
    Creates a restricted copy of an access token with reduced privs - requires win2K or higher


Args:

      ExistingTokenHandle(typing.Any):Handle to an access token (see win32security::LogonUser,win32security::OpenProcessToken
      Flags(int):Valid values are zero or a combination of DISABLE_MAX_PRIVILEGE and SANDBOX_INERT
      SidsToDisable(typing.Any):Ssequence of PySID_AND_ATTRIBUTES tuples, or None
      PrivilegesToDelete(typing.Any):Privilege LUIDS to remove from token (attributes are ignored), or None
      SidsToRestrict(typing.Any):Sequence of PySID_AND_ATTRIBUTES tuples (attributes must be 0).  Can be None.

Returns:

      int
        
    """
    pass


def LsaRegisterLogonProcess(LogonProcessName:str) -> typing.Any:
    """
    Creates a trusted connection to LSA


Args:

      LogonProcessName(str):Name to use for this logon processCommentsRequires SeTcbPrivilege (and must be enabled)

Returns:

      typing.Any
        
    """
    pass


def LsaConnectUntrusted() -> typing.Any:
    """
    Creates untrusted connection to LSA


Args:



Returns:

      typing.Any
        
    """
    pass


def LsaDeregisterLogonProcess(LsaHandle:typing.Any) -> None:
    """
    Closes connection to LSA server


Args:

      LsaHandle(typing.Any):An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess

Returns:

      None
        
    """
    pass


def LsaLookupAuthenticationPackage(LsaHandle:typing.Any,PackageName:str) -> int:
    """
    Retrieves the unique id for an authentication package


Args:

      LsaHandle(typing.Any):An Lsa handle as returned by win32security::LsaConnectUntrusted or win32security::LsaRegisterLogonProcess
      PackageName(str):Name of security package to be identified

Returns:

      int
        
    """
    pass


def LsaEnumerateLogonSessions() -> typing.Any:
    """
    Lists all current logon ids


Args:



Returns:

      typing.Any
        
    """
    pass


def LsaGetLogonSessionData(LogonId:typing.Any) -> typing.Any:
    """
    Returns information about a logon session


Args:

      LogonId(typing.Any):An LUID identifying a logon sessionReturn ValueReturns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

Returns:

      typing.Any:An LUID identifying a logon sessionReturn ValueReturns a dictionary representing a SECURITY_LOGON_SESSION_DATA structure

        
    """
    pass


def AcquireCredentialsHandle(Principal:Union[str,typing.Any],Package:Union[str,typing.Any],CredentialUse:int,LogonID:typing.Any,AuthData:tuple) -> typing.Any:
    """
    Creates a handle to credentials for use with SSPI


Args:

      Principal(str,typing.Any):Use None for current security context
      Package(str,typing.Any):Name of security package that credentials will be used with
      CredentialUse(int):Intended use of requested credentials, SECPKG_CRED_INBOUND, SECPKG_CRED_OUTBOUND, or SECPKG_CRED_BOTH
      LogonID(typing.Any):LUID representing a logon session, can be None
      AuthData(tuple):Sequence of 3 strings: (User, Domain, Password) - use none for existing credentialsReturn ValueReturns credential handle and credential's expiration time

Returns:

      typing.Any:Sequence of 3 strings: (User, Domain, Password) - use none for existing credentialsReturn ValueReturns credential handle and credential's expiration time

        
    """
    pass


def InitializeSecurityContext(Credential:typing.Any,Context:typing.Any,TargetName:Union[str,typing.Any],ContextReq:int,TargetDataRep:int,pInput:typing.Any,NewContext:typing.Any,pOutput:typing.Any) -> typing.Any:
    """
    Creates a security context based on credentials created by AcquireCredentialsHandle


Args:

      Credential(typing.Any):A credentials handle as returned by win32security::AcquireCredentialsHandle
      Context(typing.Any):Use None on initial call, then handle returned in NewContext thereafter
      TargetName(str,typing.Any):Target of context, security package specific - Use None with NTLM
      ContextReq(int):Combination of ISC_REQ_* flags
      TargetDataRep(int):One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP
      pInput(typing.Any):Data buffer - use None initially
      NewContext(typing.Any):Uninitialized context handle to receive output
      pOutput(typing.Any):Buffer that receives output data for subsequent callsReturn ValueReturn value is a tuple of (return code, attribute flags, expiration time)

Returns:

      typing.Any:Buffer that receives output data for subsequent callsReturn ValueReturn value is a tuple of (return code, attribute flags, expiration time)

        
    """
    pass


def AcceptSecurityContext(Credential:typing.Any,Context:typing.Any,pInput:typing.Any,ContextReq:int,TargetDataRep:int,NewContext:typing.Any,pOutput:typing.Any) -> typing.Any:
    """
    Builds security context between server and client


Args:

      Credential(typing.Any):Handle to server's credentials (see AcquireCredentialsHandle)
      Context(typing.Any):Use None on initial call, then handle returned in NewContext thereafter
      pInput(typing.Any):Data buffer received from client
      ContextReq(int):Combination of ASC_REQ_* flags
      TargetDataRep(int):One of SECURITY_NATIVE_DREP,SECURITY_NETWORK_DREP
      NewContext(typing.Any):Uninitialized context handle to receive output
      pOutput(typing.Any):Buffer that receives output data, to be passed back as pInput on subsequent callsReturn ValueReturns a tuple of (return code, context attributes, context expiration time)

Returns:

      typing.Any:Buffer that receives output data, to be passed back as pInput on subsequent callsReturn ValueReturns a tuple of (return code, context attributes, context expiration time)

        
    """
    pass


def QuerySecurityPackageInfo(PackageName:typing.Any) -> dict:
    """
    Retrieves parameters for a security package


Args:

      PackageName(typing.Any):Name of the security package to queryReturn ValueReturns a dictionary representing a SecPkgInfo struct

Returns:

      dict:Name of the security package to queryReturn ValueReturns a dictionary representing a SecPkgInfo struct

        
    """
    pass


def LsaCallAuthenticationPackage(LsaHandle:typing.Any,AuthenticationPackage:int,MessageType:int,ProtocolSubmitBuffer:typing.Any) -> None:
    """
    Requests the services of an authentication package


Args:

      LsaHandle(typing.Any):Lsa handle as returned by win32security::LsaRegisterLogonProcess or win32security::LsaConnectUntrusted
      AuthenticationPackage(int):Id of authentication package to call, as returned by win32security::LsaLookupAuthenticationPackage
      MessageType(int):Type of request that is being made, Kerb*Message or MsV1_0* constant
      ProtocolSubmitBuffer(typing.Any):Type is dependent on MessageTypeCommentsMessage type is embedded in different types of submit buffers in the API call, but passed separately from python for simplicity of parsing inputMessageTypeInput typeKerbQueryTicketCacheMessagelong - a logon id, use 0 for current logon sessionKerbRetrieveTicketMessagelong - a logon id, use 0 for current logon sessionKerbPurgeTicketCacheMessage(long, PyUnicode, PyUnicode) - tuple containing (LogonId, ServerName, RealmName)KerbRetrieveEncodedTicketMessage(LogonId, TargetName, TicketFlags, CacheOptions, EncryptionType, CredentialsHandle) (int, PyUnicode, int, int, int, PyCredHandle)MessageTypeReturn typeKerbQueryTicketCacheMessage(dict,...) - Returns all tickets for the specified logon session (form is KERB_TICKET_CACHE_INFO)KerbPurgeTicketCacheMessageNoneKerbRetrieveTicketMessageReturns the ticket granting ticket for the logon session as a KERB_EXTERNAL_TICKETKerbRetrieveEncodedTicketMessageReturns specified ticket as a KERB_EXTERNAL_TICKETReturn ValueType of returned object is dependent on MessageType

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


def TranslateName(accountName:typing.Any,accountNameFormat:int,accountNameFormat1:int,numChars:int=1024) -> str:
    """
    Converts a directory service object name from one format to another.


Args:

      accountName(typing.Any):object name
      accountNameFormat(int):A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the accountName name.
      accountNameFormat1(int):A value from the EXTENDED_NAME_FORMAT enumeration type indicating the format of the desired name.
      numChars(int):Number of Unicode characters to allocate for the return buffer.

Returns:

      str
        
    """
    pass


def CreateWellKnownSid(WellKnownSidType:int,DomainSid:typing.Any=None) -> typing.Any:
    """
    Returns one of the predefined well known sids


Args:

      WellKnownSidType(int):One of the Win*Sid constants
      DomainSid(typing.Any):Domain for the new SID, or None for local machine

Returns:

      typing.Any
        
    """
    pass


def MapGenericMask(AccessMask:int,GenericMapping:typing.Any) -> int:
    """
    Translates generic access rights into specific rights


Args:

      AccessMask(int):A bitmask of generic rights to be interpreted according to GenericMapping
      GenericMapping(typing.Any):A tuple of 4 bitmasks (GenericRead, GenericWrite, GenericExecute, GenericAll) containing the standard and specific rights that correspond to the generic rights.Return ValueThe input AccessMask will be returned with any generic access rights translated into specific equivalents

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