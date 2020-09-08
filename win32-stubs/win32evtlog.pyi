__all__=['', 'ReadEventLog', 'ClearEventLog', 'BackupEventLog', 'CloseEventLog', 'DeregisterEventSource', 'NotifyChangeEventLog', 'GetNumberOfEventLogRecords', 'GetOldestEventLogRecord', 'OpenEventLog', 'RegisterEventSource', 'OpenBackupEventLog', 'ReportEvent', 'EvtOpenChannelEnum', 'EvtNextChannelPath', 'EvtOpenLog', 'EvtClearLog', 'EvtExportLog', 'EvtArchiveExportedLog', 'EvtGetExtendedStatus', 'EvtQuery', 'EvtNext', 'EvtSeek', 'EvtRender', 'EvtSubscribe', 'EvtCreateBookmark', 'EvtUpdateBookmark', 'EvtGetChannelConfigProperty', 'EvtOpenChannelConfig', 'EvtOpenSession', 'EvtOpenPublisherEnum', 'EvtNextPublisherId', 'EvtOpenPublisherMetadata', 'EvtGetPublisherMetadataProperty', 'EvtOpenEventMetadataEnum', 'EvtNextEventMetadata', 'EvtGetEventMetadataProperty', 'EvtGetLogInfo', 'EvtGetEventInfo', 'EvtGetObjectArraySize', 'EvtGetObjectArrayProperty', 'EVENTLOG_AUDIT_FAILURE', 'EVENTLOG_AUDIT_SUCCESS', 'EVENTLOG_BACKWARDS_READ', 'EVENTLOG_END_ALL_PAIRED_EVENTS', 'EVENTLOG_END_PAIRED_EVENT', 'EVENTLOG_ERROR_TYPE', 'EVENTLOG_FORWARDS_READ', 'EVENTLOG_INFORMATION_TYPE', 'EVENTLOG_PAIRED_EVENT_ACTIVE', 'EVENTLOG_PAIRED_EVENT_INACTIVE', 'EVENTLOG_SEEK_READ', 'EVENTLOG_SEQUENTIAL_READ', 'EVENTLOG_START_PAIRED_EVENT', 'EVENTLOG_SUCCESS', 'EVENTLOG_WARNING_TYPE', 'EventMetadataEventChannel', 'EventMetadataEventID', 'EventMetadataEventKeyword', 'EventMetadataEventLevel', 'EventMetadataEventMessageID', 'EventMetadataEventOpcode', 'EventMetadataEventTask', 'EventMetadataEventTemplate', 'EventMetadataEventVersion', 'EvtChannelConfigAccess', 'EvtChannelConfigClassicEventlog', 'EvtChannelConfigEnabled', 'EvtChannelConfigIsolation', 'EvtChannelConfigOwningPublisher', 'EvtChannelConfigPropertyIdEND', 'EvtChannelConfigType', 'EvtChannelLoggingConfigAutoBackup', 'EvtChannelLoggingConfigLogFilePath', 'EvtChannelLoggingConfigMaxSize', 'EvtChannelLoggingConfigRetention', 'EvtChannelPublisherList', 'EvtChannelPublishingConfigBufferSize', 'EvtChannelPublishingConfigClockType', 'EvtChannelPublishingConfigControlGuid', 'EvtChannelPublishingConfigFileMax', 'EvtChannelPublishingConfigKeywords', 'EvtChannelPublishingConfigLatency', 'EvtChannelPublishingConfigLevel', 'EvtChannelPublishingConfigMaxBuffers', 'EvtChannelPublishingConfigMinBuffers', 'EvtChannelPublishingConfigSidType', 'EvtEventMetadataPropertyIdEND', 'EvtEventPath', 'EvtEventPropertyIdEND', 'EvtEventQueryIDs', 'EvtExportLogChannelPath', 'EvtExportLogFilePath', 'EvtExportLogTolerateQueryErrors', 'EvtLogAttributes', 'EvtLogCreationTime', 'EvtLogFileSize', 'EvtLogFull', 'EvtLogLastAccessTime', 'EvtLogLastWriteTime', 'EvtLogNumberOfLogRecords', 'EvtLogOldestRecordNumber', 'EvtOpenChannelPath', 'EvtOpenFilePath', 'EvtPublisherMetadataChannelReferenceFlags', 'EvtPublisherMetadataChannelReferenceID', 'EvtPublisherMetadataChannelReferenceIndex', 'EvtPublisherMetadataChannelReferenceMessageID', 'EvtPublisherMetadataChannelReferencePath', 'EvtPublisherMetadataChannelReferences', 'EvtPublisherMetadataHelpLink', 'EvtPublisherMetadataKeywordMessageID', 'EvtPublisherMetadataKeywordName', 'EvtPublisherMetadataKeywords', 'EvtPublisherMetadataKeywordValue', 'EvtPublisherMetadataLevelMessageID', 'EvtPublisherMetadataLevelName', 'EvtPublisherMetadataLevels', 'EvtPublisherMetadataLevelValue', 'EvtPublisherMetadataMessageFilePath', 'EvtPublisherMetadataOpcodeMessageID', 'EvtPublisherMetadataOpcodeName', 'EvtPublisherMetadataOpcodes', 'EvtPublisherMetadataOpcodeValue', 'EvtPublisherMetadataParameterFilePath', 'EvtPublisherMetadataPropertyIdEND', 'EvtPublisherMetadataPublisherGuid', 'EvtPublisherMetadataPublisherMessageID', 'EvtPublisherMetadataResourceFilePath', 'EvtPublisherMetadataTaskEventGuid', 'EvtPublisherMetadataTaskMessageID', 'EvtPublisherMetadataTaskName', 'EvtPublisherMetadataTasks', 'EvtPublisherMetadataTaskValue', 'EvtQueryChannelPath', 'EvtQueryFilePath', 'EvtQueryForwardDirection', 'EvtQueryReverseDirection', 'EvtQueryTolerateQueryErrors', 'EvtRenderBookmark', 'EvtRenderEventValues', 'EvtRenderEventXml', 'EvtRpcLogin', 'EvtRpcLoginAuthDefault', 'EvtRpcLoginAuthKerberos', 'EvtRpcLoginAuthNegotiate', 'EvtRpcLoginAuthNTLM', 'EvtSeekOriginMask', 'EvtSeekRelativeToBookmark', 'EvtSeekRelativeToCurrent', 'EvtSeekRelativeToFirst', 'EvtSeekRelativeToLast', 'EvtSeekStrict', 'EvtSubscribeActionDeliver', 'EvtSubscribeActionError', 'EvtSubscribeOriginMask', 'EvtSubscribeStartAfterBookmark', 'EvtSubscribeStartAtOldestRecord', 'EvtSubscribeStrict', 'EvtSubscribeToFutureEvents', 'EvtSubscribeTolerateQueryErrors', 'EvtVarTypeAnsiString', 'EvtVarTypeBinary', 'EvtVarTypeBoolean', 'EvtVarTypeByte', 'EvtVarTypeDouble', 'EvtVarTypeEvtHandle', 'EvtVarTypeEvtXml', 'EvtVarTypeFileTime', 'EvtVarTypeGuid', 'EvtVarTypeHexInt32', 'EvtVarTypeHexInt64', 'EvtVarTypeInt16', 'EvtVarTypeInt32', 'EvtVarTypeInt64', 'EvtVarTypeNull', 'EvtVarTypeSByte', 'EvtVarTypeSid', 'EvtVarTypeSingle', 'EvtVarTypeSizeT', 'EvtVarTypeString', 'EvtVarTypeSysTime', 'EvtVarTypeUInt16', 'EvtVarTypeUInt32', 'EvtVarTypeUInt64']
from typing import *
from win32helper.win32typing import *
""""""


def ReadEventLog(Handle:'Any',Flags:'int',Offset:'int',Size:'int'=4096) -> 'List[Any]':
    """
    Reads some event log records.

Args:

      Handle(Any):Handle to a an opened event log (see win32evtlog::OpenEventLog)
      Flags(int):Reading flags
      Offset(int):Record offset to read (in SEEK mode).
      Size(int):Output buffer size.Return ValueIf there are no event log records available, then an empty list is returned.

Returns:

      List[Any]:Output buffer size.
Return ValueIf there are no event log records available, then an empty list is returned.

        
    """
    pass
        

def ClearEventLog(handle:'int',eventLogName:'str') -> 'None':
    """
    Clears the event log

Args:

      handle(int):Handle to the event log to clear.
      eventLogName(str):The name of the event log to save to, or None

Returns:

      None
        
    """
    pass
        

def BackupEventLog(handle:'int',eventLogName:'str') -> 'None':
    """
    Backs up the event log

Args:

      handle(int):Handle to the event log to backup.
      eventLogName(str):The name of the event log to save to

Returns:

      None
        
    """
    pass
        

def CloseEventLog(handle:'int') -> 'None':
    """
    Closes the eventlog

Args:

      handle(int):Handle to the event log to close

Returns:

      None
        
    """
    pass
        

def DeregisterEventSource(handle:'int') -> 'None':
    """
    Deregisters an Event Source

Args:

      handle(int):Identifies the event log whose handle was returned by win32evtlog::RegisterEventSource

Returns:

      None
        
    """
    pass
        

def NotifyChangeEventLog(handle:'int',handle1:'int') -> 'None':
    """
    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

Args:

      handle(int):Handle to an event log file, obtained by calling win32evtlog::OpenEventLog function. When an event is written to this log file, the event specified by hEvent becomes signaled.
      handle1(int):A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.

Returns:

      None
        
    """
    pass
        

def GetNumberOfEventLogRecords(handle:'int') -> 'int':
    """
    Returns the number of event log records.

Args:

      handle(int):Handle to the event log to query.

Returns:

      int
        
    """
    pass
        

def GetOldestEventLogRecord() -> 'int':
    """
    Returns the number of event log records.

Args:



Returns:

      int:win32evtlog.GetOldestEventLogRecord

int = GetOldestEventLogRecord()Returns the number of event log records.
Return ValueThe result is the absolute record number of the oldest record in the given event log.

        
    """
    pass
        

def OpenEventLog(serverName:'str',sourceName:'str') -> 'PyEVTLOG_HANDLE':
    """
    Opens an event log.

Args:

      serverName(str):The server name, or None
      sourceName(str):specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.

Returns:

      PyEVTLOG_HANDLE
        
    """
    pass
        

def RegisterEventSource(serverName:'str',sourceName:'str') -> 'int':
    """
    Registers an Event Source

Args:

      serverName(str):The server name, or None
      sourceName(str):The source name

Returns:

      int
        
    """
    pass
        

def OpenBackupEventLog(serverName:'str',fileName:'str') -> 'PyEVTLOG_HANDLE':
    """
    Opens a previously saved event log.

Args:

      serverName(str):The server name, or None
      fileName(str):The filename to open

Returns:

      PyEVTLOG_HANDLE
        
    """
    pass
        

def ReportEvent(EventLog:'int',Type:'int',Category:'int',EventID:'int',UserSid:'PySID',Strings:'Any',RawData:'str') -> 'None':
    """
    Reports an event

Args:

      EventLog(int):Handle to an event log
      Type(int):win32con.EVENTLOG_* value
      Category(int):Source-specific event category
      EventID(int):Source-specific event identifier
      UserSid(PySID):Sid of current user, can be None
      Strings(Any):Sequence of unicode strings to be inserted in message
      RawData(str):Binary data for event, can be None

Returns:

      None
        
    """
    pass
        

def EvtOpenChannelEnum(Session:'PyEVT_HANDLE'=None,Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Begins an enumeration of event channels

Args:

      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtNextChannelPath(ChannelEnum:'PyEVT_HANDLE') -> 'str':
    """
    Retrieves a channel path from an enumeration

Args:

      ChannelEnum(PyEVT_HANDLE):Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      str:Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass
        

def EvtOpenLog(Path:'str',Flags:'int',Session:'PyEVT_HANDLE'=None) -> 'PyEVT_HANDLE':
    """
    Opens an event log or exported log archive

Args:

      Path(str):Event log name or Path of an export file
      Flags(int):EvtOpenChannelPath (1) or EvtOpenFilePath (2)
      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtClearLog(ChannelPath:'str',TargetFilePath:'str'=None,Session:'PyEVT_HANDLE'=None,Flags:'int'=0) -> 'None':
    """
    Clears an event log and optionally exports events to an archive

Args:

      ChannelPath(str):Name of event log to be cleared
      TargetFilePath(str):Name of file in which cleared events will be archived, or None
      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtExportLog(Path:'str',TargetFilePath:'str',Flags:'int',Query:'str'=None,Session:'PyEVT_HANDLE'=None) -> 'None':
    """
    Exports events from a channel or log file

Args:

      Path(str):Path of a live event log channel or exported log file
      TargetFilePath(str):File to create, cannot already exist
      Flags(int):Combination of EvtExportLog* flags specifying the type of path
      Query(str):Selects specific events to export
      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtArchiveExportedLog(LogFilePath:'str',Locale:'int',Session:'PyEVT_HANDLE'=None,Flags:'int'=0) -> 'None':
    """
    Localizes an exported event log file

Args:

      LogFilePath(str):Filename of an exported log file
      Locale(int):Locale id
      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):ReservedCommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtGetExtendedStatus() -> 'str':
    """
    Returns additional error info from last Evt* call

Args:



Returns:

      str
        
    """
    pass
        

def EvtQuery(Path:'str',Flags:'int',Query:'str'=None,Session:'PyEVT_HANDLE'=None) -> 'PyEVT_HANDLE':
    """
    Opens a query over a log channel or exported log file

Args:

      Path(str):Log channel or exported log file, depending on Flags
      Flags(int):Combination of EVT_QUERY_FLAGS (EvtQuery*)
      Query(str):Selects events to return, None or '*' for all events
      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtNext(ResultSet:'PyEVT_HANDLE',Count:'int',Timeout:'int'=-1,Flags:'int'=0) -> 'Tuple[PyEVT_HANDLE, ...]':
    """
    Returns events from a query

Args:

      ResultSet(PyEVT_HANDLE):Handle to event query or subscription
      Count(int):Number of events to return
      Timeout(int):Time to wait in milliseconds, use -1 for infinite
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns a tuple of handles to events.  If no items are available, returns an empty tuple instead of raising an exception.

Returns:

      Tuple[PyEVT_HANDLE, ...]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns a tuple of handles to events.  If no items are available, returns 

an empty tuple instead of raising an exception.

        
    """
    pass
        

def EvtSeek(ResultSet:'PyEVT_HANDLE',Position:'int',Flags:'int',Bookmark:'PyEVT_HANDLE'=None,Timeout:'int'=0) -> 'None':
    """
    Changes the current position in a result set

Args:

      ResultSet(PyEVT_HANDLE):Handle to event query or subscription
      Position(int):Offset (base from which to seek is specified by Flags)
      Flags(int):EvtSeekRelative* flag indicating seek origin
      Bookmark(PyEVT_HANDLE):Used as seek origin only if Flags contains EvtSeekRelativeToBookmark
      Timeout(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtRender(Event:'PyEVT_HANDLE',Flags:'int') -> 'str':
    """
    Formats an event into XML text

Args:

      Event(PyEVT_HANDLE):Handle to an event or bookmark
      Flags(int):EvtRenderEventXml or EvtRenderBookmark indicating type of handleCommentsAccepts keyword argsRendering event values (Flags=EvtRenderEventValues) is not currently supported

Returns:

      str
        
    """
    pass
        

def EvtSubscribe(ChannelPath:'str',Flags:'int',SignalEvent:'Any'=None,Callback:'Any'=None,Context:'Any'=None,Query:'str'=None,Session:'PyEVT_HANDLE'=None,Bookmark:'PyEVT_HANDLE'=None) -> 'PyEVT_HANDLE':
    """
    Requests notification for events

Args:

      ChannelPath(str):Name of an event log channel
      Flags(int):Combination of EvtSubscribe* flags determining how subscription is initiated
      SignalEvent(Any):An event handle to be set when events are available (see win32event::CreateEvent)
      Callback(Any):Python function to be called with each event
      Context(Any):Arbitrary object to be passed to the callback function
      Query(str):XML query used to select specific events, use None or '*' for all events
      Session(PyEVT_HANDLE):Handle to a session on another machine, or None for local
      Bookmark(PyEVT_HANDLE):If Flags contains EvtSubscribeStartAfterBookmark, used as starting pointCommentsAccepts keyword argsThe method used to receive events is determined by the parameters passed in. To create a push subscription, define a callback function that will be called with each event. The function will receive 3 args: First is an integer specifying why the function was called (EvtSubscribeActionError or EvtSubscribeActionDeliver) Second is the context object passed to EvtSubscribe. Third is the handle to an event log record (if not called due to an error) If an event handle is passed in, a pull subscription is created.  The event handle will be signalled when events are available, and the subscription handle can be passed to win32evtlog::EvtNext to obtain the events.

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtCreateBookmark(BookmarkXML:'str'=None) -> 'PyEVT_HANDLE':
    """
    Creates a bookmark

Args:

      BookmarkXML(str):XML representation of a bookmark as returned by win32evtlog::EvtRender, or None for a new bookmarkCommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtUpdateBookmark(Bookmark:'PyEVT_HANDLE',Event:'PyEVT_HANDLE') -> 'PyEVT_HANDLE':
    """
    Repositions a bookmark to an event

Args:

      Bookmark(PyEVT_HANDLE):Handle to a bookmark
      Event(PyEVT_HANDLE):Handle to an eventCommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtGetChannelConfigProperty(ChannelConfig:'PyEVT_HANDLE',PropertyId:'int',Flags:'int'=0) -> 'Tuple[Any, int]':
    """
    Retreives channel configuration information

Args:

      ChannelConfig(PyEVT_HANDLE):Config handle as returned by win32evtlog::EvtOpenChannelConfig
      PropertyId(int):Property to retreive, one of EvtChannel* constants
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      Tuple[Any, int]
        
    """
    pass
        

def EvtOpenChannelConfig(ChannelPath:'str',Session:'PyEVT_HANDLE'=None,Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Opens channel configuration

Args:

      ChannelPath(str):Channel to be opened
      Session(PyEVT_HANDLE):Session handle as returned by win32evtlog::EvtOpenSession, or None for local machine
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtOpenSession(Login:'PyEVT_RPC_LOGIN',LoginClass:'int',Timeout:'int'=0,Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Creates a session used to access the Event Log on another machine

Args:

      Login(PyEVT_RPC_LOGIN):Credentials to be used to access remote machine
      LoginClass(int):Type of login to perform, EvtRpcLogin is only defined value
      Timeout(int):Reserved, use only 0
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtOpenPublisherEnum(Session:'PyEVT_HANDLE'=None,Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Begins an enumeration of event publishers

Args:

      Session(PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtNextPublisherId(PublisherEnum:'PyEVT_HANDLE') -> 'str':
    """
    Returns the next publisher from an enumeration

Args:

      PublisherEnum(PyEVT_HANDLE):Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      str:Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass
        

def EvtOpenPublisherMetadata(PublisherIdentity:'str',Session:'PyEVT_HANDLE'=None,LogFilePath:'str'=None,Locale:'int'=0,Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    None

Args:

      PublisherIdentity(str):Publisher id as returned by win32evtlog::EvtNextPublisherId
      Session(PyEVT_HANDLE):Handle to remote session, or None for local machine
      LogFilePath(str):Log file from which to retrieve publisher, or None for locally registered publisher
      Locale(int):Locale to use for retrieved properties, use 0 for current locale
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtGetPublisherMetadataProperty(PublisherMetadata:'PyEVT_HANDLE',PropertyId:'int',Flags:'int'=0) -> 'Tuple[Any, int]':
    """
    Retrieves a property from an event publisher

Args:

      PublisherMetadata(PyEVT_HANDLE):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      PropertyId(int):Property to retreive, EvtPublisherMetadata*
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*) Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

Returns:

      Tuple[Any, int]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*) 

Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using 

win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

        
    """
    pass
        

def EvtOpenEventMetadataEnum(PublisherMetadata:'PyEVT_HANDLE',Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Enumerates the events that a publisher provides

Args:

      PublisherMetadata(PyEVT_HANDLE):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtNextEventMetadata(EventMetadataEnum:'PyEVT_HANDLE',Flags:'int'=0) -> 'PyEVT_HANDLE':
    """
    Retrieves the next item from an event metadata enumeration

Args:

      EventMetadataEnum(PyEVT_HANDLE):Enumeration handle as returned by win32evtlog::EvtOpenEventMetadataEnum
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      PyEVT_HANDLE
        
    """
    pass
        

def EvtGetEventMetadataProperty(EventMetadata:'PyEVT_HANDLE',PropertyId:'int',Flags:'int'=0) -> 'Tuple[Any, int]':
    """
    Retrieves a property from an event publisher

Args:

      EventMetadata(PyEVT_HANDLE):Event metadata handle as returned by win32evtlog::EvtNextEventMetadata
      PropertyId(int):Property to retreive, EventMetadata*
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*).

Returns:

      Tuple[Any, int]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*).

        
    """
    pass
        

def EvtGetLogInfo(Log:'PyEVT_HANDLE',PropertyId:'int') -> 'Tuple[Any, int]':
    """
    Retrieves log file or channel information

Args:

      Log(PyEVT_HANDLE):Event log handle as returned by win32evtlog::EvtOpenLog
      PropertyId(int):Property to retreive, EvtLog*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      Tuple[Any, int]
        
    """
    pass
        

def EvtGetEventInfo(Event:'PyEVT_HANDLE',PropertyId:'int') -> 'Tuple[Any, int]':
    """
    Retrieves information about the source of an event

Args:

      Event(PyEVT_HANDLE):Handle to an event
      PropertyId(int):Property to retreive, EvtEvent*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      Tuple[Any, int]
        
    """
    pass
        

def EvtGetObjectArraySize(ObjectArray:'PyEVT_HANDLE') -> 'int':
    """
    Returns the size of an array of event objects

Args:

      ObjectArray(PyEVT_HANDLE):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId'sCommentsAccepts keyword args

Returns:

      int
        
    """
    pass
        

def EvtGetObjectArrayProperty(ObjectArray:'PyEVT_HANDLE',PropertyId:'int',ArrayIndex:'int',Flags:'int'=0) -> 'Tuple[Any, int]':
    """
    Retrieves an item from an object array

Args:

      ObjectArray(PyEVT_HANDLE):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId's
      PropertyId(int):Type of property contained in the array
      ArrayIndex(int):Zero-based index of item to retrieve
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*)

Returns:

      Tuple[Any, int]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*)

        
    """
    pass
        
EVENTLOG_AUDIT_FAILURE = ...
EVENTLOG_AUDIT_SUCCESS = ...
EVENTLOG_BACKWARDS_READ = ...
EVENTLOG_END_ALL_PAIRED_EVENTS = ...
EVENTLOG_END_PAIRED_EVENT = ...
EVENTLOG_ERROR_TYPE = ...
EVENTLOG_FORWARDS_READ = ...
EVENTLOG_INFORMATION_TYPE = ...
EVENTLOG_PAIRED_EVENT_ACTIVE = ...
EVENTLOG_PAIRED_EVENT_INACTIVE = ...
EVENTLOG_SEEK_READ = ...
EVENTLOG_SEQUENTIAL_READ = ...
EVENTLOG_START_PAIRED_EVENT = ...
EVENTLOG_SUCCESS = ...
EVENTLOG_WARNING_TYPE = ...
EventMetadataEventChannel = ...
EventMetadataEventID = ...
EventMetadataEventKeyword = ...
EventMetadataEventLevel = ...
EventMetadataEventMessageID = ...
EventMetadataEventOpcode = ...
EventMetadataEventTask = ...
EventMetadataEventTemplate = ...
EventMetadataEventVersion = ...
EvtChannelConfigAccess = ...
EvtChannelConfigClassicEventlog = ...
EvtChannelConfigEnabled = ...
EvtChannelConfigIsolation = ...
EvtChannelConfigOwningPublisher = ...
EvtChannelConfigPropertyIdEND = ...
EvtChannelConfigType = ...
EvtChannelLoggingConfigAutoBackup = ...
EvtChannelLoggingConfigLogFilePath = ...
EvtChannelLoggingConfigMaxSize = ...
EvtChannelLoggingConfigRetention = ...
EvtChannelPublisherList = ...
EvtChannelPublishingConfigBufferSize = ...
EvtChannelPublishingConfigClockType = ...
EvtChannelPublishingConfigControlGuid = ...
EvtChannelPublishingConfigFileMax = ...
EvtChannelPublishingConfigKeywords = ...
EvtChannelPublishingConfigLatency = ...
EvtChannelPublishingConfigLevel = ...
EvtChannelPublishingConfigMaxBuffers = ...
EvtChannelPublishingConfigMinBuffers = ...
EvtChannelPublishingConfigSidType = ...
EvtEventMetadataPropertyIdEND = ...
EvtEventPath = ...
EvtEventPropertyIdEND = ...
EvtEventQueryIDs = ...
EvtExportLogChannelPath = ...
EvtExportLogFilePath = ...
EvtExportLogTolerateQueryErrors = ...
EvtLogAttributes = ...
EvtLogCreationTime = ...
EvtLogFileSize = ...
EvtLogFull = ...
EvtLogLastAccessTime = ...
EvtLogLastWriteTime = ...
EvtLogNumberOfLogRecords = ...
EvtLogOldestRecordNumber = ...
EvtOpenChannelPath = ...
EvtOpenFilePath = ...
EvtPublisherMetadataChannelReferenceFlags = ...
EvtPublisherMetadataChannelReferenceID = ...
EvtPublisherMetadataChannelReferenceIndex = ...
EvtPublisherMetadataChannelReferenceMessageID = ...
EvtPublisherMetadataChannelReferencePath = ...
EvtPublisherMetadataChannelReferences = ...
EvtPublisherMetadataHelpLink = ...
EvtPublisherMetadataKeywordMessageID = ...
EvtPublisherMetadataKeywordName = ...
EvtPublisherMetadataKeywords = ...
EvtPublisherMetadataKeywordValue = ...
EvtPublisherMetadataLevelMessageID = ...
EvtPublisherMetadataLevelName = ...
EvtPublisherMetadataLevels = ...
EvtPublisherMetadataLevelValue = ...
EvtPublisherMetadataMessageFilePath = ...
EvtPublisherMetadataOpcodeMessageID = ...
EvtPublisherMetadataOpcodeName = ...
EvtPublisherMetadataOpcodes = ...
EvtPublisherMetadataOpcodeValue = ...
EvtPublisherMetadataParameterFilePath = ...
EvtPublisherMetadataPropertyIdEND = ...
EvtPublisherMetadataPublisherGuid = ...
EvtPublisherMetadataPublisherMessageID = ...
EvtPublisherMetadataResourceFilePath = ...
EvtPublisherMetadataTaskEventGuid = ...
EvtPublisherMetadataTaskMessageID = ...
EvtPublisherMetadataTaskName = ...
EvtPublisherMetadataTasks = ...
EvtPublisherMetadataTaskValue = ...
EvtQueryChannelPath = ...
EvtQueryFilePath = ...
EvtQueryForwardDirection = ...
EvtQueryReverseDirection = ...
EvtQueryTolerateQueryErrors = ...
EvtRenderBookmark = ...
EvtRenderEventValues = ...
EvtRenderEventXml = ...
EvtRpcLogin = ...
EvtRpcLoginAuthDefault = ...
EvtRpcLoginAuthKerberos = ...
EvtRpcLoginAuthNegotiate = ...
EvtRpcLoginAuthNTLM = ...
EvtSeekOriginMask = ...
EvtSeekRelativeToBookmark = ...
EvtSeekRelativeToCurrent = ...
EvtSeekRelativeToFirst = ...
EvtSeekRelativeToLast = ...
EvtSeekStrict = ...
EvtSubscribeActionDeliver = ...
EvtSubscribeActionError = ...
EvtSubscribeOriginMask = ...
EvtSubscribeStartAfterBookmark = ...
EvtSubscribeStartAtOldestRecord = ...
EvtSubscribeStrict = ...
EvtSubscribeToFutureEvents = ...
EvtSubscribeTolerateQueryErrors = ...
EvtVarTypeAnsiString = ...
EvtVarTypeBinary = ...
EvtVarTypeBoolean = ...
EvtVarTypeByte = ...
EvtVarTypeDouble = ...
EvtVarTypeEvtHandle = ...
EvtVarTypeEvtXml = ...
EvtVarTypeFileTime = ...
EvtVarTypeGuid = ...
EvtVarTypeHexInt32 = ...
EvtVarTypeHexInt64 = ...
EvtVarTypeInt16 = ...
EvtVarTypeInt32 = ...
EvtVarTypeInt64 = ...
EvtVarTypeNull = ...
EvtVarTypeSByte = ...
EvtVarTypeSid = ...
EvtVarTypeSingle = ...
EvtVarTypeSizeT = ...
EvtVarTypeString = ...
EvtVarTypeSysTime = ...
EvtVarTypeUInt16 = ...
EvtVarTypeUInt32 = ...
EvtVarTypeUInt64 = ...