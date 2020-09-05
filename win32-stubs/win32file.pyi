from pywintypes import *
__all__=['AreFileApisANSI', 'CancelIo', 'CopyFile', 'CopyFileW', 'CreateDirectory', 'CreateDirectoryW', 'CreateDirectoryEx', 'CreateFile', 'CreateIoCompletionPort', 'CreateMailslot', 'GetMailslotInfo', 'SetMailslotInfo', 'DefineDosDevice', 'DefineDosDeviceW', 'DeleteFile', 'DeviceIoControl', 'FindClose', 'FindCloseChangeNotification', 'FindFirstChangeNotification', 'FindNextChangeNotification', 'FlushFileBuffers', 'GetBinaryType', 'GetDiskFreeSpace', 'GetDiskFreeSpaceEx', 'GetDriveType', 'GetDriveTypeW', 'GetFileAttributes', 'GetFileAttributesW', 'GetFileTime', 'SetFileTime', 'GetFileInformationByHandle', 'GetCompressedFileSize', 'GetFileSize', 'AllocateReadBuffer', 'ReadFile', 'WriteFile', 'CloseHandle', 'LockFileEx', 'UnlockFileEx', 'GetQueuedCompletionStatus', 'PostQueuedCompletionStatus', 'GetFileType', 'GetLogicalDrives', 'GetOverlappedResult', 'LockFile', 'MoveFile', 'MoveFileW', 'MoveFileEx', 'MoveFileExW', 'QueryDosDevice', 'ReadDirectoryChangesW', 'FILE_NOTIFY_INFORMATION', 'SetCurrentDirectory', 'SetEndOfFile', 'SetFileApisToANSI', 'SetFileApisToOEM', 'SetFileAttributes', 'SetFilePointer', 'SetVolumeLabel', 'UnlockFile', '_get_osfhandle', '_open_osfhandle', '_setmaxstdio', '_getmaxstdio', 'TransmitFile', 'ConnectEx', 'AcceptEx', 'CalculateSocketEndPointSize', 'GetAcceptExSockaddrs', 'WSAEventSelect', 'WSAEnumNetworkEvents', 'WSAAsyncSelect', 'WSASend', 'WSARecv', 'BuildCommDCB', 'ClearCommError', 'EscapeCommFunction', 'GetCommState', 'SetCommState', 'ClearCommBreak', 'GetCommMask', 'SetCommMask', 'GetCommModemStatus', 'GetCommTimeouts', 'SetCommTimeouts', 'PurgeComm', 'SetCommBreak', 'SetupComm', 'TransmitCommChar', 'WaitCommEvent', 'SetVolumeMountPoint', 'DeleteVolumeMountPoint', 'GetVolumeNameForVolumeMountPoint', 'GetVolumePathName', 'GetVolumePathNamesForVolumeName', 'CreateHardLink', 'CreateSymbolicLink', 'EncryptFile', 'DecryptFile', 'EncryptionDisable', 'FileEncryptionStatus', 'QueryUsersOnEncryptedFile', 'QueryRecoveryAgentsOnEncryptedFile', 'RemoveUsersFromEncryptedFile', 'AddUsersToEncryptedFile', 'DuplicateEncryptionInfoFile', 'BackupRead', 'BackupSeek', 'BackupWrite', 'SetFileShortName', 'CopyFileEx', 'MoveFileWithProgress', 'ReplaceFile', 'OpenEncryptedFileRaw', 'ReadEncryptedFileRaw', 'WriteEncryptedFileRaw', 'CloseEncryptedFileRaw', 'CreateFileW', 'DeleteFileW', 'GetFileAttributesEx', 'SetFileAttributesW', 'CreateDirectoryExW', 'RemoveDirectory', 'FindFilesW', 'FindFilesIterator', 'FindStreams', 'FindFileNames', 'GetFinalPathNameByHandle', 'SfcGetNextProtectedFile', 'SfcIsFileProtected', 'GetLongPathName', 'GetFullPathName', 'Wow64DisableWow64FsRedirection', 'Wow64RevertWow64FsRedirection', 'GetFileInformationByHandleEx', 'SetFileInformationByHandle', 'ReOpenFile', 'OpenFileById', 'CALLBACK_CHUNK_FINISHED', 'CALLBACK_STREAM_SWITCH', 'CBR_110', 'CBR_115200', 'CBR_1200', 'CBR_128000', 'CBR_14400', 'CBR_19200', 'CBR_2400', 'CBR_256000', 'CBR_300', 'CBR_38400', 'CBR_4800', 'CBR_56000', 'CBR_57600', 'CBR_600', 'CBR_9600', 'CLRBREAK', 'CLRDTR', 'CLRRTS', 'COPY_FILE_ALLOW_DECRYPTED_DESTINATION', 'COPY_FILE_COPY_SYMLINK', 'COPY_FILE_FAIL_IF_EXISTS', 'COPY_FILE_OPEN_SOURCE_FOR_WRITE', 'COPY_FILE_RESTARTABLE', 'CREATE_ALWAYS', 'CREATE_FOR_DIR', 'CREATE_FOR_IMPORT', 'CREATE_NEW', 'DRIVE_CDROM', 'DRIVE_FIXED', 'DRIVE_NO_ROOT_DIR', 'DRIVE_RAMDISK', 'DRIVE_REMOTE', 'DRIVE_REMOVABLE', 'DRIVE_UNKNOWN', 'DTR_CONTROL_DISABLE', 'DTR_CONTROL_ENABLE', 'DTR_CONTROL_HANDSHAKE', 'EV_BREAK', 'EV_CTS', 'EV_DSR', 'EV_ERR', 'EV_RING', 'EV_RLSD', 'EV_RXCHAR', 'EV_RXFLAG', 'EV_TXEMPTY', 'EVENPARITY', 'FD_ACCEPT', 'FD_ADDRESS_LIST_CHANGE', 'FD_CLOSE', 'FD_CONNECT', 'FD_GROUP_QOS', 'FD_OOB', 'FD_QOS', 'FD_READ', 'FD_ROUTING_INTERFACE_CHANGE', 'FD_WRITE', 'FILE_ALL_ACCESS', 'FILE_ATTRIBUTE_ARCHIVE', 'FILE_ATTRIBUTE_COMPRESSED', 'FILE_ATTRIBUTE_DIRECTORY', 'FILE_ATTRIBUTE_HIDDEN', 'FILE_ATTRIBUTE_NORMAL', 'FILE_ATTRIBUTE_OFFLINE', 'FILE_ATTRIBUTE_READONLY', 'FILE_ATTRIBUTE_SYSTEM', 'FILE_ATTRIBUTE_TEMPORARY', 'FILE_BEGIN', 'FILE_CURRENT', 'FILE_ENCRYPTABLE', 'FILE_END', 'FILE_FLAG_BACKUP_SEMANTICS', 'FILE_FLAG_DELETE_ON_CLOSE', 'FILE_FLAG_NO_BUFFERING', 'FILE_FLAG_OPEN_REPARSE_POINT', 'FILE_FLAG_OVERLAPPED', 'FILE_FLAG_POSIX_SEMANTICS', 'FILE_FLAG_RANDOM_ACCESS', 'FILE_FLAG_SEQUENTIAL_SCAN', 'FILE_FLAG_WRITE_THROUGH', 'FILE_GENERIC_READ', 'FILE_GENERIC_WRITE', 'FILE_IS_ENCRYPTED', 'FILE_READ_ONLY', 'FILE_ROOT_DIR', 'FILE_SHARE_DELETE', 'FILE_SHARE_READ', 'FILE_SHARE_WRITE', 'FILE_SYSTEM_ATTR', 'FILE_SYSTEM_DIR', 'FILE_SYSTEM_NOT_SUPPORT', 'FILE_TYPE_CHAR', 'FILE_TYPE_DISK', 'FILE_TYPE_PIPE', 'FILE_TYPE_UNKNOWN', 'FILE_UNKNOWN', 'FILE_USER_DISALLOWED', 'FileAllocationInfo', 'FileAttributeTagInfo', 'FileBasicInfo', 'FileCompressionInfo', 'FileDispositionInfo', 'FileEndOfFileInfo', 'FileIdBothDirectoryInfo', 'FileIdBothDirectoryRestartInfo', 'FileIdType', 'FileIoPriorityHintInfo', 'FileNameInfo', 'FileRenameInfo', 'FileStandardInfo', 'FileStreamInfo', 'GENERIC_EXECUTE', 'GENERIC_READ', 'GENERIC_WRITE', 'GetFileExInfoStandard', 'IoPriorityHintLow', 'IoPriorityHintNormal', 'IoPriorityHintVeryLow', 'MARKPARITY', 'MOVEFILE_COPY_ALLOWED', 'MOVEFILE_CREATE_HARDLINK', 'MOVEFILE_DELAY_UNTIL_REBOOT', 'MOVEFILE_FAIL_IF_NOT_TRACKABLE', 'MOVEFILE_REPLACE_EXISTING', 'MOVEFILE_WRITE_THROUGH', 'NOPARITY', 'ObjectIdType', 'ODDPARITY', 'ONE5STOPBITS', 'ONESTOPBIT', 'OPEN_ALWAYS', 'OPEN_EXISTING', 'OVERWRITE_HIDDEN', 'PROGRESS_CANCEL', 'PROGRESS_CONTINUE', 'PROGRESS_QUIET', 'PROGRESS_STOP', 'PURGE_RXABORT', 'PURGE_RXCLEAR', 'PURGE_TXABORT', 'PURGE_TXCLEAR', 'REPLACEFILE_IGNORE_MERGE_ERRORS', 'REPLACEFILE_WRITE_THROUGH', 'RTS_CONTROL_DISABLE', 'RTS_CONTROL_ENABLE', 'RTS_CONTROL_HANDSHAKE', 'RTS_CONTROL_TOGGLE', 'SCS_32BIT_BINARY', 'SCS_DOS_BINARY', 'SCS_OS216_BINARY', 'SCS_PIF_BINARY', 'SCS_POSIX_BINARY', 'SCS_WOW_BINARY', 'SECURITY_ANONYMOUS', 'SECURITY_CONTEXT_TRACKING', 'SECURITY_DELEGATION', 'SECURITY_EFFECTIVE_ONLY', 'SECURITY_IDENTIFICATION', 'SECURITY_IMPERSONATION', 'SETBREAK', 'SETDTR', 'SETRTS', 'SETXOFF', 'SETXON', 'SO_CONNECT_TIME', 'SO_UPDATE_ACCEPT_CONTEXT', 'SO_UPDATE_CONNECT_CONTEXT', 'SPACEPARITY', 'SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE', 'SYMBOLIC_LINK_FLAG_DIRECTORY', 'TF_DISCONNECT', 'TF_REUSE_SOCKET', 'TF_USE_DEFAULT_WORKER', 'TF_USE_KERNEL_APC', 'TF_USE_SYSTEM_THREAD', 'TF_WRITE_BEHIND', 'TRUNCATE_EXISTING', 'TWOSTOPBITS', 'WSA_IO_PENDING', 'WSA_OPERATION_ABORTED', 'WSAECONNABORTED', 'WSAECONNRESET', 'WSAEDISCON', 'WSAEFAULT', 'WSAEINPROGRESS', 'WSAEINTR', 'WSAEINVAL', 'WSAEMSGSIZE', 'WSAENETDOWN', 'WSAENETRESET', 'WSAENOBUFS', 'WSAENOTCONN', 'WSAENOTSOCK', 'WSAEOPNOTSUPP', 'WSAESHUTDOWN', 'WSAEWOULDBLOCK']
import typing
""""""


def AreFileApisANSI() -> int:
    """
    Determines whether a set of Win32 file functions is using the ANSI or OEM character set code page. This function is useful for 8-bit console input and output operations.


Args:



Returns:

      int
        
    """
    pass


def CancelIo(handle:typing.Any) -> None:
    """
    Cancels pending IO requests for the object.


Args:

      handle(typing.Any):The handle being cancelled.

Returns:

      None
        
    """
    pass


def CopyFile(from:typing.Any,to:typing.Any,bFailIfExists:int) -> None:
    """
    Copies a file


Args:

      from(typing.Any):The name of the file to copy from
      to(typing.Any):The name of the file to copy to
      bFailIfExists(int):Indicates if the operation should fail if the file exists.

Returns:

      None
        
    """
    pass


def CopyFileW(from:typing.Any,to:typing.Any,bFailIfExists:int) -> None:
    """
    Copies a file (NT/2000 Unicode specific version)


Args:

      from(typing.Any):The name of the file to copy from
      to(typing.Any):The name of the file to copy to
      bFailIfExists(int):Indicates if the operation should fail if the file exists.

Returns:

      None
        
    """
    pass


def CreateDirectory(name:typing.Any,sa:typing.Any) -> None:
    """
    Creates a directory


Args:

      name(typing.Any):The name of the directory to create
      sa(typing.Any):The security attributes, or None

Returns:

      None
        
    """
    pass


def CreateDirectoryW(name:typing.Any,sa:typing.Any) -> None:
    """
    Creates a directory (NT/2000 Unicode specific version)


Args:

      name(typing.Any):The name of the directory to create
      sa(typing.Any):The security attributes, or None

Returns:

      None
        
    """
    pass


def CreateDirectoryEx(templateName:typing.Any,newDirectory:typing.Any,sa:typing.Any) -> None:
    """
    Creates a directory


Args:

      templateName(typing.Any):Specifies the path of the directory to use as a template when creating the new directory.
      newDirectory(typing.Any):Specifies the name of the new directory
      sa(typing.Any):The security attributes, or None

Returns:

      None
        
    """
    pass


def CreateFile(fileName:typing.Any,desiredAccess:int,shareMode:int,attributes:typing.Any,CreationDisposition:int,flagsAndAttributes:int,hTemplateFile:typing.Any) -> int:
    """
    Creates or opens the a file or other object and returns a handle that can be used to access the object.


Args:

      fileName(typing.Any):The name of the file
      desiredAccess(int):access (read-write) mode Specifies the type of access to the object. An application can obtain read access, write access, read-write access, or device query access. This parameter can be any combination of the following values.ValueMeaning0Specifies device query access to the object. An application can query device attributes without accessing the device.GENERIC_READSpecifies read access to the object. Data can be read from the file and the file pointer can be moved. Combine with GENERIC_WRITE for read-write access.GENERIC_WRITESpecifies write access to the object. Data can be written to the file and the file pointer can be moved. Combine with GENERIC_READ for read-write access.
      shareMode(int):Set of bit flags that specifies how the object can be shared. If dwShareMode is 0, the object cannot be shared. Subsequent open operations on the object will fail, until the handle is closed. To share the object, use a combination of one or more of the following values:ValueMeaningFILE_SHARE_DELETEWindows NT: Subsequent open operations on the object will succeed only if delete access is requested.FILE_SHARE_READSubsequent open operations on the object will succeed only if read access is requested.FILE_SHARE_WRITESubsequent open operations on the object will succeed only if write access is requested.
      attributes(typing.Any):The security attributes, or None
      CreationDisposition(int):Specifies which action to take on files that exist, and which action to take when files do not exist. For more information about this parameter, see the Remarks section. This parameter must be one of the following values:ValueMeaningCREATE_NEWCreates a new file. The function fails if the specified file already exists.CREATE_ALWAYSCreates a new file. If the file exists, the function overwrites the file and clears the existing attributes.OPEN_EXISTINGOpens the file. The function fails if the file does not exist. See the Remarks section for a discussion of why you should use the OPEN_EXISTING flag if you are using the CreateFile function for devices, including the console.OPEN_ALWAYSOpens the file, if it exists. If the file does not exist, the function creates the file as if dwCreationDisposition were CREATE_NEW.TRUNCATE_EXISTINGOpens the file. Once opened, the file is truncated so that its size is zero bytes. The calling process must open the file with at least GENERIC_WRITE access. The function fails if the file does not exist.
      flagsAndAttributes(int):file attributes
      hTemplateFile(typing.Any):Specifies a handle with GENERIC_READ access to a template file. The template file supplies file attributes and extended attributes for the file being created.   Under Win95, this must be 0, else an exception will be raised.CommentsThe following objects can be opened:filespipesmailslotscommunications resourcesdisk devices (Windows NT only)consolesdirectories (open only)

Returns:

      int
        
    """
    pass


def CreateIoCompletionPort(handle:typing.Any,existing:typing.Any,completionKey:int,numThreads:int) -> int:
    """
    Can associate an instance of an opened file with a newly created or an existing input/output (I/O) completion port; or it can create an I/O completion port without associating it with a file.


Args:

      handle(typing.Any):file handle to associate with the I/O completion port
      existing(typing.Any):handle to the I/O completion port
      completionKey(int):per-file completion key for I/O completion packets
      numThreads(int):number of threads allowed to execute concurrentlyReturn ValueIf an existing handle to a completion port is passed, the result of this function will be that same handle.  See MSDN for more details.

Returns:

      int:number of threads allowed to execute concurrentlyReturn ValueIf an existing handle to a completion port is passed, the result 

of this function will be that same handle.  See MSDN for more details.

        
    """
    pass


def CreateMailslot(Name:str,MaxMessageSize:int,ReadTimeout:int,SecurityAttributes:typing.Any) -> int:
    """
    Creates a mailslot on the local machine


Args:

      Name(str):Name of the mailslot, of the form \\.\\mailslot\\[path]name
      MaxMessageSize(int):Largest message size.  Use 0 for unlimited.
      ReadTimeout(int):Timeout in milliseconds.  Use -1 for no timeout.
      SecurityAttributes(typing.Any):Determines if returned handle is inheritable, can be NoneWin32 API References

Returns:

      int
        
    """
    pass


def GetMailslotInfo(Mailslot:typing.Any) -> typing.Any:
    """
    Retrieves information about a mailslot


Args:

      Mailslot(typing.Any):Handle to a mailslotWin32 API References

Returns:

      typing.Any:Search for GetMailslotInfo at msdn, google or google groups.
Return ValueReturns (maximum message size, next message size, message count, timeout)

        
    """
    pass


def SetMailslotInfo(Mailslot:typing.Any,ReadTimeout:int) -> None:
    """
    Sets a mailslot's timeout


Args:

      Mailslot(typing.Any):Handle to a mailslot
      ReadTimeout(int):Timeout in milliseconds, use -1 for no timeoutWin32 API References

Returns:

      None
        
    """
    pass


def DefineDosDevice(flags:int,deviceName:typing.Any,targetPath:typing.Any) -> None:
    """
    Lets an application define, redefine, or delete MS-DOS device names.


Args:

      flags(int):flags specifying aspects of device definition
      deviceName(typing.Any):MS-DOS device name string
      targetPath(typing.Any):MS-DOS or path string for 32-bit Windows.

Returns:

      None
        
    """
    pass


def DefineDosDeviceW(flags:int,deviceName:typing.Any,targetPath:typing.Any) -> None:
    """
    Lets an application define, redefine, or delete MS-DOS device names. (NT/2000 Unicode specific version)


Args:

      flags(int):flags specifying aspects of device definition
      deviceName(typing.Any):MS-DOS device name string
      targetPath(typing.Any):MS-DOS or path string for 32-bit Windows.

Returns:

      None
        
    """
    pass


def DeleteFile(fileName:typing.Any) -> None:
    """
    Deletes a file.


Args:

      fileName(typing.Any):The filename to delete

Returns:

      None
        
    """
    pass


def DeviceIoControl(Device:typing.Any,IoControlCode:int,InBuffer:Union[str,typing.Any],OutBuffer:Union[int,typing.Any],Overlapped:typing.Any=None) -> typing.Any:
    """
    Sends a control code to a device or file system driver


Args:

      Device(typing.Any):Handle to a file, device, or volume
      IoControlCode(int):IOControl Code to use, from winioctlcon
      InBuffer(str,typing.Any):The input data for the operation, can be None for some operations.
      OutBuffer(int,typing.Any):Size of the buffer to allocate for output, or a writeable buffer as returned by win32file::AllocateReadBuffer.
      Overlapped(typing.Any):An overlapped object for async operations.  Device handle must have been opened with FILE_FLAG_OVERLAPPED.CommentsAccepts keyword argsReturn ValueIf a preallocated output buffer is passed in, the returned object may be the original buffer, or a view of the buffer with only the actual size of the retrieved data. If OutBuffer is a buffer size and the operation is synchronous (ie no Overlapped is passed in), returns a plain string containing the retrieved data.  For an async operation, a new writeable buffer is returned.

Returns:

      typing.Any:An overlapped object for async operations.  Device 

handle must have been opened with FILE_FLAG_OVERLAPPED.
Comments

Accepts keyword args
Return ValueIf a preallocated output buffer is passed in, the returned object 

may be the original buffer, or a view of the buffer with only the actual 

size of the retrieved data. 

If OutBuffer is a buffer size and the operation is synchronous (ie no 

Overlapped is passed in), returns a plain string containing the retrieved 

data.  For an async operation, a new writeable buffer is returned.

        
    """
    pass


def FindClose(hFindFile:int) -> None:
    """
    Closes a find handle.


Args:

      hFindFile(int):file search handle

Returns:

      None
        
    """
    pass


def FindCloseChangeNotification(hChangeHandle:int) -> None:
    """
    Closes a handle.


Args:

      hChangeHandle(int):handle to change notification to close

Returns:

      None
        
    """
    pass


def FindFirstChangeNotification(pathName:typing.Any,bWatchSubtree:int,notifyFilter:int) -> int:
    """
    Creates a change notification handle and sets up initial change notification filter conditions. A wait on a notification handle succeeds when a change matching the filter conditions occurs in the specified directory or subtree.


Args:

      pathName(typing.Any):Name of directory to watch
      bWatchSubtree(int):flag for monitoring directory or directory tree
      notifyFilter(int):filter conditions to watch for.  See win32api::FindFirstChangeNotification for details.

Returns:

      int
        
    """
    pass


def FindNextChangeNotification(hChangeHandle:int) -> int:
    """
    Requests that the operating system signal a change notification handle the next time it detects an appropriate change,


Args:

      hChangeHandle(int):handle to change notification to signal

Returns:

      int
        
    """
    pass


def FlushFileBuffers(hFile:typing.Any) -> None:
    """
    Clears the buffers for the specified file and causes all buffered data to be written to the file.


Args:

      hFile(typing.Any):open handle to file whose buffers are to be flushed

Returns:

      None
        
    """
    pass


def GetBinaryType(appName:typing.Any) -> int:
    """
    Determines whether a file is executable, and if so, what type of executable file it is. That last property determines which subsystem an executable file runs under.


Args:

      appName(typing.Any):Fully qualified path of file to test

Returns:

      int
        
    """
    pass


def GetDiskFreeSpace(rootPathName:typing.Any) -> typing.Any:
    """
    Determines the free space on a device.


Args:

      rootPathName(typing.Any):address of root pathReturn ValueThe result is a tuple of integers representing (sectors per cluster, bytes per sector, number of free clusters, total number of clusters)

Returns:

      typing.Any:address of root pathReturn ValueThe result is a tuple of integers representing (sectors per cluster, bytes per sector, number of free clusters, total number of clusters)

        
    """
    pass


def GetDiskFreeSpaceEx(rootPathName:typing.Any) -> typing.Any:
    """
    Determines the free space on a device.


Args:

      rootPathName(typing.Any):address of root pathReturn ValueThe result is a tuple of long integers:Items[0] long integer : freeBytesThe total number of free bytes on the disk that are available to the user associated with the calling thread.[1] long integer : totalBytesThe total number of bytes on the disk that are available to the user associated with the calling thread. Windows 2000: If per-user quotas are in use, this value may be less than the total number of bytes on the disk.[2] long integer : totalFreeBytesThe total number of free bytes on the disk.

Returns:

      typing.Any:address of root pathReturn ValueThe result is a tuple of long integers:
Items[0] long integer : freeBytes
The total number of free bytes on the disk that are available to the user associated with the calling thread.
[1] long integer : totalBytes
The total number of bytes on the disk that are available to the user associated with the calling thread. 

Windows 2000: If per-user quotas are in use, this value may be less than the total number of bytes on the disk.
[2] long integer : totalFreeBytes
The total number of free bytes on the disk.

        
    """
    pass


def GetDriveType(rootPathName:str) -> int:
    """
    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.


Args:

      rootPathName(str):Return ValueThe result is one of the DRIVE_* constants.

Returns:

      int:Return ValueThe result is one of the DRIVE_* constants.

        
    """
    pass


def GetDriveTypeW(rootPathName:str) -> int:
    """
    Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive. (NT/2000 Unicode specific version).


Args:

      rootPathName(str):Return ValueThe result is one of the DRIVE_* constants.

Returns:

      int:Return ValueThe result is one of the DRIVE_* constants.

        
    """
    pass


def GetFileAttributes(fileName:typing.Any) -> int:
    """
    Determines a files attributes.


Args:

      fileName(typing.Any):Name of the file to retrieve attributes for.CommentsThe win32file module exposes win32file::GetFileAttributes and win32file::GetFileAttributesW separately - both functions will accept either strings or Unicode objects but will always call the named function. This is different than win32api::GetFileAttributes, which only exposes one Python function and automatically calls the appropriate win32 function based on the type of the filename param.

Returns:

      int
        
    """
    pass


def GetFileAttributesW(fileName:typing.Any) -> int:
    """
    Determines a files attributes (NT/2000 Unicode specific version).


Args:

      fileName(typing.Any):Name of the file to retrieve attributes for.CommentsNote that win32api::GetFileAttributes will automatically call GetFileAttributesW when passed a unicode filename param.  See win32file::GetFileAttributes and win32api::GetFileAttributes for more.

Returns:

      int
        
    """
    pass


def GetFileTime(handle:typing.Any,creationTime:typing.Any,accessTime:typing.Any,writeTime:typing.Any) -> typing.Any:
    """
    Returns a file's creation, last access, and modification times.


Args:

      handle(typing.Any):Handle to the file.
      creationTime(typing.Any):
      accessTime(typing.Any):
      writeTime(typing.Any):CommentsTimes are returned in UTC time.

Returns:

      typing.Any
        
    """
    pass


def SetFileTime(File:typing.Any,CreationTime:typing.Any=None,LastAccessTime:typing.Any=None,LastWriteTime:typing.Any=None,UTCTimes:typing.Any=False) -> None:
    """
    Sets the date and time that a file was created, last accessed, or last modified.


Args:

      File(typing.Any):Previously opened handle (opened with FILE_WRITE_ATTRIBUTES access).
      CreationTime(typing.Any):File created time. None for no change.
      LastAccessTime(typing.Any):File access time. None for no change.
      LastWriteTime(typing.Any):File written time. None for no change.
      UTCTimes(typing.Any):If True, input times are treated as UTC and no conversion is done, otherwise they are treated as local times.  Defaults to False for backward compatibility. This parameter is ignored in Python 3.x, where you should always pass datetime objects with timezone information.

Returns:

      None
        
    """
    pass


def GetFileInformationByHandle(handle:typing.Any) -> tuple:
    """
    Retrieves file information for a specified file.


Args:

      handle(typing.Any):Handle to the file for which to obtain information.This handle should not be a pipe handle. The GetFileInformationByHandle function does not work with pipe handles.CommentsDepending on the underlying network components of the operating system and the type of server connected to, the GetFileInformationByHandle function may fail, return partial information, or full information for the given file. In general, you should not use GetFileInformationByHandle unless your application is intended to be run on a limited set of operating system configurations.Return ValueThe result is a tuple of:Items[0] int : dwFileAttributes[1] PyTime : ftCreationTime[2] PyTime : ftLastAccessTime[3] PyTime : ftLastWriteTime[4] int : dwVolumeSerialNumber[5] int : nFileSizeHigh[6] int : nFileSizeLow[7] int : nNumberOfLinks[8] int : nFileIndexHigh[9] int : nFileIndexLow

Returns:

      tuple:Handle to the file for which to obtain information.This handle should not be a pipe handle. The GetFileInformationByHandle function does not work with pipe handles.Comments

Depending on the underlying network components of the operating system and the type of server 

connected to, the GetFileInformationByHandle function may fail, return partial information, 

or full information for the given file. In general, you should not use GetFileInformationByHandle 

unless your application is intended to be run on a limited set of operating system configurations.
Return ValueThe result is a tuple of:
Items[0] int : dwFileAttributes

[1] PyTime : ftCreationTime

[2] PyTime : ftLastAccessTime

[3] PyTime : ftLastWriteTime

[4] int : dwVolumeSerialNumber

[5] int : nFileSizeHigh

[6] int : nFileSizeLow

[7] int : nNumberOfLinks

[8] int : nFileIndexHigh

[9] int : nFileIndexLow


        
    """
    pass


def GetCompressedFileSize() -> typing.Any:
    """
    Determines the compressed size of a file.


Args:



Returns:

      typing.Any
        
    """
    pass


def GetFileSize() -> typing.Any:
    """
    Determines the size of a file.


Args:



Returns:

      typing.Any
        
    """
    pass


def AllocateReadBuffer(bufSize:int) -> typing.Any:
    """
    None


Args:

      bufSize(int):The size of the buffer to allocate.

Returns:

      typing.Any
        
    """
    pass


def ReadFile(hFile:typing.Any,buffer/bufSize:typing.Any,overlapped:typing.Any=None) -> typing.Any:
    """
    Reads a string from a file


Args:

      hFile(typing.Any):Handle to the file
      buffer/bufSize(typing.Any):Size of the buffer to create for the result, or a buffer to fill with the result. If a buffer object and overlapped is passed, the result is the buffer itself.  If a buffer but no overlapped is passed, the result is a new string object, built from the buffer, but with a length that reflects the data actually read.
      overlapped(typing.Any):An overlapped structureCommentsin a multi-threaded overlapped environment, it is likely to be necessary to pre-allocate the read buffer using the win32file::AllocateReadBuffer method, otherwise the I/O operation may complete before you can assign to the resulting buffer.Return ValueThe result is a tuple of (hr, string/PyOVERLAPPEDReadBuffer), where hr may be 0, ERROR_MORE_DATA or ERROR_IO_PENDING. If the overlapped param is not None, then the result is a PyOVERLAPPEDReadBuffer.  Once the overlapped IO operation has completed, you can convert this to a string (str(object)) [py2k] or (bytes(object)) [py3k] to obtain the data. While the operation is in progress, you can use the slice operations (object[:end]) to obtain the data read so far. You must use the OVERLAPPED API functions to determine how much of the data is valid.

Returns:

      typing.Any:An overlapped structure
Comments

in a multi-threaded overlapped environment, it is likely to be necessary to pre-allocate the read buffer using the win32file::AllocateReadBuffer method, otherwise the I/O operation may complete before you can assign to the resulting buffer.
Return ValueThe result is a tuple of (hr, string/PyOVERLAPPEDReadBuffer), where hr may be 

0, ERROR_MORE_DATA or ERROR_IO_PENDING. 

If the overlapped param is not None, then the result is a PyOVERLAPPEDReadBuffer.  Once the overlapped IO operation 

has completed, you can convert this to a string (str(object)) [py2k] or (bytes(object)) [py3k] to obtain the data. 

While the operation is in progress, you can use the slice operations (object[:end]) to 

obtain the data read so far. 

You must use the OVERLAPPED API functions to determine how much of the data is valid.

        
    """
    pass


def WriteFile(hFile:typing.Any,data:Union[str,typing.Any],ol:typing.Any=None) -> typing.Any:
    """
    Writes a string to a file


Args:

      hFile(typing.Any):Handle to the file
      data(str,typing.Any):The data to write.
      ol(typing.Any):An overlapped structureCommentsIf you use an overlapped buffer, then it is your responsibility to ensure the string object passed remains valid until the operation completes.  If Python garbage collection reclaims the buffer before the win32 API has finished with it, the results are unpredictable.Return ValueThe result is a tuple of (errCode, nBytesWritten).  If errCode is not zero, it will be ERROR_IO_PENDING (ie, it is an overlapped request). Any other error will raise an exception.

Returns:

      typing.Any:An overlapped structure
Comments

If you use an overlapped buffer, then it is your responsibility 

to ensure the string object passed remains valid until the operation 

completes.  If Python garbage collection reclaims the buffer before the 

win32 API has finished with it, the results are unpredictable.
Return ValueThe result is a tuple of (errCode, nBytesWritten).  If errCode is not zero, 

it will be ERROR_IO_PENDING (ie, it is an overlapped request). 

Any other error will raise an exception.

        
    """
    pass


def CloseHandle(handle:typing.Any) -> None:
    """
    Closes an open handle.


Args:

      handle(typing.Any):A previously opened handle.

Returns:

      None
        
    """
    pass


def LockFileEx(hFile:typing.Any,int:typing.Any,int1:typing.Any,int1:typing.Any,ol:typing.Any=None) -> None:
    """
    Locks a file. Wrapper for LockFileEx win32 API.


Args:

      hFile(typing.Any):Handle to the file
      int(typing.Any):Flags that specify exclusive/shared and blocking/non-blocking mode
      int1(typing.Any):low-order part of number of bytes to lock
      int1(typing.Any):high-order part of number of bytes to lock
      ol(typing.Any):An overlapped structure

Returns:

      None
        
    """
    pass


def UnlockFileEx(hFile:typing.Any,int:typing.Any,int1:typing.Any,ol:typing.Any=None) -> None:
    """
    Unlocks a file. Wrapper for UnlockFileEx win32 API.


Args:

      hFile(typing.Any):Handle to the file
      int(typing.Any):low-order part of number of bytes to lock
      int1(typing.Any):high-order part of number of bytes to lock
      ol(typing.Any):An overlapped structure

Returns:

      None
        
    """
    pass


def GetQueuedCompletionStatus(hPort:typing.Any,timeOut:int) -> typing.Any:
    """
    Attempts to dequeue an I/O completion packet from a specified input/output completion port.


Args:

      hPort(typing.Any):The handle to the completion port.
      timeOut(int):Timeout in milli-seconds.CommentsThis method never throws an API error. The result is a tuple of (rc, numberOfBytesTransferred, completionKey, overlapped) If the function succeeds, rc will be set to 0, otherwise it will be set to the win32 error code.

Returns:

      typing.Any
        
    """
    pass


def PostQueuedCompletionStatus(handle:typing.Any,numberOfbytes:int=0,completionKey:int=0,overlapped:typing.Any=None) -> None:
    """
    lets you post an I/O completion packet to an I/O completion port. The I/O completion packet will satisfy an outstanding call to the GetQueuedCompletionStatus function.


Args:

      handle(typing.Any):handle to an I/O completion port
      numberOfbytes(int):value to return via GetQueuedCompletionStatus' first result
      completionKey(int):value to return via GetQueuedCompletionStatus' second result
      overlapped(typing.Any):value to return via GetQueuedCompletionStatus' third resultCommentsNote that if you post overlapped objects, but your post is closed before all pending requests are processed, the overlapped objects (including its 'handle' and 'object' members) will leak. See MS KB article Q192800 for a summary of this.

Returns:

      None
        
    """
    pass


def GetFileType(hFile:typing.Any) -> int:
    """
    Determines the type of a file.


Args:

      hFile(typing.Any):The handle to the file.

Returns:

      int
        
    """
    pass


def GetLogicalDrives() -> int:
    """
    Returns a bitmaks of the logical drives installed.


Args:



Returns:

      int
        
    """
    pass


def GetOverlappedResult(hFile:typing.Any,overlapped:typing.Any,bWait:int) -> int:
    """
    Determines the result of the most recent call with an OVERLAPPED object.


Args:

      hFile(typing.Any):The handle to the pipe or file
      overlapped(typing.Any):The overlapped object to check.
      bWait(int):Indicates if the function should wait for data to become available.CommentsThe result is the number of bytes transferred.  The overlapped object's attributes will be changed during this call.

Returns:

      int
        
    """
    pass


def LockFile(hFile:typing.Any,offsetLow:int,offsetHigh:int,nNumberOfBytesToLockLow:int,nNumberOfBytesToLockHigh:int) -> None:
    """
    Locks a specified file for exclusive access by the calling process.


Args:

      hFile(typing.Any):handle of file to lock
      offsetLow(int):low-order word of lock region offset
      offsetHigh(int):high-order word of lock region offset
      nNumberOfBytesToLockLow(int):low-order word of length to lock
      nNumberOfBytesToLockHigh(int):high-order word of length to lock

Returns:

      None
        
    """
    pass


def MoveFile(existingFileName:typing.Any,newFileName:typing.Any) -> None:
    """
    Renames an existing file or a directory (including all its children).


Args:

      existingFileName(typing.Any):Name of the existing file
      newFileName(typing.Any):New name for the file

Returns:

      None
        
    """
    pass


def MoveFileW(existingFileName:typing.Any,newFileName:typing.Any) -> None:
    """
    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).


Args:

      existingFileName(typing.Any):Name of the existing file
      newFileName(typing.Any):New name for the file

Returns:

      None
        
    """
    pass


def MoveFileEx(existingFileName:typing.Any,newFileName:typing.Any,flags:int) -> None:
    """
    Renames an existing file or a directory (including all its children).


Args:

      existingFileName(typing.Any):Name of the existing file
      newFileName(typing.Any):New name for the file, can be None for delayed delete operation
      flags(int):flag to determine how to move file (win32file.MOVEFILE_*)

Returns:

      None
        
    """
    pass


def MoveFileExW(existingFileName:typing.Any,newFileName:typing.Any,flags:int) -> None:
    """
    Renames an existing file or a directory (including all its children). (NT/2000 Unicode specific version).


Args:

      existingFileName(typing.Any):Name of the existing file
      newFileName(typing.Any):New name for the file, can be None for delayed delete operation
      flags(int):flag to determine how to move file (win32file.MOVEFILE_*)

Returns:

      None
        
    """
    pass


def QueryDosDevice(DeviceName:str) -> str:
    """
    Returns the mapping for a device name, or all device names


Args:

      DeviceName(str):Name of device to query, or None to return all defined devicesReturn ValueReturns a string containing substrings separated by NULLs with 2 terminating NULLs

Returns:

      str:Name of device to query, or None to return all defined devicesReturn ValueReturns a string containing substrings separated by NULLs with 2 terminating NULLs

        
    """
    pass


def ReadDirectoryChangesW(handle:typing.Any,size:int,bWatchSubtree:int,dwNotifyFilter:int,overlapped:typing.Any=None) -> None:
    """
    retrieves information describing the changes occurring within a directory.


Args:

      handle(typing.Any):Handle to the directory to be monitored. This directory must be opened with the FILE_LIST_DIRECTORY access right.
      size(int):Size of the buffer to allocate for the results.
      bWatchSubtree(int):Specifies whether the ReadDirectoryChangesW function will monitor the directory or the directory tree. If TRUE is specified, the function monitors the directory tree rooted at the specified directory. If FALSE is specified, the function monitors only the directory specified by the hDirectory parameter.
      dwNotifyFilter(int):Specifies filter criteria the function checks to determine if the wait operation has completed. This parameter can be one or more of the FILE_NOTIFY_CHANGE_* values.
      overlapped(typing.Any):An overlapped object.  The directory must also be opened with FILE_FLAG_OVERLAPPED.CommentsIf you pass an overlapped object, you almost certainly must pass a buffer object for the asynchronous results - failure to do so may crash Python as the asynchronous result writes to invalid memory.The FILE_NOTIFY_INFORMATION structure used by this function is variable length, depending on the length of the filename. The size of the buffer must be at least 6 bytes long + the length of the filenames returned.  The number of notifications that can be returned for a given buffer size depends on the filename lengths.Return ValueIf a buffer size is passed, the result is a list of (action, filename)If a buffer is passed, the result is None - you must use the overlapped object to determine when the information is available and how much is valid. The buffer can then be passed to win32file::FILE_NOTIFY_INFORMATION

Returns:

      None:An overlapped object.  The directory must also be opened with FILE_FLAG_OVERLAPPED.
Comments

If you pass an overlapped object, you almost certainly 

must pass a buffer object for the asynchronous results - failure 

to do so may crash Python as the asynchronous result writes to 

invalid memory.

The FILE_NOTIFY_INFORMATION structure used by this function 

is variable length, depending on the length of the filename. 

The size of the buffer must be at least 6 bytes long + the length 

of the filenames returned.  The number of notifications that can be 

returned for a given buffer size depends on the filename lengths.
Return ValueIf a buffer size is passed, the result is a list of (action, filename)



If a buffer is passed, the result is None - you must use the overlapped 

object to determine when the information is available and how much is valid. 

The buffer can then be passed to win32file::FILE_NOTIFY_INFORMATION

        
    """
    pass


def FILE_NOTIFY_INFORMATION(buffer:str,size:int) -> typing.Any:
    """
    Decodes a PyFILE_NOTIFY_INFORMATION buffer.


Args:

      buffer(str):The buffer to decode.
      size(int):The number of bytes to refer to.  Generally this will be smaller than the size of the buffer (and certainly never greater!)CommentsSee win32file::ReadDirectoryChangesW for more information.

Returns:

      typing.Any
        
    """
    pass


def SetCurrentDirectory(lpPathName:Union[str,typing.Any]) -> None:
    """
    Sets the current directory.


Args:

      lpPathName(str,typing.Any):Name of the path to set current.

Returns:

      None
        
    """
    pass


def SetEndOfFile(hFile:typing.Any) -> None:
    """
    Moves the end-of-file (EOF) position for the specified file to the current position of the file pointer.


Args:

      hFile(typing.Any):handle of file whose EOF is to be set

Returns:

      None
        
    """
    pass


def SetFileApisToANSI() -> None:
    """
    Causes a set of Win32 file functions to use the ANSI character set code page. This function is useful for 8-bit console input and output operations.


Args:



Returns:

      None
        
    """
    pass


def SetFileApisToOEM() -> None:
    """
    Causes a set of Win32 file functions to use the OEM character set code page. This function is useful for 8-bit console input and output operations.


Args:



Returns:

      None
        
    """
    pass


def SetFileAttributes(filename:typing.Any,newAttributes:int) -> None:
    """
    Changes a file's attributes.


Args:

      filename(typing.Any):filename
      newAttributes(int):attributes to set

Returns:

      None
        
    """
    pass


def SetFilePointer(handle:typing.Any,offset:typing.Any,moveMethod:int) -> None:
    """
    Moves the file pointer of an open file.


Args:

      handle(typing.Any):The file to perform the operation on.
      offset(typing.Any):Offset to move the file pointer.
      moveMethod(int):Starting point for the file pointer move. This parameter can be one of the following values.ValueMeaningFILE_BEGINThe starting point is zero or the beginning of the file.FILE_CURRENTThe starting point is the current value of the file pointer.FILE_ENDThe starting point is the current end-of-file position.

Returns:

      None
        
    """
    pass


def SetVolumeLabel(rootPathName:typing.Any,volumeName:typing.Any) -> None:
    """
    Sets a volume label for a disk drive.


Args:

      rootPathName(typing.Any):address of name of root directory for volume
      volumeName(typing.Any):name for the volume

Returns:

      None
        
    """
    pass


def UnlockFile(hFile:typing.Any,offsetLow:int,offsetHigh:int,nNumberOfBytesToUnlockLow:int,nNumberOfBytesToUnlockHigh:int) -> None:
    """
    None


Args:

      hFile(typing.Any):handle of file to unlock
      offsetLow(int):low-order word of lock region offset
      offsetHigh(int):high-order word of lock region offset
      nNumberOfBytesToUnlockLow(int):low-order word of length to unlock
      nNumberOfBytesToUnlockHigh(int):high-order word of length to unlock

Returns:

      None
        
    """
    pass


def _get_osfhandle(fd:int) -> typing.Any:
    """
    Gets operating-system file handle associated with existing stream


Args:

      fd(int):File descriptor as returned by file.fileno()

Returns:

      typing.Any
        
    """
    pass


def _open_osfhandle(osfhandle:typing.Any,flags:int) -> int:
    """
    Associates a C run-time file handle with a existing operating-system file handle.


Args:

      osfhandle(typing.Any):An open file handle
      flags(int):O_APPEND,O_RDONLY, or O_TEXT

Returns:

      int
        
    """
    pass


def _setmaxstdio(newmax:int) -> int:
    """
    Set the maximum allowed number of open stdio handles


Args:

      newmax(int):Maximum number of open stdio streams, 2048 maxReturn ValueReturns the number that was set, or -1 on failure.

Returns:

      int:Maximum number of open stdio streams, 2048 maxReturn ValueReturns the number that was set, or -1 on failure.

        
    """
    pass


def _getmaxstdio() -> int:
    """
    Returns the maximum number of CRT io streams.


Args:



Returns:

      int
        
    """
    pass


def TransmitFile(Socket:typing.Any,File:typing.Any,NumberOfBytesToWrite:int,NumberOfBytesPerSend:int,Overlapped:typing.Any,Flags:int,Head:typing.Any=None,Tail:typing.Any=None) -> None:
    """
    Transmits a file over a socket 

TransmitFile(sock, filehandle, bytes_to_write, bytes_per_send, overlap, flags [, (prepend_buf, postpend_buf)])


Args:

      Socket(typing.Any):Socket that will be used to send the file
      File(typing.Any):Handle to the file
      NumberOfBytesToWrite(int):The number of bytes in the file to transmit, use 0 for entire file.
      NumberOfBytesPerSend(int):The size, in bytes, of each block of data sent in each send operation.
      Overlapped(typing.Any):An overlapped structure, can be None.
      Flags(int):A set of flags used to modify the behavior of the TransmitFile function call. (win32file.TF_*)
      Head(typing.Any):Buffer to send on the socket before the file
      Tail(typing.Any):Buffer to send on the socket after the fileReturn ValueReturns 0 on completion, or ERROR_IO_PENDING if an overlapped operation has been queued

Returns:

      None:Buffer to send on the socket after the file
Return ValueReturns 0 on completion, or ERROR_IO_PENDING if an overlapped operation has been queued

        
    """
    pass


def ConnectEx(s:typing.Any,name:tuple,Overlapped:typing.Any,SendBuffer:typing.Any=None) -> typing.Any:
    """
    Version of connect that uses Overlapped I/O 

ConnectEx(sock, (addr, port), buf, overlap)


Args:

      s(typing.Any):A bound, unconnected socket that will be used to connect
      name(tuple):Address to connect to (host, port)
      Overlapped(typing.Any):An overlapped structure
      SendBuffer(typing.Any):Buffer to send on the socket after connectReturn ValueReturns the completion code and number of bytes sent. The completion code will be 0 for a completed operation, or ERROR_IO_PENDING for a pending overlapped operation.If the platform does not support ConnectEx (eg, Windows 2000), an exception will be thrown indicating the WSAIoctl function (which is used to fetch the function pointer) failed with error code WSAEINVAL (10022).

Returns:

      typing.Any:Buffer to send on the socket after connect
Return ValueReturns the completion code and number of bytes sent. 

The completion code will be 0 for a completed operation, or ERROR_IO_PENDING for a pending overlapped operation.



If the platform does not support ConnectEx (eg, Windows 2000), an 

exception will be thrown indicating the WSAIoctl function (which is used to 

fetch the function pointer) failed with error code WSAEINVAL (10022).

        
    """
    pass


def AcceptEx(sListening:typing.Any,sAccepting:typing.Any,buffer:typing.Any,ol:typing.Any) -> None:
    """
    Version of accept that uses Overlapped I/O


Args:

      sListening(typing.Any):Socket that had listen() called on.
      sAccepting(typing.Any):Socket that will be used as the incoming connection.
      buffer(typing.Any):Buffer to read incoming data and connection point information into. This buffer MUST be big enough to recieve your connection endpoints... AF_INET sockets need to be at least 64 bytes. The correct minimum of the buffer is determined by the protocol family that the listening socket is using.
      ol(typing.Any):An overlapped structureCommentsIn order to make sure the connection has been accepted, either use the hEvent in PyOVERLAPPED, GetOverlappedResult, or GetQueuedCompletionStatus.To use this with I/O completion ports, don't forget to attach sAccepting to your completion port.Pass a buffer of exactly the size returned by win32file::CalculateSocketEndPointSize to have AcceptEx return without reading any bytes from the remote connection.ExampleTo have sAccepting inherit the properties of sListening, you need to do the following after a connection is successfully acceptedimport structsAccepting.setsockopt(socket.SOL_SOCKET, win32file.SO_UPDATE_ACCEPT_CONTEXT, struct.pack("I", sListening.fileno()))Return ValueThe result is 0 or ERROR_IO_PENDING.  All other values will raise win32file.error.  Specifically: if the win32 function returns FALSE, WSAGetLastError() is checked for ERROR_IO_PENDING.

Returns:

      None:An overlapped structureComments

In order to make sure the connection has been accepted, either use the hEvent in PyOVERLAPPED, GetOverlappedResult, or GetQueuedCompletionStatus.

To use this with I/O completion ports, don't forget to attach sAccepting to your completion port.

Pass a buffer of exactly the size returned by win32file::CalculateSocketEndPointSize 

to have AcceptEx return without reading any bytes from the remote connection.
ExampleTo have sAccepting inherit the properties of sListening, you need to do the following after a connection is successfully accepted
import struct

sAccepting.setsockopt(socket.SOL_SOCKET, win32file.SO_UPDATE_ACCEPT_CONTEXT, struct.pack("I", sListening.fileno()))


Return ValueThe result is 0 or ERROR_IO_PENDING.  All other values will raise 

win32file.error.  Specifically: if the win32 function returns FALSE, 

WSAGetLastError() is checked for ERROR_IO_PENDING.

        
    """
    pass


def CalculateSocketEndPointSize(socket:typing.Any) -> int:
    """
    Calculate how many bytes are needed for the connection endpoints data for a socket.


Args:

      socket(typing.Any):The socket for which to determine the size.CommentsThis function allows you to determine the minumum buffer size which can be passed to win32file::AcceptEx

Returns:

      int
        
    """
    pass


def GetAcceptExSockaddrs(sAccepting:typing.Any,buffer:typing.Any) -> typing.Any:
    """
    Parses the connection endpoints from the buffer passed into AcceptEx


Args:

      sAccepting(typing.Any):Socket that was passed into the sAccepting parameter of AcceptEx
      buffer(typing.Any):Buffer you passed into AcceptExCommentsLocalSockAddr and RemoteSockAddr are ("xx.xx.xx.xx", port#) if iFamily == AF_INETotherwise LocalSockAddr and RemoteSockAddr are just binary stringsand they should be unpacked with the struct module.

Returns:

      typing.Any
        
    """
    pass


def WSAEventSelect(socket:typing.Any,hEvent:typing.Any,networkEvents:int) -> None:
    """
    Specifies an event object to be associated with the supplied set of FD_XXXX network events.


Args:

      socket(typing.Any):socket to attach to the event
      hEvent(typing.Any):Event handle for the socket to become attached to.
      networkEvents(int):A bitmask of network events that will cause hEvent to be signaled. e.g. (FD_CLOSE | FD_READ)

Returns:

      None
        
    """
    pass


def WSAEnumNetworkEvents(s:typing.Any,hEvent:typing.Any) -> dict:
    """
    Return network events that caused the event associated with the socket to be signaled.


Args:

      s(typing.Any):Socket to check for netork events, previously registered for network event notification with WSAEventSelect.
      hEvent(typing.Any):Optional handle to the event associated with socket s in the last call to WSAEventSelect. If specified, the event will be reset.Return ValueA dictionary mapping network events that occured for the specified socket since the last call to this function (e.g. FD_READ, FD_WRITE) to their associated error code, or 0 if the event occured without an error. The events returned are a subset of events previously registered for this socket with WSAEventSelect.

Returns:

      dict:Optional handle to the event associated with socket s in the last call to WSAEventSelect. If specified, the event will be reset.Return ValueA dictionary mapping network events that occured for the specified socket since the last call to this function (e.g. FD_READ, FD_WRITE) to their associated error code, or 0 if the event occured without an error. The events returned are a subset of events previously registered for this socket with WSAEventSelect.

        
    """
    pass


def WSAAsyncSelect(socket:typing.Any,hwnd:typing.Any,int:typing.Any,networkEvents:int) -> None:
    """
    Request windows message notification for the supplied set of FD_XXXX network events.


Args:

      socket(typing.Any):socket to attach to the event
      hwnd(typing.Any):Window handle for the socket to become attached to.
      int(typing.Any):Window message that will be posted.
      networkEvents(int):A bitmask of network events that will cause wMsg to be posted. e.g. (FD_CLOSE | FD_READ)

Returns:

      None
        
    """
    pass


def WSASend(s:typing.Any,buffer:Union[str,typing.Any],ol:typing.Any,dwFlags:int) -> typing.Any:
    """
    Winsock send() equivalent function for Overlapped I/O.


Args:

      s(typing.Any):Socket to send data on.
      buffer(str,typing.Any):Buffer to send data from.
      ol(typing.Any):An overlapped structure
      dwFlags(int):Optional send flags.

Returns:

      typing.Any
        
    """
    pass


def WSARecv(s:typing.Any,buffer:typing.Any,ol:typing.Any,dwFlags:int) -> typing.Any:
    """
    Winsock recv() equivalent function for Overlapped I/O.


Args:

      s(typing.Any):Socket to send data on.
      buffer(typing.Any):Buffer to send data from.
      ol(typing.Any):An overlapped structure
      dwFlags(int):Optional reception flags.

Returns:

      typing.Any
        
    """
    pass


def BuildCommDCB(def:str,dcb:typing.Any) -> typing.Any:
    """
    Fills the specified DCB structure with values specified in a device-control string. The device-control string uses the syntax of the mode command


Args:

      def(str):device-control string
      dcb(typing.Any):The device-control block

Returns:

      typing.Any
        
    """
    pass


def ClearCommError(PyHANDLE:typing.Any) -> typing.Any:
    """
    retrieves information about a communications error and reports the current status of a communications device.


Args:

      PyHANDLE(typing.Any):A handle to the device.

Returns:

      typing.Any
        
    """
    pass


def EscapeCommFunction(handle:typing.Any) -> None:
    """
    directs a specified communications device to perform an extended function.


Args:

      handle(typing.Any):The handle to the communications device.ValueMeaningCLRDTRClears the DTR (data-terminal-ready) signal.CLRRTSClears the RTS (request-to-send) signal.SETDTRSends the DTR (data-terminal-ready) signal.SETRTSSends the RTS (request-to-send) signal.SETXOFFCauses transmission to act as if an XOFF character has been received.SETXONCauses transmission to act as if an XON character has been received.SETBREAKSuspends character transmission and places the transmission line in a break state until the ClearCommBreak function is called (or EscapeCommFunction is called with the CLRBREAK extended function code). The SETBREAK extended function code is identical to the SetCommBreak function. Note that this extended function does not flush data that has not been transmitted.CLRBREAKRestores character transmission and places the transmission line in a nonbreak state. The CLRBREAK extended function code is identical to the ClearCommBreak function.

Returns:

      None
        
    """
    pass


def GetCommState(handle:typing.Any) -> typing.Any:
    """
    Returns a device-control block (a DCB structure) with the current control settings for a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      typing.Any
        
    """
    pass


def SetCommState(handle:typing.Any,dcb:typing.Any) -> None:
    """
    Configures a communications device according to the specifications in a device-control block. 

The function reinitializes all hardware and control settings, but it does not empty output or input queues.


Args:

      handle(typing.Any):The handle to the communications device.
      dcb(typing.Any):The control settings.

Returns:

      None
        
    """
    pass


def ClearCommBreak(handle:typing.Any) -> None:
    """
    Restores character transmission for a specified communications device and places the transmission line in a nonbreak state


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      None
        
    """
    pass


def GetCommMask(handle:typing.Any) -> int:
    """
    Retrieves the value of the event mask for a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      int
        
    """
    pass


def SetCommMask(handle:typing.Any,val:int) -> int:
    """
    Sets the value of the event mask for a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.
      val(int):The new mask value.

Returns:

      int
        
    """
    pass


def GetCommModemStatus(handle:typing.Any) -> int:
    """
    Retrieves modem control-register values.


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      int
        
    """
    pass


def GetCommTimeouts(handle:typing.Any) -> typing.Any:
    """
    Retrieves the time-out parameters for all read and write operations on a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      typing.Any
        
    """
    pass


def SetCommTimeouts(handle:typing.Any,val:typing.Any) -> int:
    """
    Sets the time-out parameters for all read and write operations on a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.
      val(typing.Any):The new time-out parameters.

Returns:

      int
        
    """
    pass


def PurgeComm(handle:typing.Any,action:int) -> None:
    """
    Discards all characters from the output or input buffer of a specified communications resource. It can also terminate pending read or write operations on the resource.


Args:

      handle(typing.Any):The handle to the communications device.
      action(int):The action to perform.  This parameter can be one or more of the following values.ValueMeaningPURGE_TXABORTTerminates all outstanding overlapped write operations and returns immediately, even if the write operations have not been completed.PURGE_RXABORTTerminates all outstanding overlapped read operations and returns immediately, even if the read operations have not been completed.PURGE_TXCLEARClears the output buffer (if the device driver has one).PURGE_RXCLEARClears the input buffer (if the device driver has one).

Returns:

      None
        
    """
    pass


def SetCommBreak(handle:typing.Any) -> None:
    """
    None


Args:

      handle(typing.Any):The handle to the communications device.

Returns:

      None
        
    """
    pass


def SetupComm(handle:typing.Any,dwInQueue:int,dwOutQueue:int) -> None:
    """
    Initializes the communications parameters for a specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.
      dwInQueue(int):Specifies the recommended size, in bytes, of the device's internal input buffer.
      dwOutQueue(int):Specifies the recommended size, in bytes, of the device's internal output buffer.

Returns:

      None
        
    """
    pass


def TransmitCommChar(handle:typing.Any,cChar:typing.Any) -> None:
    """
    Transmits a specified character ahead of any pending data in the output buffer of the specified communications device.


Args:

      handle(typing.Any):The handle to the communications device.
      cChar(typing.Any):The character to transmit.CommentsThe TransmitCommChar function is useful for sending an interrupt character (such as a CTRL+C) to a host system. If the device is not transmitting, TransmitCommChar cannot be called repeatedly. Once TransmitCommChar places a character in the output buffer, the character must be transmitted before the function can be called again. If the previous character has not yet been sent, TransmitCommChar returns an error.

Returns:

      None
        
    """
    pass


def WaitCommEvent(handle:typing.Any,overlapped:typing.Any) -> None:
    """
    Waits for an event to occur for a specified communications device. The set of events that are monitored by this function is contained in the event mask associated with the device handle.


Args:

      handle(typing.Any):The handle to the communications device.
      overlapped(typing.Any):This structure is required if hFile was opened with FILE_FLAG_OVERLAPPED. If hFile was opened with FILE_FLAG_OVERLAPPED, the lpOverlapped parameter must not be NULL. It must point to a valid OVERLAPPED structure. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is NULL, the function can incorrectly report that the operation is complete. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is not NULL, WaitCommEvent is performed as an overlapped operation. In this case, the OVERLAPPED structure must contain a handle to a manual-reset event object (created by using the CreateEvent function). If hFile was not opened with FILE_FLAG_OVERLAPPED, WaitCommEvent does not return until one of the specified events or an error occurs.CommentsIf an overlapped structure is passed, then the PyOVERLAPPED::dword address is passed to the Win32 API as the mask.  This means that once the overlapped operation has completed, this dword attribute can be used to determine the type of event that occurred.Return ValueThe result is a tuple of (rc, mask_val), where rc is zero for success, or the result of calling GetLastError() otherwise.  The mask_val is the new mask value once the function has returned, but if an Overlapped object is passed, this value will generally be meaningless.  See the comments for more details.

Returns:

      None:This structure is required if hFile was opened with FILE_FLAG_OVERLAPPED. 

If hFile was opened with FILE_FLAG_OVERLAPPED, the lpOverlapped parameter must not be NULL. It must point to a valid OVERLAPPED structure. If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is NULL, the function can incorrectly report that the operation is complete. 

If hFile was opened with FILE_FLAG_OVERLAPPED and lpOverlapped is not NULL, WaitCommEvent is performed as an overlapped operation. In this case, the OVERLAPPED structure must contain a handle to a manual-reset event object (created by using the CreateEvent function). 

If hFile was not opened with FILE_FLAG_OVERLAPPED, WaitCommEvent does not return until one of the specified events or an error occurs.Comments

If an overlapped structure is passed, then the PyOVERLAPPED::dword



 

address is passed to the Win32 API as the mask.  This means that once the 

overlapped operation has completed, this dword attribute can be used to 

determine the type of event that occurred.
Return ValueThe result is a tuple of (rc, mask_val), where rc is zero for success, or 

the result of calling GetLastError() otherwise.  The mask_val is the new mask value 

once the function has returned, but if an Overlapped object is passed, this value 

will generally be meaningless.  See the comments for more details.

        
    """
    pass


def SetVolumeMountPoint(VolumeMountPoint:typing.Any,VolumeName:typing.Any) -> str:
    """
    Mounts the specified volume at the specified volume mount point.


Args:

      VolumeMountPoint(typing.Any):The mount point - must be an existing empty directory on an NTFS volume
      VolumeName(typing.Any):The volume to	mount thereCommentsAccepts keyword args.Note that both	parameters must	have trailing backslashes.This method exists only on Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.ExampleUsageSetVolumeMountPoint('h:\\tmp\\','c:\\')Return ValueThe result is	the	GUID of	the	volume mounted,	as a string.

Returns:

      str:The volume to	mount thereComments

Accepts keyword args.

Note that both	parameters must	have trailing backslashes.

This method exists only on Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.
ExampleUsage
SetVolumeMountPoint('h:\\tmp\\','c:\\')


Return ValueThe result is	the	GUID of	the	volume mounted,	as a string.

        
    """
    pass


def DeleteVolumeMountPoint(VolumeMountPoint:typing.Any) -> None:
    """
    Unmounts the volume from the specified volume mount point.


Args:

      VolumeMountPoint(typing.Any):The mount point to delete - must have a trailing backslash.CommentsAccepts keyword args.Throws	an error if	it is not a	valid mount	point, returns None	on success. Use carefully - will	remove drive letter	assignment if no directory specifiedThis method requires Windows 2000 or later.  On earlier platforms, NotImplementedError will be raised.ExampleUsageDeleteVolumeMountPoint('h:\\tmp\\')

Returns:

      None
        
    """
    pass


def GetVolumeNameForVolumeMountPoint(VolumeMountPoint:typing.Any) -> str:
    """
    Returns unique volume name.


Args:

      VolumeMountPoint(typing.Any):Volume mount point or root drive - trailing backslash requiredCommentsRequires Win2K or later.Accepts keyword args.

Returns:

      str
        
    """
    pass


def GetVolumePathName(FileName:typing.Any,BufferLength:int=0) -> str:
    """
    Returns volume mount point for a path


Args:

      FileName(typing.Any):File/dir for which to return volume mount point
      BufferLength(int):Optional parm to allocate extra space for returned stringCommentsApi gives no indication of how much memory is needed, so function assumes returned path will not be longer that length of input path + 1. Use GetFullPathName first for relative paths, or GetLongPathName for 8.3 paths. Optional second parm can also be used to override the buffer size for returned pathAccepts keyword args.

Returns:

      str
        
    """
    pass


def GetVolumePathNamesForVolumeName(VolumeName:typing.Any) -> typing.Any:
    """
    Returns mounted paths for a volume


Args:

      VolumeName(typing.Any):Name of a volume as returned by win32file::GetVolumeNameForVolumeMountPointCommentsRequires WinXP or laterAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def CreateHardLink(FileName:typing.Any,ExistingFileName:typing.Any,SecurityAttributes:typing.Any=None,Transaction:typing.Any=None) -> None:
    """
    Establishes an NTFS hard link between an existing file and a new file.


Args:

      FileName(typing.Any):The name of the new directory entry to be created.
      ExistingFileName(typing.Any):The name of the existing file to which the new link will point.
      SecurityAttributes(typing.Any):Optional SECURITY_ATTRIBUTES object. MSDN describes this parameter as reserved, so use only None
      Transaction(typing.Any):Handle to a transaction, as returned by win32transaction::CreateTransactionCommentsAn NTFS hard link is similar to a POSIX hard link. This function creates a second directory entry for an existing file, can be different name in same directory or any name in a different directory. Both file paths must be on the same NTFS volume.To remove the link, simply delete it and the original file will still remain.This method exists on Windows 2000 and later.  Otherwise NotImplementedError will be raised.Accepts keyword args.If the Transaction parameter is specified, CreateHardLinkTransacted will be called (requires Vista or later)ExampleUsageCreateHardLink('h:\\dir\\newfilename.txt','h:\\otherdir\\existingfile.txt')

Returns:

      None
        
    """
    pass


def CreateSymbolicLink(SymlinkFileName:typing.Any,TargetFileName:typing.Any,Flags:int=0,Transaction:typing.Any=None) -> None:
    """
    Creates a symbolic link (reparse point)


Args:

      SymlinkFileName(typing.Any):Path of the symbolic link to be created
      TargetFileName(typing.Any):The name of file to which link will point
      Flags(int):SYMBOLIC_LINK_FLAG_DIRECTORY and SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE are the only defined flags
      Transaction(typing.Any):Handle to a transaction, as returned by win32transaction::CreateTransactionCommentsThis method only exists on Vista and later.Accepts keyword args.Requires SeCreateSymbolicLink priv.If the Transaction parameter is passed in, CreateSymbolicLinkTransacted will be called

Returns:

      None
        
    """
    pass


def EncryptFile(filename:Union[str,typing.Any]) -> None:
    """
    Encrypts specified file (requires Win2k or higher and NTFS)


Args:

      filename(str,typing.Any):File to encrypt

Returns:

      None
        
    """
    pass


def DecryptFile(filename:Union[str,typing.Any]) -> None:
    """
    Decrypts specified file (requires Win2k or higher and NTFS)


Args:

      filename(str,typing.Any):File to decrypt

Returns:

      None
        
    """
    pass


def EncryptionDisable(DirName:Union[str,typing.Any],Disable:typing.Any) -> None:
    """
    Enables/disables encryption for a directory (requires Win2k or higher and NTFS)


Args:

      DirName(str,typing.Any):Directory to enable or disable
      Disable(typing.Any):Set to False to enable encryption

Returns:

      None
        
    """
    pass


def FileEncryptionStatus(FileName:Union[str,typing.Any]) -> int:
    """
    retrieves the encryption status of the specified file.


Args:

      FileName(str,typing.Any):file to queryCommentsRequires Windows 2000 or higher.Return ValueThe result is documented as being one of FILE_ENCRYPTABLE, FILE_IS_ENCRYPTED, FILE_SYSTEM_ATTR, FILE_ROOT_DIR, FILE_SYSTEM_DIR, FILE_UNKNOWN, FILE_SYSTEM_NOT_SUPPORT, FILE_USER_DISALLOWED, or FILE_READ_ONLY

Returns:

      int:file to queryComments

Requires Windows 2000 or higher.
Return ValueThe result is documented as being one of FILE_ENCRYPTABLE, 

FILE_IS_ENCRYPTED, FILE_SYSTEM_ATTR, FILE_ROOT_DIR, FILE_SYSTEM_DIR, 

FILE_UNKNOWN, FILE_SYSTEM_NOT_SUPPORT, FILE_USER_DISALLOWED, 

or FILE_READ_ONLY

        
    """
    pass


def QueryUsersOnEncryptedFile(FileName:Union[str,typing.Any]) -> typing.Any:
    """
    Returns list of users for an encrypted file as tuples of (SID, certificate hash blob, display info)


Args:

      FileName(str,typing.Any):file to query

Returns:

      typing.Any
        
    """
    pass


def QueryRecoveryAgentsOnEncryptedFile(FileName:Union[str,typing.Any]) -> typing.Any:
    """
    Lists recovery agents for file as a tuple of tuples.


Args:

      FileName(str,typing.Any):file to queryReturn ValueThe result is a tuple of tuples - ((SID, certificate hash blob, display info),....)

Returns:

      typing.Any:file to queryReturn ValueThe result is a tuple of tuples - ((SID, certificate hash blob, display info),....)

        
    """
    pass


def RemoveUsersFromEncryptedFile(FileName:Union[str,typing.Any],pHashes:typing.Any) -> None:
    """
    Removes specified certificates from file - if certificate is not found, it is ignored


Args:

      FileName(str,typing.Any):File from which to remove users
      pHashes(typing.Any):Sequence representing an ENCRYPTION_CERTIFICATE_HASH_LIST structure, as returned by QueryUsersOnEncryptedFile

Returns:

      None
        
    """
    pass


def AddUsersToEncryptedFile(FileName:Union[str,typing.Any],pUsers:typing.Any) -> None:
    """
    Allows user identified by SID and EFS certificate access to decrypt specified file


Args:

      FileName(str,typing.Any):File that additional users will be allowed to decrypt
      pUsers(typing.Any):Sequence representing ENCRYPTION_CERTIFICATE_LIST - elements are sequences consisting of users' Sid, encoded EFS certficate (user must export a .cer to obtain this data), and encoding type (usually 1 for X509_ASN_ENCODING)

Returns:

      None
        
    """
    pass


def DuplicateEncryptionInfoFile(SrcFileName:typing.Any,DstFileName:typing.Any,CreationDisposition:int,Attributes:int,SecurityAttributes:typing.Any=None) -> None:
    """
    Duplicates EFS encryption from one file to another


Args:

      SrcFileName(typing.Any):Encrypted file to read EFS metadata from
      DstFileName(typing.Any):File to be encrypted using EFS data from source file
      CreationDisposition(int):Specifies whether an existing file should be overwritten (CREATE_NEW or CREATE_ALWAYS)
      Attributes(int):File attributes
      SecurityAttributes(typing.Any):Specifies security for destination fileCommentsRequires Windows XP or laterAccepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def BackupRead(hFile:typing.Any,NumberOfBytesToRead:int,Buffer:typing.Any,bAbort:int,bProcessSecurity:int,lpContext:int) -> typing.Any:
    """
    Reads streams of data from a file


Args:

      hFile(typing.Any):File handle opened by CreateFile
      NumberOfBytesToRead(int):Number of bytes to be read from file
      Buffer(typing.Any):Writeable buffer object that receives data read
      bAbort(int):If true, ends read operation and frees backup context
      bProcessSecurity(int):Indicates whether file's ACL stream should be read
      lpContext(int):Pass 0 on first call, then pass back value returned from last call thereafterCommentsReturns number of bytes read, data buffer, and context pointer for next operation If Buffer is None, a new buffer will be created of size NbrOfBytesToRead that can be passed back in subsequent calls

Returns:

      typing.Any
        
    """
    pass


def BackupSeek(hFile:typing.Any,NumberOfBytesToSeek:typing.Any,lpContext:int) -> typing.Any:
    """
    Seeks forward in a file stream


Args:

      hFile(typing.Any):File handle used by a BackupRead operation
      NumberOfBytesToSeek(typing.Any):Number of bytes to move forward in current stream
      lpContext(int):Context pointer returned from a BackupRead operationCommentsFunction will only seek to end of current stream, used to seek past bad data or find beginning position for read of next stream Returns number of bytes actually moved

Returns:

      typing.Any
        
    """
    pass


def BackupWrite(hFile:typing.Any,NumberOfBytesToWrite:int,Buffer:str,bAbort:int,bProcessSecurity:int,lpContext:int) -> typing.Any:
    """
    Restores file data


Args:

      hFile(typing.Any):File handle opened by CreateFile
      NumberOfBytesToWrite(int):Length of data to be written to file
      Buffer(str):A string or buffer object that contains the data to be written
      bAbort(int):If true, ends write operation and frees backup context
      bProcessSecurity(int):Indicates whether ACL's should be restored
      lpContext(int):Pass 0 on first call, then pass back value returned from last call thereafterCommentsReturns number of bytes written and context pointer for next operation

Returns:

      typing.Any
        
    """
    pass


def SetFileShortName(hFile:typing.Any,ShortName:typing.Any) -> None:
    """
    Set the 8.3 name of a file


Args:

      hFile(typing.Any):Handle to a file or directory
      ShortName(typing.Any):The 8.3 name to be applied to the fileCommentsThis function is only available on WinXP and laterFile handle must be opened with FILE_FLAG_BACKUP_SEMANTICS, and SE_RESTORE_NAME privilege must be enabled

Returns:

      None
        
    """
    pass


def CopyFileEx(ExistingFileName:typing.Any,NewFileName:typing.Any,ProgressRoutine:typing.Any=None,Data:typing.Any=None,Cancel:typing.Any=False,CopyFlags:int=0,Transaction:typing.Any=None) -> None:
    """
    Restartable file copy with optional progress routine


Args:

      ExistingFileName(typing.Any):File to be copied
      NewFileName(typing.Any):Place to which it will be copied
      ProgressRoutine(typing.Any):A python function that receives progress updates, can be None
      Data(typing.Any):An arbitrary object to be passed to the callback function
      Cancel(typing.Any):Pass True to cancel a restartable copy that was previously interrupted
      CopyFlags(int):Combination of COPY_FILE_* flags
      Transaction(typing.Any):Handle to a transaction as returned by win32transaction::CreateTransactionCommentsAccepts keyword args.On Vista and later, the Transaction arg can be passed to invoke CopyFileTransactedWin32 API References

Returns:

      None
        
    """
    pass


def MoveFileWithProgress(ExistingFileName:typing.Any,NewFileName:typing.Any,ProgressRoutine:typing.Any=None,Data:typing.Any=None,Flags:int=0,Transaction:typing.Any=None) -> None:
    """
    Moves a file, and reports progress to a callback function


Args:

      ExistingFileName(typing.Any):File or directory to be moved
      NewFileName(typing.Any):Destination, can be None if flags contain MOVEFILE_DELAY_UNTIL_REBOOT
      ProgressRoutine(typing.Any):A python function that receives progress updates, can be None
      Data(typing.Any):An arbitrary object to be passed to the callback function
      Flags(int):Combination of MOVEFILE_* flags
      Transaction(typing.Any):Handle to a transaction (optional).  See win32transaction::CreateTransaction.CommentsOnly available on Windows 2000 or laterAccepts keyword arguments.On Vista and later, the Transaction arg can be passed to invoke MoveFileTransacted

Returns:

      None
        
    """
    pass


def ReplaceFile(ReplacedFileName:typing.Any,ReplacementFileName:typing.Any,BackupFileName:typing.Any=None,ReplaceFlags:int=0,Exclude:None=None,Reserved:None=None) -> None:
    """
    Replaces one file with another


Args:

      ReplacedFileName(typing.Any):File to be replaced
      ReplacementFileName(typing.Any):File that will replace it
      BackupFileName(typing.Any):Place at which to create a backup of the replaced file, can be None
      ReplaceFlags(int):Combination of REPLACEFILE_* flags
      Exclude(None):Reserved, use None if passed in
      Reserved(None):Reserved, use None if passed inCommentsOnly available on Windows 2000 or later

Returns:

      None
        
    """
    pass


def OpenEncryptedFileRaw(FileName:typing.Any,Flags:int) -> typing.Any:
    """
    Initiates a backup or restore operation on an encrypted file


Args:

      FileName(typing.Any):Name of file on which to operate
      Flags(int):CREATE_FOR_IMPORT, CREATE_FOR_DIR, OVERWRITE_HIDDEN, or 0 for exportCommentsOnly available on Windows 2000 or laterReturn ValueReturns a PyCObject containing an operation context that can be passed to win32file::ReadEncryptedFileRaw or win32file::WriteEncryptedFileRaw.  Context must be destroyed using win32file::CloseEncryptedFileRaw.

Returns:

      typing.Any:CREATE_FOR_IMPORT, CREATE_FOR_DIR, OVERWRITE_HIDDEN, or 0 for exportComments

Only available on Windows 2000 or later
Return ValueReturns a PyCObject containing an operation context that can be passed to 

win32file::ReadEncryptedFileRaw or win32file::WriteEncryptedFileRaw.  Context must be 

destroyed using win32file::CloseEncryptedFileRaw.

        
    """
    pass


def ReadEncryptedFileRaw(ExportCallback:typing.Any,CallbackContext:typing.Any,Context:typing.Any) -> None:
    """
    Reads the encrypted bytes of a file for backup and restore purposes


Args:

      ExportCallback(typing.Any):Python function that receives chunks of data as it is read
      CallbackContext(typing.Any):Arbitrary Python object to be passed to callback function
      Context(typing.Any):Context object returned from win32file::OpenEncryptedFileRawCommentsOnly available on Windows 2000 or later

Returns:

      None
        
    """
    pass


def WriteEncryptedFileRaw(ImportCallback:typing.Any,CallbackContext:typing.Any,Context:typing.Any) -> None:
    """
    Writes raw bytes to an encrypted file


Args:

      ImportCallback(typing.Any):Python function that supplies data to be written
      CallbackContext(typing.Any):Arbitrary Python object to be passed to callback function
      Context(typing.Any):Context object returned from win32file::OpenEncryptedFileRawCommentsOnly available on Windows 2000 or later

Returns:

      None
        
    """
    pass


def CloseEncryptedFileRaw(Context:typing.Any) -> None:
    """
    None


Args:

      Context(typing.Any):Context object returned from win32file::OpenEncryptedFileRawCommentsOnly available on Windows 2000 or later

Returns:

      None
        
    """
    pass


def CreateFileW(FileName:typing.Any,DesiredAccess:int,ShareMode:int,SecurityAttributes:typing.Any,CreationDisposition:int,FlagsAndAttributes:int,TemplateFile:typing.Any=None,Transaction:typing.Any=None,MiniVersion:int=None,ExtendedParameter:None=None) -> int:
    """
    None


Args:

      FileName(typing.Any):Name of file
      DesiredAccess(int):Combination of access mode flags.  See MSDN docs.
      ShareMode(int):Combination of FILE_SHARE_READ, FILE_SHARE_WRITE, FILE_SHARE_DELETE
      SecurityAttributes(typing.Any):Specifies security descriptor and handle inheritance, can be None
      CreationDisposition(int):One of CREATE_ALWAYS,CREATE_NEW,OPEN_ALWAYS,OPEN_EXISTING or TRUNCATE_EXISTING
      FlagsAndAttributes(int):Combination of FILE_ATTRIBUTE_* and FILE_FLAG_* flags
      TemplateFile(typing.Any):Handle to file to be used as template, can be None
      Transaction(typing.Any):Handle to the transaction as returned by win32transaction::CreateTransaction
      MiniVersion(int):Transacted version of file to open, can be None
      ExtendedParameter(None):Reserved, use only NoneCommentsIf Transaction is specified, CreateFileTransacted will be called (requires Vista or later)Accepts keyword arguments.Win32 API References

Returns:

      int
        
    """
    pass


def DeleteFileW(FileName:typing.Any,Transaction:typing.Any=None) -> None:
    """
    Deletes a file (Unicode version)


Args:

      FileName(typing.Any):Name of file to be deleted
      Transaction(typing.Any):Transaction handle as returned by win32transaction::CreateTransactionCommentsIf a transaction handle is passed in, DeleteFileTransacted will be called (requires Windows Vista).Accepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def GetFileAttributesEx(FileName:typing.Any,InfoLevelId:int,Transaction:typing.Any=None) -> tuple:
    """
    Retrieves attributes for a specified file or directory.


Args:

      FileName(typing.Any):File or directory for which to retrieve information In the ANSI version of this function, the name is limited to MAX_PATH characters. To extend this limit to nearly 32,000 wide characters, call the Unicode version of the function (win32file::GetFileAttributesExW) and prepend r"\\?\\" to the path.
      InfoLevelId(int):An integer that gives the set of attribute information to obtain. See the Win32 SDK documentation for more information.
      Transaction(typing.Any):Handle to a transaction (optional).  See win32transaction::CreateTransaction. If this parameter is specified, GetFileAttributesTransacted will be called (requires Vista or later).CommentsNot all file systems can record creation and last access time and not all file systems record them in the same manner. For example, on Windows NT FAT, create time has a resolution of 10 milliseconds, write time has a resolution of 2 seconds, and access time has a resolution of 1 day (really, the access date). On NTFS, access time has a resolution of 1 hour. Furthermore, FAT records times on disk in local time, while NTFS records times on disk in UTC, so it is not affected by changes in time zone or daylight saving time.Accepts keyword arguments.InfoLevelIdInformation returnedGetFileExInfoStandardTuple representing a WIN32_FILE_ATTRIBUTE_DATA strucWin32 API References

Returns:

      tuple:Search for GetFileAttributesTransacted at msdn, google or google groups.
Return ValueThe result is a tuple of:
Items
        
    """
    pass


def SetFileAttributesW(FileName:typing.Any,FileAttributes:int,Transaction:typing.Any=None) -> None:
    """
    Sets a file's attributes


Args:

      FileName(typing.Any):File or directory whose attributes are to be changed
      FileAttributes(int):Combination of FILE_ATTRIBUTE_* flags
      Transaction(typing.Any):Handle to the transaction.  See win32transaction::CreateTransaction.CommentsIf Transaction is not None, SetFileAttributesTransacted will be called (requires Vista or later)Accepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def CreateDirectoryExW(TemplateDirectory:typing.Any,NewDirectory:typing.Any,SecurityAttributes:typing.Any=None,Transaction:typing.Any=None) -> None:
    """
    Creates a directory (Unicode version)


Args:

      TemplateDirectory(typing.Any):Directory to use as a template, can be None
      NewDirectory(typing.Any):Name of directory to be created
      SecurityAttributes(typing.Any):Security for new directory (optional)
      Transaction(typing.Any):Handle to a transaction (optional).  See win32transaction::CreateTransaction.CommentsIf a transaction handle is passed, CreateDirectoryTransacted will be called (requires Vista or later).Accepts keyword arguments.Win32 API References

Returns:

      None
        
    """
    pass


def RemoveDirectory(PathName:typing.Any,Transaction:typing.Any=None) -> None:
    """
    Removes an existing directory


Args:

      PathName(typing.Any):Name of directory to be removed
      Transaction(typing.Any):Handle to a transaction (optional). See win32transaction::CreateTransaction.CommentsIf a transaction handle is passed in, RemoveDirectoryTransacted will be called (requires Vista or later)Accepts keyword arguments.  Implemented only as Unicode.Win32 API References

Returns:

      None
        
    """
    pass


def FindFilesW(FileName:str,Transaction:typing.Any=None) -> list:
    """
    Retrieves a list of matching filenames, using the Windows Unicode API.  An interface to the API FindFirstFileW/FindNextFileW/Find close functions.


Args:

      FileName(str):A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).
      Transaction(typing.Any):Transaction handle as returned by win32transaction::CreateTransaction.  Can be None. If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted searchCommentsAccepts keyword args.FindFirstFileTransacted will be called if a transaction handle is passed in.Win32 API References

Returns:

      list:Search for FindClose at msdn, google or google groups.
Return ValueThe return value is a list of WIN32_FIND_DATA tuples.

        
    """
    pass


def FindFilesIterator(FileName:str,Transaction:typing.Any=None) -> typing.Any:
    """
    None


Args:

      FileName(str):A string that specifies a valid directory or path and filename, which can contain wildcard characters (* and ?).
      Transaction(typing.Any):Handle to a transaction, can be None. If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted searchCommentsAccepts keyword args.FindFirstFileTransacted will be called if a transaction handle is passed in.Return ValueThe result is a Python iterator, with each next() method returning a WIN32_FIND_DATA tuple.

Returns:

      typing.Any:Handle to a transaction, can be None. 

If this parameter is not None, FindFirstFileTransacted will be called to perform a transacted search
Comments

Accepts keyword args.

FindFirstFileTransacted will be called if a transaction handle is passed in.
Return ValueThe result is a Python iterator, with each next() method 

returning a WIN32_FIND_DATA tuple.

        
    """
    pass


def FindStreams(FileName:typing.Any,Transaction:typing.Any=None) -> typing.Any:
    """
    List the data streams for a file


Args:

      FileName(typing.Any):Name of file (or directory) to operate on
      Transaction(typing.Any):Handle to a transaction, can be NoneCommentsThis uses the API functions FindFirstStreamW, FindNextStreamW and FindCloseAvailable on Windows Server 2003 and VistaIf the Transaction arg is not None, FindFirstStreamTransacted will be called in place of FindFirstStreamWReturn ValueReturns a list of tuples containing each stream's size and name

Returns:

      typing.Any:Handle to a transaction, can be None
Comments

This uses the API functions FindFirstStreamW, FindNextStreamW and FindClose

Available on Windows Server 2003 and Vista

If the Transaction arg is not None, FindFirstStreamTransacted will be called in place of FindFirstStreamW
Return ValueReturns a list of tuples containing each stream's size and name

        
    """
    pass


def FindFileNames(FileName:typing.Any,Transaction:typing.Any=None) -> typing.Any:
    """
    Enumerates hard links that point to specified file


Args:

      FileName(typing.Any):Name of file for which to find links
      Transaction(typing.Any):Handle to a transaction, can be NoneCommentsThis uses the API functions FindFirstFileNameW, FindNextFileNameW and FindCloseAvailable on Vista and laterIf Transaction is specified, a transacted search is performed using FindFirstFileNameTransacted

Returns:

      typing.Any
        
    """
    pass


def GetFinalPathNameByHandle(File:typing.Any,Flags:int) -> str:
    """
    Returns the file name for an open file handle


Args:

      File(typing.Any):An open file handle
      Flags(int):Specifies type of path to return. (win32con.FILE_NAME_NORMALIZED,FILE_NAME_OPENED,VOLUME_NAME_DOS,VOLUME_NAME_GUID,VOLUME_NAME_NONE,VOLUME_NAME_NT)CommentsExists on Windows Vista or later.Accepts keyword arguments.Win32 API References

Returns:

      str
        
    """
    pass


def SfcGetNextProtectedFile() -> typing.Any:
    """
    Returns list of protected operating system files


Args:



Returns:

      typing.Any
        
    """
    pass


def SfcIsFileProtected(ProtFileName:typing.Any) -> typing.Any:
    """
    Checks if a file is protected


Args:

      ProtFileName(typing.Any):Name of file to be checked

Returns:

      typing.Any
        
    """
    pass


def GetLongPathName(ShortPath:typing.Any,Transaction:typing.Any=None) -> str:
    """
    Retrieves the long path for a short path (8.3 filename)


Args:

      ShortPath(typing.Any):8.3 path to be expanded
      Transaction(typing.Any):Handle to a transaction.  If specified, GetLongPathNameTransacted will be called.CommentsAccepts keyword args

Returns:

      str
        
    """
    pass


def GetFullPathName(FileName:Union[str,typing.Any],Transaction:typing.Any=None) -> typing.Any:
    """
    Returns full path for path passed in


Args:

      FileName(str,typing.Any):Path on which to operate
      Transaction(typing.Any):Handle to a transaction as returned by win32transaction::CreateTransactionCommentsThis function takes either a plain string or a unicode string, and returns the same type If unicode is passed in, GetFullPathNameW is called, which supports filenames longer than MAX_PATHIf Transaction parameter is specified, GetFullPathNameTransacted is called (requires Vista or later)

Returns:

      typing.Any
        
    """
    pass


def Wow64DisableWow64FsRedirection() -> int:
    """
    Disables file system redirection for 32-bit processes running on a 64-bit system


Args:



Returns:

      int:win32file.Wow64DisableWow64FsRedirection

int = Wow64DisableWow64FsRedirection()Disables file system redirection for 32-bit processes running on a 64-bit system
Comments

Requires 64-bit XP or later
Return ValueReturns a state value to be passed to win32file::Wow64RevertWow64FsRedirection

        
    """
    pass


def Wow64RevertWow64FsRedirection(OldValue:int) -> None:
    """
    Reenables file system redirection for 32-bit processes running on a 64-bit system


Args:

      OldValue(int):State returned from Wow64DisableWow64FsRedirectionCommentsRequires 64-bit XP or later

Returns:

      None
        
    """
    pass


def GetFileInformationByHandleEx(File:typing.Any,FileInformationClass:int) -> typing.Any:
    """
    Retrieves extended file information for an open file handle.


Args:

      File(typing.Any):Handle to a file or directory.  Do not pass a pipe handle.
      FileInformationClass(int):Type of data to return, one of win32file.File*Info valuesCommentsAvailable on Vista and later.Accepts keyword args.Return ValueType of returned object is determined by the requested information classClassReturned infoFileBasicInfoDict representing a FILE_BASIC_INFO structFileStandardInfoDict representing a FILE_STANDARD_INFO structFileNameInfoString containing the file name, without the drive letterFileCompressionInfoDict representing a FILE_COMPRESSION_INFO structFileAttributeTagInfoDict representing a FILE_ATTRIBUTE_TAG_INFO structFileIdBothDirectoryInfoSequence of dicts representing FILE_ID_BOTH_DIR_INFO structs.  Call in loop until no more files are returned.FileIdBothDirectoryRestartInfoSequence of dicts representing FILE_ID_BOTH_DIR_INFO structs.FileStreamInfoSequence of dicts representing FILE_STREAM_INFO structs

Returns:

      typing.Any:Type of data to return, one of win32file.File*Info valuesComments

Available on Vista and later.

Accepts keyword args.
Return ValueType of returned object is determined by the requested information class



Class


Returned info



FileBasicInfoDict representing a FILE_BASIC_INFO struct
FileStandardInfoDict representing a FILE_STANDARD_INFO struct
FileNameInfoString containing the file name, without the drive letter
FileCompressionInfoDict representing a FILE_COMPRESSION_INFO struct
FileAttributeTagInfoDict representing a FILE_ATTRIBUTE_TAG_INFO struct
FileIdBothDirectoryInfoSequence of dicts representing FILE_ID_BOTH_DIR_INFO structs.  Call in loop until no more files are returned.
FileIdBothDirectoryRestartInfoSequence of dicts representing FILE_ID_BOTH_DIR_INFO structs.
FileStreamInfoSequence of dicts representing FILE_STREAM_INFO structs

        
    """
    pass


def SetFileInformationByHandle(File:typing.Any,FileInformationClass:int,Information:typing.Any) -> None:
    """
    Changes file characteristics by file handle


Args:

      File(typing.Any):Handle to a file or directory.  Do not pass a pipe handle.
      FileInformationClass(int):Type of data, one of win32file.File*Info values
      Information(typing.Any):Type is dependent on the class to be changedClassType of inputFileBasicInfoDict representing a FILE_BASIC_INFO struct, containing {"CreationTime":PyTime, "LastAccessTime":PyTime,  "LastWriteTime":PyTime, "ChangeTime":PyTime, "FileAttributes":int}FileRenameInfoDict representing a FILE_RENAME_INFO struct, containing {"ReplaceIfExists":boolean, "RootDirectory":PyHANDLE, "FileName":str} MSDN says the RootDirectory is "A handle to the root directory in which the file to be renamed is located". However, this is actually the destination dir, can be None to stay in same dir.FileDispositionInfoBoolean indicating if file should be deleted when handle is closedFileAllocationInfoInt giving the allocation size.FileEndOfFileInfoInt giving the EOF position, cannot be greater than allocated size.FileIoPriorityHintInfoInt containing the IO priority (IoPriorityHint*)CommentsAvailable on Vista and later.Accepts keyword args.

Returns:

      None
        
    """
    pass


def ReOpenFile(OriginalFile:typing.Any,DesiredAccess:int,ShareMode:int,Flags:int) -> int:
    """
    Creates a new handle to an open file


Args:

      OriginalFile(typing.Any):An open file handle
      DesiredAccess(int):Access mode, cannot conflict with original access mode
      ShareMode(int):Sharing mode (FILE_SHARE_*), cannot conflict with original share mode
      Flags(int):Combination of FILE_FLAG_* flagsCommentsAvailable on Vista and later.Accepts keyword args.

Returns:

      int
        
    """
    pass


def OpenFileById(File:typing.Any,FileId:Union[int,typing.Any],DesiredAccess:int,ShareMode:int,Flags:int,SecurityAttributes:typing.Any=None) -> int:
    """
    Opens a file by File Id or Object Id


Args:

      File(typing.Any):Handle to a file on the volume that contains the file to open
      FileId(int,typing.Any):File Id or Object Id of the file to open
      DesiredAccess(int):Access mode
      ShareMode(int):Sharing mode (FILE_SHARE_*)
      Flags(int):Combination of FILE_FLAG_* flags
      SecurityAttributes(typing.Any):Reserved, use only NoneCommentsAvailable on Vista and later.Accepts keyword args.

Returns:

      int
        
    """
    pass

CALLBACK_CHUNK_FINISHED = ...
CALLBACK_STREAM_SWITCH = ...
CBR_110 = ...
CBR_115200 = ...
CBR_1200 = ...
CBR_128000 = ...
CBR_14400 = ...
CBR_19200 = ...
CBR_2400 = ...
CBR_256000 = ...
CBR_300 = ...
CBR_38400 = ...
CBR_4800 = ...
CBR_56000 = ...
CBR_57600 = ...
CBR_600 = ...
CBR_9600 = ...
CLRBREAK = ...
CLRDTR = ...
CLRRTS = ...
COPY_FILE_ALLOW_DECRYPTED_DESTINATION = ...
COPY_FILE_COPY_SYMLINK = ...
COPY_FILE_FAIL_IF_EXISTS = ...
COPY_FILE_OPEN_SOURCE_FOR_WRITE = ...
COPY_FILE_RESTARTABLE = ...
CREATE_ALWAYS = ...
CREATE_FOR_DIR = ...
CREATE_FOR_IMPORT = ...
CREATE_NEW = ...
DRIVE_CDROM = ...
DRIVE_FIXED = ...
DRIVE_NO_ROOT_DIR = ...
DRIVE_RAMDISK = ...
DRIVE_REMOTE = ...
DRIVE_REMOVABLE = ...
DRIVE_UNKNOWN = ...
DTR_CONTROL_DISABLE = ...
DTR_CONTROL_ENABLE = ...
DTR_CONTROL_HANDSHAKE = ...
EV_BREAK = ...
EV_CTS = ...
EV_DSR = ...
EV_ERR = ...
EV_RING = ...
EV_RLSD = ...
EV_RXCHAR = ...
EV_RXFLAG = ...
EV_TXEMPTY = ...
EVENPARITY = ...
FD_ACCEPT = ...
FD_ADDRESS_LIST_CHANGE = ...
FD_CLOSE = ...
FD_CONNECT = ...
FD_GROUP_QOS = ...
FD_OOB = ...
FD_QOS = ...
FD_READ = ...
FD_ROUTING_INTERFACE_CHANGE = ...
FD_WRITE = ...
FILE_ALL_ACCESS = ...
FILE_ATTRIBUTE_ARCHIVE = ...
FILE_ATTRIBUTE_COMPRESSED = ...
FILE_ATTRIBUTE_DIRECTORY = ...
FILE_ATTRIBUTE_HIDDEN = ...
FILE_ATTRIBUTE_NORMAL = ...
FILE_ATTRIBUTE_OFFLINE = ...
FILE_ATTRIBUTE_READONLY = ...
FILE_ATTRIBUTE_SYSTEM = ...
FILE_ATTRIBUTE_TEMPORARY = ...
FILE_BEGIN = ...
FILE_CURRENT = ...
FILE_ENCRYPTABLE = ...
FILE_END = ...
FILE_FLAG_BACKUP_SEMANTICS = ...
FILE_FLAG_DELETE_ON_CLOSE = ...
FILE_FLAG_NO_BUFFERING = ...
FILE_FLAG_OPEN_REPARSE_POINT = ...
FILE_FLAG_OVERLAPPED = ...
FILE_FLAG_POSIX_SEMANTICS = ...
FILE_FLAG_RANDOM_ACCESS = ...
FILE_FLAG_SEQUENTIAL_SCAN = ...
FILE_FLAG_WRITE_THROUGH = ...
FILE_GENERIC_READ = ...
FILE_GENERIC_WRITE = ...
FILE_IS_ENCRYPTED = ...
FILE_READ_ONLY = ...
FILE_ROOT_DIR = ...
FILE_SHARE_DELETE = ...
FILE_SHARE_READ = ...
FILE_SHARE_WRITE = ...
FILE_SYSTEM_ATTR = ...
FILE_SYSTEM_DIR = ...
FILE_SYSTEM_NOT_SUPPORT = ...
FILE_TYPE_CHAR = ...
FILE_TYPE_DISK = ...
FILE_TYPE_PIPE = ...
FILE_TYPE_UNKNOWN = ...
FILE_UNKNOWN = ...
FILE_USER_DISALLOWED = ...
FileAllocationInfo = ...
FileAttributeTagInfo = ...
FileBasicInfo = ...
FileCompressionInfo = ...
FileDispositionInfo = ...
FileEndOfFileInfo = ...
FileIdBothDirectoryInfo = ...
FileIdBothDirectoryRestartInfo = ...
FileIdType = ...
FileIoPriorityHintInfo = ...
FileNameInfo = ...
FileRenameInfo = ...
FileStandardInfo = ...
FileStreamInfo = ...
GENERIC_EXECUTE = ...
GENERIC_READ = ...
GENERIC_WRITE = ...
GetFileExInfoStandard = ...
IoPriorityHintLow = ...
IoPriorityHintNormal = ...
IoPriorityHintVeryLow = ...
MARKPARITY = ...
MOVEFILE_COPY_ALLOWED = ...
MOVEFILE_CREATE_HARDLINK = ...
MOVEFILE_DELAY_UNTIL_REBOOT = ...
MOVEFILE_FAIL_IF_NOT_TRACKABLE = ...
MOVEFILE_REPLACE_EXISTING = ...
MOVEFILE_WRITE_THROUGH = ...
NOPARITY = ...
ObjectIdType = ...
ODDPARITY = ...
ONE5STOPBITS = ...
ONESTOPBIT = ...
OPEN_ALWAYS = ...
OPEN_EXISTING = ...
OVERWRITE_HIDDEN = ...
PROGRESS_CANCEL = ...
PROGRESS_CONTINUE = ...
PROGRESS_QUIET = ...
PROGRESS_STOP = ...
PURGE_RXABORT = ...
PURGE_RXCLEAR = ...
PURGE_TXABORT = ...
PURGE_TXCLEAR = ...
REPLACEFILE_IGNORE_MERGE_ERRORS = ...
REPLACEFILE_WRITE_THROUGH = ...
RTS_CONTROL_DISABLE = ...
RTS_CONTROL_ENABLE = ...
RTS_CONTROL_HANDSHAKE = ...
RTS_CONTROL_TOGGLE = ...
SCS_32BIT_BINARY = ...
SCS_DOS_BINARY = ...
SCS_OS216_BINARY = ...
SCS_PIF_BINARY = ...
SCS_POSIX_BINARY = ...
SCS_WOW_BINARY = ...
SECURITY_ANONYMOUS = ...
SECURITY_CONTEXT_TRACKING = ...
SECURITY_DELEGATION = ...
SECURITY_EFFECTIVE_ONLY = ...
SECURITY_IDENTIFICATION = ...
SECURITY_IMPERSONATION = ...
SETBREAK = ...
SETDTR = ...
SETRTS = ...
SETXOFF = ...
SETXON = ...
SO_CONNECT_TIME = ...
SO_UPDATE_ACCEPT_CONTEXT = ...
SO_UPDATE_CONNECT_CONTEXT = ...
SPACEPARITY = ...
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE = ...
SYMBOLIC_LINK_FLAG_DIRECTORY = ...
TF_DISCONNECT = ...
TF_REUSE_SOCKET = ...
TF_USE_DEFAULT_WORKER = ...
TF_USE_KERNEL_APC = ...
TF_USE_SYSTEM_THREAD = ...
TF_WRITE_BEHIND = ...
TRUNCATE_EXISTING = ...
TWOSTOPBITS = ...
WSA_IO_PENDING = ...
WSA_OPERATION_ABORTED = ...
WSAECONNABORTED = ...
WSAECONNRESET = ...
WSAEDISCON = ...
WSAEFAULT = ...
WSAEINPROGRESS = ...
WSAEINTR = ...
WSAEINVAL = ...
WSAEMSGSIZE = ...
WSAENETDOWN = ...
WSAENETRESET = ...
WSAENOBUFS = ...
WSAENOTCONN = ...
WSAENOTSOCK = ...
WSAEOPNOTSUPP = ...
WSAESHUTDOWN = ...
WSAEWOULDBLOCK = ...