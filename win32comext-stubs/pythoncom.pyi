__all__=['', '_GetInterfaceCount', '_GetInterfaceCount', 'CoCreateFreeThreadedMarshaler', 'CoCreateInstanceEx', 'CoCreateInstance', 'CoFreeUnusedLibraries', 'CoInitialize', 'CoInitializeEx', 'CoInitializeSecurity', 'CoGetInterfaceAndReleaseStream', 'CoMarshalInterThreadInterfaceInStream', 'CoMarshalInterface', 'CoUnmarshalInterface', 'CoReleaseMarshalData', 'CoGetObject', 'CoUninitialize', 'CoRegisterClassObject', 'CoResumeClassObjects', 'CoRevokeClassObject', 'CoTreatAsClass', 'CoWaitForMultipleHandles', 'Connect', 'CreateGuid', 'CreateBindCtx', 'CreateFileMoniker', 'CreateItemMoniker', 'CreatePointerMoniker', 'CreateTypeLib', 'CreateTypeLib2', 'CreateStreamOnHGlobal', 'CreateILockBytesOnHGlobal', 'EnableQuitMessage', 'FUNCDESC', 'GetActiveObject', 'GetClassFile', 'GetFacilityString', 'GetRecordFromGuids', 'GetRecordFromTypeInfo', 'GetRunningObjectTable', 'GetScodeString', 'GetScodeRangeString', 'GetSeverityString', 'IsGatewayRegistered', 'LoadRegTypeLib', 'LoadTypeLib', 'MakePyFactory', 'MkParseDisplayName', 'New', 'ObjectFromAddress', 'ObjectFromLresult', 'OleInitialize', 'OleGetClipboard', 'OleFlushClipboard', 'OleIsCurrentClipboard', 'OleSetClipboard', 'OleLoadFromStream', 'OleSaveToStream', 'OleLoad', 'ProgIDFromCLSID', 'PumpWaitingMessages', 'PumpMessages', 'QueryPathOfRegTypeLib', 'ReadClassStg', 'ReadClassStm', 'RegisterTypeLib', 'UnRegisterTypeLib', 'RegisterActiveObject', 'RevokeActiveObject', 'RegisterDragDrop', 'RevokeDragDrop', 'DoDragDrop', 'StgCreateDocfile', 'StgCreateDocfileOnILockBytes', 'StgOpenStorageOnILockBytes', 'StgIsStorageFile', 'STGMEDIUM', 'StgOpenStorage', 'StgOpenStorageEx', 'StgCreateStorageEx', 'TYPEATTR', 'VARDESC', 'WrapObject', 'WriteClassStg', 'WriteClassStm', 'UnwrapObject', 'FmtIdToPropStgName', 'PropStgNameToFmtId', 'CoGetCallContext', 'CoGetObjectContext', 'CoGetCancelObject', 'CoSetCancelObject', 'CoEnableCallCancellation', 'CoDisableCallCancellation']
from typing import *
from win32helper.win32typing import *
"""A module, encapsulating the OLE automation API"""


def _GetInterfaceCount() -> 'int':
    """
    Retrieves the number of interface objects currently in existance

Args:



Returns:

      int
        
    """
    pass
        

def _GetInterfaceCount() -> 'int':
    """
    Retrieves the number of interface objects currently in existance

Args:



Returns:

      int
        
    """
    pass
        

def CoCreateFreeThreadedMarshaler(unk:'PyIUnknown') -> 'PyIUnknown':
    """
    Creates an aggregatable object capable of 

context-dependent marshaling.

Args:

      unk(PyIUnknown):The unknown object to marshal.

Returns:

      PyIUnknown
        
    """
    pass
        

def CoCreateInstanceEx(clsid:'PyIID',unkOuter:'PyIUnknown',context:'int',serverInfo:'Tuple[Any, Any, Any, Any]',iids:'List[PyIID]') -> 'PyIUnknown':
    """
    Create a new instance of an OLE automation server possibly on a 

remote machine.

Args:

      clsid(PyIID):Class identifier (CLSID) of the object
      unkOuter(PyIUnknown):The outer unknown, or None
      context(int):The create context for the object, combination of pythoncom.CLSCTX_* flags
      serverInfo(Tuple[Any, Any, Any, Any]):May be None, or describes the remote server to execute on.
      iids(List[PyIID]):A list of IIDs required from the object

Returns:

      PyIUnknown
        
    """
    pass
        

def CoCreateInstance(clsid:'PyIID',unkOuter:'PyIUnknown',context:'int',iid:'PyIID') -> 'PyIUnknown':
    """
    Create a new instance of an OLE automation server.

Args:

      clsid(PyIID):Class identifier (CLSID) of the object
      unkOuter(PyIUnknown):The outer unknown, or None
      context(int):The create context for the object, combination of pythoncom.CLSCTX_* flags
      iid(PyIID):The IID required from the object

Returns:

      PyIUnknown
        
    """
    pass
        

def CoFreeUnusedLibraries() -> 'None':
    """
    Unloads any DLLs that are no longer in use and that, when loaded, were 

specified to be freed automatically.

Args:



Returns:

      None
        
    """
    pass
        

def CoInitialize() -> 'None':
    """
    Initialize the COM libraries for the calling thread.

Args:



Returns:

      None:pythoncom.CoInitialize
CoInitialize()Initialize the COM libraries for the calling thread.
Comments

Apart from the error handling semantics, this is equivalent 

to pythoncom::CoInitializeEx(pythoncom.COINIT_APARTMENTTHREADED). 

See pythoncom::CoInitializeEx for a description.
Return ValueThis function will ignore the RPC_E_CHANGED_MODE error, as 

that error indicates someone else beat you to the initialization, and 

did so with a different threading model.  This error is ignored as it 

still means COM is ready for use on this thread, and as this function 

does not explicitly specify a threading model the caller probably 

doesn't care what model it is. 

All other COM errors will raise pythoncom.error as usual.  Use 

pythoncom::CoInitializeEx if you also want to handle the RPC_E_CHANGED_MODE 

error.

        
    """
    pass
        

def CoInitializeEx(flags:'int') -> 'None':
    """
    Initialize the COM libraries for the calling thread.

Args:

      flags(int):Flags for the initialization.CommentsThere is no need to call this for the main Python thread, as it is called automatically by pythoncom (using sys.coinit_flags as the param, or COINIT_APARTMENTTHREADED if sys.coinit_flags does not exist). You must call this manually if you create a thread which wishes to use COM.Return ValueThis function will raise pythoncom.error for all error return values, including RPC_E_CHANGED_MODE error.  This is in contrast to pythoncom::CoInitialize which will hide that specific error.  If your code is happy to work in a threading model other than the one you specified, you must explicitly handle (and presumably ignore) this exception.

Returns:

      None:Flags for the initialization.Comments

There is no need to call this for the main Python thread, as it is called 

automatically by pythoncom (using sys.coinit_flags as the param, or COINIT_APARTMENTTHREADED 

if sys.coinit_flags does not exist). 

You must call this manually if you create a thread which wishes to use COM.
Return ValueThis function will raise pythoncom.error for all error 

return values, including RPC_E_CHANGED_MODE error.  This is 

in contrast to pythoncom::CoInitialize which will hide that 

specific error.  If your code is happy to work in a threading model 

other than the one you specified, you must explicitly handle 

(and presumably ignore) this exception.

        
    """
    pass
        

def CoInitializeSecurity(sd:'PySECURITY_DESCRIPTOR',authSvc:'Any',reserved1:'Any',authnLevel:'int',impLevel:'int',authInfo:'Any',capabilities:'int',reserved2:'Any') -> 'None':
    """
    Registers security and sets the default security values.

Args:

      sd(PySECURITY_DESCRIPTOR):Security descriptor containing access permissions for process' objects, can be None. If Capabilities contains EOAC_APPID, sd should be an AppId (guid), or None to use server executable. If Capabilities contains EOAC_ACCESS_CONTROL, sd parameter should be an IAccessControl interface.
      authSvc(Any):A value of None tells COM to choose which authentication services to use.  An empty list means use no services.
      reserved1(Any):Must be None
      authnLevel(int):One of pythoncom.RPC_C_AUTHN_LEVEL_* values. The default authentication level for proxies. On the server side, COM will fail calls that arrive at a lower level. All calls to AddRef and Release are made at this level.
      impLevel(int):One of pythoncom.RPC_C_IMP_LEVEL_* values.  The default impersonation level for proxies. This value is not checked on the server side. AddRef and Release calls are made with this impersonation level so even security aware apps should set this carefully. Setting IUnknown security only affects calls to QueryInterface, not AddRef or Release.
      authInfo(Any):Must be None
      capabilities(int):Authentication capabilities, combination of pythoncom.EOAC_* flags.
      reserved2(Any):Must be None

Returns:

      None
        
    """
    pass
        

def CoGetInterfaceAndReleaseStream(stream:'PyIStream',iid:'PyIID') -> 'PyIUnknown':
    """
    Unmarshals a buffer containing an interface pointer 

and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.

Args:

      stream(PyIStream):The stream to unmarshal the object from.
      iid(PyIID):The IID if the interface to unmarshal.

Returns:

      PyIUnknown
        
    """
    pass
        

def CoMarshalInterThreadInterfaceInStream(iid:'PyIID',unk:'PyIUnknown') -> 'PyIStream':
    """
    Marshals an interface pointer from one thread 

to another thread in the same process.

Args:

      iid(PyIID):The IID of the interface to marshal.
      unk(PyIUnknown):The interface to marshal.

Returns:

      PyIStream
        
    """
    pass
        

def CoMarshalInterface(Stm:'PyIStream',riid:'PyIID',Unk:'PyIUnknown',DestContext:'int',flags:'int') -> 'None':
    """
    Marshals an interface into a stream

Args:

      Stm(PyIStream):An IStream interface into which marshalled interface will be written
      riid(PyIID):IID of interface to be marshalled
      Unk(PyIUnknown):Base IUnknown of the object to be marshalled
      DestContext(int):MSHCTX_* flag indicating where object will be unmarshalled
      flags(int):MSHLFLAGS_* flag indicating marshalling options

Returns:

      None
        
    """
    pass
        

def CoUnmarshalInterface(Stm:'PyIStream',riid:'PyIID') -> 'Any':
    """
    Unmarshals an interface

Args:

      Stm(PyIStream):Stream containing marshalled interface
      riid(PyIID):IID of interface to be unmarshalled

Returns:

      Any
        
    """
    pass
        

def CoReleaseMarshalData(Stm:'PyIStream') -> 'None':
    """
    Frees resources used by a marshalled interface

Args:

      Stm(PyIStream):Stream containing marshalled interfaceCommentsThis is usually only needed when the interface could not be successfully unmarshalled

Returns:

      None
        
    """
    pass
        

def CoGetObject(name:'str',iid:'PyIID',bindOpts:'None'=None) -> 'PyIUnknown':
    """
    Converts a display name into a moniker that identifies the object 

named, and then binds to the object identified by the moniker.

Args:

      name(str):
      iid(PyIID):The IID of the interface to return.
      bindOpts(None):Must be None

Returns:

      PyIUnknown
        
    """
    pass
        

def CoUninitialize() -> 'None':
    """
    Uninitialize the COM libraries for the calling thread.

Args:



Returns:

      None
        
    """
    pass
        

def CoRegisterClassObject(iid:'PyIID',factory:'PyIUnknown',context:'int',flags:'int') -> 'int':
    """
    Registers an EXE class object with OLE so other applications can 

connect to it.

Args:

      iid(PyIID):The IID of the object to register
      factory(PyIUnknown):The class factory object.  It is the Python programmers responsibility to ensure this object remains alive until the class is unregistered.
      context(int):The create context for the server.  Must be a combination of the CLSCTX_* flags.
      flags(int):Create flags.CommentsThe class factory object should be PyIClassFactory object, but as per the COM documentation, only PyIUnknown is checked.Return ValueThe result is a handle which should be revoked using pythoncom::CoRevokeClassObject

Returns:

      int:Create flags.Comments

The class factory object should be PyIClassFactory object, but as per the COM documentation, only PyIUnknown is checked.
Return ValueThe result is a handle which should be revoked using pythoncom::CoRevokeClassObject

        
    """
    pass
        

def CoResumeClassObjects() -> 'None':
    """
    Called by a server that can register multiple class objects to inform the 

OLE SCM about all registered classes, and permits activation requests for those class objects.

Args:



Returns:

      None
        
    """
    pass
        

def CoRevokeClassObject(reg:'int') -> 'None':
    """
    None

Args:

      reg(int):The value returned from pythoncom::CoRegisterClassObject

Returns:

      None
        
    """
    pass
        

def CoTreatAsClass(clsidold:'PyIID',clsidnew:'PyIID') -> 'None':
    """
    Establishes or removes an emulation, in which objects of one class are treated as 

objects of a different class.

Args:

      clsidold(PyIID):CLSID of the object to be emulated.
      clsidnew(PyIID):CLSID of the object that should emulate the original object. This replaces any existing emulation for clsidOld. Can be ommitted or CLSID_NULL, in which case any existing emulation for clsidOld is removed.

Returns:

      None
        
    """
    pass
        

def CoWaitForMultipleHandles(Flags:'int',Timeout:'int',Handles:'List[int]') -> 'int':
    """
    Waits for specified handles to be signaled or for a specified 

timeout period to elapse.

Args:

      Flags(int):Combination of pythoncom.COWAIT_* values
      Timeout(int):Timeout in milliseconds
      Handles(List[int]):Sequence of handles

Returns:

      int
        
    """
    pass
        

def Connect(cls:'Any') -> 'PyIDispatch':
    """
    Connect to an already running OLE automation server.

Args:

      cls(Any):An identifier for the program.  Usually "program.item"CommentsThis function is equivalent to pythoncom::GetActiveObject(clsid).pythoncom::QueryInterace(pythoncom.IID_IDispatch)

Returns:

      PyIDispatch
        
    """
    pass
        

def CreateGuid() -> 'PyIID':
    """
    Creates a new, unique GUIID.

Args:



Returns:

      PyIID
        
    """
    pass
        

def CreateBindCtx() -> 'PyIBindCtx':
    """
    None

Args:



Returns:

      PyIBindCtx
        
    """
    pass
        

def CreateFileMoniker(filename:'str') -> 'PyIMoniker':
    """
    None

Args:

      filename(str):The name of the file.

Returns:

      PyIMoniker
        
    """
    pass
        

def CreateItemMoniker(delim:'str',item:'str') -> 'PyIMoniker':
    """
    Creates an item moniker 

that identifies an object within a containing object (typically a compound document).

Args:

      delim(str):String containing the delimiter (typically "!") used to separate this item's display name from the display name of its containing object.
      item(str):String indicating the containing object's name for the object being identified.

Returns:

      PyIMoniker
        
    """
    pass
        

def CreatePointerMoniker(IUnknown:'PyIUnknown') -> 'PyIMoniker':
    """
    None

Args:

      IUnknown(PyIUnknown):The interface for the moniker.

Returns:

      PyIMoniker
        
    """
    pass
        

def CreateTypeLib() -> 'Any':
    """
    Provides access to a new object instance that supports the 

ICreateTypeLib interface.

Args:



Returns:

      Any
        
    """
    pass
        

def CreateTypeLib2() -> 'Any':
    """
    Provides access to a new object instance that supports the 

ICreateTypeLib2 interface.

Args:



Returns:

      Any
        
    """
    pass
        

def CreateStreamOnHGlobal(hGlobal:'int'=None,DeleteOnRelease:'bool'=True) -> 'PyIStream':
    """
    Creates an in-memory stream storage object

Args:

      hGlobal(int):Global memory handle.  If None, a new global memory object is allocated.
      DeleteOnRelease(bool):Indicates if global memory should be freed when IStream object is destroyed.

Returns:

      PyIStream
        
    """
    pass
        

def CreateILockBytesOnHGlobal(hGlobal:'int'=None,DeleteOnRelease:'bool'=True) -> 'PyILockBytes':
    """
    Creates an ILockBytes interface based on global memory

Args:

      hGlobal(int):Global memory handle.  If None, a new global memory object is allocated.
      DeleteOnRelease(bool):Indicates if global memory should be freed when interface is released.

Returns:

      PyILockBytes
        
    """
    pass
        

def EnableQuitMessage(threadId:'int') -> 'None':
    """
    Indicates the thread PythonCOM should post a WM_QUIT message to.

Args:

      threadId(int):The thread ID.

Returns:

      None
        
    """
    pass
        

def FUNCDESC() -> 'FUNCDESC':
    """
    Creates a new FUNCDESC object

Args:



Returns:

      FUNCDESC
        
    """
    pass
        

def GetActiveObject(cls:'Any') -> 'PyIUnknown':
    """
    Retrieves an object representing a running object registered with 

OLE

Args:

      cls(Any):The IID for the program.  As for all CLSID's in Python, a "program.name" or IID format string may be used, or a real PyIID object.

Returns:

      PyIUnknown
        
    """
    pass
        

def GetClassFile(fileName:'str') -> 'PyIID':
    """
    Supplies the CLSID associated with the given filename.

Args:

      fileName(str):The filename for which you are requesting the associated CLSID.

Returns:

      PyIID
        
    """
    pass
        

def GetFacilityString(scode:'int') -> 'str':
    """
    Returns the facility string, given an OLE scode.

Args:

      scode(int):The OLE error code for the facility string requested.

Returns:

      str
        
    """
    pass
        

def GetRecordFromGuids(iid:'PyIID',verMajor:'int',verMinor:'int',lcid:'int',infoIID:'PyIID',data:'Any'=None) -> 'Any':
    """
    Creates a new record object from the given GUIDs

Args:

      iid(PyIID):The GUID of the type library
      verMajor(int):The major version number of the type lib.
      verMinor(int):The minor version number of the type lib.
      lcid(int):The LCID of the type lib.
      infoIID(PyIID):The GUID of the record info in the library
      data(Any):The raw data to initialize the record with.

Returns:

      Any
        
    """
    pass
        

def GetRecordFromTypeInfo(TypeInfo:'PyITypeInfo') -> 'Any':
    """
    None

Args:

      TypeInfo(PyITypeInfo):The type information to be converted into a PyRecord objectCommentsThis function will fail if the specified type info does not have a guid defined

Returns:

      Any
        
    """
    pass
        

def GetRunningObjectTable(reserved:'int'=0) -> 'PyIRunningObjectTable':
    """
    None

Args:

      reserved(int):A reserved parameter.  Should be zero unless you have inside information that I don't!

Returns:

      PyIRunningObjectTable
        
    """
    pass
        

def GetScodeString(scode:'int') -> 'str':
    """
    Returns the string for an OLE scode (HRESULT)

Args:

      scode(int):The OLE error code for the scode string requested.CommentsThis will obtain the COM Error message for a given HRESULT. Internally, PythonCOM uses this function to obtain the description when a com_error COM Exception is raised.

Returns:

      str
        
    """
    pass
        

def GetScodeRangeString(scode:'int') -> 'str':
    """
    Returns the scode range string, given an OLE scode.

Args:

      scode(int):An OLE error code to return the scode range string for.

Returns:

      str
        
    """
    pass
        

def GetSeverityString(scode:'int') -> 'str':
    """
    Returns the severity string, given an OLE scode.

Args:

      scode(int):The OLE error code for the severity string requested.

Returns:

      str
        
    """
    pass
        

def IsGatewayRegistered(iid:'PyIID') -> 'int':
    """
    Returns true if a gateway has been registered for the given IID

Args:

      iid(PyIID):IID of the interface.

Returns:

      int
        
    """
    pass
        

def LoadRegTypeLib(iid:'PyIID',versionMajor:'int',versionMinor:'int',lcid:'int') -> 'PyITypeLib':
    """
    Loads a registered type library.

Args:

      iid(PyIID):The IID of the type library.
      versionMajor(int):The major version number of the library
      versionMinor(int):The minor version number of the library
      lcid(int):The locale ID to use.CommentsLoadRegTypeLib compares the requested version numbers against those found in the system registry, and takes one of the following actions: If one of the registered libraries exactly matches both the requested major and minor version numbers, then that type library is loaded.  If one or more registered type libraries exactly match the requested major version number, and has a greater minor version number than that requested, the one with the greatest minor version number is loaded.  If none of the registered type libraries exactly match the requested major version number (or if none of those that do exactly match the major version number also have a minor version number greater than or equal to the requested minor version number), then LoadRegTypeLib returns an error.

Returns:

      PyITypeLib
        
    """
    pass
        

def LoadTypeLib(libFileName:'str') -> 'PyITypeLib':
    """
    Loads a registered type library.

Args:

      libFileName(str):The path to the file containing the type information.

Returns:

      PyITypeLib
        
    """
    pass
        

def MakePyFactory(iid:'PyIID') -> 'PyIClassFactory':
    """
    None

Args:

      iid(PyIID):The IID of the object the class factory provides.

Returns:

      PyIClassFactory
        
    """
    pass
        

def MkParseDisplayName(displayName:'str',bindCtx:'PyIBindCtx'=None) -> 'Tuple[PyIMoniker, int, PyIBindCtx]':
    """
    None

Args:

      displayName(str):The display name to parse
      bindCtx(PyIBindCtx):The bind context object to use.CommentsIf a binding context is not provided, then one will be created. Any binding context created or passed in will be returned to the caller.

Returns:

      Tuple[PyIMoniker, int, PyIBindCtx]
        
    """
    pass
        

def New(cls:'Any') -> 'PyIDispatch':
    """
    Create a new instance of an OLE automation server.

Args:

      cls(Any):An identifier for the program.  Usually "program.item"CommentsThis is just a wrapper for the CoCreateInstance method. Specifically, this call is identical to: pythoncom.CoCreateInstance(cls, None, pythoncom.CLSCTX_SERVER, pythoncom.IID_IDispatch)

Returns:

      PyIDispatch
        
    """
    pass
        

def ObjectFromAddress(address:'int',iid:'PyIID') -> 'PyIUnknown':
    """
    Returns a COM object given its address in memory.

Args:

      address(int):The address which holds a COM object
      iid(PyIID):The IID to queryReturn ValueThis method is useful for applications which return objects via non-standard mechanisms - eg, Windows Explorer allows you to send a specific message to the explorer window and the result will be the address of an object Explorer implements. This method allows you to recover the object from that address.

Returns:

      PyIUnknown:The IID to query
Return ValueThis method is useful for applications which return objects via non-standard 

mechanisms - eg, Windows Explorer allows you to send a specific message to the 

explorer window and the result will be the address of an object Explorer implements. 

This method allows you to recover the object from that address.

        
    """
    pass
        

def ObjectFromLresult(lresult:'int',iid:'PyIID',wparm:'int') -> 'PyIUnknown':
    """
    Retrieves a requested 

interface pointer for an object based on a previously generated object reference.

Args:

      lresult(int):
      iid(PyIID):The IID to query
      wparm(int):

Returns:

      PyIUnknown
        
    """
    pass
        

def OleInitialize() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def OleGetClipboard() -> 'PyIDataObject':
    """
    Retrieves a data object that you can use to access the contents 

of the clipboard.

Args:



Returns:

      PyIDataObject
        
    """
    pass
        

def OleFlushClipboard() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def OleIsCurrentClipboard(dataObj:'PyIDataObject') -> 'Union[Any]':
    """
    Determines whether the data object pointer previously placed on 

the clipboard by the OleSetClipboard function is still on the clipboard.

Args:

      dataObj(PyIDataObject):The data object to check

Returns:

      Union[Any]
        
    """
    pass
        

def OleSetClipboard(dataObj:'PyIDataObject') -> 'None':
    """
    Places a pointer to a specific data object onto the clipboard. This makes the 

data object accessible to the OleGetClipboard function.

Args:

      dataObj(PyIDataObject):The data object to place on the clipboard. This parameter can be None in which case the clipboard is emptied.

Returns:

      None
        
    """
    pass
        

def OleLoadFromStream(stream:'PyIStream',iid:'PyIID') -> 'None':
    """
    Load an object from an IStream.

Args:

      stream(PyIStream):The stream to load the object from.
      iid(PyIID):The IID if the interface to load.

Returns:

      None
        
    """
    pass
        

def OleSaveToStream(persist:'PyIPersistStream',stream:'PyIStream') -> 'None':
    """
    Save an object to an IStream.

Args:

      persist(PyIPersistStream):The object to save
      stream(PyIStream):The stream to save the object to.

Returns:

      None
        
    """
    pass
        

def OleLoad(storage:'PyIStorage',iid:'PyIID',site:'PyIOleClientSite') -> 'None':
    """
    Loads into memory an object nested within a specified storage object.

Args:

      storage(PyIStorage):The storage object from which to load
      iid(PyIID):The IID if the interface to load.
      site(PyIOleClientSite):The client site for the object.

Returns:

      None
        
    """
    pass
        

def ProgIDFromCLSID(clsid:'Any') -> 'str':
    """
    Converts a CLSID to a progID.

Args:

      clsid(Any):A CLSID (either in a string, or in an PyIID object)

Returns:

      str
        
    """
    pass
        

def PumpWaitingMessages() -> 'int':
    """
    Pumps all waiting messages for the current thread.

Args:



Returns:

      int:Search for PeekMessage and DispatchMessage at msdn, google or google groups.
Return ValueReturns 1 if a WM_QUIT message was received, else 0

        
    """
    pass
        

def PumpMessages() -> 'None':
    """
    Pumps all messages for the current thread until a WM_QUIT message.

Args:



Returns:

      None
        
    """
    pass
        

def QueryPathOfRegTypeLib(iid:'PyIID',versionMajor:'int',versionMinor:'int',lcid:'int') -> 'str':
    """
    Retrieves the path of a registered type library.

Args:

      iid(PyIID):The IID of the type library.
      versionMajor(int):The major version number of the library
      versionMinor(int):The minor version number of the library
      lcid(int):The locale ID to use.

Returns:

      str
        
    """
    pass
        

def ReadClassStg(storage:'PyIStorage') -> 'PyIID':
    """
    Reads a CLSID from a storage object.

Args:

      storage(PyIStorage):The storage to read the CLSID from.

Returns:

      PyIID
        
    """
    pass
        

def ReadClassStm(Stm:'PyIStream') -> 'PyIID':
    """
    Retrieves the CLSID from a stream

Args:

      Stm(PyIStream):An IStream interface

Returns:

      PyIID
        
    """
    pass
        

def RegisterTypeLib(typelib:'PyITypeLib',fullPath:'str',lcid:'int',helpDir:'str'=None) -> 'None':
    """
    Adds information about a type library to the system registry.

Args:

      typelib(PyITypeLib):The type library being registered.
      fullPath(str):Fully qualified path specification for the type library being registered
      lcid(int):The locale ID to use.CommentsThis function can be used during application initialization to register the application's type library correctly. When RegisterTypeLib is called to register a type library, both the minor and major version numbers are registered in hexadecimal.  In addition to filling in a complete registry entry under the type library key, RegisterTypeLib adds entries for each of the dispinterfaces and Automation-compatible interfaces, including dual interfaces. This information is required to create instances of these interfaces. Coclasses are not registered (that is, RegisterTypeLib does not write any values to the CLSID key of the coclass).
      helpDir(str):Directory in which the Help file for the library being registered can be found. Can be None.

Returns:

      None
        
    """
    pass
        

def UnRegisterTypeLib(iid:'PyIID',versionMajor:'int',versionMinor:'int',lcid:'int',syskind:'int') -> 'str':
    """
    Unregister a Type Library.

Args:

      iid(PyIID):The IID of the type library.
      versionMajor(int):The major version number of the library
      versionMinor(int):The minor version number of the library
      lcid(int):The locale ID to use.
      syskind(int):The target operating system.CommentsRemoves type library information from the system registry. Use this API to allow applications to properly uninstall themselves. In-process objects typically call this API from DllUnregisterServer.

Returns:

      str
        
    """
    pass
        

def RegisterActiveObject(obUnknown:'PyIUnknown',clsid:'PyIID',flags:'int') -> 'int':
    """
    Register an object as the active object for its class

Args:

      obUnknown(PyIUnknown):The object to register.
      clsid(PyIID):The CLSID for the object
      flags(int):Flags to use.Return ValueThe result is a handle which should be pass to pythoncom::RevokeActiveObject

Returns:

      int:Flags to use.Return ValueThe result is a handle which should be pass to pythoncom::RevokeActiveObject

        
    """
    pass
        

def RevokeActiveObject(handle:'int') -> 'None':
    """
    Ends an objects status as active.

Args:

      handle(int):A handle obtained from pythoncom::RegisterActiveObject

Returns:

      None
        
    """
    pass
        

def RegisterDragDrop(hwnd:'int',dropTarget:'PyIDropTarget') -> 'None':
    """
    None

Args:

      hwnd(int):Handle to a window
      dropTarget(PyIDropTarget):Object that implements the IDropTarget interface

Returns:

      None
        
    """
    pass
        

def RevokeDragDrop(hwnd:'int') -> 'None':
    """
    Revokes the registration of the 

specified application window as a potential target for OLE drag-and-drop 

operations.

Args:

      hwnd(int):Handle to a window registered as an OLE drop target.

Returns:

      None
        
    """
    pass
        

def DoDragDrop() -> 'None':
    """
    Carries out an OLE drag and drop operation.

Args:



Returns:

      None
        
    """
    pass
        

def StgCreateDocfile(name:'str',mode:'int',reserved:'int'=0) -> 'PyIStorage':
    """
    None

Args:

      name(str):the path of the compound file to create. It is passed uninterpreted to the file system. This can be a relative name or None.  If None, a temporary stream is created.
      mode(int):Specifies the access mode used to open the storage.
      reserved(int):A reserved value

Returns:

      PyIStorage
        
    """
    pass
        

def StgCreateDocfileOnILockBytes(lockBytes:'PyILockBytes',mode:'int',reserved:'int'=0) -> 'PyIStorage':
    """
    None

Args:

      lockBytes(PyILockBytes):The PyILockBytes interface on the underlying byte array object on which to create a compound file.
      mode(int):Specifies the access mode used to open the storage.
      reserved(int):A reserved value

Returns:

      PyIStorage
        
    """
    pass
        

def StgOpenStorageOnILockBytes(lockBytes:'PyILockBytes',stgPriority:'PyIStorage',snbExclude:'Any'=None,reserved:'int'=0) -> 'PyIStorage':
    """
    None

Args:

      lockBytes(PyILockBytes):The PyILockBytes interface on the underlying byte array object on which to open an existing storage object.
      stgPriority(PyIStorage):Usually None, or another parent storage.
      snbExclude(Any):Not yet supported - must be None
      reserved(int):A reserved value

Returns:

      PyIStorage
        
    """
    pass
        

def StgIsStorageFile(name:'str') -> 'int':
    """
    Indicates whether a particular disk file contains a storage object.

Args:

      name(str):The path to the file to check.Return ValueThe return value is 1 if a storage file, else 0.  This method will also raise com_error if the StgIsStorageFile function returns a failure HRESULT.

Returns:

      int:The path to the file to check.Return ValueThe return value is 1 if a storage file, else 0.  This 

method will also raise com_error if the StgIsStorageFile function 

returns a failure HRESULT.

        
    """
    pass
        

def STGMEDIUM() -> 'PySTGMEDIUM':
    """
    Creates a new STGMEDIUM object

Args:



Returns:

      PySTGMEDIUM
        
    """
    pass
        

def StgOpenStorage(name:'str',other:'PyIStorage',mode:'int',snbExclude:'Any'=None,reserved:'int'=0) -> 'PyIStorage':
    """
    Opens an existing root storage object in the file system.

Args:

      name(str):Name of the stream, or possibly None if storageOther is non None.
      other(PyIStorage):Usually None, or another parent storage.
      mode(int):Specifies the access mode used to open the storage.  A combination of the storagecon.STGM_* constants.
      snbExclude(Any):Not yet supported - must be None
      reserved(int):A reserved value

Returns:

      PyIStorage
        
    """
    pass
        

def StgOpenStorageEx(Name:'str',Mode:'int',stgfmt:'int',Attrs:'int',riid:'PyIID',StgOptions:'dict'=None) -> 'PyIStorage':
    """
    Advanced version of StgOpenStorage, win2k or better

Args:

      Name(str):Name of the stream or file to open
      Mode(int):Access mode, combination of storagecon.STGM_* flags
      stgfmt(int):Storage format (STGFMT_STORAGE,STGFMT_FILE,STGFMT_ANY, or STGFMT_DOCFILE)
      Attrs(int):File flags and attributes, only used with STGFMT_DOCFILE
      riid(PyIID):Interface id to return, IStorage or IPropertySetStorage
      StgOptions(dict):Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)CommentsRequires Win2k or laterAccepts keyword args

Returns:

      PyIStorage
        
    """
    pass
        

def StgCreateStorageEx(Name:'str',Mode:'int',stgfmt:'int',Attrs:'int',riid:'PyIID',StgOptions:'dict'=None,SecurityDescriptor:'PySECURITY_DESCRIPTOR'=None) -> 'PyIStorage':
    """
    Creates a new structured storage file or property set

Args:

      Name(str):Name of the stream or file to open
      Mode(int):Access mode, combination of storagecon.STGM_* flags
      stgfmt(int):Storage format, storagecon.STGFMT_*
      Attrs(int):File flags and attributes, only used with STGFMT_DOCFILE
      riid(PyIID):Interface id to return, IStorage or IPropertySetStorage
      StgOptions(dict):Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)
      SecurityDescriptor(PySECURITY_DESCRIPTOR):Specifies security for the new file. Must be None on Windows XP.CommentsRequires Win2k or laterAccepts keyword args

Returns:

      PyIStorage
        
    """
    pass
        

def TYPEATTR() -> 'TYPEATTR':
    """
    Creates a new TYPEATTR object

Args:



Returns:

      TYPEATTR
        
    """
    pass
        

def VARDESC() -> 'VARDESC':
    """
    Creates a new VARDESC object

Args:



Returns:

      VARDESC
        
    """
    pass
        

def WrapObject(ob:'Any',gatewayIID:'PyIID',interfaceIID:'PyIID') -> 'PyIUnknown':
    """
    Wraps a Python instance in a gateway object.

Args:

      ob(Any):The object to wrap.
      gatewayIID(PyIID):The IID of the gateway object to create (ie, the interface of the server object wrapped by the return value)
      interfaceIID(PyIID):The IID of the interface object to create (ie, the interface of the returned object)Return ValueNote that there are 2 objects created by this call - a gateway (server) object, suitable for use by other external COM clients/hosts, as well as the returned Python interface (client) object, which maps to the new gateway. There are some unusual cases where the 2 IID parameters will not be identical. If you need to do this, you should know exactly what you are doing, and why!

Returns:

      PyIUnknown:The IID of the interface object to create (ie, the interface of the 

returned object)
Return ValueNote that there are 2 objects created by this call - a gateway (server) object, suitable for 

use by other external COM clients/hosts, as well as the returned Python interface (client) object, which 

maps to the new gateway. 

There are some unusual cases where the 2 IID parameters will not be identical. 

If you need to do this, you should know exactly what you are doing, and why!

        
    """
    pass
        

def WriteClassStg(storage:'PyIStorage',iid:'PyIID') -> 'None':
    """
    Writes a CLSID to a storage object

Args:

      storage(PyIStorage):Storage object into which CLSID will be written.
      iid(PyIID):The IID to write

Returns:

      None
        
    """
    pass
        

def WriteClassStm(Stm:'PyIStream',clsid:'PyIID') -> 'None':
    """
    Writes a CLSID to a stream.

Args:

      Stm(PyIStream):An IStream interface
      clsid(PyIID):The IID to write

Returns:

      None
        
    """
    pass
        

def UnwrapObject(ob:'PyIUnknown') -> 'PyIDispatch':
    """
    Unwraps a Python instance in a gateway object.

Args:

      ob(PyIUnknown):The object to unwrap.CommentsIf the object is not a PythonCOM object, then ValueError is raised.

Returns:

      PyIDispatch
        
    """
    pass
        

def FmtIdToPropStgName(fmtid:'PyIID') -> 'Any':
    """
    Converts a FMTID to its stream name

Args:

      fmtid(PyIID):Format id - a property storage GUID (FMTID_* IIDs)

Returns:

      Any
        
    """
    pass
        

def PropStgNameToFmtId(Name:'Union[str, Any]') -> 'PyIID':
    """
    Converts a property set name to its format id (GUID)

Args:

      Name(Union[str, Any]):Storage stream name

Returns:

      PyIID
        
    """
    pass
        

def CoGetCallContext(riid:'PyIID') -> 'PyIServerSecurity':
    """
    Creates interfaces used to access client security 

requirements and perform impersonation

Args:

      riid(PyIID):The interface to create, IID_IServerSecurity or IID_ISecurityCallContextCommentsISecurityCallContext will only be available for a server that uses role-based security

Returns:

      PyIServerSecurity
        
    """
    pass
        

def CoGetObjectContext(riid:'PyIID') -> 'PyIContext':
    """
    Creates an interface to interact with the context of the 

current object

Args:

      riid(PyIID):The interface to returnCommentsRequires Win2k or laterCOM applications can use this function to create IComThreadingInfo, IContext, or IContextCallback COM+ applications may also create IObjectContext, IObjectContextInfo, IObjectContextActivity, or IContextState

Returns:

      PyIContext
        
    """
    pass
        

def CoGetCancelObject(riid:'PyIID',ThreadID:'int'=0) -> 'PyICancelMethodCalls':
    """
    Retrieves an interface used to cancel a pending call

Args:

      riid(PyIID):The interface to returnCommentsRequires Win2k or later
      ThreadID(int):Id of thread with pending call, or 0 for current thread

Returns:

      PyICancelMethodCalls
        
    """
    pass
        

def CoSetCancelObject(Unk:'PyIUnknown') -> 'None':
    """
    None

Args:

      Unk(PyIUnknown):An interface that support ICancelMethodCalls, can be None to unregister current cancel objectCommentsRequires Win2k or later

Returns:

      None
        
    """
    pass
        

def CoEnableCallCancellation() -> 'None':
    """
    Enables call cancellation for synchronous calls on the current thread

Args:



Returns:

      None
        
    """
    pass
        

def CoDisableCallCancellation() -> 'None':
    """
    Disables call cancellation for synchronous calls on the current thread

Args:



Returns:

      None
        
    """
    pass
        