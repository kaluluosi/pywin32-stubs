__all__=['', 'PSGetItemPropertyHandler', 'PSGetPropertyDescription', 'PSGetPropertySystem', 'PSGetNameFromPropertyKey', 'PSGetPropertyKeyFromName', 'PSRegisterPropertySchema', 'PSUnregisterPropertySchema', 'SHGetPropertyStoreFromParsingName', 'StgSerializePropVariant', 'StgDeserializePropVariant', 'PSCreateMemoryPropertyStore', 'PSCreatePropertyStoreFromPropertySetStorage', 'PSLookupPropertyHandlerCLSID', 'SHGetPropertyStoreForWindow', 'PSGetPropertyFromPropertyStorage', 'PSGetNamedPropertyFromPropertyStorage', 'PSCreateSimplePropertyChange', 'PSCreatePropertyChangeArray', 'SHSetDefaultProperties']
from typing import *
from win32helper.win32typing import *
"""A module, encapsulating the Vista Property System interfaces"""


def PSGetItemPropertyHandler(Item:'PyIShellItem',riid:'PyIID',ReadWrite:'bool'=False) -> 'PyIPropertyStore':
    """
    Retrieves the property store for a shell item

Args:

      Item(PyIShellItem):A shell item
      riid(PyIID):Interface to return
      ReadWrite(bool):Pass True for a writeable property store

Returns:

      PyIPropertyStore
        
    """
    pass
        

def PSGetPropertyDescription(Key:'PyPROPERTYKEY',riid:'PyIID') -> 'PyIPropertyDescription':
    """
    Gets a description interface for a property

Args:

      Key(PyPROPERTYKEY):A property key identifier
      riid(PyIID):The interface to returnCommentsPossible interfaces include IPropertyDescription, IPropertyDescriptionAliasInfo, and IPropertyDescriptionSearchInfo

Returns:

      PyIPropertyDescription
        
    """
    pass
        

def PSGetPropertySystem(riid:'PyIID') -> 'PyIPropertySystem':
    """
    Creates an IPropertySystem interface

Args:

      riid(PyIID):The interface to return

Returns:

      PyIPropertySystem
        
    """
    pass
        

def PSGetNameFromPropertyKey(Key:'PyPROPERTYKEY') -> 'str':
    """
    Retrieves the canonical name of a property

Args:

      Key(PyPROPERTYKEY):A property key

Returns:

      str
        
    """
    pass
        

def PSGetPropertyKeyFromName(Name:'str') -> 'PyPROPERTYKEY':
    """
    Retrieves the property key by canonical name

Args:

      Name(str):The canonical name of a property (eg System.Author)

Returns:

      PyPROPERTYKEY
        
    """
    pass
        

def PSRegisterPropertySchema(filename:'Any') -> 'None':
    """
    Registers a group of properties described in a schema file

Args:

      filename(Any):An XML file that defines a property schema (*.propdesc)

Returns:

      None
        
    """
    pass
        

def PSUnregisterPropertySchema(filename:'Any') -> 'None':
    """
    Removes a property schema definition

Args:

      filename(Any):A previously registered schema definition file

Returns:

      None
        
    """
    pass
        

def SHGetPropertyStoreFromParsingName(Path:'str',Flags:'int',riid:'PyIID',BindCtx:'PyIBindCtx'=None) -> 'PyIPropertyStore':
    """
    Retrieves the property store for an item by 

path

Args:

      Path(str):Path to file
      Flags(int):Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)
      riid(PyIID):The interface to returnCommentsThis function does not exist on XP, even with Desktop Search installed
      BindCtx(PyIBindCtx):Bind context, or None

Returns:

      PyIPropertyStore
        
    """
    pass
        

def StgSerializePropVariant(propvar:'PyPROPVARIANT') -> 'bytes':
    """
    None

Args:

      propvar(PyPROPVARIANT):The value to serialize

Returns:

      bytes
        
    """
    pass
        

def StgDeserializePropVariant(prop:'bytes') -> 'PyPROPVARIANT':
    """
    None

Args:

      prop(bytes):Buffer or bytes object (or str in Python 2) containing a serialized value

Returns:

      PyPROPVARIANT
        
    """
    pass
        

def PSCreateMemoryPropertyStore(riid:'PyIID') -> 'PyIPropertyStore':
    """
    Creates a temporary property store that is not 

connected to any backing storage

Args:

      riid(PyIID):The interface to createCommentsMay also be used to create PyINamedPropertyStore, PyIPropertyStoreCache, PyIPersistStream, or PyIPropertyBag

Returns:

      PyIPropertyStore
        
    """
    pass
        

def PSCreatePropertyStoreFromPropertySetStorage(pss:'PyIPropertySetStorage',Mode:'int',riid:'PyIID') -> 'PyIPropertyStore':
    """
    None

Args:

      pss(PyIPropertySetStorage):Property container to be adapted
      Mode(int):Read or write mode, shellcon.STGM_*.  Must match mode used to open input interface.
      riid(PyIID):The interface to createCommentsThis function does not work for the NTFS property storage implementation based on alternate data streams.

Returns:

      PyIPropertyStore
        
    """
    pass
        

def PSLookupPropertyHandlerCLSID(FilePath:'str') -> 'PyIID':
    """
    Returns the GUID of the property handler for a file

Args:

      FilePath(str):Name of fileCommentsIf no handler is found, the returned error code can be deceptive as it seems to indicate that the file itself was not found

Returns:

      PyIID
        
    """
    pass
        

def SHGetPropertyStoreForWindow(hwnd:'int',riid:'PyIID') -> 'PyIPropertyStore':
    """
    Retrieves a collection of a window's properties

Args:

      hwnd(int):Handle to a window
      riid(PyIID):The interface to createCommentsRequires Windows 7 or later.Return ValueThe returned store can be used to set the System.AppUserModel.ID property that determines how windows are grouped on the taskbar

Returns:

      PyIPropertyStore:The interface to create
Comments

Requires Windows 7 or later.
Return ValueThe returned store can be used to set the System.AppUserModel.ID property that determines how windows 

are grouped on the taskbar

        
    """
    pass
        

def PSGetPropertyFromPropertyStorage(ps:'Any',key:'PyPROPERTYKEY') -> 'PyPROPVARIANT':
    """
    Extracts a property value from a serialized 

buffer by key

Args:

      ps(Any):Bytes or buffer (or str in python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)
      key(PyPROPERTYKEY):Property to return

Returns:

      PyPROPVARIANT
        
    """
    pass
        

def PSGetNamedPropertyFromPropertyStorage(ps:'Any',name:'str') -> 'PyPROPVARIANT':
    """
    Extracts a property value from a serialized 

buffer by name

Args:

      ps(Any):Bytes or buffer (or str in python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)
      name(str):Property to return

Returns:

      PyPROPVARIANT
        
    """
    pass
        

def PSCreateSimplePropertyChange(flags:'int',key:'PyPROPERTYKEY',val:'PyPROPVARIANT',riid:'PyIID') -> 'PyIPropertyChange':
    """
    None

Args:

      flags(int):The change operation, pscon.PKA_*
      key(PyPROPERTYKEY):The property key
      val(PyPROPVARIANT):The value that the change operation will apply
      riid(PyIID):The interface to return.

Returns:

      PyIPropertyChange
        
    """
    pass
        

def PSCreatePropertyChangeArray() -> 'PyIPropertyChangeArray':
    """
    None

Args:



Returns:

      PyIPropertyChangeArray
        
    """
    pass
        

def SHSetDefaultProperties(hwnd:'int',Item:'PyIShellItem',FileOpFlags:'int'=0,Sink:'PyGFileOperationProgressSink'=None) -> 'None':
    """
    Sets the default properties for a file.

Args:

      hwnd(int):Parent window for any notifications, can be None
      Item(PyIShellItem):Shell item whose defaults are to be set
      FileOpFlags(int):File operation flags, as used with PyIFileOperation::SetOperationFlags
      Sink(PyGFileOperationProgressSink):Event sink to receive notificationsCommentsDefault properties are registered by filetype under SetDefaultsFor value.

Returns:

      None
        
    """
    pass
        