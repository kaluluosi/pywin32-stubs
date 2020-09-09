__all__=['', '_GetInterfaceCount', '_GetInterfaceCount', 'CoCreateFreeThreadedMarshaler', 'CoCreateInstanceEx', 'CoCreateInstance', 'CoFreeUnusedLibraries', 'CoInitialize', 'CoInitializeEx', 'CoInitializeSecurity', 'CoGetInterfaceAndReleaseStream', 'CoMarshalInterThreadInterfaceInStream', 'CoMarshalInterface', 'CoUnmarshalInterface', 'CoReleaseMarshalData', 'CoGetObject', 'CoUninitialize', 'CoRegisterClassObject', 'CoResumeClassObjects', 'CoRevokeClassObject', 'CoTreatAsClass', 'CoWaitForMultipleHandles', 'Connect', 'CreateGuid', 'CreateBindCtx', 'CreateFileMoniker', 'CreateItemMoniker', 'CreatePointerMoniker', 'CreateTypeLib', 'CreateTypeLib2', 'CreateStreamOnHGlobal', 'CreateILockBytesOnHGlobal', 'EnableQuitMessage', 'FUNCDESC', 'GetActiveObject', 'GetClassFile', 'GetFacilityString', 'GetRecordFromGuids', 'GetRecordFromTypeInfo', 'GetRunningObjectTable', 'GetScodeString', 'GetScodeRangeString', 'GetSeverityString', 'IsGatewayRegistered', 'LoadRegTypeLib', 'LoadTypeLib', 'MakePyFactory', 'MkParseDisplayName', 'New', 'ObjectFromAddress', 'ObjectFromLresult', 'OleInitialize', 'OleGetClipboard', 'OleFlushClipboard', 'OleIsCurrentClipboard', 'OleSetClipboard', 'OleLoadFromStream', 'OleSaveToStream', 'OleLoad', 'ProgIDFromCLSID', 'PumpWaitingMessages', 'PumpMessages', 'QueryPathOfRegTypeLib', 'ReadClassStg', 'ReadClassStm', 'RegisterTypeLib', 'UnRegisterTypeLib', 'RegisterActiveObject', 'RevokeActiveObject', 'RegisterDragDrop', 'RevokeDragDrop', 'DoDragDrop', 'StgCreateDocfile', 'StgCreateDocfileOnILockBytes', 'StgOpenStorageOnILockBytes', 'StgIsStorageFile', 'STGMEDIUM', 'StgOpenStorage', 'StgOpenStorageEx', 'StgCreateStorageEx', 'TYPEATTR', 'VARDESC', 'WrapObject', 'WriteClassStg', 'WriteClassStm', 'UnwrapObject', 'FmtIdToPropStgName', 'PropStgNameToFmtId', 'CoGetCallContext', 'CoGetObjectContext', 'CoGetCancelObject', 'CoSetCancelObject', 'CoEnableCallCancellation', 'CoDisableCallCancellation']
import typing
from win32helper import win32typing
"""A module, encapsulating the OLE automation API"""


def _GetInterfaceCount() -> 'typing.Any':
    """
    Retrieves the number of interface objects currently in existance

Args:



Returns:

      typing.Any
        
    """
    pass
        

def _GetInterfaceCount() -> 'typing.Any':
    """
    Retrieves the number of interface objects currently in existance

Args:



Returns:

      typing.Any
        
    """
    pass
        

def CoCreateFreeThreadedMarshaler(unk:'win32typing.PyIUnknown') -> 'win32typing.PyIUnknown':
    """
    Creates an aggregatable object capable of 

context-dependent marshaling.

Args:

      unk(win32typing.PyIUnknown):The unknown object to marshal.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def CoCreateInstanceEx(clsid:'win32typing.PyIID',unkOuter:'win32typing.PyIUnknown',context:'typing.Any',serverInfo:'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]',iids:'typing.List[win32typing.PyIID]') -> 'win32typing.PyIUnknown':
    """
    Create a new instance of an OLE automation server possibly on a 

remote machine.

Args:

      clsid(win32typing.PyIID):Class identifier (CLSID) of the object
      unkOuter(win32typing.PyIUnknown):The outer unknown, or None
      context(typing.Any):The create context for the object, combination of pythoncom.CLSCTX_* flags
      serverInfo(typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]):May be None, or describes the remote server to execute on.
      iids(typing.List[win32typing.PyIID]):A list of IIDs required from the object

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def CoCreateInstance(clsid:'win32typing.PyIID',unkOuter:'win32typing.PyIUnknown',context:'typing.Any',iid:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Create a new instance of an OLE automation server.

Args:

      clsid(win32typing.PyIID):Class identifier (CLSID) of the object
      unkOuter(win32typing.PyIUnknown):The outer unknown, or None
      context(typing.Any):The create context for the object, combination of pythoncom.CLSCTX_* flags
      iid(win32typing.PyIID):The IID required from the object

Returns:

      win32typing.PyIUnknown
        
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
        

def CoInitializeEx(flags:'typing.Any') -> 'None':
    """
    Initialize the COM libraries for the calling thread.

Args:

      flags(typing.Any):Flags for the initialization.CommentsThere is no need to call this for the main Python thread, as it is called automatically by pythoncom (using sys.coinit_flags as the param, or COINIT_APARTMENTTHREADED if sys.coinit_flags does not exist). You must call this manually if you create a thread which wishes to use COM.Return ValueThis function will raise pythoncom.error for all error return values, including RPC_E_CHANGED_MODE error.  This is in contrast to pythoncom::CoInitialize which will hide that specific error.  If your code is happy to work in a threading model other than the one you specified, you must explicitly handle (and presumably ignore) this exception.

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
        

def CoInitializeSecurity(sd:'win32typing.PySECURITY_DESCRIPTOR',authSvc:'typing.Any',reserved1:'typing.Any',authnLevel:'typing.Any',impLevel:'typing.Any',authInfo:'typing.Any',capabilities:'typing.Any',reserved2:'typing.Any') -> 'None':
    """
    Registers security and sets the default security values.

Args:

      sd(win32typing.PySECURITY_DESCRIPTOR):Security descriptor containing access permissions for process' objects, can be None. If Capabilities contains EOAC_APPID, sd should be an AppId (guid), or None to use server executable. If Capabilities contains EOAC_ACCESS_CONTROL, sd parameter should be an IAccessControl interface.
      authSvc(typing.Any):A value of None tells COM to choose which authentication services to use.  An empty list means use no services.
      reserved1(typing.Any):Must be None
      authnLevel(typing.Any):One of pythoncom.RPC_C_AUTHN_LEVEL_* values. The default authentication level for proxies. On the server side, COM will fail calls that arrive at a lower level. All calls to AddRef and Release are made at this level.
      impLevel(typing.Any):One of pythoncom.RPC_C_IMP_LEVEL_* values.  The default impersonation level for proxies. This value is not checked on the server side. AddRef and Release calls are made with this impersonation level so even security aware apps should set this carefully. Setting IUnknown security only affects calls to QueryInterface, not AddRef or Release.
      authInfo(typing.Any):Must be None
      capabilities(typing.Any):Authentication capabilities, combination of pythoncom.EOAC_* flags.
      reserved2(typing.Any):Must be None

Returns:

      None
        
    """
    pass
        

def CoGetInterfaceAndReleaseStream(stream:'win32typing.PyIStream',iid:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Unmarshals a buffer containing an interface pointer 

and releases the stream when an interface pointer has been marshaled from another thread to the calling thread.

Args:

      stream(win32typing.PyIStream):The stream to unmarshal the object from.
      iid(win32typing.PyIID):The IID if the interface to unmarshal.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def CoMarshalInterThreadInterfaceInStream(iid:'win32typing.PyIID',unk:'win32typing.PyIUnknown') -> 'win32typing.PyIStream':
    """
    Marshals an interface pointer from one thread 

to another thread in the same process.

Args:

      iid(win32typing.PyIID):The IID of the interface to marshal.
      unk(win32typing.PyIUnknown):The interface to marshal.

Returns:

      win32typing.PyIStream
        
    """
    pass
        

def CoMarshalInterface(Stm:'win32typing.PyIStream',riid:'win32typing.PyIID',Unk:'win32typing.PyIUnknown',DestContext:'typing.Any',flags:'typing.Any') -> 'None':
    """
    Marshals an interface into a stream

Args:

      Stm(win32typing.PyIStream):An IStream interface into which marshalled interface will be written
      riid(win32typing.PyIID):IID of interface to be marshalled
      Unk(win32typing.PyIUnknown):Base IUnknown of the object to be marshalled
      DestContext(typing.Any):MSHCTX_* flag indicating where object will be unmarshalled
      flags(typing.Any):MSHLFLAGS_* flag indicating marshalling options

Returns:

      None
        
    """
    pass
        

def CoUnmarshalInterface(Stm:'win32typing.PyIStream',riid:'win32typing.PyIID') -> 'typing.Any':
    """
    Unmarshals an interface

Args:

      Stm(win32typing.PyIStream):Stream containing marshalled interface
      riid(win32typing.PyIID):IID of interface to be unmarshalled

Returns:

      typing.Any
        
    """
    pass
        

def CoReleaseMarshalData(Stm:'win32typing.PyIStream') -> 'None':
    """
    Frees resources used by a marshalled interface

Args:

      Stm(win32typing.PyIStream):Stream containing marshalled interfaceCommentsThis is usually only needed when the interface could not be successfully unmarshalled

Returns:

      None
        
    """
    pass
        

def CoGetObject(name:'str',iid:'win32typing.PyIID',bindOpts:'typing.Any'=None) -> 'win32typing.PyIUnknown':
    """
    Converts a display name into a moniker that identifies the object 

named, and then binds to the object identified by the moniker.

Args:

      name(str):
      iid(win32typing.PyIID):The IID of the interface to return.
      bindOpts(typing.Any):Must be None

Returns:

      win32typing.PyIUnknown
        
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
        

def CoRegisterClassObject(iid:'win32typing.PyIID',factory:'win32typing.PyIUnknown',context:'typing.Any',flags:'typing.Any') -> 'typing.Any':
    """
    Registers an EXE class object with OLE so other applications can 

connect to it.

Args:

      iid(win32typing.PyIID):The IID of the object to register
      factory(win32typing.PyIUnknown):The class factory object.  It is the Python programmers responsibility to ensure this object remains alive until the class is unregistered.
      context(typing.Any):The create context for the server.  Must be a combination of the CLSCTX_* flags.
      flags(typing.Any):Create flags.CommentsThe class factory object should be PyIClassFactory object, but as per the COM documentation, only PyIUnknown is checked.Return ValueThe result is a handle which should be revoked using pythoncom::CoRevokeClassObject

Returns:

      typing.Any:Create flags.Comments

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
        

def CoRevokeClassObject(reg:'typing.Any') -> 'None':
    """
    None

Args:

      reg(typing.Any):The value returned from pythoncom::CoRegisterClassObject

Returns:

      None
        
    """
    pass
        

def CoTreatAsClass(clsidold:'win32typing.PyIID',clsidnew:'win32typing.PyIID') -> 'None':
    """
    Establishes or removes an emulation, in which objects of one class are treated as 

objects of a different class.

Args:

      clsidold(win32typing.PyIID):CLSID of the object to be emulated.
      clsidnew(win32typing.PyIID):CLSID of the object that should emulate the original object. This replaces any existing emulation for clsidOld. Can be ommitted or CLSID_NULL, in which case any existing emulation for clsidOld is removed.

Returns:

      None
        
    """
    pass
        

def CoWaitForMultipleHandles(Flags:'typing.Any',Timeout:'typing.Any',Handles:'typing.List[int]') -> 'typing.Any':
    """
    Waits for specified handles to be signaled or for a specified 

timeout period to elapse.

Args:

      Flags(typing.Any):Combination of pythoncom.COWAIT_* values
      Timeout(typing.Any):Timeout in milliseconds
      Handles(typing.List[int]):Sequence of handles

Returns:

      typing.Any
        
    """
    pass
        

def Connect(cls:'typing.Any') -> 'win32typing.PyIDispatch':
    """
    Connect to an already running OLE automation server.

Args:

      cls(typing.Any):An identifier for the program.  Usually "program.item"CommentsThis function is equivalent to pythoncom::GetActiveObject(clsid).pythoncom::QueryInterace(pythoncom.IID_IDispatch)

Returns:

      win32typing.PyIDispatch
        
    """
    pass
        

def CreateGuid() -> 'win32typing.PyIID':
    """
    Creates a new, unique GUIID.

Args:



Returns:

      win32typing.PyIID
        
    """
    pass
        

def CreateBindCtx() -> 'win32typing.PyIBindCtx':
    """
    None

Args:



Returns:

      win32typing.PyIBindCtx
        
    """
    pass
        

def CreateFileMoniker(filename:'str') -> 'win32typing.PyIMoniker':
    """
    None

Args:

      filename(str):The name of the file.

Returns:

      win32typing.PyIMoniker
        
    """
    pass
        

def CreateItemMoniker(delim:'str',item:'str') -> 'win32typing.PyIMoniker':
    """
    Creates an item moniker 

that identifies an object within a containing object (typically a compound document).

Args:

      delim(str):String containing the delimiter (typically "!") used to separate this item's display name from the display name of its containing object.
      item(str):String indicating the containing object's name for the object being identified.

Returns:

      win32typing.PyIMoniker
        
    """
    pass
        

def CreatePointerMoniker(IUnknown:'win32typing.PyIUnknown') -> 'win32typing.PyIMoniker':
    """
    None

Args:

      IUnknown(win32typing.PyIUnknown):The interface for the moniker.

Returns:

      win32typing.PyIMoniker
        
    """
    pass
        

def CreateTypeLib() -> 'typing.Any':
    """
    Provides access to a new object instance that supports the 

ICreateTypeLib interface.

Args:



Returns:

      typing.Any
        
    """
    pass
        

def CreateTypeLib2() -> 'typing.Any':
    """
    Provides access to a new object instance that supports the 

ICreateTypeLib2 interface.

Args:



Returns:

      typing.Any
        
    """
    pass
        

def CreateStreamOnHGlobal(hGlobal:'int'=None,DeleteOnRelease:'typing.Any'=True) -> 'win32typing.PyIStream':
    """
    Creates an in-memory stream storage object

Args:

      hGlobal(int):Global memory handle.  If None, a new global memory object is allocated.
      DeleteOnRelease(typing.Any):Indicates if global memory should be freed when IStream object is destroyed.

Returns:

      win32typing.PyIStream
        
    """
    pass
        

def CreateILockBytesOnHGlobal(hGlobal:'int'=None,DeleteOnRelease:'typing.Any'=True) -> 'win32typing.PyILockBytes':
    """
    Creates an ILockBytes interface based on global memory

Args:

      hGlobal(int):Global memory handle.  If None, a new global memory object is allocated.
      DeleteOnRelease(typing.Any):Indicates if global memory should be freed when interface is released.

Returns:

      win32typing.PyILockBytes
        
    """
    pass
        

def EnableQuitMessage(threadId:'typing.Any') -> 'None':
    """
    Indicates the thread PythonCOM should post a WM_QUIT message to.

Args:

      threadId(typing.Any):The thread ID.

Returns:

      None
        
    """
    pass
        

def FUNCDESC() -> 'win32typing.FUNCDESC':
    """
    Creates a new FUNCDESC object

Args:



Returns:

      win32typing.FUNCDESC
        
    """
    pass
        

def GetActiveObject(cls:'typing.Any') -> 'win32typing.PyIUnknown':
    """
    Retrieves an object representing a running object registered with 

OLE

Args:

      cls(typing.Any):The IID for the program.  As for all CLSID's in Python, a "program.name" or IID format string may be used, or a real PyIID object.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def GetClassFile(fileName:'typing.Any') -> 'win32typing.PyIID':
    """
    Supplies the CLSID associated with the given filename.

Args:

      fileName(typing.Any):The filename for which you are requesting the associated CLSID.

Returns:

      win32typing.PyIID
        
    """
    pass
        

def GetFacilityString(scode:'typing.Any') -> 'str':
    """
    Returns the facility string, given an OLE scode.

Args:

      scode(typing.Any):The OLE error code for the facility string requested.

Returns:

      str
        
    """
    pass
        

def GetRecordFromGuids(iid:'win32typing.PyIID',verMajor:'typing.Any',verMinor:'typing.Any',lcid:'typing.Any',infoIID:'win32typing.PyIID',data:'typing.Any'=None) -> 'typing.Any':
    """
    Creates a new record object from the given GUIDs

Args:

      iid(win32typing.PyIID):The GUID of the type library
      verMajor(typing.Any):The major version number of the type lib.
      verMinor(typing.Any):The minor version number of the type lib.
      lcid(typing.Any):The LCID of the type lib.
      infoIID(win32typing.PyIID):The GUID of the record info in the library
      data(typing.Any):The raw data to initialize the record with.

Returns:

      typing.Any
        
    """
    pass
        

def GetRecordFromTypeInfo(TypeInfo:'win32typing.PyITypeInfo') -> 'typing.Any':
    """
    None

Args:

      TypeInfo(win32typing.PyITypeInfo):The type information to be converted into a PyRecord objectCommentsThis function will fail if the specified type info does not have a guid defined

Returns:

      typing.Any
        
    """
    pass
        

def GetRunningObjectTable(reserved:'typing.Any'=0) -> 'win32typing.PyIRunningObjectTable':
    """
    None

Args:

      reserved(typing.Any):A reserved parameter.  Should be zero unless you have inside information that I don't!

Returns:

      win32typing.PyIRunningObjectTable
        
    """
    pass
        

def GetScodeString(scode:'typing.Any') -> 'str':
    """
    Returns the string for an OLE scode (HRESULT)

Args:

      scode(typing.Any):The OLE error code for the scode string requested.CommentsThis will obtain the COM Error message for a given HRESULT. Internally, PythonCOM uses this function to obtain the description when a com_error COM Exception is raised.

Returns:

      str
        
    """
    pass
        

def GetScodeRangeString(scode:'typing.Any') -> 'str':
    """
    Returns the scode range string, given an OLE scode.

Args:

      scode(typing.Any):An OLE error code to return the scode range string for.

Returns:

      str
        
    """
    pass
        

def GetSeverityString(scode:'typing.Any') -> 'str':
    """
    Returns the severity string, given an OLE scode.

Args:

      scode(typing.Any):The OLE error code for the severity string requested.

Returns:

      str
        
    """
    pass
        

def IsGatewayRegistered(iid:'win32typing.PyIID') -> 'typing.Any':
    """
    Returns true if a gateway has been registered for the given IID

Args:

      iid(win32typing.PyIID):IID of the interface.

Returns:

      typing.Any
        
    """
    pass
        

def LoadRegTypeLib(iid:'win32typing.PyIID',versionMajor:'typing.Any',versionMinor:'typing.Any',lcid:'typing.Any') -> 'win32typing.PyITypeLib':
    """
    Loads a registered type library.

Args:

      iid(win32typing.PyIID):The IID of the type library.
      versionMajor(typing.Any):The major version number of the library
      versionMinor(typing.Any):The minor version number of the library
      lcid(typing.Any):The locale ID to use.CommentsLoadRegTypeLib compares the requested version numbers against those found in the system registry, and takes one of the following actions: If one of the registered libraries exactly matches both the requested major and minor version numbers, then that type library is loaded.  If one or more registered type libraries exactly match the requested major version number, and has a greater minor version number than that requested, the one with the greatest minor version number is loaded.  If none of the registered type libraries exactly match the requested major version number (or if none of those that do exactly match the major version number also have a minor version number greater than or equal to the requested minor version number), then LoadRegTypeLib returns an error.

Returns:

      win32typing.PyITypeLib
        
    """
    pass
        

def LoadTypeLib(libFileName:'str') -> 'win32typing.PyITypeLib':
    """
    Loads a registered type library.

Args:

      libFileName(str):The path to the file containing the type information.

Returns:

      win32typing.PyITypeLib
        
    """
    pass
        

def MakePyFactory(iid:'win32typing.PyIID') -> 'win32typing.PyIClassFactory':
    """
    None

Args:

      iid(win32typing.PyIID):The IID of the object the class factory provides.

Returns:

      win32typing.PyIClassFactory
        
    """
    pass
        

def MkParseDisplayName(displayName:'str',bindCtx:'win32typing.PyIBindCtx'=None) -> 'typing.Tuple[win32typing.PyIMoniker, typing.Any, win32typing.PyIBindCtx]':
    """
    None

Args:

      displayName(str):The display name to parse
      bindCtx(win32typing.PyIBindCtx):The bind context object to use.CommentsIf a binding context is not provided, then one will be created. Any binding context created or passed in will be returned to the caller.

Returns:

      typing.Tuple[win32typing.PyIMoniker, typing.Any, win32typing.PyIBindCtx]
        
    """
    pass
        

def New(cls:'typing.Any') -> 'win32typing.PyIDispatch':
    """
    Create a new instance of an OLE automation server.

Args:

      cls(typing.Any):An identifier for the program.  Usually "program.item"CommentsThis is just a wrapper for the CoCreateInstance method. Specifically, this call is identical to: pythoncom.CoCreateInstance(cls, None, pythoncom.CLSCTX_SERVER, pythoncom.IID_IDispatch)

Returns:

      win32typing.PyIDispatch
        
    """
    pass
        

def ObjectFromAddress(address:'typing.Any',iid:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Returns a COM object given its address in memory.

Args:

      address(typing.Any):The address which holds a COM object
      iid(win32typing.PyIID):The IID to queryReturn ValueThis method is useful for applications which return objects via non-standard mechanisms - eg, Windows Explorer allows you to send a specific message to the explorer window and the result will be the address of an object Explorer implements. This method allows you to recover the object from that address.

Returns:

      win32typing.PyIUnknown:The IID to query
Return ValueThis method is useful for applications which return objects via non-standard 

mechanisms - eg, Windows Explorer allows you to send a specific message to the 

explorer window and the result will be the address of an object Explorer implements. 

This method allows you to recover the object from that address.

        
    """
    pass
        

def ObjectFromLresult(lresult:'typing.Any',iid:'win32typing.PyIID',wparm:'typing.Any') -> 'win32typing.PyIUnknown':
    """
    Retrieves a requested 

interface pointer for an object based on a previously generated object reference.

Args:

      lresult(typing.Any):
      iid(win32typing.PyIID):The IID to query
      wparm(typing.Any):

Returns:

      win32typing.PyIUnknown
        
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
        

def OleGetClipboard() -> 'win32typing.PyIDataObject':
    """
    Retrieves a data object that you can use to access the contents 

of the clipboard.

Args:



Returns:

      win32typing.PyIDataObject
        
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
        

def OleIsCurrentClipboard(dataObj:'win32typing.PyIDataObject') -> 'typing.Union[typing.Any]':
    """
    Determines whether the data object pointer previously placed on 

the clipboard by the OleSetClipboard function is still on the clipboard.

Args:

      dataObj(win32typing.PyIDataObject):The data object to check

Returns:

      typing.Union[typing.Any]
        
    """
    pass
        

def OleSetClipboard(dataObj:'win32typing.PyIDataObject') -> 'None':
    """
    Places a pointer to a specific data object onto the clipboard. This makes the 

data object accessible to the OleGetClipboard function.

Args:

      dataObj(win32typing.PyIDataObject):The data object to place on the clipboard. This parameter can be None in which case the clipboard is emptied.

Returns:

      None
        
    """
    pass
        

def OleLoadFromStream(stream:'win32typing.PyIStream',iid:'win32typing.PyIID') -> 'None':
    """
    Load an object from an IStream.

Args:

      stream(win32typing.PyIStream):The stream to load the object from.
      iid(win32typing.PyIID):The IID if the interface to load.

Returns:

      None
        
    """
    pass
        

def OleSaveToStream(persist:'win32typing.PyIPersistStream',stream:'win32typing.PyIStream') -> 'None':
    """
    Save an object to an IStream.

Args:

      persist(win32typing.PyIPersistStream):The object to save
      stream(win32typing.PyIStream):The stream to save the object to.

Returns:

      None
        
    """
    pass
        

def OleLoad(storage:'win32typing.PyIStorage',iid:'win32typing.PyIID',site:'win32typing.PyIOleClientSite') -> 'None':
    """
    Loads into memory an object nested within a specified storage object.

Args:

      storage(win32typing.PyIStorage):The storage object from which to load
      iid(win32typing.PyIID):The IID if the interface to load.
      site(win32typing.PyIOleClientSite):The client site for the object.

Returns:

      None
        
    """
    pass
        

def ProgIDFromCLSID(clsid:'typing.Any') -> 'str':
    """
    Converts a CLSID to a progID.

Args:

      clsid(typing.Any):A CLSID (either in a string, or in an PyIID object)

Returns:

      str
        
    """
    pass
        

def PumpWaitingMessages() -> 'typing.Any':
    """
    Pumps all waiting messages for the current thread.

Args:



Returns:

      typing.Any:Search for PeekMessage and DispatchMessage at msdn, google or google groups.
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
        

def QueryPathOfRegTypeLib(iid:'win32typing.PyIID',versionMajor:'typing.Any',versionMinor:'typing.Any',lcid:'typing.Any') -> 'str':
    """
    Retrieves the path of a registered type library.

Args:

      iid(win32typing.PyIID):The IID of the type library.
      versionMajor(typing.Any):The major version number of the library
      versionMinor(typing.Any):The minor version number of the library
      lcid(typing.Any):The locale ID to use.

Returns:

      str
        
    """
    pass
        

def ReadClassStg(storage:'win32typing.PyIStorage') -> 'win32typing.PyIID':
    """
    Reads a CLSID from a storage object.

Args:

      storage(win32typing.PyIStorage):The storage to read the CLSID from.

Returns:

      win32typing.PyIID
        
    """
    pass
        

def ReadClassStm(Stm:'win32typing.PyIStream') -> 'win32typing.PyIID':
    """
    Retrieves the CLSID from a stream

Args:

      Stm(win32typing.PyIStream):An IStream interface

Returns:

      win32typing.PyIID
        
    """
    pass
        

def RegisterTypeLib(typelib:'win32typing.PyITypeLib',fullPath:'str',lcid:'typing.Any',helpDir:'str'=None) -> 'None':
    """
    Adds information about a type library to the system registry.

Args:

      typelib(win32typing.PyITypeLib):The type library being registered.
      fullPath(str):Fully qualified path specification for the type library being registered
      lcid(typing.Any):The locale ID to use.CommentsThis function can be used during application initialization to register the application's type library correctly. When RegisterTypeLib is called to register a type library, both the minor and major version numbers are registered in hexadecimal.  In addition to filling in a complete registry entry under the type library key, RegisterTypeLib adds entries for each of the dispinterfaces and Automation-compatible interfaces, including dual interfaces. This information is required to create instances of these interfaces. Coclasses are not registered (that is, RegisterTypeLib does not write any values to the CLSID key of the coclass).
      helpDir(str):Directory in which the Help file for the library being registered can be found. Can be None.

Returns:

      None
        
    """
    pass
        

def UnRegisterTypeLib(iid:'win32typing.PyIID',versionMajor:'typing.Any',versionMinor:'typing.Any',lcid:'typing.Any',syskind:'typing.Any') -> 'str':
    """
    Unregister a Type Library.

Args:

      iid(win32typing.PyIID):The IID of the type library.
      versionMajor(typing.Any):The major version number of the library
      versionMinor(typing.Any):The minor version number of the library
      lcid(typing.Any):The locale ID to use.
      syskind(typing.Any):The target operating system.CommentsRemoves type library information from the system registry. Use this API to allow applications to properly uninstall themselves. In-process objects typically call this API from DllUnregisterServer.

Returns:

      str
        
    """
    pass
        

def RegisterActiveObject(obUnknown:'win32typing.PyIUnknown',clsid:'win32typing.PyIID',flags:'typing.Any') -> 'typing.Any':
    """
    Register an object as the active object for its class

Args:

      obUnknown(win32typing.PyIUnknown):The object to register.
      clsid(win32typing.PyIID):The CLSID for the object
      flags(typing.Any):Flags to use.Return ValueThe result is a handle which should be pass to pythoncom::RevokeActiveObject

Returns:

      typing.Any:Flags to use.Return ValueThe result is a handle which should be pass to pythoncom::RevokeActiveObject

        
    """
    pass
        

def RevokeActiveObject(handle:'typing.Any') -> 'None':
    """
    Ends an objects status as active.

Args:

      handle(typing.Any):A handle obtained from pythoncom::RegisterActiveObject

Returns:

      None
        
    """
    pass
        

def RegisterDragDrop(hwnd:'int',dropTarget:'win32typing.PyIDropTarget') -> 'None':
    """
    None

Args:

      hwnd(int):Handle to a window
      dropTarget(win32typing.PyIDropTarget):Object that implements the IDropTarget interface

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
        

def StgCreateDocfile(name:'str',mode:'typing.Any',reserved:'typing.Any'=0) -> 'win32typing.PyIStorage':
    """
    None

Args:

      name(str):the path of the compound file to create. It is passed uninterpreted to the file system. This can be a relative name or None.  If None, a temporary stream is created.
      mode(typing.Any):Specifies the access mode used to open the storage.
      reserved(typing.Any):A reserved value

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def StgCreateDocfileOnILockBytes(lockBytes:'win32typing.PyILockBytes',mode:'typing.Any',reserved:'typing.Any'=0) -> 'win32typing.PyIStorage':
    """
    None

Args:

      lockBytes(win32typing.PyILockBytes):The PyILockBytes interface on the underlying byte array object on which to create a compound file.
      mode(typing.Any):Specifies the access mode used to open the storage.
      reserved(typing.Any):A reserved value

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def StgOpenStorageOnILockBytes(lockBytes:'win32typing.PyILockBytes',stgPriority:'win32typing.PyIStorage',snbExclude:'typing.Any'=None,reserved:'typing.Any'=0) -> 'win32typing.PyIStorage':
    """
    None

Args:

      lockBytes(win32typing.PyILockBytes):The PyILockBytes interface on the underlying byte array object on which to open an existing storage object.
      stgPriority(win32typing.PyIStorage):Usually None, or another parent storage.
      snbExclude(typing.Any):Not yet supported - must be None
      reserved(typing.Any):A reserved value

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def StgIsStorageFile(name:'str') -> 'typing.Any':
    """
    Indicates whether a particular disk file contains a storage object.

Args:

      name(str):The path to the file to check.Return ValueThe return value is 1 if a storage file, else 0.  This method will also raise com_error if the StgIsStorageFile function returns a failure HRESULT.

Returns:

      typing.Any:The path to the file to check.Return ValueThe return value is 1 if a storage file, else 0.  This 

method will also raise com_error if the StgIsStorageFile function 

returns a failure HRESULT.

        
    """
    pass
        

def STGMEDIUM() -> 'win32typing.PySTGMEDIUM':
    """
    Creates a new STGMEDIUM object

Args:



Returns:

      win32typing.PySTGMEDIUM
        
    """
    pass
        

def StgOpenStorage(name:'str',other:'win32typing.PyIStorage',mode:'typing.Any',snbExclude:'typing.Any'=None,reserved:'typing.Any'=0) -> 'win32typing.PyIStorage':
    """
    Opens an existing root storage object in the file system.

Args:

      name(str):Name of the stream, or possibly None if storageOther is non None.
      other(win32typing.PyIStorage):Usually None, or another parent storage.
      mode(typing.Any):Specifies the access mode used to open the storage.  A combination of the storagecon.STGM_* constants.
      snbExclude(typing.Any):Not yet supported - must be None
      reserved(typing.Any):A reserved value

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def StgOpenStorageEx(Name:'str',Mode:'typing.Any',stgfmt:'typing.Any',Attrs:'typing.Any',riid:'win32typing.PyIID',StgOptions:'typing.Any'=None) -> 'win32typing.PyIStorage':
    """
    Advanced version of StgOpenStorage, win2k or better

Args:

      Name(str):Name of the stream or file to open
      Mode(typing.Any):Access mode, combination of storagecon.STGM_* flags
      stgfmt(typing.Any):Storage format (STGFMT_STORAGE,STGFMT_FILE,STGFMT_ANY, or STGFMT_DOCFILE)
      Attrs(typing.Any):File flags and attributes, only used with STGFMT_DOCFILE
      riid(win32typing.PyIID):Interface id to return, IStorage or IPropertySetStorage
      StgOptions(typing.Any):Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)CommentsRequires Win2k or laterAccepts keyword args

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def StgCreateStorageEx(Name:'str',Mode:'typing.Any',stgfmt:'typing.Any',Attrs:'typing.Any',riid:'win32typing.PyIID',StgOptions:'typing.Any'=None,SecurityDescriptor:'win32typing.PySECURITY_DESCRIPTOR'=None) -> 'win32typing.PyIStorage':
    """
    Creates a new structured storage file or property set

Args:

      Name(str):Name of the stream or file to open
      Mode(typing.Any):Access mode, combination of storagecon.STGM_* flags
      stgfmt(typing.Any):Storage format, storagecon.STGFMT_*
      Attrs(typing.Any):File flags and attributes, only used with STGFMT_DOCFILE
      riid(win32typing.PyIID):Interface id to return, IStorage or IPropertySetStorage
      StgOptions(typing.Any):Dictionary representing STGOPTIONS struct (only used with STGFMT_DOCFILE)
      SecurityDescriptor(win32typing.PySECURITY_DESCRIPTOR):Specifies security for the new file. Must be None on Windows XP.CommentsRequires Win2k or laterAccepts keyword args

Returns:

      win32typing.PyIStorage
        
    """
    pass
        

def TYPEATTR() -> 'win32typing.TYPEATTR':
    """
    Creates a new TYPEATTR object

Args:



Returns:

      win32typing.TYPEATTR
        
    """
    pass
        

def VARDESC() -> 'win32typing.VARDESC':
    """
    Creates a new VARDESC object

Args:



Returns:

      win32typing.VARDESC
        
    """
    pass
        

def WrapObject(ob:'typing.Any',gatewayIID:'win32typing.PyIID',interfaceIID:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Wraps a Python instance in a gateway object.

Args:

      ob(typing.Any):The object to wrap.
      gatewayIID(win32typing.PyIID):The IID of the gateway object to create (ie, the interface of the server object wrapped by the return value)
      interfaceIID(win32typing.PyIID):The IID of the interface object to create (ie, the interface of the returned object)Return ValueNote that there are 2 objects created by this call - a gateway (server) object, suitable for use by other external COM clients/hosts, as well as the returned Python interface (client) object, which maps to the new gateway. There are some unusual cases where the 2 IID parameters will not be identical. If you need to do this, you should know exactly what you are doing, and why!

Returns:

      win32typing.PyIUnknown:The IID of the interface object to create (ie, the interface of the 

returned object)
Return ValueNote that there are 2 objects created by this call - a gateway (server) object, suitable for 

use by other external COM clients/hosts, as well as the returned Python interface (client) object, which 

maps to the new gateway. 

There are some unusual cases where the 2 IID parameters will not be identical. 

If you need to do this, you should know exactly what you are doing, and why!

        
    """
    pass
        

def WriteClassStg(storage:'win32typing.PyIStorage',iid:'win32typing.PyIID') -> 'None':
    """
    Writes a CLSID to a storage object

Args:

      storage(win32typing.PyIStorage):Storage object into which CLSID will be written.
      iid(win32typing.PyIID):The IID to write

Returns:

      None
        
    """
    pass
        

def WriteClassStm(Stm:'win32typing.PyIStream',clsid:'win32typing.PyIID') -> 'None':
    """
    Writes a CLSID to a stream.

Args:

      Stm(win32typing.PyIStream):An IStream interface
      clsid(win32typing.PyIID):The IID to write

Returns:

      None
        
    """
    pass
        

def UnwrapObject(ob:'win32typing.PyIUnknown') -> 'win32typing.PyIDispatch':
    """
    Unwraps a Python instance in a gateway object.

Args:

      ob(win32typing.PyIUnknown):The object to unwrap.CommentsIf the object is not a PythonCOM object, then ValueError is raised.

Returns:

      win32typing.PyIDispatch
        
    """
    pass
        

def FmtIdToPropStgName(fmtid:'win32typing.PyIID') -> 'typing.Any':
    """
    Converts a FMTID to its stream name

Args:

      fmtid(win32typing.PyIID):Format id - a property storage GUID (FMTID_* IIDs)

Returns:

      typing.Any
        
    """
    pass
        

def PropStgNameToFmtId(Name:'typing.Union[typing.Any, str]') -> 'win32typing.PyIID':
    """
    Converts a property set name to its format id (GUID)

Args:

      Name(typing.Union[typing.Any, str]):Storage stream name

Returns:

      win32typing.PyIID
        
    """
    pass
        

def CoGetCallContext(riid:'win32typing.PyIID') -> 'win32typing.PyIServerSecurity':
    """
    Creates interfaces used to access client security 

requirements and perform impersonation

Args:

      riid(win32typing.PyIID):The interface to create, IID_IServerSecurity or IID_ISecurityCallContextCommentsISecurityCallContext will only be available for a server that uses role-based security

Returns:

      win32typing.PyIServerSecurity
        
    """
    pass
        

def CoGetObjectContext(riid:'win32typing.PyIID') -> 'win32typing.PyIContext':
    """
    Creates an interface to interact with the context of the 

current object

Args:

      riid(win32typing.PyIID):The interface to returnCommentsRequires Win2k or laterCOM applications can use this function to create IComThreadingInfo, IContext, or IContextCallback COM+ applications may also create IObjectContext, IObjectContextInfo, IObjectContextActivity, or IContextState

Returns:

      win32typing.PyIContext
        
    """
    pass
        

def CoGetCancelObject(riid:'win32typing.PyIID',ThreadID:'typing.Any'=0) -> 'win32typing.PyICancelMethodCalls':
    """
    Retrieves an interface used to cancel a pending call

Args:

      riid(win32typing.PyIID):The interface to returnCommentsRequires Win2k or later
      ThreadID(typing.Any):Id of thread with pending call, or 0 for current thread

Returns:

      win32typing.PyICancelMethodCalls
        
    """
    pass
        

def CoSetCancelObject(Unk:'win32typing.PyIUnknown') -> 'None':
    """
    None

Args:

      Unk(win32typing.PyIUnknown):An interface that support ICancelMethodCalls, can be None to unregister current cancel objectCommentsRequires Win2k or later

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
        