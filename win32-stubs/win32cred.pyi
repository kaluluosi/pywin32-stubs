__all__=['CredMarshalCredential', 'CredUnmarshalCredential', 'CredIsMarshaledCredential', 'CredEnumerate', 'CredGetTargetInfo', 'CredWriteDomainCredentials', 'CredReadDomainCredentials', 'CredDelete', 'CredWrite', 'CredRead', 'CredRename', 'CredUICmdLinePromptForCredentials', 'CredUIPromptForCredentials', 'CredUIConfirmCredentials', 'CredUIReadSSOCredW', 'CredUIStoreSSOCredW', 'CredUIParseUserName']
from typing import *
from .win32typing import *
""""""


def CredMarshalCredential(CredType:'int',Credential:'Union[str]') -> 'str':
    """
    Marshals a credential into a unicode string

Args:

      CredType(int):CertCredential or UsernameTargetCredential
      Credential(Union[str]):The credential to be marshalled.  Type is dependent on CredType.CredTypeType of CredentialCertCredentialString containing the SHA1 hash of user's certificateUsernameTargetCredentialUnicode string containing a username for which credentials exist in current logon sessionCommentsCredentials with Flags that contain CRED_FLAGS_USERNAME_TARGET can be marshalled to be passed as the username to functions that normally require a username/password combination, such as win32security::LogonUser and win32net::NetUseAdd

Returns:

      str
        
    """
    pass
        

def CredUnmarshalCredential(MarshaledCredential:'str') -> 'Tuple[int, str]':
    """
    None

Args:

      MarshaledCredential(str):Unicode string containing marshaled credentialCredTypeType of output credentialsCertCredentialCharacter string containing SHA1 hash of a certificateUsernameTargetCredentialUnicode string containing usernameReturn ValueReturns the credential type and credentials.

Returns:

      Tuple[int, str]:Unicode string 

containing marshaled credential


CredType


Type of output credentials



CertCredentialCharacter string containing SHA1 hash of a certificate
UsernameTargetCredentialUnicode string containing username
Return ValueReturns the credential type and credentials.

        
    """
    pass
        

def CredIsMarshaledCredential(MarshaledCredential:'str') -> 'Any':
    """
    Checks if a string matches the form of a marshaled credential

Args:

      MarshaledCredential(str):Marshaled credential as returned by win32cred::CredMarshalCredential

Returns:

      Any
        
    """
    pass
        

def CredEnumerate(Filter:'str'=None,Flags:'int'=0) -> 'Tuple[dict, ...]':
    """
    Lists credentials for current logon session

Args:

      Filter(str):Matches credentials' target names by prefix, can be None
      Flags(int):Reserved, use 0 if passed inReturn ValueReturns a sequence of PyCREDENTIAL dictionaries

Returns:

      Tuple[dict, ...]:Reserved, use 0 if passed in
Return ValueReturns a sequence of PyCREDENTIAL dictionaries

        
    """
    pass
        

def CredGetTargetInfo(TargetName:'str',Flags:'int'=0) -> 'dict':
    """
    Determines type and location of credential target

Args:

      TargetName(str):Name of server that is target of stored credentials
      Flags(int):CRED_ALLOW_NAME_RESOLUTION, or 0CommentsThe target information will not be available until an attempt is made to authenticate against itReturn ValueReturns a PyCREDENTIAL_TARGET_INFORMATION dict

Returns:

      dict:CRED_ALLOW_NAME_RESOLUTION, or 0
Comments

The target information will not be available until an attempt is made to authenticate against it
Return ValueReturns a PyCREDENTIAL_TARGET_INFORMATION dict

        
    """
    pass
        

def CredWriteDomainCredentials(TargetInfo:'dict',Credential:'dict',Flags:'int'=0) -> 'None':
    """
    Creates or updates credential for a domain or server

Args:

      TargetInfo(dict):PyCREDENTIAL_TARGET_INFORMATION identifying the target domain. At least one of the Names is required
      Credential(dict):PyCREDENTIAL dict containing the credentials to be stored
      Flags(int):CRED_PRESERVE_CREDENTIAL_BLOB is only defined flagCommentsWhen updating a credential, to preserve a previously stored password use None or '' for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags

Returns:

      None
        
    """
    pass
        

def CredReadDomainCredentials(TargetInfo:'dict',Flags:'int'=0) -> 'Tuple[dict, ...]':
    """
    Retrieves credentials for a domain or server

Args:

      TargetInfo(dict):PyCREDENTIAL_TARGET_INFORMATION identifying a domain or server. At least one of the Names is required.
      Flags(int):CRED_CACHE_TARGET_INFORMATION is only valid flagReturn ValueReturns a sequence of PyCREDENTIAL dicts

Returns:

      Tuple[dict, ...]:CRED_CACHE_TARGET_INFORMATION is only valid flag
Return ValueReturns a sequence of PyCREDENTIAL dicts

        
    """
    pass
        

def CredDelete(TargetName:'str',Type:'int',Flags:'int'=0) -> 'None':
    """
    Deletes a stored credential

Args:

      TargetName(str):Target of credential to be deleted
      Type(int):One of the CRED_TYPE_* values
      Flags(int):Reserved, use only 0

Returns:

      None
        
    """
    pass
        

def CredWrite(Credential:'dict',Flags:'int'=0) -> 'None':
    """
    Creates or updates a stored credential

Args:

      Credential(dict):PyCREDENTIAL dict containing the credentials to be stored
      Flags(int):CRED_PRESERVE_CREDENTIAL_BLOB is only defined flagCommentsWhen updating a credential, to preserve a previously stored password use None or '' for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags

Returns:

      None
        
    """
    pass
        

def CredRead(TargetName:'str',Type:'int',Flags:'int'=0) -> 'dict':
    """
    Retrieves a stored credential

Args:

      TargetName(str):The target of the credentials to retrieve
      Type(int):One of the CRED_TYPE_* constants
      Flags(int):Reserved, use 0Return ValueReturns a PyCREDENTIAL dict

Returns:

      dict:Reserved, use 0
Return ValueReturns a PyCREDENTIAL dict

        
    """
    pass
        

def CredRename(OldTargetName:'str',NewTargetName:'str',Type:'int',Flags:'int'=0) -> 'dict':
    """
    Changes the target name of stored credentials

Args:

      OldTargetName(str):The target of credential to be renamed
      NewTargetName(str):New target for the specified credential
      Type(int):Type of the credential to be renamed (CRED_TYPE_*)
      Flags(int):Reserved, use only 0CommentsCRED_FLAGS_USERNAME_TARGET credentials can't be renamed since their TargetName and Username must be equal

Returns:

      dict
        
    """
    pass
        

def CredUICmdLinePromptForCredentials(TargetName:'str',Flags:'int',AuthError:'int'=0,UserName:'str'=None,Password:'str'=None,Save:'Any'=True) -> 'Tuple[str, str, Any]':
    """
    Prompt for 

username/passwd from a console app

Args:

      TargetName(str):Server or domain against which to authenticate
      Flags(int):Combination of CREDUI_FLAGS_* valuesCommentsThe command-line version of this function does not accept certificates, so Flags must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARDReturn ValueReturns the username and password entered, and a boolean indicating if credential was saved
      AuthError(int):Error code indicating why credentials are required, can be 0
      UserName(str):Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars
      Password(str):Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars
      Save(Any):Specifies default value for Save prompt

Returns:

      Tuple[str, str, Any]:Combination of CREDUI_FLAGS_* values
Comments

The command-line version of this function does not accept certificates, so Flags 

must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARD
Return ValueReturns the username and password entered, and a boolean indicating if credential was saved

        
    """
    pass
        

def CredUIPromptForCredentials(TargetName:'str',AuthError:'int'=0,UserName:'str'=None,Password:'str'=None,Save:'Any'=True,Flags:'int'=0,UiInfo:'dict'=None) -> 'Tuple[str, str, Any]':
    """
    Initiates dialog to request 

user credentials

Args:

      TargetName(str):Server or domain against which to authenticate
      AuthError(int):Error code indicating why credentials are required, can be 0
      UserName(str):Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars
      Password(str):Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars
      Save(Any):Specifies whether Save checkbox defaults to checked or unchecked
      Flags(int):Combination of CREDUI_FLAGS_* values
      UiInfo(dict):PyCREDUI_INFO dict for customizing the dialog, can be NoneReturn ValueReturns the username, password, and a boolean indicating if credential was persisted

Returns:

      Tuple[str, str, Any]:PyCREDUI_INFO dict for customizing the dialog, can be None
Return ValueReturns the username, password, and a boolean indicating if credential was persisted

        
    """
    pass
        

def CredUIConfirmCredentials(TargetName:'str',Confirm:'Any') -> 'None':
    """
    Confirms whether credentials entered by user are valid or not

Args:

      TargetName(str):Target of credentials that are pending confirmation
      Confirm(Any):Indicates if authentication succeededCommentsThis function should be called to confirm credentials entered via win32cred::CredUICmdLinePromptForCredentials or win32cred::CredUIPromptForCredentials if CREDUI_FLAGS_EXPECT_CONFIRMATION was passed in Flags to either function. Sequence of operations: Prompt for credentials Authenticate against target using credentials Call this function to indicate if authentication succeeded or not

Returns:

      None
        
    """
    pass
        

def CredUIReadSSOCredW(Realm:'str'=None) -> 'str':
    """
    Retrieves single sign on username

Args:

      Realm(str):Realm for which to read username, can be None

Returns:

      str
        
    """
    pass
        

def CredUIStoreSSOCredW(Realm:'str',Username:'str',Password:'str',Persist:'Any') -> 'None':
    """
    Creates a single sign on credential

Args:

      Realm(str):Realm for which to read username, can be None for default realm
      Username(str):Username for realm
      Password(str):User's password
      Persist(Any):Specifies whether to save credential

Returns:

      None
        
    """
    pass
        

def CredUIParseUserName(UserName:'str') -> 'Tuple[str, str]':
    """
    Parses a full username into domain and 

username

Args:

      UserName(str):Username as returned by win32cred::CredUIPromptForCredentialsReturn ValueReturns the username and domain

Returns:

      Tuple[str, str]:Username as returned by win32cred::CredUIPromptForCredentialsReturn ValueReturns the username and domain

        
    """
    pass
        