__all__=['', 'AssocCreate', 'AssocCreateForClasses', 'DragQueryFile', 'DragQueryFileW', 'DragQueryPoint', 'IsUserAnAdmin', 'SHCreateDataObject', 'SHCreateDefaultContextMenu', 'SHCreateDefaultExtractIcon', 'SHCreateShellFolderView', 'SHCreateShellItemArray', 'SHCreateShellItemArrayFromDataObject', 'SHCreateShellItemArrayFromIDLists', 'SHCreateShellItemArrayFromShellItem', 'SHGetPathFromIDList', 'SHGetPathFromIDListW', 'SHBrowseForFolder', 'SHGetFileInfo', 'SHGetFolderPath', 'SHSetFolderPath', 'SHGetFolderLocation', 'SHGetNameFromIDList', 'SHGetSpecialFolderPath', 'SHGetSpecialFolderLocation', 'SHAddToRecentDocs', 'SHChangeNotify', 'SHEmptyRecycleBin', 'SHQueryRecycleBin', 'SHGetDesktopFolder', 'SHUpdateImage', 'SHChangeNotify', 'SHChangeNotifyRegister', 'SHChangeNotifyDeregister', 'SHCreateItemFromIDList', 'SHCreateItemFromParsingName', 'SHCreateItemFromRelativeName', 'SHCreateItemInKnownFolder', 'SHCreateItemWithParent', 'SHGetIDListFromObject', 'SHGetInstanceExplorer', 'SHFileOperation', 'StringAsCIDA', 'CIDAAsString', 'StringAsPIDL', 'AddressAsPIDL', 'PIDLAsString', 'SHGetSettings', 'FILEGROUPDESCRIPTORAsString', 'StringAsFILEGROUPDESCRIPTOR', 'ShellExecuteEx', 'SHGetViewStatePropertyBag', 'SHILCreateFromPath', 'SHCreateShellItem', 'SHOpenFolderAndSelectItems', 'SHCreateStreamOnFileEx', 'SetCurrentProcessExplicitAppUserModelID', 'GetCurrentProcessExplicitAppUserModelID', 'SHParseDisplayName']
from typing import *
from win32helper.win32typing import *
"""A module wrapping Windows Shell functions and interfaces"""


def AssocCreate() -> 'PyIQueryAssociations':
    """
    None

Args:



Returns:

      PyIQueryAssociations
        
    """
    pass
        

def AssocCreateForClasses() -> 'PyIUnknown':
    """
    Retrieves an object that implements an IQueryAssociations 

interface.

Args:



Returns:

      PyIUnknown
        
    """
    pass
        

def DragQueryFile(hglobal:'int',index:'int') -> 'Union[str, int]':
    """
    Retrieves the names (or count) of dropped files

Args:

      hglobal(int):The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.
      index(int):The index to retrieve.  If -1, the result if an integer representing the valid index values.

Returns:

      Union[str, int]
        
    """
    pass
        

def DragQueryFileW(hglobal:'int',index:'int') -> 'Union[str, int]':
    """
    Retrieves the names (or count) of dropped files

Args:

      hglobal(int):The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.
      index(int):The index to retrieve.  If -1, the result if an integer representing the valid index values.

Returns:

      Union[str, int]
        
    """
    pass
        

def DragQueryPoint(hglobal:'int') -> 'Tuple[int, int, int]':
    """
    Retrieves the position of the mouse pointer at the time a file was 

dropped during a drag-and-drop operation.

Args:

      hglobal(int):The HGLOBAL object - generally obtained the 'data_handle' property of a PySTGMEDIUMCommentsThe window for which coordinates are returned is the window that received the WM_DROPFILES messageReturn ValueThe first item of the return tuple is True if the drop occurred in the client area of the window, or False if the drop did not occur in the client area of the window.

Returns:

      Tuple[int, int, int]:The HGLOBAL object - generally obtained the 

'data_handle' property of a PySTGMEDIUMComments

The window for which coordinates are returned is the window that received the WM_DROPFILES message
Return ValueThe first item of the return tuple is True if the drop occurred in the client area of the window, or False if 

the drop did not occur in the client area of the window.

        
    """
    pass
        

def IsUserAnAdmin() -> 'bool':
    """
    Tests whether the current user is a member of the Administrator's group.

Args:



Returns:

      bool:shell.IsUserAnAdmin

bool = IsUserAnAdmin()Tests whether the current user is a member of the Administrator's group.
Comments

This method is only available with version 5 or later of the shell controls
Return ValueThe result is true or false, or a com_error with E_NOTIMPL is raised.

        
    """
    pass
        

def SHCreateDataObject(parent:'Any',children:'List[Any]',do_inner:'PyIDataObject',iid:'PyIID') -> 'PyIUnknown':
    """
    None

Args:

      parent(Any):
      children(List[Any]):
      do_inner(PyIDataObject):The inner data object, or None bNoneOK */))
      iid(PyIID):The IID to query forCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIUnknown
        
    """
    pass
        

def SHCreateDefaultContextMenu(dcm:'Any',iid:'PyIID') -> 'PyIUnknown':
    """
    None

Args:

      dcm(Any):
      iid(PyIID):The IID to query forCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIUnknown
        
    """
    pass
        

def SHCreateDefaultExtractIcon() -> 'PyIDefaultExtractIconInit':
    """
    Creates a standard icon extractor, whose 

defaults can be further configured via the IDefaultExtractIconInit interface.

Args:



Returns:

      PyIDefaultExtractIconInit
        
    """
    pass
        

def SHCreateShellFolderView(sf:'PyIShellFolder',viewOuter:'PyIShellView'=None,callbacks:'Any'=None) -> 'PyIShellView':
    """
    Creates a new instance of the default Shell folder view 

object.

Args:

      sf(PyIShellFolder):
      viewOuter(PyIShellView):
      callbacks(Any):

Returns:

      PyIShellView
        
    """
    pass
        

def SHCreateShellItemArray(parent:'PyIDL',sf:'PyIShellFolder',children:'List[PyIDL]') -> 'PyIShellItemArray':
    """
    Creates a Shell item array object.

Args:

      parent(PyIDL):Absolute ID list of parent folder, or None if sf is specified
      sf(PyIShellFolder):The Shell data source object that is the parent of the child items specified in children. If parent is specified, this parameter can be NULL. bNoneOK */))
      children(List[PyIDL]):Sequence of relative IDLs for items in the parent folderCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromDataObject(do:'PyIDataObject',iid:'PyIID') -> 'PyIShellItemArray':
    """
    Creates a shell item array from an 

IDataObject 

interface that contains a list of items (eg CF_HDROP)

Args:

      do(PyIDataObject):A data object that can be rendered as a list of items
      iid(PyIID):The interface to createCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromIDLists(pidls:'List[PyIDL]') -> 'PyIShellItemArray':
    """
    Creates a shell item array from a number of 

item identifiers

Args:

      pidls(List[PyIDL]):A sequence of absolute IDLs.CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromShellItem(si:'PyIShellItem',riid:'PyIID') -> 'PyIShellItemArray':
    """
    Creates an item array containing a single 

item

Args:

      si(PyIShellItem):A shell item bNoneOK */))
      riid(PyIID):The interface to returnCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItemArray
        
    """
    pass
        

def SHGetPathFromIDList(idl:'PyIDL') -> 'str':
    """
    Converts an IDLIST to a path.

Args:

      idl(PyIDL):The ITEMIDLIST

Returns:

      str
        
    """
    pass
        

def SHGetPathFromIDListW(idl:'PyIDL') -> 'str':
    """
    Converts an IDLIST to a path.

Args:

      idl(PyIDL):The ITEMIDLIST

Returns:

      str
        
    """
    pass
        

def SHBrowseForFolder(hwndOwner:'int'=None,pidlRoot:'PyIDL'=None,title:'Union[str, Any]'=None,flags:'int'=0,callback:'Any'=None,callback_data:'Any'=None) -> 'Tuple[PyIDL, Any, Any]':
    """
    Displays a dialog box that enables the user 

to select a shell folder.

Args:

      hwndOwner(int):Parent window for the dialog box, can be None
      pidlRoot(PyIDL):PIDL identifying the place to start browsing. Desktop is used if not specified
      title(Union[str, Any]):Title to be displayed with the directory tree
      flags(int):Combination of shellcon.BIF_* flags
      callback(Any):A callable object to be used as the callback, or None
      callback_data(Any):An object passed to the callback functionCommentsIf you provide a callback function, it should take 4 args: hwnd, msg, lp, data.  Data will be whatever you passed as callback_data, and the rest are integers.  See the Microsoft documentation for SHBrowseForFolder, or the browse_for_folder.py shell sample for more information.Return ValueThe result is ALWAYS a tuple of 3 items.  If the user cancels the dialog, all items are None.  If the dialog is closed normally, the result is a tuple of (PIDL, DisplayName, iImageList)

Returns:

      Tuple[PyIDL, Any, Any]:An object passed to the callback function
Comments

If you provide a callback function, it should take 4 args: 

hwnd, msg, lp, data.  Data will be whatever you passed as callback_data, 

and the rest are integers.  See the Microsoft documentation for 

SHBrowseForFolder, or the browse_for_folder.py shell sample for more 

information.
Return ValueThe result is ALWAYS a tuple of 3 items.  If the user cancels the 

dialog, all items are None.  If the dialog is closed normally, the result is 

a tuple of (PIDL, DisplayName, iImageList)

        
    """
    pass
        

def SHGetFileInfo(name:'Union[str, PyIDL]',dwFileAttributes:'int',uFlags:'int',infoAttrs:'int'=0) -> 'Tuple[int, SHFILEINFO]':
    """
    Retrieves information about an object in the file system, such as a 

file, a folder, a directory, or a drive root.

Args:

      name(Union[str, PyIDL]):The path and file name. Both absolute and relative paths are valid. If the uFlags parameter includes the SHGFI_PIDL flag, this parameter must be a valid PyIDL object that uniquely identifies the file within the shell's namespace. The PIDL must be a fully qualified PIDL. Relative PIDLs are not allowed. If the uFlags parameter includes the SHGFI_USEFILEATTRIBUTES flag, this parameter does not have to be a valid file name. The function will proceed as if the file exists with the specified name and with the file attributes passed in the dwFileAttributes parameter. This allows you to obtain information about a file type by passing just the extension for pszPath and passing FILE_ATTRIBUTE_NORMAL in dwFileAttributes. This string can use either short (the 8.3 form) or long file names.
      dwFileAttributes(int):Combination of one or more file attribute flags (FILE_ATTRIBUTE_ values). If uFlags does not include the SHGFI_USEFILEATTRIBUTES flag, this parameter is ignored.
      uFlags(int):Combination of shellcon.SHGFI_* flags that specify the file information to retrieve.  See MSDN for details
      infoAttrs(int):Flags copied to the SHFILEINFO.dwAttributes member - useful when flags contains SHGFI_ATTR_SPECIFIED

Returns:

      Tuple[int, SHFILEINFO]
        
    """
    pass
        

def SHGetFolderPath(hwndOwner:'int',nFolder:'int',handle:'int',flags:'int') -> 'Union[str]':
    """
    Retrieves the path of a folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(int):One of the CSIDL_* constants specifying the path.
      handle(int):An access token that can be used to represent a particular user, or None
      flags(int):Controls which path is returned.  May be SHGFP_TYPE_CURRENT or SHGFP_TYPE_DEFAULTCommentsThis method is only available with later versions of shell32.dll, or if you have shfolder.dll installed on earlier systems

Returns:

      Union[str]
        
    """
    pass
        

def SHSetFolderPath(csidl:'int',Path:'Union[str, Any]',hToken:'int'=None) -> 'None':
    """
    Sets the location of one of the special folders

Args:

      csidl(int):One of the shellcon.CSIDL_* values
      Path(Union[str, Any]):The full path to be set
      hToken(int):Handle to an access token, can be NoneCommentsThis function is only available on Windows 2000 or later

Returns:

      None
        
    """
    pass
        

def SHGetFolderLocation(hwndOwner:'int',nFolder:'int',hToken:'int'=None,reserved:'int'=0) -> 'PyIDL':
    """
    Retrieves the PIDL of a folder.

Args:

      hwndOwner(int):Window in which to display any neccessary dialogs
      nFolder(int):One of the CSIDL_* constants specifying the path.
      hToken(int):An access token that can be used to represent a particular user, or None
      reserved(int):Must be 0CommentsThis method is only available with version 5 or later of the shell controls

Returns:

      PyIDL
        
    """
    pass
        

def SHGetNameFromIDList(pidl:'PyIDL',flags:'int') -> 'str':
    """
    Retrieves the display name of an item from an ID list.

Args:

      pidl(PyIDL):Absolute ID list of the item
      flags(int):Type of name to return, shellcon.SIGDN_*CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      str
        
    """
    pass
        

def SHGetSpecialFolderPath(hwndOwner:'int',nFolder:'int',bCreate:'int'=0) -> 'str':
    """
    Retrieves the path of a special folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(int):One of the CSIDL_* constants specifying the path.
      bCreate(int):Should the path be created.CommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.  If the function fails, a COM Exception with HRESULT=E_FAIL will be raised.

Returns:

      str
        
    """
    pass
        

def SHGetSpecialFolderLocation(hwndOwner:'int',nFolder:'int') -> 'PyIDL':
    """
    Retrieves the PIDL of a special folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(int):One of the CSIDL_* constants specifying the path.

Returns:

      PyIDL
        
    """
    pass
        

def SHAddToRecentDocs(Flags:'int',data:'Any') -> 'None':
    """
    Adds a document to the shell's list of recently used documents or clears all 

documents from the list. The user gains access to the list through the Start menu of the Windows taskbar.

Args:

      Flags(int):Value from SHARD enum indicating how the item is identified.
      data(Any):Type of input is determined by the SHARD_* flag.  Use None to clear recent items list.FlagsType of inputSHARD_PATHAString containing a file pathSHARD_PATHWString containing a file pathSHARD_PIDLPyIDL, or a buffer containing a PIDL (see shell::PIDLAsString)SHARD_APPIDINFOTuple of (PyIShellItem, str), where str is an AppIDSHARD_APPIDINFOIDLISTTuple of (PyIDL, str), where str is an AppIDSHARD_LINKPyIShellLinkSHARD_APPIDINFOLINKTuple of (PyIShellLink, str) where str is an AppIDSHARD_SHELLITEMPyIShellItemCommentsOn Windows 7, the entry is also added to the application's jump list.The underlying API function has no return value, and therefore no way to indicate failure.Win32 API References

Returns:

      None
        
    """
    pass
        

def SHChangeNotify(EventId:'int',Flags:'int',Item1:'Any',Item2:'Any') -> 'None':
    """
    Notifies the system of an event that an application has performed. An application 

should use this function if it performs an action that may affect the shell.

Args:

      EventId(int):Combination of shellcon.SHCNE_* constants
      Flags(int):Combination of shellcon.SHCNF_* constants that specify type of last 2 parameters Only one of the type flags may be specified, combined with one of the SHCNF_FLUSH* flags
      Item1(Any):Type is dependent on the event to be signalled
      Item2(Any):Type is dependent on the event to be signalled

Returns:

      None
        
    """
    pass
        

def SHEmptyRecycleBin(hwnd:'int',path:'str',flags:'int') -> 'None':
    """
    Empties the recycle bin on the specified drive.

Args:

      hwnd(int):Handle to parent window, can be None
      path(str):A NULL-terminated string that contains the path of the root drive on which the recycle bin is located. This parameter can contain the address of a string formatted with the drive, folder, and subfolder names (c:\\windows\\system . . .). It can also contain an empty string or NULL. If this value is an empty string or NULL, all recycle bins on all drives will be emptied.
      flags(int):One of the SHERB_* values.CommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.

Returns:

      None
        
    """
    pass
        

def SHQueryRecycleBin(RootPath:'str'=None) -> 'Tuple[Any, Any]':
    """
    Retrieves the total size and number of items in the Recycle Bin for a 

specified drive

Args:

      RootPath(str):A path containing the drive whose recycle bin will be queried, or None for all drives

Returns:

      Tuple[Any, Any]
        
    """
    pass
        

def SHGetDesktopFolder() -> 'PyIShellFolder':
    """
    None

Args:



Returns:

      PyIShellFolder
        
    """
    pass
        

def SHUpdateImage(HashItem:'str',Index:'int',Flags:'int',ImageIndex:'int') -> 'None':
    """
    Notifies the shell that an image in the system image list has changed.

Args:

      HashItem(str):Full path of file containing the icon as returned by PyIExtractIcon::GetIconLocation
      Index(int):Index of the icon in the above file
      Flags(int):GIL_NOTFILENAME or GIL_SIMULATEDOC
      ImageIndex(int):Index of the icon in the system image list

Returns:

      None
        
    """
    pass
        

def SHChangeNotify(EventId:'int',Flags:'int',Item1:'Any',Item2:'Any') -> 'None':
    """
    Notifies the system of an event that an application has performed. An application 

should use this function if it performs an action that may affect the shell.

Args:

      EventId(int):Combination of shellcon.SHCNE_* constants
      Flags(int):Combination of shellcon.SHCNF_* constants that specify type of last 2 parameters Only one of the type flags may be specified, combined with one of the SHCNF_FLUSH* flags
      Item1(Any):Type is dependent on the event to be signalled
      Item2(Any):Type is dependent on the event to be signalled

Returns:

      None
        
    """
    pass
        

def SHChangeNotifyRegister(hwnd:'int',sources:'int',events:'int',msg:'int') -> 'int':
    """
    Registers a window that receives notifications from the file system or 

shell.

Args:

      hwnd(int):Handle to the window that receives the change or notification messages.
      sources(int):One or more values that indicate the type of events for which to receive notifications.
      events(int):Change notification events for which to receive notification.
      msg(int):Message to be posted to the window procedure.

Returns:

      int
        
    """
    pass
        

def SHChangeNotifyDeregister(_id:'int') -> 'None':
    """
    Unregisters the client's window process from receiving notification events

Args:

      _id(int):The registration identifier (ID) returned by shell::SHChangeNotifyRegister.

Returns:

      None
        
    """
    pass
        

def SHCreateItemFromIDList(pidl:'PyIDL',riid:'PyIID') -> 'PyIShellItem':
    """
    None

Args:

      pidl(PyIDL):An absolute item identifier list
      riid(PyIID):The interface to createCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHCreateItemFromParsingName(name:'str',ctx:'PyIBindCtx',riid:'PyIID') -> 'PyIShellItem':
    """
    Creates and initializes a Shell item object from a 

parsing name.

Args:

      name(str):The display name of the item to create, eg a file path
      ctx(PyIBindCtx):Bind context, can be None
      riid(PyIID):The interface to create, IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHCreateItemFromRelativeName(Parent:'PyIShellItem',Name:'str',ctx:'PyIBindCtx',riid:'PyIID') -> 'PyIShellItem':
    """
    Creates and initializes a Shell item object from a 

relative parsing name.

Args:

      Parent(PyIShellItem):Shell item interface on the parent folder
      Name(str):Relative name of an item within the parent folder
      ctx(PyIBindCtx):Bind context for parsing, can be None
      riid(PyIID):The interface to return, IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHCreateItemInKnownFolder(FolderId:'PyIID',Flags:'int',Name:'str',riid:'PyIID') -> 'PyIShellItem':
    """
    Creates a Shell item object for a single file that exists 

inside a known folder.

Args:

      FolderId(PyIID):The GUID of a known folder (shell.FOLDERID_*)
      Flags(int):Combination of shellcon.KF_FLAG_* flags controlling how folder is handled
      Name(str):Name of an item in the folder.  Pass None to bind to the known folder itself.
      riid(PyIID):The interface to return, usually IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHCreateItemWithParent(Parent:'PyIDL',sfParent:'PyIShellFolder',child:'PyIDL',riid:'PyIID') -> 'PyIShellItem':
    """
    Create a Shell item, given a parent folder and a child item 

ID.

Args:

      Parent(PyIDL):Absolute item id list of the parent folder.  Pass None if the below shell folder is used.
      sfParent(PyIShellFolder):Parent folder object.  Can be None if parent id list is specified.
      child(PyIDL):Relative item id list for an object in the parent folder
      riid(PyIID):The interface to return, usually IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHGetIDListFromObject(unk:'PyIUnknown') -> 'PyIDL':
    """
    Retrieves the PIDL of an object.

Args:

      unk(PyIUnknown):CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIDL
        
    """
    pass
        

def SHGetInstanceExplorer() -> 'PyIUnknown':
    """
    Allows components that run in a Web browser (Iexplore.exe) or a 

nondefault Windows Explorer (Explorer.exe) process to hold a reference to the process. The components can use the 

reference to prevent the process from closing prematurely.

Args:



Returns:

      PyIUnknown
        
    """
    pass
        

def SHFileOperation(operation:'SHFILEOPSTRUCT') -> 'Tuple[int, int]':
    """
    Copies, moves, renames, or deletes a file system object.

Args:

      operation(SHFILEOPSTRUCT):Defines the operation to perform.Return ValueThe result is a tuple containing int result of the function itself, and the result of the fAnyOperationsAborted member after the operation.  If Flags contains FOF_WANTMAPPINGHANDLE, returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names of renamed files.  This will only have any content if FOF_RENAMEONCOLLISION was specified, and some filename conflicts actually occurred.

Returns:

      Tuple[int, int]:Defines the operation to perform.Return ValueThe result is a tuple containing int result of the function itself, and the result of the 

fAnyOperationsAborted member after the operation.  If Flags contains FOF_WANTMAPPINGHANDLE, 

returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names 

of renamed files.  This will only have any content if FOF_RENAMEONCOLLISION was specified, and some 

filename conflicts actually occurred.

        
    """
    pass
        

def StringAsCIDA(pidl:'str') -> 'Tuple[PyIDL, list]':
    """
    Given a CIDA as a raw string, return the folder PIDL and list of 

children

Args:

      pidl(str):The PIDL as a raw string.Return ValueThe result is the PIDL of the folder, and a list of child PIDLs.

Returns:

      Tuple[PyIDL, list]:The PIDL as a raw string.Return ValueThe result is the PIDL of the folder, and a list of child PIDLs.

        
    """
    pass
        

def CIDAAsString(pidl:'str') -> 'str':
    """
    Given a (pidl, child_pidls) object, return a CIDA as a string

Args:

      pidl(str):The PIDL as a raw string.Return ValueThe result is a string with the CIDA bytes.

Returns:

      str:The PIDL as a raw string.Return ValueThe result is a string with the CIDA bytes.

        
    """
    pass
        

def StringAsPIDL(pidl:'str') -> 'PyIDL':
    """
    Given a PIDL as a raw string, return a PIDL object (ie, a list of strings)

Args:

      pidl(str):The PIDL as a raw string.

Returns:

      PyIDL
        
    """
    pass
        

def AddressAsPIDL(address:'int') -> 'PyIDL':
    """
    Given the address of a PIDL in memory, return a PIDL object (ie, a list of 

strings)

Args:

      address(int):The address of the PIDL

Returns:

      PyIDL
        
    """
    pass
        

def PIDLAsString(pidl:'PyIDL') -> 'str':
    """
    Given a PIDL object, return the raw PIDL bytes as a string

Args:

      pidl(PyIDL):The PIDL object (ie, a list of strings)

Returns:

      str
        
    """
    pass
        

def SHGetSettings(mask:'int'=-1) -> 'dict':
    """
    Retrieves the current shell option settings.

Args:

      mask(int):The values being requested - one of the shellcon.SSF_* constantsCommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.Return ValueThe result is a dictionary, the contents of which depend on the mask param.  Key names are the same as the SHELLFLAGSTATE structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc

Returns:

      dict:The values being requested - one of the shellcon.SSF_* constants
Comments

This method is only available in shell version 4.71.  If the 

function is not available, a COM Exception with HRESULT=E_NOTIMPL 

will be raised.
Return ValueThe result is a dictionary, the contents of which depend on 

the mask param.  Key names are the same as the SHELLFLAGSTATE 

structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc

        
    """
    pass
        

def FILEGROUPDESCRIPTORAsString(descriptors:'List[Any]',arg:'bool') -> 'str':
    """
    Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, 

each with FILEDESCRIPTOR attributes

Args:

      descriptors(List[Any]):A sequence of FILEDESCRIPTOR objects. Each filedescriptor object must be a mapping/dictionary, with the following optional attributes: dwFlags, clsid, sizel, pointl, dwFileAttributes, ftCreationTime, ftLastAccessTime, ftLastWriteTime, nFileSize If these attributes do not exist, or are None, they will be ignored - hence you only need specify attributes you care about. In general, you can omit dwFlags - it will be set correctly based on what other attributes exist.
      arg(bool):If true, a FILEDESCRIPTORW object is created

Returns:

      str
        
    """
    pass
        

def StringAsFILEGROUPDESCRIPTOR(buf:'Any',make_unicode:'bool'=-1) -> 'List[dict]':
    """
    Decodes a FILEGROUPDESCRIPTOR packed in a string

Args:

      buf(Any):A string packed as either FILEGROUPDESCRIPTORW or FILEGROUPDESCRIPTORW
      make_unicode(bool):Should this be treated as a FILEDESCRIPTORW?  If -1 the size of the buffer will be used to make that determination.  Thus, if the buffer is not the exact size of a correct FILEDESCRIPTORW or FILEDESCRIPTORA, you will need to specify this parameter.

Returns:

      List[dict]
        
    """
    pass
        

def ShellExecuteEx(lpVerb:'str',lpFile:'str',lpParameters:'str',lpDirectory:'str',lpIDList:'PyIDL',obClass:'str',hkeyClass:'int',dwHotKey:'int',hIcon:'int',hMonitor:'int',fMask:'int'=0,hwnd:'int'=0,nShow:'int'=0) -> 'dict':
    """
    Performs an operation on a file.

Args:

      lpVerb(str):
      lpFile(str):
      lpParameters(str):
      lpDirectory(str):
      lpIDList(PyIDL):
      obClass(str):
      hkeyClass(int):
      dwHotKey(int):
      hIcon(int):
      hMonitor(int):Return ValueThe result is a dictionary based on documented result values in the structure.  Currently this is "hInstApp" and "hProcess"
      fMask(int):The default mask for the structure.  Other masks may be added based on what paramaters are supplied.
      hwnd(int):
      nShow(int):

Returns:

      dict:Return ValueThe result is a dictionary based on documented result values 

in the structure.  Currently this is "hInstApp" and "hProcess"

        
    """
    pass
        

def SHGetViewStatePropertyBag(pidl:'PyIDL',BagName:'str',Flags:'int',riid:'PyIID') -> 'PyIPropertyBag':
    """
    Retrieves an interface for the view state of a folder

Args:

      pidl(PyIDL):An item id list that identifies the folder
      BagName(str):Name of the property bag to retrieve
      Flags(int):Combination of SHGVSPB_* flags
      riid(PyIID):The interface to return, usually IID_IPropertyBagCommentsThis function will also return IPropertyBag2, but we don't have a python implementation of this interface yet

Returns:

      PyIPropertyBag
        
    """
    pass
        

def SHILCreateFromPath(Path:'str',Flags:'int') -> 'Tuple[PyIDL, int]':
    """
    Retrieves the PIDL and attributes for a path

Args:

      Path(str):The path whose PIDL will be returned
      Flags(int):A combination of SFGAO_* constants as used with GetAttributesOfReturn ValueReturns the PIDL for the given path and any requested attributes

Returns:

      Tuple[PyIDL, int]:A combination of SFGAO_* constants as used with GetAttributesOfReturn ValueReturns the PIDL for the given path and any requested attributes

        
    """
    pass
        

def SHCreateShellItem(pidlParent:'PyIDL',sfParent:'PyIShellFolder',Child:'PyIDL') -> 'PyIShellItem':
    """
    Creates an IShellItem interface from a PIDL

Args:

      pidlParent(PyIDL):PIDL of parent folder, can be None
      sfParent(PyIShellFolder):IShellFolder interface of parent folder, can be None
      Child(PyIDL):PIDL identifying desired item.  Must be an absolute PIDL if parent is not specified.CommentsThis function is only available on XP and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIShellItem
        
    """
    pass
        

def SHOpenFolderAndSelectItems(Folder:'PyIDL',Items:'Tuple[PyIDL, ...]',Flags:'int'=0) -> 'None':
    """
    Displays a shell folder with items pre-selected

Args:

      Folder(PyIDL):An absolute item id list identifying a shell folder
      Items(Tuple[PyIDL, ...]):A sequence of relative item ids identifying items in the folder
      Flags(int):Combination of OFASI_* flags (not used on XP)CommentsThis function is only available on XP and later. COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      None
        
    """
    pass
        

def SHCreateStreamOnFileEx(File:'str',Mode:'int',Attributes:'int',Create:'bool',Template:'None'=None) -> 'PyIStream':
    """
    Creates an IStream interface that reads and writes to a file

Args:

      File(str):Name of file to be connected to the stream
      Mode(int):Combination of storagecon.STGM_* flags specifying the access mode
      Attributes(int):Combination of win32con.FILE_ATTRIBUTE_* flags
      Create(bool):Determines if function should fail when file exists (see MSDN docs for full explanation)
      Template(None):Reserved, use only NoneCommentsAccepts keyword args.This function is only available on WinXP and later. COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      PyIStream
        
    """
    pass
        

def SetCurrentProcessExplicitAppUserModelID(AppID:'str') -> 'None':
    """
    Sets the taskbar identifier

Args:

      AppID(str):The Application User Model ID used to group taskbar buttonsCommentsShould be used early in process startup before creating any windowsRequires Windows 7 or later

Returns:

      None
        
    """
    pass
        

def GetCurrentProcessExplicitAppUserModelID() -> 'str':
    """
    Retrieves the current taskbar identifier

Args:



Returns:

      str
        
    """
    pass
        

def SHParseDisplayName(Name:'str',Attributes:'int',BindCtx:'PyIBindCtx'=None) -> 'Tuple[PyIDL, int]':
    """
    Translates a display name into a shell item identifier

Args:

      Name(str):Display name of a shell item, such as a file path
      Attributes(int):Bitmask of shell attributes to retrieve, combination of shellcon.SFGAO_*
      BindCtx(PyIBindCtx):Bind context, can be NoneCommentsAccepts keyword argsRequires XP or laterReturn ValueReturns the item id list and any requested attribute flags

Returns:

      Tuple[PyIDL, int]:Bind context, can be None
Comments

Accepts keyword args

Requires XP or later
Return ValueReturns the item id list and any requested attribute flags

        
    """
    pass
        