__all__=['', 'AssocCreate', 'AssocCreateForClasses', 'DragQueryFile', 'DragQueryFileW', 'DragQueryPoint', 'IsUserAnAdmin', 'SHCreateDataObject', 'SHCreateDefaultContextMenu', 'SHCreateDefaultExtractIcon', 'SHCreateShellFolderView', 'SHCreateShellItemArray', 'SHCreateShellItemArrayFromDataObject', 'SHCreateShellItemArrayFromIDLists', 'SHCreateShellItemArrayFromShellItem', 'SHGetPathFromIDList', 'SHGetPathFromIDListW', 'SHBrowseForFolder', 'SHGetFileInfo', 'SHGetFolderPath', 'SHSetFolderPath', 'SHGetFolderLocation', 'SHGetNameFromIDList', 'SHGetSpecialFolderPath', 'SHGetSpecialFolderLocation', 'SHAddToRecentDocs', 'SHChangeNotify', 'SHEmptyRecycleBin', 'SHQueryRecycleBin', 'SHGetDesktopFolder', 'SHUpdateImage', 'SHChangeNotify', 'SHChangeNotifyRegister', 'SHChangeNotifyDeregister', 'SHCreateItemFromIDList', 'SHCreateItemFromParsingName', 'SHCreateItemFromRelativeName', 'SHCreateItemInKnownFolder', 'SHCreateItemWithParent', 'SHGetIDListFromObject', 'SHGetInstanceExplorer', 'SHFileOperation', 'StringAsCIDA', 'CIDAAsString', 'StringAsPIDL', 'AddressAsPIDL', 'PIDLAsString', 'SHGetSettings', 'FILEGROUPDESCRIPTORAsString', 'StringAsFILEGROUPDESCRIPTOR', 'ShellExecuteEx', 'SHGetViewStatePropertyBag', 'SHILCreateFromPath', 'SHCreateShellItem', 'SHOpenFolderAndSelectItems', 'SHCreateStreamOnFileEx', 'SetCurrentProcessExplicitAppUserModelID', 'GetCurrentProcessExplicitAppUserModelID', 'SHParseDisplayName']
import typing
from win32helper import win32typing
"""A module wrapping Windows Shell functions and interfaces"""


def AssocCreate() -> 'win32typing.PyIQueryAssociations':
    """
    None

Args:



Returns:

      win32typing.PyIQueryAssociations
        
    """
    pass
        

def AssocCreateForClasses() -> 'win32typing.PyIUnknown':
    """
    Retrieves an object that implements an IQueryAssociations 

interface.

Args:



Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def DragQueryFile(hglobal:'int',index:'typing.Any') -> 'typing.Union[typing.Any, str]':
    """
    Retrieves the names (or count) of dropped files

Args:

      hglobal(int):The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.
      index(typing.Any):The index to retrieve.  If -1, the result if an integer representing the valid index values.

Returns:

      typing.Union[typing.Any, str]
        
    """
    pass
        

def DragQueryFileW(hglobal:'int',index:'typing.Any') -> 'typing.Union[typing.Any, str]':
    """
    Retrieves the names (or count) of dropped files

Args:

      hglobal(int):The HGLOBAL object - generally obtained via the 'data_handle' property of a PySTGMEDIUM object.
      index(typing.Any):The index to retrieve.  If -1, the result if an integer representing the valid index values.

Returns:

      typing.Union[typing.Any, str]
        
    """
    pass
        

def DragQueryPoint(hglobal:'int') -> 'typing.Tuple[typing.Any, typing.Any, typing.Any]':
    """
    Retrieves the position of the mouse pointer at the time a file was 

dropped during a drag-and-drop operation.

Args:

      hglobal(int):The HGLOBAL object - generally obtained the 'data_handle' property of a PySTGMEDIUMCommentsThe window for which coordinates are returned is the window that received the WM_DROPFILES messageReturn ValueThe first item of the return tuple is True if the drop occurred in the client area of the window, or False if the drop did not occur in the client area of the window.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any]:The HGLOBAL object - generally obtained the 

'data_handle' property of a PySTGMEDIUMComments

The window for which coordinates are returned is the window that received the WM_DROPFILES message
Return ValueThe first item of the return tuple is True if the drop occurred in the client area of the window, or False if 

the drop did not occur in the client area of the window.

        
    """
    pass
        

def IsUserAnAdmin() -> 'typing.Any':
    """
    Tests whether the current user is a member of the Administrator's group.

Args:



Returns:

      typing.Any:shell.IsUserAnAdmin

bool = IsUserAnAdmin()Tests whether the current user is a member of the Administrator's group.
Comments

This method is only available with version 5 or later of the shell controls
Return ValueThe result is true or false, or a com_error with E_NOTIMPL is raised.

        
    """
    pass
        

def SHCreateDataObject(parent:'typing.Any',children:'typing.List[typing.Any]',do_inner:'win32typing.PyIDataObject',iid:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    None

Args:

      parent(typing.Any):
      children(typing.List[typing.Any]):
      do_inner(win32typing.PyIDataObject):The inner data object, or None bNoneOK */))
      iid(win32typing.PyIID):The IID to query forCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def SHCreateDefaultContextMenu(dcm:'typing.Any',iid:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    None

Args:

      dcm(typing.Any):
      iid(win32typing.PyIID):The IID to query forCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def SHCreateDefaultExtractIcon() -> 'win32typing.PyIDefaultExtractIconInit':
    """
    Creates a standard icon extractor, whose 

defaults can be further configured via the IDefaultExtractIconInit interface.

Args:



Returns:

      win32typing.PyIDefaultExtractIconInit
        
    """
    pass
        

def SHCreateShellFolderView(sf:'win32typing.PyIShellFolder',viewOuter:'win32typing.PyIShellView'=None,callbacks:'typing.Any'=None) -> 'win32typing.PyIShellView':
    """
    Creates a new instance of the default Shell folder view 

object.

Args:

      sf(win32typing.PyIShellFolder):
      viewOuter(win32typing.PyIShellView):
      callbacks(typing.Any):

Returns:

      win32typing.PyIShellView
        
    """
    pass
        

def SHCreateShellItemArray(parent:'win32typing.PyIDL',sf:'win32typing.PyIShellFolder',children:'typing.List[win32typing.PyIDL]') -> 'win32typing.PyIShellItemArray':
    """
    Creates a Shell item array object.

Args:

      parent(win32typing.PyIDL):Absolute ID list of parent folder, or None if sf is specified
      sf(win32typing.PyIShellFolder):The Shell data source object that is the parent of the child items specified in children. If parent is specified, this parameter can be NULL. bNoneOK */))
      children(typing.List[win32typing.PyIDL]):Sequence of relative IDLs for items in the parent folderCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromDataObject(do:'win32typing.PyIDataObject',iid:'win32typing.PyIID') -> 'win32typing.PyIShellItemArray':
    """
    Creates a shell item array from an 

IDataObject 

interface that contains a list of items (eg CF_HDROP)

Args:

      do(win32typing.PyIDataObject):A data object that can be rendered as a list of items
      iid(win32typing.PyIID):The interface to createCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromIDLists(pidls:'typing.List[win32typing.PyIDL]') -> 'win32typing.PyIShellItemArray':
    """
    Creates a shell item array from a number of 

item identifiers

Args:

      pidls(typing.List[win32typing.PyIDL]):A sequence of absolute IDLs.CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItemArray
        
    """
    pass
        

def SHCreateShellItemArrayFromShellItem(si:'win32typing.PyIShellItem',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItemArray':
    """
    Creates an item array containing a single 

item

Args:

      si(win32typing.PyIShellItem):A shell item bNoneOK */))
      riid(win32typing.PyIID):The interface to returnCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItemArray
        
    """
    pass
        

def SHGetPathFromIDList(idl:'win32typing.PyIDL') -> 'str':
    """
    Converts an IDLIST to a path.

Args:

      idl(win32typing.PyIDL):The ITEMIDLIST

Returns:

      str
        
    """
    pass
        

def SHGetPathFromIDListW(idl:'win32typing.PyIDL') -> 'str':
    """
    Converts an IDLIST to a path.

Args:

      idl(win32typing.PyIDL):The ITEMIDLIST

Returns:

      str
        
    """
    pass
        

def SHBrowseForFolder(hwndOwner:'int'=None,pidlRoot:'win32typing.PyIDL'=None,title:'typing.Union[typing.Any, str]'=None,flags:'typing.Any'=0,callback:'typing.Any'=None,callback_data:'typing.Any'=None) -> 'typing.Tuple[win32typing.PyIDL, typing.Any, typing.Any]':
    """
    Displays a dialog box that enables the user 

to select a shell folder.

Args:

      hwndOwner(int):Parent window for the dialog box, can be None
      pidlRoot(win32typing.PyIDL):PIDL identifying the place to start browsing. Desktop is used if not specified
      title(typing.Union[typing.Any, str]):Title to be displayed with the directory tree
      flags(typing.Any):Combination of shellcon.BIF_* flags
      callback(typing.Any):A callable object to be used as the callback, or None
      callback_data(typing.Any):An object passed to the callback functionCommentsIf you provide a callback function, it should take 4 args: hwnd, msg, lp, data.  Data will be whatever you passed as callback_data, and the rest are integers.  See the Microsoft documentation for SHBrowseForFolder, or the browse_for_folder.py shell sample for more information.Return ValueThe result is ALWAYS a tuple of 3 items.  If the user cancels the dialog, all items are None.  If the dialog is closed normally, the result is a tuple of (PIDL, DisplayName, iImageList)

Returns:

      typing.Tuple[win32typing.PyIDL, typing.Any, typing.Any]:An object passed to the callback function
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
        

def SHGetFileInfo(name:'typing.Union[win32typing.PyIDL, str]',dwFileAttributes:'typing.Any',uFlags:'typing.Any',infoAttrs:'typing.Any'=0) -> 'typing.Tuple[typing.Any, win32typing.SHFILEINFO]':
    """
    Retrieves information about an object in the file system, such as a 

file, a folder, a directory, or a drive root.

Args:

      name(typing.Union[win32typing.PyIDL, str]):The path and file name. Both absolute and relative paths are valid. If the uFlags parameter includes the SHGFI_PIDL flag, this parameter must be a valid PyIDL object that uniquely identifies the file within the shell's namespace. The PIDL must be a fully qualified PIDL. Relative PIDLs are not allowed. If the uFlags parameter includes the SHGFI_USEFILEATTRIBUTES flag, this parameter does not have to be a valid file name. The function will proceed as if the file exists with the specified name and with the file attributes passed in the dwFileAttributes parameter. This allows you to obtain information about a file type by passing just the extension for pszPath and passing FILE_ATTRIBUTE_NORMAL in dwFileAttributes. This string can use either short (the 8.3 form) or long file names.
      dwFileAttributes(typing.Any):Combination of one or more file attribute flags (FILE_ATTRIBUTE_ values). If uFlags does not include the SHGFI_USEFILEATTRIBUTES flag, this parameter is ignored.
      uFlags(typing.Any):Combination of shellcon.SHGFI_* flags that specify the file information to retrieve.  See MSDN for details
      infoAttrs(typing.Any):Flags copied to the SHFILEINFO.dwAttributes member - useful when flags contains SHGFI_ATTR_SPECIFIED

Returns:

      typing.Tuple[typing.Any, win32typing.SHFILEINFO]
        
    """
    pass
        

def SHGetFolderPath(hwndOwner:'int',nFolder:'typing.Any',handle:'int',flags:'typing.Any') -> 'typing.Union[str]':
    """
    Retrieves the path of a folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(typing.Any):One of the CSIDL_* constants specifying the path.
      handle(int):An access token that can be used to represent a particular user, or None
      flags(typing.Any):Controls which path is returned.  May be SHGFP_TYPE_CURRENT or SHGFP_TYPE_DEFAULTCommentsThis method is only available with later versions of shell32.dll, or if you have shfolder.dll installed on earlier systems

Returns:

      typing.Union[str]
        
    """
    pass
        

def SHSetFolderPath(csidl:'typing.Any',Path:'typing.Union[typing.Any]',hToken:'int'=None) -> 'None':
    """
    Sets the location of one of the special folders

Args:

      csidl(typing.Any):One of the shellcon.CSIDL_* values
      Path(typing.Union[typing.Any]):The full path to be set
      hToken(int):Handle to an access token, can be NoneCommentsThis function is only available on Windows 2000 or later

Returns:

      None
        
    """
    pass
        

def SHGetFolderLocation(hwndOwner:'typing.Any',nFolder:'typing.Any',hToken:'int'=None,reserved:'typing.Any'=0) -> 'win32typing.PyIDL':
    """
    Retrieves the PIDL of a folder.

Args:

      hwndOwner(typing.Any):Window in which to display any neccessary dialogs
      nFolder(typing.Any):One of the CSIDL_* constants specifying the path.
      hToken(int):An access token that can be used to represent a particular user, or None
      reserved(typing.Any):Must be 0CommentsThis method is only available with version 5 or later of the shell controls

Returns:

      win32typing.PyIDL
        
    """
    pass
        

def SHGetNameFromIDList(pidl:'win32typing.PyIDL',flags:'typing.Any') -> 'typing.Any':
    """
    Retrieves the display name of an item from an ID list.

Args:

      pidl(win32typing.PyIDL):Absolute ID list of the item
      flags(typing.Any):Type of name to return, shellcon.SIGDN_*CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      typing.Any
        
    """
    pass
        

def SHGetSpecialFolderPath(hwndOwner:'int',nFolder:'typing.Any',bCreate:'typing.Any'=0) -> 'str':
    """
    Retrieves the path of a special folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(typing.Any):One of the CSIDL_* constants specifying the path.
      bCreate(typing.Any):Should the path be created.CommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.  If the function fails, a COM Exception with HRESULT=E_FAIL will be raised.

Returns:

      str
        
    """
    pass
        

def SHGetSpecialFolderLocation(hwndOwner:'int',nFolder:'typing.Any') -> 'win32typing.PyIDL':
    """
    Retrieves the PIDL of a special folder.

Args:

      hwndOwner(int):Parent window, can be None (or 0)
      nFolder(typing.Any):One of the CSIDL_* constants specifying the path.

Returns:

      win32typing.PyIDL
        
    """
    pass
        

def SHAddToRecentDocs(Flags:'typing.Any',data:'typing.Any') -> 'None':
    """
    Adds a document to the shell's list of recently used documents or clears all 

documents from the list. The user gains access to the list through the Start menu of the Windows taskbar.

Args:

      Flags(typing.Any):Value from SHARD enum indicating how the item is identified.
      data(typing.Any):Type of input is determined by the SHARD_* flag.  Use None to clear recent items list.FlagsType of inputSHARD_PATHAString containing a file pathSHARD_PATHWString containing a file pathSHARD_PIDLPyIDL, or a buffer containing a PIDL (see shell::PIDLAsString)SHARD_APPIDINFOTuple of (PyIShellItem, str), where str is an AppIDSHARD_APPIDINFOIDLISTTuple of (PyIDL, str), where str is an AppIDSHARD_LINKPyIShellLinkSHARD_APPIDINFOLINKTuple of (PyIShellLink, str) where str is an AppIDSHARD_SHELLITEMPyIShellItemCommentsOn Windows 7, the entry is also added to the application's jump list.The underlying API function has no return value, and therefore no way to indicate failure.Win32 API References

Returns:

      None
        
    """
    pass
        

def SHChangeNotify(EventId:'typing.Any',Flags:'typing.Any',Item1:'typing.Any',Item2:'typing.Any') -> 'None':
    """
    Notifies the system of an event that an application has performed. An application 

should use this function if it performs an action that may affect the shell.

Args:

      EventId(typing.Any):Combination of shellcon.SHCNE_* constants
      Flags(typing.Any):Combination of shellcon.SHCNF_* constants that specify type of last 2 parameters Only one of the type flags may be specified, combined with one of the SHCNF_FLUSH* flags
      Item1(typing.Any):Type is dependent on the event to be signalled
      Item2(typing.Any):Type is dependent on the event to be signalled

Returns:

      None
        
    """
    pass
        

def SHEmptyRecycleBin(hwnd:'int',path:'str',flags:'typing.Any') -> 'None':
    """
    Empties the recycle bin on the specified drive.

Args:

      hwnd(int):Handle to parent window, can be None
      path(str):A NULL-terminated string that contains the path of the root drive on which the recycle bin is located. This parameter can contain the address of a string formatted with the drive, folder, and subfolder names (c:\\windows\\system . . .). It can also contain an empty string or NULL. If this value is an empty string or NULL, all recycle bins on all drives will be emptied.
      flags(typing.Any):One of the SHERB_* values.CommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.

Returns:

      None
        
    """
    pass
        

def SHQueryRecycleBin(RootPath:'str'=None) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves the total size and number of items in the Recycle Bin for a 

specified drive

Args:

      RootPath(str):A path containing the drive whose recycle bin will be queried, or None for all drives

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def SHGetDesktopFolder() -> 'win32typing.PyIShellFolder':
    """
    None

Args:



Returns:

      win32typing.PyIShellFolder
        
    """
    pass
        

def SHUpdateImage(HashItem:'str',Index:'typing.Any',Flags:'typing.Any',ImageIndex:'typing.Any') -> 'None':
    """
    Notifies the shell that an image in the system image list has changed.

Args:

      HashItem(str):Full path of file containing the icon as returned by PyIExtractIcon::GetIconLocation
      Index(typing.Any):Index of the icon in the above file
      Flags(typing.Any):GIL_NOTFILENAME or GIL_SIMULATEDOC
      ImageIndex(typing.Any):Index of the icon in the system image list

Returns:

      None
        
    """
    pass
        

def SHChangeNotify(EventId:'typing.Any',Flags:'typing.Any',Item1:'typing.Any',Item2:'typing.Any') -> 'None':
    """
    Notifies the system of an event that an application has performed. An application 

should use this function if it performs an action that may affect the shell.

Args:

      EventId(typing.Any):Combination of shellcon.SHCNE_* constants
      Flags(typing.Any):Combination of shellcon.SHCNF_* constants that specify type of last 2 parameters Only one of the type flags may be specified, combined with one of the SHCNF_FLUSH* flags
      Item1(typing.Any):Type is dependent on the event to be signalled
      Item2(typing.Any):Type is dependent on the event to be signalled

Returns:

      None
        
    """
    pass
        

def SHChangeNotifyRegister(hwnd:'int',sources:'typing.Any',events:'typing.Any',msg:'typing.Any') -> 'typing.Any':
    """
    Registers a window that receives notifications from the file system or 

shell.

Args:

      hwnd(int):Handle to the window that receives the change or notification messages.
      sources(typing.Any):One or more values that indicate the type of events for which to receive notifications.
      events(typing.Any):Change notification events for which to receive notification.
      msg(typing.Any):Message to be posted to the window procedure.

Returns:

      typing.Any
        
    """
    pass
        

def SHChangeNotifyDeregister(_id:'typing.Any') -> 'None':
    """
    Unregisters the client's window process from receiving notification events

Args:

      _id(typing.Any):The registration identifier (ID) returned by shell::SHChangeNotifyRegister.

Returns:

      None
        
    """
    pass
        

def SHCreateItemFromIDList(pidl:'win32typing.PyIDL',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItem':
    """
    None

Args:

      pidl(win32typing.PyIDL):An absolute item identifier list
      riid(win32typing.PyIID):The interface to createCommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHCreateItemFromParsingName(name:'typing.Any',ctx:'win32typing.PyIBindCtx',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItem':
    """
    Creates and initializes a Shell item object from a 

parsing name.

Args:

      name(typing.Any):The display name of the item to create, eg a file path
      ctx(win32typing.PyIBindCtx):Bind context, can be None
      riid(win32typing.PyIID):The interface to create, IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHCreateItemFromRelativeName(Parent:'win32typing.PyIShellItem',Name:'typing.Any',ctx:'win32typing.PyIBindCtx',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItem':
    """
    Creates and initializes a Shell item object from a 

relative parsing name.

Args:

      Parent(win32typing.PyIShellItem):Shell item interface on the parent folder
      Name(typing.Any):Relative name of an item within the parent folder
      ctx(win32typing.PyIBindCtx):Bind context for parsing, can be None
      riid(win32typing.PyIID):The interface to return, IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHCreateItemInKnownFolder(FolderId:'win32typing.PyIID',Flags:'typing.Any',Name:'typing.Any',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItem':
    """
    Creates a Shell item object for a single file that exists 

inside a known folder.

Args:

      FolderId(win32typing.PyIID):The GUID of a known folder (shell.FOLDERID_*)
      Flags(typing.Any):Combination of shellcon.KF_FLAG_* flags controlling how folder is handled
      Name(typing.Any):Name of an item in the folder.  Pass None to bind to the known folder itself.
      riid(win32typing.PyIID):The interface to return, usually IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHCreateItemWithParent(Parent:'win32typing.PyIDL',sfParent:'win32typing.PyIShellFolder',child:'win32typing.PyIDL',riid:'win32typing.PyIID') -> 'win32typing.PyIShellItem':
    """
    Create a Shell item, given a parent folder and a child item 

ID.

Args:

      Parent(win32typing.PyIDL):Absolute item id list of the parent folder.  Pass None if the below shell folder is used.
      sfParent(win32typing.PyIShellFolder):Parent folder object.  Can be None if parent id list is specified.
      child(win32typing.PyIDL):Relative item id list for an object in the parent folder
      riid(win32typing.PyIID):The interface to return, usually IID_IShellItem or IID_IShellItem2CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHGetIDListFromObject(unk:'win32typing.PyIUnknown') -> 'win32typing.PyIDL':
    """
    Retrieves the PIDL of an object.

Args:

      unk(win32typing.PyIUnknown):CommentsThis function is only available on Vista and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIDL
        
    """
    pass
        

def SHGetInstanceExplorer() -> 'win32typing.PyIUnknown':
    """
    Allows components that run in a Web browser (Iexplore.exe) or a 

nondefault Windows Explorer (Explorer.exe) process to hold a reference to the process. The components can use the 

reference to prevent the process from closing prematurely.

Args:



Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def SHFileOperation(operation:'win32typing.SHFILEOPSTRUCT') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Copies, moves, renames, or deletes a file system object.

Args:

      operation(win32typing.SHFILEOPSTRUCT):Defines the operation to perform.Return ValueThe result is a tuple containing int result of the function itself, and the result of the fAnyOperationsAborted member after the operation.  If Flags contains FOF_WANTMAPPINGHANDLE, returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names of renamed files.  This will only have any content if FOF_RENAMEONCOLLISION was specified, and some filename conflicts actually occurred.

Returns:

      typing.Tuple[typing.Any, typing.Any]:Defines the operation to perform.Return ValueThe result is a tuple containing int result of the function itself, and the result of the 

fAnyOperationsAborted member after the operation.  If Flags contains FOF_WANTMAPPINGHANDLE, 

returned tuple will have a 3rd member containing a sequence of 2-tuples with the old and new file names 

of renamed files.  This will only have any content if FOF_RENAMEONCOLLISION was specified, and some 

filename conflicts actually occurred.

        
    """
    pass
        

def StringAsCIDA(pidl:'str') -> 'typing.Tuple[win32typing.PyIDL, typing.Any]':
    """
    Given a CIDA as a raw string, return the folder PIDL and list of 

children

Args:

      pidl(str):The PIDL as a raw string.Return ValueThe result is the PIDL of the folder, and a list of child PIDLs.

Returns:

      typing.Tuple[win32typing.PyIDL, typing.Any]:The PIDL as a raw string.Return ValueThe result is the PIDL of the folder, and a list of child PIDLs.

        
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
        

def StringAsPIDL(pidl:'str') -> 'win32typing.PyIDL':
    """
    Given a PIDL as a raw string, return a PIDL object (ie, a list of strings)

Args:

      pidl(str):The PIDL as a raw string.

Returns:

      win32typing.PyIDL
        
    """
    pass
        

def AddressAsPIDL(address:'typing.Any') -> 'win32typing.PyIDL':
    """
    Given the address of a PIDL in memory, return a PIDL object (ie, a list of 

strings)

Args:

      address(typing.Any):The address of the PIDL

Returns:

      win32typing.PyIDL
        
    """
    pass
        

def PIDLAsString(pidl:'win32typing.PyIDL') -> 'str':
    """
    Given a PIDL object, return the raw PIDL bytes as a string

Args:

      pidl(win32typing.PyIDL):The PIDL object (ie, a list of strings)

Returns:

      str
        
    """
    pass
        

def SHGetSettings(mask:'typing.Any'=-1) -> 'typing.Any':
    """
    Retrieves the current shell option settings.

Args:

      mask(typing.Any):The values being requested - one of the shellcon.SSF_* constantsCommentsThis method is only available in shell version 4.71.  If the function is not available, a COM Exception with HRESULT=E_NOTIMPL will be raised.Return ValueThe result is a dictionary, the contents of which depend on the mask param.  Key names are the same as the SHELLFLAGSTATE structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc

Returns:

      typing.Any:The values being requested - one of the shellcon.SSF_* constants
Comments

This method is only available in shell version 4.71.  If the 

function is not available, a COM Exception with HRESULT=E_NOTIMPL 

will be raised.
Return ValueThe result is a dictionary, the contents of which depend on 

the mask param.  Key names are the same as the SHELLFLAGSTATE 

structure members - 'fShowExtensions', 'fNoConfirmRecycle', etc

        
    """
    pass
        

def FILEGROUPDESCRIPTORAsString(descriptors:'typing.List[typing.Any]',arg:'typing.Any') -> 'str':
    """
    Creates a FILEGROUPDESCRIPTOR from a sequence of mapping objects, 

each with FILEDESCRIPTOR attributes

Args:

      descriptors(typing.List[typing.Any]):A sequence of FILEDESCRIPTOR objects. Each filedescriptor object must be a mapping/dictionary, with the following optional attributes: dwFlags, clsid, sizel, pointl, dwFileAttributes, ftCreationTime, ftLastAccessTime, ftLastWriteTime, nFileSize If these attributes do not exist, or are None, they will be ignored - hence you only need specify attributes you care about. In general, you can omit dwFlags - it will be set correctly based on what other attributes exist.
      arg(typing.Any):If true, a FILEDESCRIPTORW object is created

Returns:

      str
        
    """
    pass
        

def StringAsFILEGROUPDESCRIPTOR(buf:'typing.Any',make_unicode:'typing.Any'=-1) -> 'typing.List[typing.Any]':
    """
    Decodes a FILEGROUPDESCRIPTOR packed in a string

Args:

      buf(typing.Any):A string packed as either FILEGROUPDESCRIPTORW or FILEGROUPDESCRIPTORW
      make_unicode(typing.Any):Should this be treated as a FILEDESCRIPTORW?  If -1 the size of the buffer will be used to make that determination.  Thus, if the buffer is not the exact size of a correct FILEDESCRIPTORW or FILEDESCRIPTORA, you will need to specify this parameter.

Returns:

      typing.List[typing.Any]
        
    """
    pass
        

def ShellExecuteEx(lpVerb:'str',lpFile:'str',lpParameters:'str',lpDirectory:'str',lpIDList:'win32typing.PyIDL',obClass:'str',hkeyClass:'typing.Any',dwHotKey:'typing.Any',hIcon:'int',hMonitor:'int',fMask:'typing.Any'=0,hwnd:'int'=0,nShow:'typing.Any'=0) -> 'typing.Any':
    """
    Performs an operation on a file.

Args:

      lpVerb(str):
      lpFile(str):
      lpParameters(str):
      lpDirectory(str):
      lpIDList(win32typing.PyIDL):
      obClass(str):
      hkeyClass(typing.Any):
      dwHotKey(typing.Any):
      hIcon(int):
      hMonitor(int):Return ValueThe result is a dictionary based on documented result values in the structure.  Currently this is "hInstApp" and "hProcess"
      fMask(typing.Any):The default mask for the structure.  Other masks may be added based on what paramaters are supplied.
      hwnd(int):
      nShow(typing.Any):

Returns:

      typing.Any:Return ValueThe result is a dictionary based on documented result values 

in the structure.  Currently this is "hInstApp" and "hProcess"

        
    """
    pass
        

def SHGetViewStatePropertyBag(pidl:'win32typing.PyIDL',BagName:'str',Flags:'typing.Any',riid:'win32typing.PyIID') -> 'win32typing.PyIPropertyBag':
    """
    Retrieves an interface for the view state of a folder

Args:

      pidl(win32typing.PyIDL):An item id list that identifies the folder
      BagName(str):Name of the property bag to retrieve
      Flags(typing.Any):Combination of SHGVSPB_* flags
      riid(win32typing.PyIID):The interface to return, usually IID_IPropertyBagCommentsThis function will also return IPropertyBag2, but we don't have a python implementation of this interface yet

Returns:

      win32typing.PyIPropertyBag
        
    """
    pass
        

def SHILCreateFromPath(Path:'str',Flags:'typing.Any') -> 'typing.Tuple[win32typing.PyIDL, typing.Any]':
    """
    Retrieves the PIDL and attributes for a path

Args:

      Path(str):The path whose PIDL will be returned
      Flags(typing.Any):A combination of SFGAO_* constants as used with GetAttributesOfReturn ValueReturns the PIDL for the given path and any requested attributes

Returns:

      typing.Tuple[win32typing.PyIDL, typing.Any]:A combination of SFGAO_* constants as used with GetAttributesOfReturn ValueReturns the PIDL for the given path and any requested attributes

        
    """
    pass
        

def SHCreateShellItem(pidlParent:'win32typing.PyIDL',sfParent:'win32typing.PyIShellFolder',Child:'win32typing.PyIDL') -> 'win32typing.PyIShellItem':
    """
    Creates an IShellItem interface from a PIDL

Args:

      pidlParent(win32typing.PyIDL):PIDL of parent folder, can be None
      sfParent(win32typing.PyIShellFolder):IShellFolder interface of parent folder, can be None
      Child(win32typing.PyIDL):PIDL identifying desired item.  Must be an absolute PIDL if parent is not specified.CommentsThis function is only available on XP and later; a COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIShellItem
        
    """
    pass
        

def SHOpenFolderAndSelectItems(Folder:'win32typing.PyIDL',Items:'typing.Tuple[win32typing.PyIDL, ...]',Flags:'typing.Any'=0) -> 'None':
    """
    Displays a shell folder with items pre-selected

Args:

      Folder(win32typing.PyIDL):An absolute item id list identifying a shell folder
      Items(typing.Tuple[win32typing.PyIDL, ...]):A sequence of relative item ids identifying items in the folder
      Flags(typing.Any):Combination of OFASI_* flags (not used on XP)CommentsThis function is only available on XP and later. COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      None
        
    """
    pass
        

def SHCreateStreamOnFileEx(File:'typing.Any',Mode:'typing.Any',Attributes:'typing.Any',Create:'typing.Any',Template:'typing.Any'=None) -> 'win32typing.PyIStream':
    """
    Creates an IStream interface that reads and writes to a file

Args:

      File(typing.Any):Name of file to be connected to the stream
      Mode(typing.Any):Combination of storagecon.STGM_* flags specifying the access mode
      Attributes(typing.Any):Combination of win32con.FILE_ATTRIBUTE_* flags
      Create(typing.Any):Determines if function should fail when file exists (see MSDN docs for full explanation)
      Template(typing.Any):Reserved, use only NoneCommentsAccepts keyword args.This function is only available on WinXP and later. COM exception with E_NOTIMPL will be thrown if the function can't be located.

Returns:

      win32typing.PyIStream
        
    """
    pass
        

def SetCurrentProcessExplicitAppUserModelID(AppID:'typing.Any') -> 'None':
    """
    Sets the taskbar identifier

Args:

      AppID(typing.Any):The Application User Model ID used to group taskbar buttonsCommentsShould be used early in process startup before creating any windowsRequires Windows 7 or later

Returns:

      None
        
    """
    pass
        

def GetCurrentProcessExplicitAppUserModelID() -> 'typing.Any':
    """
    Retrieves the current taskbar identifier

Args:



Returns:

      typing.Any
        
    """
    pass
        

def SHParseDisplayName(Name:'typing.Any',Attributes:'typing.Any',BindCtx:'win32typing.PyIBindCtx'=None) -> 'typing.Tuple[win32typing.PyIDL, typing.Any]':
    """
    Translates a display name into a shell item identifier

Args:

      Name(typing.Any):Display name of a shell item, such as a file path
      Attributes(typing.Any):Bitmask of shell attributes to retrieve, combination of shellcon.SFGAO_*
      BindCtx(win32typing.PyIBindCtx):Bind context, can be NoneCommentsAccepts keyword argsRequires XP or laterReturn ValueReturns the item id list and any requested attribute flags

Returns:

      typing.Tuple[win32typing.PyIDL, typing.Any]:Bind context, can be None
Comments

Accepts keyword args

Requires XP or later
Return ValueReturns the item id list and any requested attribute flags

        
    """
    pass
        