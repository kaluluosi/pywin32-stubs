from pywintypes import *
__all__=['CredMarshalCredential', 'CredUnmarshalCredential', 'CredIsMarshaledCredential', 'CredEnumerate', 'CredGetTargetInfo', 'CredWriteDomainCredentials', 'CredReadDomainCredentials', 'CredDelete', 'CredWrite', 'CredRead', 'CredRename', 'CredUICmdLinePromptForCredentials', 'CredUIPromptForCredentials', 'CredUIConfirmCredentials', 'CredUIReadSSOCredW', 'CredUIStoreSSOCredW', 'CredUIParseUserName']
import typing
""""""


def CredMarshalCredential(CredType:int,Credential:Union[str,typing.Any]) -> str:
    """
    Marshals a credential into a unicode string


Args:

      CredType(int):CertCredential or UsernameTargetCredential
      Credential(str,typing.Any):The credential to be marshalled.  Type is dependent on CredType.CredTypeType of CredentialCertCredentialString containing the SHA1 hash of user's certificateUsernameTargetCredentialUnicode string containing a username for which credentials exist in current logon sessionCommentsCredentials with Flags that contain CRED_FLAGS_USERNAME_TARGET can be marshalled to be passed as the username to functions that normally require a username/password combination, such as win32security::LogonUser and win32net::NetUseAdd

Returns:

      str
        
    """
    pass


def CredUnmarshalCredential(MarshaledCredential:typing.Any) -> typing.Any:
    """
    None


Args:

      MarshaledCredential(typing.Any):Unicode string containing marshaled credentialCredTypeType of output credentialsCertCredentialCharacter string containing SHA1 hash of a certificateUsernameTargetCredentialUnicode string containing usernameReturn ValueReturns the credential type and credentials.

Returns:

      typing.Any:Unicode string 

containing marshaled credential


CredType


Type of output credentials



CertCredentialCharacter string containing SHA1 hash of a certificate
UsernameTargetCredentialUnicode string containing username
Return ValueReturns the credential type and credentials.

        
    """
    pass


def CredIsMarshaledCredential(MarshaledCredential:typing.Any) -> typing.Any:
    """
    Checks if a string matches the form of a marshaled credential


Args:

      MarshaledCredential(typing.Any):Marshaled credential as returned by win32cred::CredMarshalCredential

Returns:

      typing.Any
        
    """
    pass


def CredEnumerate(Filter:typing.Any=None,Flags:int=0) -> typing.Any:
    """
    Lists credentials for current logon session


Args:

      Filter(typing.Any):Matches credentials' target names by prefix, can be None
      Flags(int):Reserved, use 0 if passed inReturn ValueReturns a sequence of PyCREDENTIAL dictionaries

Returns:

      typing.Any:Reserved, use 0 if passed in
Return ValueReturns a sequence of PyCREDENTIAL dictionaries

        
    """
    pass


def CredGetTargetInfo(TargetName:typing.Any,Flags:int=0) -> dict:
    """
    Determines type and location of credential target


Args:

      TargetName(typing.Any):Name of server that is target of stored credentials
      Flags(int):CRED_ALLOW_NAME_RESOLUTION, or 0CommentsThe target information will not be available until an attempt is made to authenticate against itReturn ValueReturns a PyCREDENTIAL_TARGET_INFORMATION dict

Returns:

      dict:CRED_ALLOW_NAME_RESOLUTION, or 0
Comments

The target information will not be available until an attempt is made to authenticate against it
Return ValueReturns a PyCREDENTIAL_TARGET_INFORMATION dict

        
    """
    pass


def CredWriteDomainCredentials(TargetInfo:dict,Credential:dict,Flags:int=0) -> None:
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


def CredReadDomainCredentials(TargetInfo:dict,Flags:int=0) -> typing.Any:
    """
    Retrieves credentials for a domain or server


Args:

      TargetInfo(dict):PyCREDENTIAL_TARGET_INFORMATION identifying a domain or server. At least one of the Names is required.
      Flags(int):CRED_CACHE_TARGET_INFORMATION is only valid flagReturn ValueReturns a sequence of PyCREDENTIAL dicts

Returns:

      typing.Any:CRED_CACHE_TARGET_INFORMATION is only valid flag
Return ValueReturns a sequence of PyCREDENTIAL dicts

        
    """
    pass


def CredDelete(TargetName:typing.Any,Type:int,Flags:int=0) -> None:
    """
    Deletes a stored credential


Args:

      TargetName(typing.Any):Target of credential to be deleted
      Type(int):One of the CRED_TYPE_* values
      Flags(int):Reserved, use only 0

Returns:

      None
        
    """
    pass


def CredWrite(Credential:dict,Flags:int=0) -> None:
    """
    Creates or updates a stored credential


Args:

      Credential(dict):PyCREDENTIAL dict containing the credentials to be stored
      Flags(int):CRED_PRESERVE_CREDENTIAL_BLOB is only defined flagCommentsWhen updating a credential, to preserve a previously stored password use None or '' for CredentialBlob member of Credential and pass CRED_PRESERVE_CREDENTIAL_BLOB in Flags

Returns:

      None
        
    """
    pass


def CredRead(TargetName:typing.Any,Type:int,Flags:int=0) -> dict:
    """
    Retrieves a stored credential


Args:

      TargetName(typing.Any):The target of the credentials to retrieve
      Type(int):One of the CRED_TYPE_* constants
      Flags(int):Reserved, use 0Return ValueReturns a PyCREDENTIAL dict

Returns:

      dict:Reserved, use 0
Return ValueReturns a PyCREDENTIAL dict

        
    """
    pass


def CredRename(OldTargetName:typing.Any,NewTargetName:typing.Any,Type:int,Flags:int=0) -> dict:
    """
    Changes the target name of stored credentials


Args:

      OldTargetName(typing.Any):The target of credential to be renamed
      NewTargetName(typing.Any):New target for the specified credential
      Type(int):Type of the credential to be renamed (CRED_TYPE_*)
      Flags(int):Reserved, use only 0CommentsCRED_FLAGS_USERNAME_TARGET credentials can't be renamed since their TargetName and Username must be equal

Returns:

      dict
        
    """
    pass


def CredUICmdLinePromptForCredentials(TargetName:typing.Any,Flags:int,AuthError:int=0,UserName:typing.Any=None,Password:typing.Any=None,Save:typing.Any=True) -> typing.Any:
    """
    Prompt for 

username/passwd from a console app


Args:

      TargetName(typing.Any):Server or domain against which to authenticate
      Flags(int):Combination of CREDUI_FLAGS_* valuesCommentsThe command-line version of this function does not accept certificates, so Flags must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARDReturn ValueReturns the username and password entered, and a boolean indicating if credential was saved
      AuthError(int):Error code indicating why credentials are required, can be 0
      UserName(typing.Any):Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars
      Password(typing.Any):Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars
      Save(typing.Any):Specifies default value for Save prompt

Returns:

      typing.Any:Combination of CREDUI_FLAGS_* values
Comments

The command-line version of this function does not accept certificates, so Flags 

must contain CREDUI_FLAGS_EXCLUDE_CERTIFICATES or CREDUI_FLAGS_REQUIRE_SMARTCARD
Return ValueReturns the username and password entered, and a boolean indicating if credential was saved

        
    """
    pass


def CredUIPromptForCredentials(TargetName:typing.Any,AuthError:int=0,UserName:typing.Any=None,Password:typing.Any=None,Save:typing.Any=True,Flags:int=0,UiInfo:dict=None) -> typing.Any:
    """
    Initiates dialog to request 

user credentials


Args:

      TargetName(typing.Any):Server or domain against which to authenticate
      AuthError(int):Error code indicating why credentials are required, can be 0
      UserName(typing.Any):Default username, can be None.  At most CREDUI_MAX_USERNAME_LENGTH chars
      Password(typing.Any):Password, can be None.  At most CREDUI_MAX_PASSWORD_LENGTH chars
      Save(typing.Any):Specifies whether Save checkbox defaults to checked or unchecked
      Flags(int):Combination of CREDUI_FLAGS_* values
      UiInfo(dict):PyCREDUI_INFO dict for customizing the dialog, can be NoneReturn ValueReturns the username, password, and a boolean indicating if credential was persisted

Returns:

      typing.Any:PyCREDUI_INFO dict for customizing the dialog, can be None
Return ValueReturns the username, password, and a boolean indicating if credential was persisted

        
    """
    pass


def CredUIConfirmCredentials(TargetName:typing.Any,Confirm:typing.Any) -> None:
    """
    Confirms whether credentials entered by user are valid or not


Args:

      TargetName(typing.Any):Target of credentials that are pending confirmation
      Confirm(typing.Any):Indicates if authentication succeededCommentsThis function should be called to confirm credentials entered via win32cred::CredUICmdLinePromptForCredentials or win32cred::CredUIPromptForCredentials if CREDUI_FLAGS_EXPECT_CONFIRMATION was passed in Flags to either function. Sequence of operations: Prompt for credentials Authenticate against target using credentials Call this function to indicate if authentication succeeded or not

Returns:

      None
        
    """
    pass


def CredUIReadSSOCredW(Realm:typing.Any=None) -> str:
    """
    Retrieves single sign on username


Args:

      Realm(typing.Any):Realm for which to read username, can be None

Returns:

      str
        
    """
    pass


def CredUIStoreSSOCredW(Realm:typing.Any,Username:typing.Any,Password:typing.Any,Persist:typing.Any) -> None:
    """
    Creates a single sign on credential


Args:

      Realm(typing.Any):Realm for which to read username, can be None for default realm
      Username(typing.Any):Username for realm
      Password(typing.Any):User's password
      Persist(typing.Any):Specifies whether to save credential

Returns:

      None
        
    """
    pass


def CredUIParseUserName(UserName:typing.Any) -> typing.Any:
    """
    Parses a full username into domain and 

username


Args:

      UserName(typing.Any):Username as returned by win32cred::CredUIPromptForCredentialsReturn ValueReturns the username and domain

Returns:

      typing.Any:Username as returned by win32cred::CredUIPromptForCredentialsReturn ValueReturns the username and domain

        
    """
    pass
