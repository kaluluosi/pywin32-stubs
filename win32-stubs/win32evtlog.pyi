__all__=['', 'ReadEventLog', 'ClearEventLog', 'BackupEventLog', 'CloseEventLog', 'DeregisterEventSource', 'NotifyChangeEventLog', 'GetNumberOfEventLogRecords', 'GetOldestEventLogRecord', 'OpenEventLog', 'RegisterEventSource', 'OpenBackupEventLog', 'ReportEvent', 'EvtOpenChannelEnum', 'EvtNextChannelPath', 'EvtOpenLog', 'EvtClearLog', 'EvtExportLog', 'EvtArchiveExportedLog', 'EvtGetExtendedStatus', 'EvtQuery', 'EvtNext', 'EvtSeek', 'EvtRender', 'EvtSubscribe', 'EvtCreateBookmark', 'EvtUpdateBookmark', 'EvtGetChannelConfigProperty', 'EvtOpenChannelConfig', 'EvtOpenSession', 'EvtOpenPublisherEnum', 'EvtNextPublisherId', 'EvtOpenPublisherMetadata', 'EvtGetPublisherMetadataProperty', 'EvtOpenEventMetadataEnum', 'EvtNextEventMetadata', 'EvtGetEventMetadataProperty', 'EvtGetLogInfo', 'EvtGetEventInfo', 'EvtGetObjectArraySize', 'EvtGetObjectArrayProperty', 'EVENTLOG_AUDIT_FAILURE', 'EVENTLOG_AUDIT_SUCCESS', 'EVENTLOG_BACKWARDS_READ', 'EVENTLOG_END_ALL_PAIRED_EVENTS', 'EVENTLOG_END_PAIRED_EVENT', 'EVENTLOG_ERROR_TYPE', 'EVENTLOG_FORWARDS_READ', 'EVENTLOG_INFORMATION_TYPE', 'EVENTLOG_PAIRED_EVENT_ACTIVE', 'EVENTLOG_PAIRED_EVENT_INACTIVE', 'EVENTLOG_SEEK_READ', 'EVENTLOG_SEQUENTIAL_READ', 'EVENTLOG_START_PAIRED_EVENT', 'EVENTLOG_SUCCESS', 'EVENTLOG_WARNING_TYPE', 'EventMetadataEventChannel', 'EventMetadataEventID', 'EventMetadataEventKeyword', 'EventMetadataEventLevel', 'EventMetadataEventMessageID', 'EventMetadataEventOpcode', 'EventMetadataEventTask', 'EventMetadataEventTemplate', 'EventMetadataEventVersion', 'EvtChannelConfigAccess', 'EvtChannelConfigClassicEventlog', 'EvtChannelConfigEnabled', 'EvtChannelConfigIsolation', 'EvtChannelConfigOwningPublisher', 'EvtChannelConfigPropertyIdEND', 'EvtChannelConfigType', 'EvtChannelLoggingConfigAutoBackup', 'EvtChannelLoggingConfigLogFilePath', 'EvtChannelLoggingConfigMaxSize', 'EvtChannelLoggingConfigRetention', 'EvtChannelPublisherList', 'EvtChannelPublishingConfigBufferSize', 'EvtChannelPublishingConfigClockType', 'EvtChannelPublishingConfigControlGuid', 'EvtChannelPublishingConfigFileMax', 'EvtChannelPublishingConfigKeywords', 'EvtChannelPublishingConfigLatency', 'EvtChannelPublishingConfigLevel', 'EvtChannelPublishingConfigMaxBuffers', 'EvtChannelPublishingConfigMinBuffers', 'EvtChannelPublishingConfigSidType', 'EvtEventMetadataPropertyIdEND', 'EvtEventPath', 'EvtEventPropertyIdEND', 'EvtEventQueryIDs', 'EvtExportLogChannelPath', 'EvtExportLogFilePath', 'EvtExportLogTolerateQueryErrors', 'EvtLogAttributes', 'EvtLogCreationTime', 'EvtLogFileSize', 'EvtLogFull', 'EvtLogLastAccessTime', 'EvtLogLastWriteTime', 'EvtLogNumberOfLogRecords', 'EvtLogOldestRecordNumber', 'EvtOpenChannelPath', 'EvtOpenFilePath', 'EvtPublisherMetadataChannelReferenceFlags', 'EvtPublisherMetadataChannelReferenceID', 'EvtPublisherMetadataChannelReferenceIndex', 'EvtPublisherMetadataChannelReferenceMessageID', 'EvtPublisherMetadataChannelReferencePath', 'EvtPublisherMetadataChannelReferences', 'EvtPublisherMetadataHelpLink', 'EvtPublisherMetadataKeywordMessageID', 'EvtPublisherMetadataKeywordName', 'EvtPublisherMetadataKeywords', 'EvtPublisherMetadataKeywordValue', 'EvtPublisherMetadataLevelMessageID', 'EvtPublisherMetadataLevelName', 'EvtPublisherMetadataLevels', 'EvtPublisherMetadataLevelValue', 'EvtPublisherMetadataMessageFilePath', 'EvtPublisherMetadataOpcodeMessageID', 'EvtPublisherMetadataOpcodeName', 'EvtPublisherMetadataOpcodes', 'EvtPublisherMetadataOpcodeValue', 'EvtPublisherMetadataParameterFilePath', 'EvtPublisherMetadataPropertyIdEND', 'EvtPublisherMetadataPublisherGuid', 'EvtPublisherMetadataPublisherMessageID', 'EvtPublisherMetadataResourceFilePath', 'EvtPublisherMetadataTaskEventGuid', 'EvtPublisherMetadataTaskMessageID', 'EvtPublisherMetadataTaskName', 'EvtPublisherMetadataTasks', 'EvtPublisherMetadataTaskValue', 'EvtQueryChannelPath', 'EvtQueryFilePath', 'EvtQueryForwardDirection', 'EvtQueryReverseDirection', 'EvtQueryTolerateQueryErrors', 'EvtRenderBookmark', 'EvtRenderEventValues', 'EvtRenderEventXml', 'EvtRpcLogin', 'EvtRpcLoginAuthDefault', 'EvtRpcLoginAuthKerberos', 'EvtRpcLoginAuthNegotiate', 'EvtRpcLoginAuthNTLM', 'EvtSeekOriginMask', 'EvtSeekRelativeToBookmark', 'EvtSeekRelativeToCurrent', 'EvtSeekRelativeToFirst', 'EvtSeekRelativeToLast', 'EvtSeekStrict', 'EvtSubscribeActionDeliver', 'EvtSubscribeActionError', 'EvtSubscribeOriginMask', 'EvtSubscribeStartAfterBookmark', 'EvtSubscribeStartAtOldestRecord', 'EvtSubscribeStrict', 'EvtSubscribeToFutureEvents', 'EvtSubscribeTolerateQueryErrors', 'EvtVarTypeAnsiString', 'EvtVarTypeBinary', 'EvtVarTypeBoolean', 'EvtVarTypeByte', 'EvtVarTypeDouble', 'EvtVarTypeEvtHandle', 'EvtVarTypeEvtXml', 'EvtVarTypeFileTime', 'EvtVarTypeGuid', 'EvtVarTypeHexInt32', 'EvtVarTypeHexInt64', 'EvtVarTypeInt16', 'EvtVarTypeInt32', 'EvtVarTypeInt64', 'EvtVarTypeNull', 'EvtVarTypeSByte', 'EvtVarTypeSid', 'EvtVarTypeSingle', 'EvtVarTypeSizeT', 'EvtVarTypeString', 'EvtVarTypeSysTime', 'EvtVarTypeUInt16', 'EvtVarTypeUInt32', 'EvtVarTypeUInt64']
import typing
from win32helper import win32typing
""""""


def ReadEventLog(Handle:'typing.Any',Flags:'typing.Any',Offset:'typing.Any',Size:'typing.Any'=4096) -> 'typing.List[typing.Any]':
    """
    Reads some event log records.

Args:

      Handle(typing.Any):Handle to a an opened event log (see win32evtlog::OpenEventLog)
      Flags(typing.Any):Reading flags
      Offset(typing.Any):Record offset to read (in SEEK mode).
      Size(typing.Any):Output buffer size.Return ValueIf there are no event log records available, then an empty list is returned.

Returns:

      typing.List[typing.Any]:Output buffer size.
Return ValueIf there are no event log records available, then an empty list is returned.

        
    """
    pass
        

def ClearEventLog(handle:'typing.Any',eventLogName:'str') -> 'None':
    """
    Clears the event log

Args:

      handle(typing.Any):Handle to the event log to clear.
      eventLogName(str):The name of the event log to save to, or None

Returns:

      None
        
    """
    pass
        

def BackupEventLog(handle:'typing.Any',eventLogName:'str') -> 'None':
    """
    Backs up the event log

Args:

      handle(typing.Any):Handle to the event log to backup.
      eventLogName(str):The name of the event log to save to

Returns:

      None
        
    """
    pass
        

def CloseEventLog(handle:'typing.Any') -> 'None':
    """
    Closes the eventlog

Args:

      handle(typing.Any):Handle to the event log to close

Returns:

      None
        
    """
    pass
        

def DeregisterEventSource(handle:'typing.Any') -> 'None':
    """
    Deregisters an Event Source

Args:

      handle(typing.Any):Identifies the event log whose handle was returned by win32evtlog::RegisterEventSource

Returns:

      None
        
    """
    pass
        

def NotifyChangeEventLog(handle:'typing.Any',handle1:'typing.Any') -> 'None':
    """
    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.

Args:

      handle(typing.Any):Handle to an event log file, obtained by calling win32evtlog::OpenEventLog function. When an event is written to this log file, the event specified by hEvent becomes signaled.
      handle1(typing.Any):A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.

Returns:

      None
        
    """
    pass
        

def GetNumberOfEventLogRecords(handle:'typing.Any') -> 'typing.Any':
    """
    Returns the number of event log records.

Args:

      handle(typing.Any):Handle to the event log to query.

Returns:

      typing.Any
        
    """
    pass
        

def GetOldestEventLogRecord() -> 'typing.Any':
    """
    Returns the number of event log records.

Args:



Returns:

      typing.Any:win32evtlog.GetOldestEventLogRecord

int = GetOldestEventLogRecord()Returns the number of event log records.
Return ValueThe result is the absolute record number of the oldest record in the given event log.

        
    """
    pass
        

def OpenEventLog(serverName:'str',sourceName:'str') -> 'win32typing.PyEVTLOG_HANDLE':
    """
    Opens an event log.

Args:

      serverName(str):The server name, or None
      sourceName(str):specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.

Returns:

      win32typing.PyEVTLOG_HANDLE
        
    """
    pass
        

def RegisterEventSource(serverName:'str',sourceName:'str') -> 'typing.Any':
    """
    Registers an Event Source

Args:

      serverName(str):The server name, or None
      sourceName(str):The source name

Returns:

      typing.Any
        
    """
    pass
        

def OpenBackupEventLog(serverName:'str',fileName:'str') -> 'win32typing.PyEVTLOG_HANDLE':
    """
    Opens a previously saved event log.

Args:

      serverName(str):The server name, or None
      fileName(str):The filename to open

Returns:

      win32typing.PyEVTLOG_HANDLE
        
    """
    pass
        

def ReportEvent(EventLog:'int',Type:'typing.Any',Category:'typing.Any',EventID:'typing.Any',UserSid:'win32typing.PySID',Strings:'typing.Any',RawData:'typing.Any') -> 'None':
    """
    Reports an event

Args:

      EventLog(int):Handle to an event log
      Type(typing.Any):win32con.EVENTLOG_* value
      Category(typing.Any):Source-specific event category
      EventID(typing.Any):Source-specific event identifier
      UserSid(win32typing.PySID):Sid of current user, can be None
      Strings(typing.Any):Sequence of unicode strings to be inserted in message
      RawData(typing.Any):Binary data for event, can be None

Returns:

      None
        
    """
    pass
        

def EvtOpenChannelEnum(Session:'win32typing.PyEVT_HANDLE'=None,Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Begins an enumeration of event channels

Args:

      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtNextChannelPath(ChannelEnum:'win32typing.PyEVT_HANDLE') -> 'typing.Any':
    """
    Retrieves a channel path from an enumeration

Args:

      ChannelEnum(win32typing.PyEVT_HANDLE):Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      typing.Any:Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass
        

def EvtOpenLog(Path:'typing.Any',Flags:'typing.Any',Session:'win32typing.PyEVT_HANDLE'=None) -> 'win32typing.PyEVT_HANDLE':
    """
    Opens an event log or exported log archive

Args:

      Path(typing.Any):Event log name or Path of an export file
      Flags(typing.Any):EvtOpenChannelPath (1) or EvtOpenFilePath (2)
      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtClearLog(ChannelPath:'typing.Any',TargetFilePath:'typing.Any'=None,Session:'win32typing.PyEVT_HANDLE'=None,Flags:'typing.Any'=0) -> 'None':
    """
    Clears an event log and optionally exports events to an archive

Args:

      ChannelPath(typing.Any):Name of event log to be cleared
      TargetFilePath(typing.Any):Name of file in which cleared events will be archived, or None
      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtExportLog(Path:'typing.Any',TargetFilePath:'typing.Any',Flags:'typing.Any',Query:'typing.Any'=None,Session:'win32typing.PyEVT_HANDLE'=None) -> 'None':
    """
    Exports events from a channel or log file

Args:

      Path(typing.Any):Path of a live event log channel or exported log file
      TargetFilePath(typing.Any):File to create, cannot already exist
      Flags(typing.Any):Combination of EvtExportLog* flags specifying the type of path
      Query(typing.Any):Selects specific events to export
      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtArchiveExportedLog(LogFilePath:'typing.Any',Locale:'typing.Any',Session:'win32typing.PyEVT_HANDLE'=None,Flags:'typing.Any'=0) -> 'None':
    """
    Localizes an exported event log file

Args:

      LogFilePath(typing.Any):Filename of an exported log file
      Locale(typing.Any):Locale id
      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(typing.Any):ReservedCommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtGetExtendedStatus() -> 'typing.Any':
    """
    Returns additional error info from last Evt* call

Args:



Returns:

      typing.Any
        
    """
    pass
        

def EvtQuery(Path:'typing.Any',Flags:'typing.Any',Query:'typing.Any'=None,Session:'win32typing.PyEVT_HANDLE'=None) -> 'win32typing.PyEVT_HANDLE':
    """
    Opens a query over a log channel or exported log file

Args:

      Path(typing.Any):Log channel or exported log file, depending on Flags
      Flags(typing.Any):Combination of EVT_QUERY_FLAGS (EvtQuery*)
      Query(typing.Any):Selects events to return, None or '*' for all events
      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtNext(ResultSet:'win32typing.PyEVT_HANDLE',Count:'typing.Any',Timeout:'typing.Any'=-1,Flags:'typing.Any'=0) -> 'typing.Tuple[win32typing.PyEVT_HANDLE, ...]':
    """
    Returns events from a query

Args:

      ResultSet(win32typing.PyEVT_HANDLE):Handle to event query or subscription
      Count(typing.Any):Number of events to return
      Timeout(typing.Any):Time to wait in milliseconds, use -1 for infinite
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns a tuple of handles to events.  If no items are available, returns an empty tuple instead of raising an exception.

Returns:

      typing.Tuple[win32typing.PyEVT_HANDLE, ...]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns a tuple of handles to events.  If no items are available, returns 

an empty tuple instead of raising an exception.

        
    """
    pass
        

def EvtSeek(ResultSet:'win32typing.PyEVT_HANDLE',Position:'typing.Any',Flags:'typing.Any',Bookmark:'win32typing.PyEVT_HANDLE'=None,Timeout:'typing.Any'=0) -> 'None':
    """
    Changes the current position in a result set

Args:

      ResultSet(win32typing.PyEVT_HANDLE):Handle to event query or subscription
      Position(typing.Any):Offset (base from which to seek is specified by Flags)
      Flags(typing.Any):EvtSeekRelative* flag indicating seek origin
      Bookmark(win32typing.PyEVT_HANDLE):Used as seek origin only if Flags contains EvtSeekRelativeToBookmark
      Timeout(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass
        

def EvtRender(Event:'win32typing.PyEVT_HANDLE',Flags:'typing.Any') -> 'typing.Any':
    """
    Formats an event into XML text

Args:

      Event(win32typing.PyEVT_HANDLE):Handle to an event or bookmark
      Flags(typing.Any):EvtRenderEventXml or EvtRenderBookmark indicating type of handleCommentsAccepts keyword argsRendering event values (Flags=EvtRenderEventValues) is not currently supported

Returns:

      typing.Any
        
    """
    pass
        

def EvtSubscribe(ChannelPath:'typing.Any',Flags:'typing.Any',SignalEvent:'typing.Any'=None,Callback:'typing.Any'=None,Context:'typing.Any'=None,Query:'typing.Any'=None,Session:'win32typing.PyEVT_HANDLE'=None,Bookmark:'win32typing.PyEVT_HANDLE'=None) -> 'win32typing.PyEVT_HANDLE':
    """
    Requests notification for events

Args:

      ChannelPath(typing.Any):Name of an event log channel
      Flags(typing.Any):Combination of EvtSubscribe* flags determining how subscription is initiated
      SignalEvent(typing.Any):An event handle to be set when events are available (see win32event::CreateEvent)
      Callback(typing.Any):Python function to be called with each event
      Context(typing.Any):Arbitrary object to be passed to the callback function
      Query(typing.Any):XML query used to select specific events, use None or '*' for all events
      Session(win32typing.PyEVT_HANDLE):Handle to a session on another machine, or None for local
      Bookmark(win32typing.PyEVT_HANDLE):If Flags contains EvtSubscribeStartAfterBookmark, used as starting pointCommentsAccepts keyword argsThe method used to receive events is determined by the parameters passed in. To create a push subscription, define a callback function that will be called with each event. The function will receive 3 args: First is an integer specifying why the function was called (EvtSubscribeActionError or EvtSubscribeActionDeliver) Second is the context object passed to EvtSubscribe. Third is the handle to an event log record (if not called due to an error) If an event handle is passed in, a pull subscription is created.  The event handle will be signalled when events are available, and the subscription handle can be passed to win32evtlog::EvtNext to obtain the events.

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtCreateBookmark(BookmarkXML:'typing.Any'=None) -> 'win32typing.PyEVT_HANDLE':
    """
    Creates a bookmark

Args:

      BookmarkXML(typing.Any):XML representation of a bookmark as returned by win32evtlog::EvtRender, or None for a new bookmarkCommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtUpdateBookmark(Bookmark:'win32typing.PyEVT_HANDLE',Event:'win32typing.PyEVT_HANDLE') -> 'win32typing.PyEVT_HANDLE':
    """
    Repositions a bookmark to an event

Args:

      Bookmark(win32typing.PyEVT_HANDLE):Handle to a bookmark
      Event(win32typing.PyEVT_HANDLE):Handle to an eventCommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtGetChannelConfigProperty(ChannelConfig:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any',Flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retreives channel configuration information

Args:

      ChannelConfig(win32typing.PyEVT_HANDLE):Config handle as returned by win32evtlog::EvtOpenChannelConfig
      PropertyId(typing.Any):Property to retreive, one of EvtChannel* constants
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def EvtOpenChannelConfig(ChannelPath:'typing.Any',Session:'win32typing.PyEVT_HANDLE'=None,Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Opens channel configuration

Args:

      ChannelPath(typing.Any):Channel to be opened
      Session(win32typing.PyEVT_HANDLE):Session handle as returned by win32evtlog::EvtOpenSession, or None for local machine
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtOpenSession(Login:'win32typing.PyEVT_RPC_LOGIN',LoginClass:'typing.Any',Timeout:'typing.Any'=0,Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Creates a session used to access the Event Log on another machine

Args:

      Login(win32typing.PyEVT_RPC_LOGIN):Credentials to be used to access remote machine
      LoginClass(typing.Any):Type of login to perform, EvtRpcLogin is only defined value
      Timeout(typing.Any):Reserved, use only 0
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtOpenPublisherEnum(Session:'win32typing.PyEVT_HANDLE'=None,Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Begins an enumeration of event publishers

Args:

      Session(win32typing.PyEVT_HANDLE):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtNextPublisherId(PublisherEnum:'win32typing.PyEVT_HANDLE') -> 'typing.Any':
    """
    Returns the next publisher from an enumeration

Args:

      PublisherEnum(win32typing.PyEVT_HANDLE):Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      typing.Any:Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass
        

def EvtOpenPublisherMetadata(PublisherIdentity:'typing.Any',Session:'win32typing.PyEVT_HANDLE'=None,LogFilePath:'typing.Any'=None,Locale:'typing.Any'=0,Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    None

Args:

      PublisherIdentity(typing.Any):Publisher id as returned by win32evtlog::EvtNextPublisherId
      Session(win32typing.PyEVT_HANDLE):Handle to remote session, or None for local machine
      LogFilePath(typing.Any):Log file from which to retrieve publisher, or None for locally registered publisher
      Locale(typing.Any):Locale to use for retrieved properties, use 0 for current locale
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtGetPublisherMetadataProperty(PublisherMetadata:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any',Flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves a property from an event publisher

Args:

      PublisherMetadata(win32typing.PyEVT_HANDLE):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      PropertyId(typing.Any):Property to retreive, EvtPublisherMetadata*
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*) Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

Returns:

      typing.Tuple[typing.Any, typing.Any]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*) 

Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using 

win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

        
    """
    pass
        

def EvtOpenEventMetadataEnum(PublisherMetadata:'win32typing.PyEVT_HANDLE',Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Enumerates the events that a publisher provides

Args:

      PublisherMetadata(win32typing.PyEVT_HANDLE):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtNextEventMetadata(EventMetadataEnum:'win32typing.PyEVT_HANDLE',Flags:'typing.Any'=0) -> 'win32typing.PyEVT_HANDLE':
    """
    Retrieves the next item from an event metadata enumeration

Args:

      EventMetadataEnum(win32typing.PyEVT_HANDLE):Enumeration handle as returned by win32evtlog::EvtOpenEventMetadataEnum
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword args

Returns:

      win32typing.PyEVT_HANDLE
        
    """
    pass
        

def EvtGetEventMetadataProperty(EventMetadata:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any',Flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves a property from an event publisher

Args:

      EventMetadata(win32typing.PyEVT_HANDLE):Event metadata handle as returned by win32evtlog::EvtNextEventMetadata
      PropertyId(typing.Any):Property to retreive, EventMetadata*
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*).

Returns:

      typing.Tuple[typing.Any, typing.Any]:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*).

        
    """
    pass
        

def EvtGetLogInfo(Log:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves log file or channel information

Args:

      Log(win32typing.PyEVT_HANDLE):Event log handle as returned by win32evtlog::EvtOpenLog
      PropertyId(typing.Any):Property to retreive, EvtLog*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def EvtGetEventInfo(Event:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves information about the source of an event

Args:

      Event(win32typing.PyEVT_HANDLE):Handle to an event
      PropertyId(typing.Any):Property to retreive, EvtEvent*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Tuple[typing.Any, typing.Any]
        
    """
    pass
        

def EvtGetObjectArraySize(ObjectArray:'win32typing.PyEVT_HANDLE') -> 'typing.Any':
    """
    Returns the size of an array of event objects

Args:

      ObjectArray(win32typing.PyEVT_HANDLE):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId'sCommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass
        

def EvtGetObjectArrayProperty(ObjectArray:'win32typing.PyEVT_HANDLE',PropertyId:'typing.Any',ArrayIndex:'typing.Any',Flags:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Retrieves an item from an object array

Args:

      ObjectArray(win32typing.PyEVT_HANDLE):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId's
      PropertyId(typing.Any):Type of property contained in the array
      ArrayIndex(typing.Any):Zero-based index of item to retrieve
      Flags(typing.Any):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*)

Returns:

      typing.Tuple[typing.Any, typing.Any]:Reserved, use only 0
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