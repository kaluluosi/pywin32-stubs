__all__=['', 'HrGetExchangeStatus', 'HrGetMailboxDN', 'HrGetServerDN', 'HrMAPIFindDefaultMsgStore', 'HrMAPIFindIPMSubtree', 'HrMAPIFindInbox', 'HrMAPIFindSubfolderEx', 'HrMAPIFindFolder', 'HrMAPIFindFolderEx', 'HrMAPIFindStore', 'HrCreateProfileName', 'HrCreateDirEntryIdEx', 'HrFindExchangeGlobalAddressList', 'HrMailboxLogon', 'HrMailboxLogoff', 'HrMAPIOpenFolderEx', 'HrMAPISetPropBoolean', 'HrMAPISetPropLong', 'HrOpenExchangePublicStore', 'HrOpenExchangePrivateStore', 'HrOpenExchangePublicFolders', 'HrOpenSessionObject', 'HrOpenSiteContainer', 'HrOpenSiteContainerAddressing', 'OPENSTORE_HOME_LOGON', 'OPENSTORE_OVERRIDE_HOME_MDB', 'OPENSTORE_PUBLIC', 'OPENSTORE_TAKE_OWNERSHIP', 'OPENSTORE_USE_ADMIN_PRIVILEGE']
import typing
from win32helper import win32typing
"""A COM interface to Exchange's API"""


def HrGetExchangeStatus(server:'typing.Union[str]') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Obtains the current state of the server on a computer.

Args:

      server(typing.Union[str]):The name of the server to query.Return ValueThe result is a tuple of serviceState, serverState

Returns:

      typing.Tuple[typing.Any, typing.Any]:The name of the server to query.Return ValueThe result is a tuple of serviceState, serverState

        
    """
    pass
        

def HrGetMailboxDN(session:'typing.Any') -> 'str':
    """
    Retrieves the distinguished name (DN) for a mailbox

Args:

      session(typing.Any):The root folder.

Returns:

      str
        
    """
    pass
        

def HrGetServerDN(session:'typing.Any') -> 'str':
    """
    Retrieves the distinguished name (DN) for a server

Args:

      session(typing.Any):The root folder.

Returns:

      str
        
    """
    pass
        

def HrMAPIFindDefaultMsgStore(session:'win32typing.PyIMAPISession') -> 'str':
    """
    Retrieves the entry identifier of the default information store.

Args:

      session(win32typing.PyIMAPISession):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindIPMSubtree(msgStore:'win32typing.PyIMsgStore') -> 'str':
    """
    Retrieves the entry ID of the IPM (interpersonal message) subtree folder

Args:

      msgStore(win32typing.PyIMsgStore):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindInbox(msgStore:'win32typing.PyIMsgStore') -> 'str':
    """
    Retrieves the Entry ID of the IPM inbox folder

Args:

      msgStore(win32typing.PyIMsgStore):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindSubfolderEx(rootFolder:'win32typing.PyIMAPIFolder',sep:'typing.Union[str]',name:'typing.Union[str]') -> 'win32typing.PyIMsgStore':
    """
    Retrieves a subfolder in an information store using the hierarchical path name of the folder.

Args:

      rootFolder(win32typing.PyIMAPIFolder):The root folder.
      sep(typing.Union[str]):The folder seperator character.
      name(typing.Union[str]):The folder name

Returns:

      win32typing.PyIMsgStore
        
    """
    pass
        

def HrMAPIFindFolder(folder:'win32typing.PyIMAPIFolder',name:'str') -> 'str':
    """
    Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder.

Args:

      folder(win32typing.PyIMAPIFolder):The folder to search
      name(str):Name of the folder

Returns:

      str
        
    """
    pass
        

def HrMAPIFindFolderEx(msgStore:'win32typing.PyIMsgStore',sepString:'str',path:'str') -> 'str':
    """
    Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder.

Args:

      msgStore(win32typing.PyIMsgStore):The folder to search
      sepString(str):The character seperating the folder names - eg '\\'
      path(str):Path to the folder

Returns:

      str
        
    """
    pass
        

def HrMAPIFindStore(session:'win32typing.PyIMAPISession',name:'str') -> 'win32typing.PyIMsgStore':
    """
    Retrieves a pointer to the entry identifier of an information store from the display name of the store.

Args:

      session(win32typing.PyIMAPISession):
      name(str):

Returns:

      win32typing.PyIMsgStore
        
    """
    pass
        

def HrCreateProfileName(profPrefix:'typing.Union[str]') -> 'str':
    """
    Creates a profile with the specified name

Args:

      profPrefix(typing.Union[str]):A prefix for the new profile.

Returns:

      str
        
    """
    pass
        

def HrCreateDirEntryIdEx(addrBook:'win32typing.PyIAddrBook',distinguishedName:'str') -> 'str':
    """
    Creates a directory identifier for a MAPI object, given the address of the object in the directory

Args:

      addrBook(win32typing.PyIAddrBook):The address book interface
      distinguishedName(str):The dn of the object to obtain the entry ID for.

Returns:

      str
        
    """
    pass
        

def HrFindExchangeGlobalAddressList(addrBook:'win32typing.PyIAddrBook') -> 'str':
    """
    Retrieves the entry identifier of the global address list (GAL) container in the address book.

Args:

      addrBook(win32typing.PyIAddrBook):The interface containing the address book

Returns:

      str
        
    """
    pass
        

def HrMailboxLogon(session:'win32typing.PyIMAPISession',msgStore:'win32typing.PyIMsgStore',msgStoreDN:'typing.Union[str]',mailboxDN:'typing.Union[str]') -> 'win32typing.PyIMsgStore':
    """
    Logs on a server and mailbox.

Args:

      session(win32typing.PyIMAPISession):The session object
      msgStore(win32typing.PyIMsgStore):
      msgStoreDN(typing.Union[str]):
      mailboxDN(typing.Union[str]):

Returns:

      win32typing.PyIMsgStore
        
    """
    pass
        

def HrMailboxLogoff(inbox:'win32typing.PyIMsgStore') -> 'None':
    """
    Logs off a server and mailbox.

Args:

      inbox(win32typing.PyIMsgStore):The open inbox.

Returns:

      None
        
    """
    pass
        

def HrMAPIOpenFolderEx(msgStore:'win32typing.PyIMsgStore',sep:'typing.Union[str]',name:'typing.Union[str]') -> 'win32typing.PyIMAPIFolder':
    """
    Opens a folder in the information store from the hierarchical path name of the folder.

Args:

      msgStore(win32typing.PyIMsgStore):
      sep(typing.Union[str]):The folder seperator character.
      name(typing.Union[str]):The folder name

Returns:

      win32typing.PyIMAPIFolder
        
    """
    pass
        

def HrMAPISetPropBoolean(obj:'win32typing.PyIMAPIProp',tag:'typing.Any') -> 'None':
    """
    Sets a boolean property.

Args:

      obj(win32typing.PyIMAPIProp):The object to set
      tag(typing.Any):The property tag

Returns:

      None
        
    """
    pass
        

def HrMAPISetPropLong(obj:'win32typing.PyIMAPIProp',tag:'typing.Any') -> 'None':
    """
    Sets a long property.

Args:

      obj(win32typing.PyIMAPIProp):The object to set
      tag(typing.Any):The property tag

Returns:

      None
        
    """
    pass
        

def HrOpenExchangePublicStore(session:'win32typing.PyIMAPISession') -> 'win32typing.PyIMsgStore':
    """
    Retrieves an interface to the public information store provider.

Args:

      session(win32typing.PyIMAPISession):The MAPI session object

Returns:

      win32typing.PyIMsgStore
        
    """
    pass
        

def HrOpenExchangePrivateStore(session:'win32typing.PyIMAPISession') -> 'win32typing.PyIMsgStore':
    """
    Locates the primary user information store provider.

Args:

      session(win32typing.PyIMAPISession):The MAPI session object

Returns:

      win32typing.PyIMsgStore
        
    """
    pass
        

def HrOpenExchangePublicFolders(store:'win32typing.PyIMsgStore') -> 'win32typing.PyIMAPIFolder':
    """
    Opens the root of the public folder hierarchy in the public information store.

Args:

      store(win32typing.PyIMsgStore):

Returns:

      win32typing.PyIMAPIFolder
        
    """
    pass
        

def HrOpenSessionObject(session:'win32typing.PyIMAPISession') -> 'win32typing.PyIMAPIProp':
    """
    None

Args:

      session(win32typing.PyIMAPISession):The MAPI session object

Returns:

      win32typing.PyIMAPIProp
        
    """
    pass
        

def HrOpenSiteContainer(session:'win32typing.PyIMAPISession') -> 'win32typing.PyIMAPIProp':
    """
    None

Args:

      session(win32typing.PyIMAPISession):The MAPI session object

Returns:

      win32typing.PyIMAPIProp
        
    """
    pass
        

def HrOpenSiteContainerAddressing(session:'win32typing.PyIMAPISession') -> 'win32typing.PyIMAPIProp':
    """
    None

Args:

      session(win32typing.PyIMAPISession):The MAPI session object

Returns:

      win32typing.PyIMAPIProp
        
    """
    pass
        
OPENSTORE_HOME_LOGON = ...
OPENSTORE_OVERRIDE_HOME_MDB = ...
OPENSTORE_PUBLIC = ...
OPENSTORE_TAKE_OWNERSHIP = ...
OPENSTORE_USE_ADMIN_PRIVILEGE = ...