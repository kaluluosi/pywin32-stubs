__all__=['', 'CryptProtectData', 'CryptUnprotectData', 'CryptEnumProviders', 'CryptEnumProviderTypes', 'CryptGetDefaultProvider', 'CryptSetProviderEx', 'CryptAcquireContext', 'CryptFindLocalizedName', 'CertEnumSystemStore', 'CertEnumSystemStoreLocation', 'CertEnumPhysicalStore', 'CertRegisterSystemStore', 'CertUnregisterSystemStore', 'CertOpenStore', 'CertOpenSystemStore', 'CryptFindOIDInfo', 'CertAlgIdToOID', 'CertOIDToAlgId', 'CryptGetKeyIdentifierProperty', 'CryptEnumKeyIdentifierProperties', 'CryptEnumOIDInfo', 'CertAddSerializedElementToStore', 'CryptQueryObject', 'CryptDecodeMessage', 'CryptEncryptMessage', 'CryptDecryptMessage', 'CryptSignAndEncryptMessage', 'CryptVerifyMessageSignature', 'CryptGetMessageCertificates', 'CryptGetMessageSignerCount', 'CryptSignMessage', 'CryptVerifyDetachedMessageSignature', 'CryptDecryptAndVerifyMessageSignature', 'CryptEncodeObjectEx', 'CryptDecodeObjectEx', 'CertNameToStr', 'CryptFormatObject', 'PFXImportCertStore', 'PFXVerifyPassword', 'PFXIsPFXBlob', 'CryptBinaryToString', 'CryptStringToBinary']
import typing
import win32typing
"""An interface to the win32 Cryptography API"""


def CryptProtectData(DataIn:'typing.Any',DataDescr:'str'=None,OptionalEntropy:'typing.Any'=None,Reserved:'typing.Any'=None,PromptStruct:'win32typing.PyCRYPTPROTECT_PROMPTSTRUCT'=None,Flags:'typing.Any'=0) -> 'typing.Any':
    """
    Encrypts data using a session key derived from current user's logon 

credentials

Args:

      DataIn(typing.Any):Data to be encrypted.
      DataDescr(str):Description to add to the data
      OptionalEntropy(typing.Any):Extra entropy (eg password) for encryption process, can be None
      Reserved(typing.Any):Must be None
      PromptStruct(win32typing.PyCRYPTPROTECT_PROMPTSTRUCT):Contains options for UI display during encryption and decryption, can be None
      Flags(typing.Any):Combination of CRYPTPROTECT_* flags

Returns:

      typing.Any
        
    """
    pass
        

def CryptUnprotectData(DataIn:'typing.Any',OptionalEntropy:'typing.Any'=None,Reserved:'typing.Any'=None,PromptStruct:'win32typing.PyCRYPTPROTECT_PROMPTSTRUCT'=None,Flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    None

Args:

      DataIn(typing.Any):Data to be decrypted.
      OptionalEntropy(typing.Any):Extra entropy passed to CryptProtectData
      Reserved(typing.Any):Must be None
      PromptStruct(win32typing.PyCRYPTPROTECT_PROMPTSTRUCT):Contains options for UI display during encryption and decryption, can be None
      Flags(typing.Any):Combination of CRYPTPROTECT_* flagsReturn ValueThe result is a tuple of (description, data) where description is the description that was passed to win32crypt::CryptProtectData, and data is the unencrypted data.

Returns:

      typing.Tuple[typing.Any, typing.Any]:Combination of CRYPTPROTECT_* flags
Return ValueThe result is a tuple of (description, data) where description 

is the description that was passed to win32crypt::CryptProtectData, and 

data is the unencrypted data.

        
    """
    pass
        

def CryptEnumProviders() -> 'typing.List[typing.Tuple[str, typing.Any]]':
    """
    List cryptography providers

Args:



Returns:

      typing.List[typing.Tuple[str, typing.Any]]:win32crypt.CryptEnumProviders

[(PyUnicode,int),...] = CryptEnumProviders()List cryptography providers
Return ValueReturns a sequence of tuples containing provider name and type

        
    """
    pass
        

def CryptEnumProviderTypes() -> 'typing.List[typing.Tuple[str, typing.Any]]':
    """
    Lists available local cryptographic provider 

types

Args:



Returns:

      typing.List[typing.Tuple[str, typing.Any]]:win32crypt.CryptEnumProviderTypes

[(PyUnicode,int),...] = CryptEnumProviderTypes()Lists available local cryptographic provider 

types
Comments

Windows XP sp3 has a bug that causes this function to always fail with ERROR_MORE_DATA (234) 

See KB959160 for a hotfix
Return ValueReturns a sequence of tuples containing name and identifier of provider types

        
    """
    pass
        

def CryptGetDefaultProvider(ProvType:'typing.Any',Flags:'typing.Any') -> 'str':
    """
    Returns default provider for local machine or current user

Args:

      ProvType(typing.Any):Type of provider (PROV_* constant)
      Flags(typing.Any):CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT

Returns:

      str
        
    """
    pass
        

def CryptSetProviderEx(ProvName:'str',ProvType:'typing.Any',Flags:'typing.Any') -> 'None':
    """
    Sets default provider (for machine or user) for specified type

Args:

      ProvName(str):Name of new default provider (MS_*_PROV value)
      ProvType(typing.Any):One of the PROV_* provider types
      Flags(typing.Any):CRYPT_MACHINE_DEFAULT or CRYPT_USER_DEFAULT.  Combine with CRYPT_DELETE_DEFAULT to remove default.

Returns:

      None
        
    """
    pass
        

def CryptAcquireContext(Container:'str',Provider:'str',ProvType:'typing.Any',Flags:'typing.Any') -> 'win32typing.PyCRYPTPROV':
    """
    Retrieve handle to a cryptographic service provider

Args:

      Container(str):Name of key container, can be none to use a Provider's default key container (usually username)
      Provider(str):Name of cryptographic provider. (MS_*_PROV) Use None for user's default provider.
      ProvType(typing.Any):One of the PROV_* constants
      Flags(typing.Any):Combination of CRYPT_VERIFYCONTEXT,CRYPT_NEWKEYSET,CRYPT_MACHINE_KEYSET,CRYPT_DELETEKEYSET,CRYPT_SILENTReturn ValueReturns None if CRYPT_DELETEKEYSET is specified, otherwise returns a handle to the provider

Returns:

      win32typing.PyCRYPTPROV:Combination of 

CRYPT_VERIFYCONTEXT,CRYPT_NEWKEYSET,CRYPT_MACHINE_KEYSET,CRYPT_DELETEKEYSET,CRYPT_SILENTReturn ValueReturns None if CRYPT_DELETEKEYSET is specified, otherwise returns a handle to the provider

        
    """
    pass
        

def CryptFindLocalizedName(CryptName:'str') -> 'str':
    """
    Returns localized name for predefined system stores (Root, 

My, .Default, .LocalMachine)

Args:

      CryptName(str):Name of a system store

Returns:

      str
        
    """
    pass
        

def CertEnumSystemStore(dwFlags:'typing.Any',pvSystemStoreLocationPara:'typing.Any'=None) -> 'typing.List[typing.Any]':
    """
    Lists system stores

Args:

      dwFlags(typing.Any):CERT_SYSTEM_STORE_* location, can be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG
      pvSystemStoreLocationPara(typing.Any):Optional If flags contains CERT_SYSTEM_STORE_RELOCATE_FLAG must be a sequence (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA, otherwise should be a unicode store name

Returns:

      typing.List[typing.Any]
        
    """
    pass
        

def CertEnumSystemStoreLocation(Flags:'typing.Any'=0) -> 'typing.List[typing.Any]':
    """
    Lists system store locations

Args:

      Flags(typing.Any):Reserved, must be 0 if passed in

Returns:

      typing.List[typing.Any]
        
    """
    pass
        

def CertEnumPhysicalStore(pvSystemStore:'str',dwFlags:'typing.Any') -> 'typing.List[typing.Any]':
    """
    Lists physical stores on computer

Args:

      pvSystemStore(str):Name of system store to enumerate physical locations for
      dwFlags(typing.Any):CERT_SYSTEM_STORE_* constant, CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet

Returns:

      typing.List[typing.Any]
        
    """
    pass
        

def CertRegisterSystemStore(SystemStore:'str',Flags:'typing.Any') -> 'None':
    """
    Registers a certificate store

Args:

      SystemStore(str):string/unicode name of store to be registered, or a sequence of (PyHkey, unicode) representing a CERT_SYSTEM_STORE_RELOCATE_PARA struct
      Flags(typing.Any):One of the CERT_SYSTEM_STORE_* location constants, can also be combined with CERT_SYSTEM_STORE_RELOCATE_FLAG and CERT_STORE_CREATE_NEW_FLAG

Returns:

      None
        
    """
    pass
        

def CertUnregisterSystemStore(SystemStore:'str',Flags:'typing.Any') -> 'None':
    """
    Unregisters a certificate store

Args:

      SystemStore(str):Name of System store to be unregistered
      Flags(typing.Any):CERT_SYSTEM_STORE_RELOCATE_FLAG, CERT_STORE_DELETE_FLAG (CERT_SYSTEM_STORE_RELOCATE_FLAG  not supported yet)

Returns:

      None
        
    """
    pass
        

def CertOpenStore(StoreProvider:'typing.Any',MsgAndCertEncodingType:'typing.Any',CryptProv:'win32typing.PyCRYPTPROV',Flags:'typing.Any',Para:'typing.Any'=None) -> 'win32typing.PyCERTSTORE':
    """
    Opens a certificate store

Args:

      StoreProvider(typing.Any):CERT_STORE_PROV_*, currently does not accept string provider names
      MsgAndCertEncodingType(typing.Any):Only used with CERT_STORE_PROV_MSG, CERT_STORE_PROV_PKCS7, and CERT_STORE_PROV_FILENAME. Usually should be X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING
      CryptProv(win32typing.PyCRYPTPROV):Handle to a CSP, can be None to use default provider
      Flags(typing.Any):Combination of CERT_STORE_*_FLAG flags
      Para(typing.Any):PyCERT_SYSTEM_STORE_RELOCATE_PARA, or data specific to provider

Returns:

      win32typing.PyCERTSTORE
        
    """
    pass
        

def CertOpenSystemStore(SubsystemProtocol:'str',Prov:'win32typing.PyCRYPTPROV'=None) -> 'win32typing.PyCERTSTORE':
    """
    Opens most commonly used Certificate Stores

Args:

      SubsystemProtocol(str):Name of store to open, will be created if it doesn't already exist
      Prov(win32typing.PyCRYPTPROV):Handle to CSP, use None for default provider

Returns:

      win32typing.PyCERTSTORE
        
    """
    pass
        

def CryptFindOIDInfo(KeyType:'typing.Any',Key:'typing.Any',GroupId:'typing.Any'=0) -> 'typing.Any':
    """
    Returns information about an algorithm identifier or object identifier

Args:

      KeyType(typing.Any):One of CRYPT_OID_INFO_OID_KEY,CRYPT_OID_INFO_NAME_KEY,CRYPT_OID_INFO_ALGID_KEY,CRYPT_OID_INFO_SIGN_KEY
      Key(typing.Any):Type is dependent on KeyType
      GroupId(typing.Any):CRYPT_*_GROUP_ID constant, or 0Return ValueReturns a dictionary of CRYPT_OID_INFO dataKeyTypeType of KeyCRYPT_OID_INFO_OID_KEYAn szOID_* character stringCRYPT_OID_INFO_NAME_KEYA unicode nameCRYPT_OID_INFO_ALGID_KEYAn ALG_ID, one of the CALG_* integer constantsCRYPT_OID_INFO_SIGN_KEYA tuple of 2 CALG_* integers (hash algorithm, public key algorithm)

Returns:

      typing.Any:CRYPT_*_GROUP_ID constant, or 0
Return ValueReturns a dictionary of CRYPT_OID_INFO data



KeyType


Type of Key



CRYPT_OID_INFO_OID_KEYAn szOID_* character string
CRYPT_OID_INFO_NAME_KEYA unicode name
CRYPT_OID_INFO_ALGID_KEYAn ALG_ID, one of the CALG_* integer constants
CRYPT_OID_INFO_SIGN_KEYA tuple of 2 CALG_* integers (hash algorithm, public key algorithm)

        
    """
    pass
        

def CertAlgIdToOID(AlgId:'typing.Any') -> 'str':
    """
    Converts an integer ALG_ID to it's szOID_ string representation

Args:

      AlgId(typing.Any):An algorithm identifierCommentsIf there is no corresponding OID, None is returned

Returns:

      str
        
    """
    pass
        

def CertOIDToAlgId(ObjId:'str') -> 'typing.Any':
    """
    Converts a string object identfier to a numeric algorith identifier

Args:

      ObjId(str):String szOID_* identifierCommentsIf no matching ALG_ID is found, 0 is returned

Returns:

      typing.Any
        
    """
    pass
        

def CryptGetKeyIdentifierProperty(KeyIdentifier:'str',PropId:'typing.Any',Flags:'typing.Any'=0,ComputerName:'str'=None) -> 'typing.Any':
    """
    Retrieves a property from a certificate by its key 

indentifier

Args:

      KeyIdentifier(str):Hash that identifies a certificate key
      PropId(typing.Any):Property identifier, one of the CERT_*_PROP_ID values
      Flags(typing.Any):Use CRYPT_KEYID_MACHINE_FLAG for machine keyset. (CRYPT_KEYID_ALLOC_FLAG is always added to Flags)
      ComputerName(str):Name of remote computer, use None for local machineCommentsCERT_KEY_PROV_INFO_PROP_ID is only property currently supported

Returns:

      typing.Any
        
    """
    pass
        

def CryptEnumKeyIdentifierProperties(KeyIdentifier:'str'=None,PropId:'typing.Any'=0,Flags:'typing.Any'=0,ComputerName:'str'=None) -> 'typing.Any':
    """
    Enumerates private keys for certificates and their 

properties

Args:

      KeyIdentifier(str):Id of a certificate key, can be None for all keys
      PropId(typing.Any):CERT_*_PROP_ID constant. Limits returned values to specified propery, Use 0 for all
      Flags(typing.Any):Can be CRYPT_KEYID_MACHINE_FLAG to list keys for local machine, or remote machine if ComputerName is given
      ComputerName(str):Name of remote computer, use None for local machine

Returns:

      typing.Any
        
    """
    pass
        

def CryptEnumOIDInfo(GroupId:'typing.Any'=0) -> 'typing.Any':
    """
    Lists registered Object Identifiers that belong to specified group

Args:

      GroupId(typing.Any):The type of OIDs to enmerate, one of the CRYPT_*_OID_GROUP_ID constants or 0 to list all

Returns:

      typing.Any
        
    """
    pass
        

def CertAddSerializedElementToStore(CertStore:'win32typing.PyCERTSTORE',Element:'typing.Any',AddDisposition:'typing.Any',ContextTypeFlags:'typing.Any',Flags:'typing.Any'=0) -> 'win32typing.PyCERT_CONTEXT':
    """
    Imports a serialized Certificate context, 

CRL, or CTL

Args:

      CertStore(win32typing.PyCERTSTORE):Certificate Store to which the context will be added, can be None
      Element(typing.Any):Serialized data
      AddDisposition(typing.Any):one of CERT_STORE_ADD_* values
      ContextTypeFlags(typing.Any):One of CERT_STORE_*_CONTEXT_FLAG constants
      Flags(typing.Any):Reserved, use only 0CommentsCurrently only Certificate contexts are supported

Returns:

      win32typing.PyCERT_CONTEXT
        
    """
    pass
        

def CryptQueryObject(ObjectType:'typing.Any',Object:'typing.Any',ExpectedContentTypeFlags:'typing.Any',ExpectedFormatTypeFlags:'typing.Any',Flags:'typing.Any'=0) -> 'typing.Any':
    """
    Determines the cryptographic type of input data

Args:

      ObjectType(typing.Any):Type of input, CERT_QUERY_OBJECT_BLOB or CERT_QUERY_OBJECT_FILE
      Object(typing.Any):Raw data or a filename containing the data to be queried depending on ObjectType
      ExpectedContentTypeFlags(typing.Any):One of the CERT_QUERY_CONTENT_FLAG_* constants
      ExpectedFormatTypeFlags(typing.Any):One of the CERT_QUERY_FORMAT_FLAG_* constants
      Flags(typing.Any):Reserved, use only 0Return ValueReturns a dictionary containing {MsgAndCertEncodingType:int,	## encoding type, usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING ContentType:int,				## One of the CERT_QUERY_CONTENT_* constants FormatType:int,					## One of the CERT_QUERY_FORMAT_* constants CertStore:PyCERTSTORE,		## Handle to certificate store containing all certficates in the object, may be None 	Msg:PyCRYPTMSG,				## If input doesn't contains a PKCS7 message, will be None Context:PyCERT_CONTEXT}		## A certificate, CRL, or CTL context depending on ContentType, may be None

Returns:

      typing.Any:Reserved, use only 0
Return ValueReturns a dictionary containing 

{MsgAndCertEncodingType:int,	## encoding type, usually X509_ASN_ENCODING combined with PKCS_7_ASN_ENCODING 

ContentType:int,				## One of the CERT_QUERY_CONTENT_* constants 

FormatType:int,					## One of the CERT_QUERY_FORMAT_* constants 

CertStore:PyCERTSTORE,		## Handle to certificate store containing all certficates in the object, may be 

None 	Msg:PyCRYPTMSG,				## If input doesn't contains a PKCS7 message, will be None 

Context:PyCERT_CONTEXT}		## A certificate, CRL, or CTL context depending on ContentType, may be None

        
    """
    pass
        

def CryptDecodeMessage(EncodedBlob:'typing.Any',DecryptPara:'typing.Any',MsgTypeFlags:'typing.Any',VerifyPara:'typing.Any'=None,SignerIndex:'typing.Any'=0,PrevInnerContentType:'typing.Any'=0,ReturnData:'typing.Any'=True) -> 'typing.Any':
    """
    Decodes and decrypts a message, and verifies its signatures

Args:

      EncodedBlob(typing.Any):Data to be decoded
      DecryptPara(typing.Any):PyCRYPT_DECRYPT_MESSAGE_PARA containing decryption parms
      MsgTypeFlags(typing.Any):Combination of CMSG_DATA_FLAG, CMSG_SIGNED_FLAG, CMSG_ENVELOPED_FLAG, CMSG_SIGNED_AND_ENVELOPED_FLAG, or CMSG_HASHED_FLAG
      VerifyPara(typing.Any):PyCRYPT_VERIFY_MESSAGE_PARA containing signature verification parms
      SignerIndex(typing.Any):Index of the signer to verify,  ignored if message is not signed.
      PrevInnerContentType(typing.Any):Content type returned from previous call, used during subsequent pass on a nested message
      ReturnData(typing.Any):Indicates if decoded data should be returned.CommentsOnly one level of encoding is interpreted.  Some types of messages will need multiple calls to completely decode. For example, to decode a message created by win32crypt::CryptSignAndEncryptMessage, one pass with CMSG_ENVELOPED_FLAG 	and a second pass using CMSG_SIGNED_FLAG are required to recover the original message text.Return ValueOutput params are returned as a dict containing: {MsgType:int},					&nbsp&nbsp##Type of message decoded, one of CMSG_DATA,CMSG_SIGNED,CMSG_ENVELOPED,CMSG_SIGNED_AND_ENVELOPED,CMSG_HASHED 	InnerContentType:int, &nbsp&nbsp##Type of decoded content returned, uses same set of values as MsgType.  CMSG_DATA indicates unencoded data. Decoded:str,					&nbsp&nbsp##The decoded data, will be None if ReturnData is False. XchgCert:PyCERT_CONTEXT,	&nbsp&nbsp##Certificate used to decode message SignerCert:PyCERT_CONTEXT}	&nbsp&nbsp##Certificate used to sign message

Returns:

      typing.Any:Indicates if decoded data should be returned.
Comments

Only one level of encoding is interpreted.  Some types of messages will need multiple calls to completely 

decode. 

For example, to decode a message created by win32crypt::CryptSignAndEncryptMessage, one pass with 

CMSG_ENVELOPED_FLAG 	and a second pass using CMSG_SIGNED_FLAG are required to recover the original message text.
Return ValueOutput params are returned as a dict containing: 

{MsgType:int},					&nbsp&nbsp##Type of message decoded, one of 

CMSG_DATA,CMSG_SIGNED,CMSG_ENVELOPED,CMSG_SIGNED_AND_ENVELOPED,CMSG_HASHED 	InnerContentType:int, 

&nbsp&nbsp##Type of decoded content returned, uses same set of values as MsgType.  CMSG_DATA indicates unencoded data. 

Decoded:str,					&nbsp&nbsp##The decoded data, will be None if ReturnData is False. 

XchgCert:PyCERT_CONTEXT,	&nbsp&nbsp##Certificate used to decode message 

SignerCert:PyCERT_CONTEXT}	&nbsp&nbsp##Certificate used to sign message

        
    """
    pass
        

def CryptEncryptMessage(EncryptPara:'win32typing.PyCRYPT_ENCRYPT_MESSAGE_PARA',RecipientCert:'typing.Tuple[win32typing.PyCERT_CONTEXT, ...]',ToBeEncrypted:'typing.Any') -> 'typing.Any':
    """
    Encrypts and encodes a message

Args:

      EncryptPara(win32typing.PyCRYPT_ENCRYPT_MESSAGE_PARA):Encryption parameters
      RecipientCert(typing.Tuple[win32typing.PyCERT_CONTEXT, ...]):Sequence of handles to recipients' certificates
      ToBeEncrypted(typing.Any):Data to be encrypted

Returns:

      typing.Any
        
    """
    pass
        

def CryptDecryptMessage(DecryptPara:'win32typing.PyCRYPT_DECRYPT_MESSAGE_PARA',EncryptedBlob:'typing.Any') -> 'typing.Tuple[typing.Any, win32typing.PyCERT_CONTEXT]':
    """
    Decrypts an encrypted and encoded message

Args:

      DecryptPara(win32typing.PyCRYPT_DECRYPT_MESSAGE_PARA):Dictionary containing decryption parameters
      EncryptedBlob(typing.Any):Buffer containing an encrypted messageReturn ValueReturns the decrypted message and a handle to the certificate used to decrypt it

Returns:

      typing.Tuple[typing.Any, win32typing.PyCERT_CONTEXT]:Buffer containing an encrypted messageReturn ValueReturns the decrypted message and a handle to the certificate used to decrypt it

        
    """
    pass
        

def CryptSignAndEncryptMessage(SignPara:'win32typing.PyCRYPT_SIGN_MESSAGE_PARA',EncryptPara:'win32typing.PyCRYPT_ENCRYPT_MESSAGE_PARA',RecipientCert:'typing.Tuple[win32typing.PyCERT_CONTEXT, ...]',ToBeSignedAndEncrypted:'typing.Any') -> 'typing.Any':
    """
    Encrypts, encodes and signs a message using a certificate

Args:

      SignPara(win32typing.PyCRYPT_SIGN_MESSAGE_PARA):Message signing parameters
      EncryptPara(win32typing.PyCRYPT_ENCRYPT_MESSAGE_PARA):Encryption parameters
      RecipientCert(typing.Tuple[win32typing.PyCERT_CONTEXT, ...]):Sequence of certificates of intended recipients
      ToBeSignedAndEncrypted(typing.Any):Buffer containing data to be encoded in the message

Returns:

      typing.Any
        
    """
    pass
        

def CryptVerifyMessageSignature(SignedBlob:'typing.Any',SignerIndex:'typing.Any'=0,VerifyPara:'win32typing.PyCRYPT_VERIFY_MESSAGE_PARA'=None,ReturnData:'typing.Any'=False) -> 'typing.Tuple[win32typing.PyCERT_CONTEXT, typing.Any]':
    """
    Verifies the signature of an encoded 

message

Args:

      SignedBlob(typing.Any):Buffer containing a signed message
      SignerIndex(typing.Any):Index of the signer to verify, zero-based
      VerifyPara(win32typing.PyCRYPT_VERIFY_MESSAGE_PARA):Signature verification parameters, use None for defaults
      ReturnData(typing.Any):Indicates if decoded data should be returned.Return ValueReturns the signing certificate and the decoded data.  If ReturnData parm is False, None is returned for data.

Returns:

      typing.Tuple[win32typing.PyCERT_CONTEXT, typing.Any]:Indicates if decoded data should be returned.
Return ValueReturns the signing certificate and the decoded data.  If ReturnData parm is False, None is returned for data.

        
    """
    pass
        

def CryptGetMessageCertificates(SignedBlob:'typing.Any',MsgAndCertEncodingType:'typing.Any',CryptProv:'win32typing.PyCRYPTPROV'=None,Flags:'typing.Any'=0) -> 'win32typing.PyCERTSTORE':
    """
    Extracts certificates encoded in a message

Args:

      SignedBlob(typing.Any):Buffer containing a signed message
      MsgAndCertEncodingType(typing.Any):Message and certificate encoding types
      CryptProv(win32typing.PyCRYPTPROV):Handle to a CSP, use None for default
      Flags(typing.Any):Same flags used with win32crypt::CertOpenStore

Returns:

      win32typing.PyCERTSTORE
        
    """
    pass
        

def CryptGetMessageSignerCount(SignedBlob:'typing.Any',MsgEncodingType:'typing.Any') -> 'typing.Any':
    """
    Finds the number of signers of an encoded message

Args:

      SignedBlob(typing.Any):Buffer containing a signed message
      MsgEncodingType(typing.Any):Message encoding type

Returns:

      typing.Any
        
    """
    pass
        

def CryptSignMessage(SignPara:'win32typing.PyCRYPT_SIGN_MESSAGE_PARA',ToBeSigned:'typing.Tuple[typing.Any, ...]',DetachedSignature:'typing.Any'=False) -> 'typing.Any':
    """
    Signs and encodes a message

Args:

      SignPara(win32typing.PyCRYPT_SIGN_MESSAGE_PARA):Message signing parameters
      ToBeSigned(typing.Tuple[typing.Any, ...]):Sequence of strings containing message data.  Can only contain 1 string if DetachedSignature parm is False.
      DetachedSignature(typing.Any):If True, only the signature itself is encoded in output msg.

Returns:

      typing.Any
        
    """
    pass
        

def CryptVerifyDetachedMessageSignature(SignerIndex:'typing.Any',DetachedSignBlob:'typing.Any',ToBeSigned:'typing.Tuple[typing.Any, ...]',VerifyPara:'win32typing.PyCRYPT_VERIFY_MESSAGE_PARA'=None) -> 'win32typing.PyCERT_CONTEXT':
    """
    Verifies a signature that is encoded 

separately from the data

Args:

      SignerIndex(typing.Any):Index of the signer to verify
      DetachedSignBlob(typing.Any):Buffer containing an encoded signature
      ToBeSigned(typing.Tuple[typing.Any, ...]):Sequence of buffers containing message data.
      VerifyPara(win32typing.PyCRYPT_VERIFY_MESSAGE_PARA):Signature verification parameters, use None for defaultsReturn ValueReturns the signing certificate

Returns:

      win32typing.PyCERT_CONTEXT:Signature verification parameters, use 

None for defaults
Return ValueReturns the signing certificate

        
    """
    pass
        

def CryptDecryptAndVerifyMessageSignature(EncryptedBlob:'typing.Any',DecryptPara:'win32typing.PyCRYPT_DECRYPT_MESSAGE_PARA',VerifyPara:'win32typing.PyCRYPT_VERIFY_MESSAGE_PARA'=None,SignerIndex:'typing.Any'=0) -> 'typing.Any':
    """
    Decrypts and decodes a signed message, and verifies 

its signatures

Args:

      EncryptedBlob(typing.Any):Encoded message to be decrypted.
      DecryptPara(win32typing.PyCRYPT_DECRYPT_MESSAGE_PARA):Decryption parms
      VerifyPara(win32typing.PyCRYPT_VERIFY_MESSAGE_PARA):Signature verification parms
      SignerIndex(typing.Any):Index of the signer to verify, zero-based.CommentsUsage is similar to CryptDecodeMessage, except that it undoes all levels of encoding and returns the bare message.   This function is the counterpart of CryptSignAndEncryptMessage.Return ValueOutput params are returned as a dict containing: Decrypted:str,					&nbsp&nbsp##The decrypted message contents XchgCert:PyCERT_CONTEXT,	&nbsp&nbsp##Certificate whose private key was used to decrypt message SignerCert:PyCERT_CONTEXT	&nbsp&nbsp##Certificate used to sign message

Returns:

      typing.Any:Index of the signer to verify, zero-based.
Comments

Usage is similar to CryptDecodeMessage, except that it undoes all levels of encoding and 

returns the bare message.   This function is the counterpart of CryptSignAndEncryptMessage.
Return ValueOutput params are returned as a dict containing: 

Decrypted:str,					&nbsp&nbsp##The decrypted message contents 

XchgCert:PyCERT_CONTEXT,	&nbsp&nbsp##Certificate whose private key was used to decrypt message 

SignerCert:PyCERT_CONTEXT	&nbsp&nbsp##Certificate used to sign message

        
    """
    pass
        

def CryptEncodeObjectEx(StructType:'typing.Union[typing.Any]',StructInfo:'typing.Any',CertEncodingType:'typing.Any',Flags:'typing.Any'=0,EncodePara:'typing.Any'=None) -> 'typing.Any':
    """
    Serializes and ASN encodes cryptographic structures

Args:

      StructType(typing.Union[typing.Any]):OID identifying type of data to be encoded, either szOID_* string or a numeric id
      StructInfo(typing.Any):Information to be encoded.  Contents of dict are dependent on StructType
      CertEncodingType(typing.Any):Encoding types
      Flags(typing.Any):Encoding options, combination of CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..
      EncodePara(typing.Any):Not supported, use only NoneStructTypeType of inputszOID_ENHANCED_KEY_USAGEPyCTL_USAGE (sequence of OID's)X509_ENHANCED_KEY_USAGEPyCTL_USAGE (sequence of OID's)szOID_KEY_USAGEPyCRYPT_BIT_BLOBX509_KEY_USAGEPyCRYPT_BIT_BLOBX509_BITSPyCRYPT_BIT_BLOB

Returns:

      typing.Any
        
    """
    pass
        

def CryptDecodeObjectEx(StructType:'typing.Union[typing.Any]',Encoded:'typing.Any',CertEncodingType:'typing.Any',Flags:'typing.Any'=0,DecodePara:'typing.Any'=None) -> 'typing.Any':
    """
    Decodes ASN encoded data

Args:

      StructType(typing.Union[typing.Any]):An OID identifying the type of data to be decoded, can be either str or int
      Encoded(typing.Any):String or buffer containing ASN encoded data
      CertEncodingType(typing.Any):Encoding types
      Flags(typing.Any):Encoding options, can be combination CRYPT_UNICODE_* constants.  CRYPT_ENCODE_ALLOC_FLAG is added to flags..
      DecodePara(typing.Any):Not supported, use only NoneOIDObject returnedszOID_ENHANCED_KEY_USAGESequence of OIDsX509_ENHANCED_KEY_USAGESequence of OIDsszOID_KEY_USAGEPyCRYPT_BIT_BLOBX509_KEY_USAGEPyCRYPT_BIT_BLOBX509_BITSPyCRYPT_BIT_BLOBszOID_SUBJECT_ALT_NAMEPyCERT_ALT_NAME_INFOszOID_SUBJECT_ALT_NAME2PyCERT_ALT_NAME_INFOszOID_ISSUER_ALT_NAMEPyCERT_ALT_NAME_INFOszOID_ISSUER_ALT_NAME2PyCERT_ALT_NAME_INFOszOID_NEXT_UPDATE_LOCATIONPyCERT_ALT_NAME_INFOX509_ALTERNATE_NAMEPyCERT_ALT_NAME_INFOX509_NAME_VALUEPyCERT_NAME_VALUEX509_UNICODE_ANY_STRINGPyCERT_NAME_VALUEX509_UNICODE_NAME_VALUEPyCERT_NAME_VALUEX509_NAMEPyCERT_NAME_INFOX509_UNICODE_NAMEPyCERT_NAME_INFOszOID_KEY_ATTRIBUTESPyCERT_KEY_ATTRIBUTES_INFOX509_KEY_ATTRIBUTESPyCERT_KEY_ATTRIBUTES_INFOszOID_BASIC_CONSTRAINTSPyCERT_BASIC_CONSTRAINTS_INFOX509_BASIC_CONSTRAINTSPyCERT_BASIC_CONSTRAINTS_INFOszOID_BASIC_CONSTRAINTS2PyCERT_BASIC_CONSTRAINTS2_INFOX509_BASIC_CONSTRAINTS2PyCERT_BASIC_CONSTRAINTS2_INFOszOID_CERT_POLICIESSequence of PyCERT_POLICY_INFO objectsszOID_APPLICATION_CERT_POLICIESSequence of PyCERT_POLICY_INFO objectsX509_CERT_POLICIESSequence of PyCERT_POLICY_INFO objectsszOID_SUBJECT_KEY_IDENTIFIERBinary string containing the key identifierszOID_AUTHORITY_KEY_IDENTIFIERPyCERT_AUTHORITY_KEY_ID_INFOX509_AUTHORITY_KEY_IDPyCERT_AUTHORITY_KEY_ID_INFOReturn ValueType of object returned is dependent on the StructType to be decoded

Returns:

      typing.Any:Not supported, use only None



OID


Object returned



szOID_ENHANCED_KEY_USAGESequence of OIDs
X509_ENHANCED_KEY_USAGESequence of OIDs
szOID_KEY_USAGEPyCRYPT_BIT_BLOB
X509_KEY_USAGEPyCRYPT_BIT_BLOB
X509_BITSPyCRYPT_BIT_BLOB
szOID_SUBJECT_ALT_NAMEPyCERT_ALT_NAME_INFO
szOID_SUBJECT_ALT_NAME2PyCERT_ALT_NAME_INFO
szOID_ISSUER_ALT_NAMEPyCERT_ALT_NAME_INFO
szOID_ISSUER_ALT_NAME2PyCERT_ALT_NAME_INFO
szOID_NEXT_UPDATE_LOCATIONPyCERT_ALT_NAME_INFO
X509_ALTERNATE_NAMEPyCERT_ALT_NAME_INFO
X509_NAME_VALUEPyCERT_NAME_VALUE
X509_UNICODE_ANY_STRINGPyCERT_NAME_VALUE
X509_UNICODE_NAME_VALUEPyCERT_NAME_VALUE
X509_NAMEPyCERT_NAME_INFO
X509_UNICODE_NAMEPyCERT_NAME_INFO
szOID_KEY_ATTRIBUTESPyCERT_KEY_ATTRIBUTES_INFO
X509_KEY_ATTRIBUTESPyCERT_KEY_ATTRIBUTES_INFO
szOID_BASIC_CONSTRAINTSPyCERT_BASIC_CONSTRAINTS_INFO
X509_BASIC_CONSTRAINTSPyCERT_BASIC_CONSTRAINTS_INFO
szOID_BASIC_CONSTRAINTS2PyCERT_BASIC_CONSTRAINTS2_INFO
X509_BASIC_CONSTRAINTS2PyCERT_BASIC_CONSTRAINTS2_INFO
szOID_CERT_POLICIESSequence of PyCERT_POLICY_INFO objects
szOID_APPLICATION_CERT_POLICIESSequence of PyCERT_POLICY_INFO objects
X509_CERT_POLICIESSequence of PyCERT_POLICY_INFO objects
szOID_SUBJECT_KEY_IDENTIFIERBinary string containing the key identifier
szOID_AUTHORITY_KEY_IDENTIFIERPyCERT_AUTHORITY_KEY_ID_INFO
X509_AUTHORITY_KEY_IDPyCERT_AUTHORITY_KEY_ID_INFO
Return ValueType of object returned is dependent on the StructType to be decoded

        
    """
    pass
        

def CertNameToStr(Name:'typing.Any',StrType:'typing.Any',CertEncodingType:'typing.Any') -> 'typing.Any':
    """
    Converts an encoded CERT_NAME_INFO into a formatted string

Args:

      Name(typing.Any):String containing an encoded CERT_NAME_INFO, as used with certificate Issuer and Subject
      StrType(typing.Any):Type of string to format, one of CERT_SIMPLE_NAME_STR,CERT_OID_NAME_STR,CERT_X500_NAME_STR
      CertEncodingType(typing.Any):Input encodingCommentsUsually this encoded data is contained in a CERT_NAME_BLOB

Returns:

      typing.Any
        
    """
    pass
        

def CryptFormatObject(StructType:'typing.Union[typing.Any]',Encoded:'typing.Any',CertEncodingType:'typing.Any',FormatStrType:'typing.Any'=0,FormatType:'typing.Any'=0,FormatStruct:'typing.Any'=None) -> 'typing.Any':
    """
    Formats an encoded buffer into a readable string

Args:

      StructType(typing.Union[typing.Any]):OID identifying the type of encoded data, one of the szOID_* strings or an integer OID
      Encoded(typing.Any):String containing encoded data to be formatted
      CertEncodingType(typing.Any):Input encoding
      FormatStrType(typing.Any):String formatting options, combination of CRYPT_FORMAT_STR_MULTI_LINE, CRYPT_FORMAT_STR_NO_HEX
      FormatType(typing.Any):Reserved, use only 0
      FormatStruct(typing.Any):Reserved, use only NoneCommentsWill handle all of the common certificate extension typesWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def PFXImportCertStore(PFX:'typing.Any',Password:'typing.Any',Flags:'typing.Any') -> 'win32typing.PyCERTSTORE':
    """
    Creates a certificate store from PKCS#12 data (*.PFX files)

Args:

      PFX(typing.Any):Buffer containing PKCS#12-formatted certificate(s)
      Password(typing.Any):Password used to encrypt the data, may be None
      Flags(typing.Any):Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSETCommentsMSDN docs specify that *one* of the Flags can be used, but in practice a combination is allowedDepending on the encrypting application, a blank password ("") may be treated differently that a NULL password (None), so if you have a PFX with no password try both.Win32 API References

Returns:

      win32typing.PyCERTSTORE
        
    """
    pass
        

def PFXVerifyPassword(PFX:'typing.Any',Password:'typing.Any',Flags:'typing.Any') -> 'typing.Any':
    """
    Checks if a PFX blob can be decrypted with given password

Args:

      PFX(typing.Any):Buffer containing PKCS#12-formatted certificate(s)
      Password(typing.Any):Password used to encrypt the data, may be None
      Flags(typing.Any):Allowed flags are CRYPT_EXPORTABLE,CRYPT_USER_PROTECTED,CRYPT_MACHINE_KEYSET, and CRYPT_USER_KEYSETWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def PFXIsPFXBlob(PFX:'typing.Any') -> 'typing.Any':
    """
    Checks if data buffer contains a PFX blob

Args:

      PFX(typing.Any):Buffer containing data to be checkedWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def CryptBinaryToString(Binary:'typing.Any',Flags:'typing.Any') -> 'typing.Any':
    """
    Formats a binary buffer into the specified type of string

Args:

      Binary(typing.Any):Buffer containing raw data to be formatted
      Flags(typing.Any):Type of output desired, win32cryptcon.CRYPT_STRING_* valueWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def CryptStringToBinary(String:'typing.Any',Flags:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any, typing.Any]':
    """
    Converts a formatted string back into raw bytes

Args:

      String(typing.Any):Formatted string to be converted to raw binary data
      Flags(typing.Any):Input format (win32cryptcon.CRYPT_STRING_*)Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any]:Search for CryptStringToBinary at msdn, google or google groups.
Return ValueReturns the decoded binary data, number of header characters skipped, and CRYPT_STRING_* value 

denoting the type of data found (used if input Flags is one of *_ANY values)

        
    """
    pass
        