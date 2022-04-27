__all__=['', 'PSGetItemPropertyHandler', 'PSGetPropertyDescription', 'PSGetPropertySystem', 'PSGetNameFromPropertyKey', 'PSGetPropertyKeyFromName', 'PSRegisterPropertySchema', 'PSUnregisterPropertySchema', 'SHGetPropertyStoreFromParsingName', 'StgSerializePropVariant', 'StgDeserializePropVariant', 'PSCreateMemoryPropertyStore', 'PSCreatePropertyStoreFromPropertySetStorage', 'PSLookupPropertyHandlerCLSID', 'SHGetPropertyStoreForWindow', 'PSGetPropertyFromPropertyStorage', 'PSGetNamedPropertyFromPropertyStorage', 'PSCreateSimplePropertyChange', 'PSCreatePropertyChangeArray', 'SHSetDefaultProperties']
import typing
import win32typing
"""A module, encapsulating the Vista Property System interfaces"""


def PSGetItemPropertyHandler(Item:'win32typing.PyIShellItem',riid:'win32typing.PyIID',ReadWrite:'typing.Any'=False) -> 'win32typing.PyIPropertyStore':
    """
    Retrieves the property store for a shell item

Args:

      Item(win32typing.PyIShellItem):A shell item
      riid(win32typing.PyIID):Interface to return
      ReadWrite(typing.Any):Pass True for a writeable property store

Returns:

      win32typing.PyIPropertyStore
        
    """
    pass
        

def PSGetPropertyDescription(Key:'win32typing.PyPROPERTYKEY',riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyDescription':
    """
    Gets a description interface for a property

Args:

      Key(win32typing.PyPROPERTYKEY):A property key identifier
      riid(win32typing.PyIID):The interface to returnCommentsPossible interfaces include IPropertyDescription, IPropertyDescriptionAliasInfo, and IPropertyDescriptionSearchInfo

Returns:

      win32typing.PyIPropertyDescription
        
    """
    pass
        

def PSGetPropertySystem(riid:'win32typing.PyIID') -> 'win32typing.PyIPropertySystem':
    """
    Creates an IPropertySystem interface

Args:

      riid(win32typing.PyIID):The interface to return

Returns:

      win32typing.PyIPropertySystem
        
    """
    pass
        

def PSGetNameFromPropertyKey(Key:'win32typing.PyPROPERTYKEY') -> 'str':
    """
    Retrieves the canonical name of a property

Args:

      Key(win32typing.PyPROPERTYKEY):A property key

Returns:

      str
        
    """
    pass
        

def PSGetPropertyKeyFromName(Name:'typing.Any') -> 'win32typing.PyPROPERTYKEY':
    """
    Retrieves the property key by canonical name

Args:

      Name(typing.Any):The canonical name of a property (eg System.Author)

Returns:

      win32typing.PyPROPERTYKEY
        
    """
    pass
        

def PSRegisterPropertySchema(filename:'typing.Any') -> 'None':
    """
    Registers a group of properties described in a schema file

Args:

      filename(typing.Any):An XML file that defines a property schema (*.propdesc)

Returns:

      None
        
    """
    pass
        

def PSUnregisterPropertySchema(filename:'typing.Any') -> 'None':
    """
    Removes a property schema definition

Args:

      filename(typing.Any):A previously registered schema definition file

Returns:

      None
        
    """
    pass
        

def SHGetPropertyStoreFromParsingName(Path:'str',Flags:'typing.Any',riid:'win32typing.PyIID',BindCtx:'win32typing.PyIBindCtx'=None) -> 'win32typing.PyIPropertyStore':
    """
    Retrieves the property store for an item by 

path

Args:

      Path(str):Path to file
      Flags(typing.Any):Combination of GETPROPERTYSTOREFLAGS values (shellcon.GPS_*)
      riid(win32typing.PyIID):The interface to returnCommentsThis function does not exist on XP, even with Desktop Search installed
      BindCtx(win32typing.PyIBindCtx):Bind context, or None

Returns:

      win32typing.PyIPropertyStore
        
    """
    pass
        

def StgSerializePropVariant(propvar:'win32typing.PyPROPVARIANT') -> 'typing.Any':
    """
    None

Args:

      propvar(win32typing.PyPROPVARIANT):The value to serialize

Returns:

      typing.Any
        
    """
    pass
        

def StgDeserializePropVariant(prop:'typing.Any') -> 'win32typing.PyPROPVARIANT':
    """
    None

Args:

      prop(typing.Any):Buffer or bytes object (or str in Python 2) containing a serialized value

Returns:

      win32typing.PyPROPVARIANT
        
    """
    pass
        

def PSCreateMemoryPropertyStore(riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyStore':
    """
    Creates a temporary property store that is not 

connected to any backing storage

Args:

      riid(win32typing.PyIID):The interface to createCommentsMay also be used to create PyINamedPropertyStore, PyIPropertyStoreCache, PyIPersistStream, or PyIPropertyBag

Returns:

      win32typing.PyIPropertyStore
        
    """
    pass
        

def PSCreatePropertyStoreFromPropertySetStorage(pss:'win32typing.PyIPropertySetStorage',Mode:'typing.Any',riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyStore':
    """
    None

Args:

      pss(win32typing.PyIPropertySetStorage):Property container to be adapted
      Mode(typing.Any):Read or write mode, shellcon.STGM_*.  Must match mode used to open input interface.
      riid(win32typing.PyIID):The interface to createCommentsThis function does not work for the NTFS property storage implementation based on alternate data streams.

Returns:

      win32typing.PyIPropertyStore
        
    """
    pass
        

def PSLookupPropertyHandlerCLSID(FilePath:'typing.Any') -> 'win32typing.PyIID':
    """
    Returns the GUID of the property handler for a file

Args:

      FilePath(typing.Any):Name of fileCommentsIf no handler is found, the returned error code can be deceptive as it seems to indicate that the file itself was not found

Returns:

      win32typing.PyIID
        
    """
    pass
        

def SHGetPropertyStoreForWindow(hwnd:'int',riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyStore':
    """
    Retrieves a collection of a window's properties

Args:

      hwnd(int):Handle to a window
      riid(win32typing.PyIID):The interface to createCommentsRequires Windows 7 or later.Return ValueThe returned store can be used to set the System.AppUserModel.ID property that determines how windows are grouped on the taskbar

Returns:

      win32typing.PyIPropertyStore:The interface to create
Comments

Requires Windows 7 or later.
Return ValueThe returned store can be used to set the System.AppUserModel.ID property that determines how windows 

are grouped on the taskbar

        
    """
    pass
        

def PSGetPropertyFromPropertyStorage(ps:'typing.Any',key:'win32typing.PyPROPERTYKEY') -> 'win32typing.PyPROPVARIANT':
    """
    Extracts a property value from a serialized 

buffer by key

Args:

      ps(typing.Any):Bytes or buffer (or str in python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)
      key(win32typing.PyPROPERTYKEY):Property to return

Returns:

      win32typing.PyPROPVARIANT
        
    """
    pass
        

def PSGetNamedPropertyFromPropertyStorage(ps:'typing.Any',name:'typing.Any') -> 'win32typing.PyPROPVARIANT':
    """
    Extracts a property value from a serialized 

buffer by name

Args:

      ps(typing.Any):Bytes or buffer (or str in python 2) containing a serialized property set (see PyIPersistSerializedPropStorage::GetPropertyStorage)
      name(typing.Any):Property to return

Returns:

      win32typing.PyPROPVARIANT
        
    """
    pass
        

def PSCreateSimplePropertyChange(flags:'typing.Any',key:'win32typing.PyPROPERTYKEY',val:'win32typing.PyPROPVARIANT',riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyChange':
    """
    None

Args:

      flags(typing.Any):The change operation, pscon.PKA_*
      key(win32typing.PyPROPERTYKEY):The property key
      val(win32typing.PyPROPVARIANT):The value that the change operation will apply
      riid(win32typing.PyIID):The interface to return.

Returns:

      win32typing.PyIPropertyChange
        
    """
    pass
        

def PSCreatePropertyChangeArray() -> 'win32typing.PyIPropertyChangeArray':
    """
    None

Args:



Returns:

      win32typing.PyIPropertyChangeArray
        
    """
    pass
        

def SHSetDefaultProperties(hwnd:'int',Item:'win32typing.PyIShellItem',FileOpFlags:'typing.Any'=0,Sink:'win32typing.PyGFileOperationProgressSink'=None) -> 'None':
    """
    Sets the default properties for a file.

Args:

      hwnd(int):Parent window for any notifications, can be None
      Item(win32typing.PyIShellItem):Shell item whose defaults are to be set
      FileOpFlags(typing.Any):File operation flags, as used with PyIFileOperation::SetOperationFlags
      Sink(win32typing.PyGFileOperationProgressSink):Event sink to receive notificationsCommentsDefault properties are registered by filetype under SetDefaultsFor value.

Returns:

      None
        
    """
    pass
        