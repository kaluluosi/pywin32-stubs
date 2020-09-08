__all__=['', 'HrGetExchangeStatus', 'HrGetMailboxDN', 'HrGetServerDN', 'HrMAPIFindDefaultMsgStore', 'HrMAPIFindIPMSubtree', 'HrMAPIFindInbox', 'HrMAPIFindSubfolderEx', 'HrMAPIFindFolder', 'HrMAPIFindFolderEx', 'HrMAPIFindStore', 'HrCreateProfileName', 'HrCreateDirEntryIdEx', 'HrFindExchangeGlobalAddressList', 'HrMailboxLogon', 'HrMailboxLogoff', 'HrMAPIOpenFolderEx', 'HrMAPISetPropBoolean', 'HrMAPISetPropLong', 'HrOpenExchangePublicStore', 'HrOpenExchangePrivateStore', 'HrOpenExchangePublicFolders', 'HrOpenSessionObject', 'HrOpenSiteContainer', 'HrOpenSiteContainerAddressing', 'OPENSTORE_HOME_LOGON', 'OPENSTORE_OVERRIDE_HOME_MDB', 'OPENSTORE_PUBLIC', 'OPENSTORE_TAKE_OWNERSHIP', 'OPENSTORE_USE_ADMIN_PRIVILEGE']
from typing import *
from win32helper.win32typing import *
"""A COM interface to Exchange's API"""


def HrGetExchangeStatus(server:'Union[str]') -> 'Tuple[int, int]':
    """
    Obtains the current state of the server on a computer.

Args:

      server(Union[str]):The name of the server to query.Return ValueThe result is a tuple of serviceState, serverState

Returns:

      Tuple[int, int]:The name of the server to query.Return ValueThe result is a tuple of serviceState, serverState

        
    """
    pass
        

def HrGetMailboxDN(session:'Any') -> 'str':
    """
    Retrieves the distinguished name (DN) for a mailbox

Args:

      session(Any):The root folder.

Returns:

      str
        
    """
    pass
        

def HrGetServerDN(session:'Any') -> 'str':
    """
    Retrieves the distinguished name (DN) for a server

Args:

      session(Any):The root folder.

Returns:

      str
        
    """
    pass
        

def HrMAPIFindDefaultMsgStore(session:'PyIMAPISession') -> 'str':
    """
    Retrieves the entry identifier of the default information store.

Args:

      session(PyIMAPISession):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindIPMSubtree(msgStore:'PyIMsgStore') -> 'str':
    """
    Retrieves the entry ID of the IPM (interpersonal message) subtree folder

Args:

      msgStore(PyIMsgStore):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindInbox(msgStore:'PyIMsgStore') -> 'str':
    """
    Retrieves the Entry ID of the IPM inbox folder

Args:

      msgStore(PyIMsgStore):

Returns:

      str
        
    """
    pass
        

def HrMAPIFindSubfolderEx(rootFolder:'PyIMAPIFolder',sep:'Union[str]',name:'Union[str]') -> 'PyIMsgStore':
    """
    Retrieves a subfolder in an information store using the hierarchical path name of the folder.

Args:

      rootFolder(PyIMAPIFolder):The root folder.
      sep(Union[str]):The folder seperator character.
      name(Union[str]):The folder name

Returns:

      PyIMsgStore
        
    """
    pass
        

def HrMAPIFindFolder(folder:'PyIMAPIFolder',name:'str') -> 'str':
    """
    Retrieves the entry ID for a folder in an information store using the hierarchical path name of the folder.

Args:

      folder(PyIMAPIFolder):The folder to search
      name(str):Name of the folder

Returns:

      str
        
    """
    pass
        

def HrMAPIFindFolderEx(msgStore:'PyIMsgStore',sepString:'str',path:'str') -> 'str':
    """
    Retrieves the entry ID of a folder in an information store using the hierarchical path name of the folder.

Args:

      msgStore(PyIMsgStore):The folder to search
      sepString(str):The character seperating the folder names - eg '\\'
      path(str):Path to the folder

Returns:

      str
        
    """
    pass
        

def HrMAPIFindStore(session:'PyIMAPISession',name:'str') -> 'PyIMsgStore':
    """
    Retrieves a pointer to the entry identifier of an information store from the display name of the store.

Args:

      session(PyIMAPISession):
      name(str):

Returns:

      PyIMsgStore
        
    """
    pass
        

def HrCreateProfileName(profPrefix:'Union[str]') -> 'str':
    """
    Creates a profile with the specified name

Args:

      profPrefix(Union[str]):A prefix for the new profile.

Returns:

      str
        
    """
    pass
        

def HrCreateDirEntryIdEx(addrBook:'PyIAddrBook',distinguishedName:'str') -> 'str':
    """
    Creates a directory identifier for a MAPI object, given the address of the object in the directory

Args:

      addrBook(PyIAddrBook):The address book interface
      distinguishedName(str):The dn of the object to obtain the entry ID for.

Returns:

      str
        
    """
    pass
        

def HrFindExchangeGlobalAddressList(addrBook:'PyIAddrBook') -> 'str':
    """
    Retrieves the entry identifier of the global address list (GAL) container in the address book.

Args:

      addrBook(PyIAddrBook):The interface containing the address book

Returns:

      str
        
    """
    pass
        

def HrMailboxLogon(session:'PyIMAPISession',msgStore:'PyIMsgStore',msgStoreDN:'Union[str]',mailboxDN:'Union[str]') -> 'PyIMsgStore':
    """
    Logs on a server and mailbox.

Args:

      session(PyIMAPISession):The session object
      msgStore(PyIMsgStore):
      msgStoreDN(Union[str]):
      mailboxDN(Union[str]):

Returns:

      PyIMsgStore
        
    """
    pass
        

def HrMailboxLogoff(inbox:'PyIMsgStore') -> 'None':
    """
    Logs off a server and mailbox.

Args:

      inbox(PyIMsgStore):The open inbox.

Returns:

      None
        
    """
    pass
        

def HrMAPIOpenFolderEx(msgStore:'PyIMsgStore',sep:'Union[str]',name:'Union[str]') -> 'PyIMAPIFolder':
    """
    Opens a folder in the information store from the hierarchical path name of the folder.

Args:

      msgStore(PyIMsgStore):
      sep(Union[str]):The folder seperator character.
      name(Union[str]):The folder name

Returns:

      PyIMAPIFolder
        
    """
    pass
        

def HrMAPISetPropBoolean(obj:'PyIMAPIProp',tag:'int') -> 'None':
    """
    Sets a boolean property.

Args:

      obj(PyIMAPIProp):The object to set
      tag(int):The property tag

Returns:

      None
        
    """
    pass
        

def HrMAPISetPropLong(obj:'PyIMAPIProp',tag:'int') -> 'None':
    """
    Sets a long property.

Args:

      obj(PyIMAPIProp):The object to set
      tag(int):The property tag

Returns:

      None
        
    """
    pass
        

def HrOpenExchangePublicStore(session:'PyIMAPISession') -> 'PyIMsgStore':
    """
    Retrieves an interface to the public information store provider.

Args:

      session(PyIMAPISession):The MAPI session object

Returns:

      PyIMsgStore
        
    """
    pass
        

def HrOpenExchangePrivateStore(session:'PyIMAPISession') -> 'PyIMsgStore':
    """
    Locates the primary user information store provider.

Args:

      session(PyIMAPISession):The MAPI session object

Returns:

      PyIMsgStore
        
    """
    pass
        

def HrOpenExchangePublicFolders(store:'PyIMsgStore') -> 'PyIMAPIFolder':
    """
    Opens the root of the public folder hierarchy in the public information store.

Args:

      store(PyIMsgStore):

Returns:

      PyIMAPIFolder
        
    """
    pass
        

def HrOpenSessionObject(session:'PyIMAPISession') -> 'PyIMAPIProp':
    """
    None

Args:

      session(PyIMAPISession):The MAPI session object

Returns:

      PyIMAPIProp
        
    """
    pass
        

def HrOpenSiteContainer(session:'PyIMAPISession') -> 'PyIMAPIProp':
    """
    None

Args:

      session(PyIMAPISession):The MAPI session object

Returns:

      PyIMAPIProp
        
    """
    pass
        

def HrOpenSiteContainerAddressing(session:'PyIMAPISession') -> 'PyIMAPIProp':
    """
    None

Args:

      session(PyIMAPISession):The MAPI session object

Returns:

      PyIMAPIProp
        
    """
    pass
        
OPENSTORE_HOME_LOGON = ...
OPENSTORE_OVERRIDE_HOME_MDB = ...
OPENSTORE_PUBLIC = ...
OPENSTORE_TAKE_OWNERSHIP = ...
OPENSTORE_USE_ADMIN_PRIVILEGE = ...