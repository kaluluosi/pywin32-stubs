from pywintypes import *
__all__=['ReadEventLog', 'ClearEventLog', 'BackupEventLog', 'CloseEventLog', 'DeregisterEventSource', 'NotifyChangeEventLog', 'GetNumberOfEventLogRecords', 'GetOldestEventLogRecord', 'OpenEventLog', 'RegisterEventSource', 'OpenBackupEventLog', 'ReportEvent', 'EvtOpenChannelEnum', 'EvtNextChannelPath', 'EvtOpenLog', 'EvtClearLog', 'EvtExportLog', 'EvtArchiveExportedLog', 'EvtGetExtendedStatus', 'EvtQuery', 'EvtNext', 'EvtSeek', 'EvtRender', 'EvtSubscribe', 'EvtCreateBookmark', 'EvtUpdateBookmark', 'EvtGetChannelConfigProperty', 'EvtOpenChannelConfig', 'EvtOpenSession', 'EvtOpenPublisherEnum', 'EvtNextPublisherId', 'EvtOpenPublisherMetadata', 'EvtGetPublisherMetadataProperty', 'EvtOpenEventMetadataEnum', 'EvtNextEventMetadata', 'EvtGetEventMetadataProperty', 'EvtGetLogInfo', 'EvtGetEventInfo', 'EvtGetObjectArraySize', 'EvtGetObjectArrayProperty', 'EVENTLOG_AUDIT_FAILURE', 'EVENTLOG_AUDIT_SUCCESS', 'EVENTLOG_BACKWARDS_READ', 'EVENTLOG_END_ALL_PAIRED_EVENTS', 'EVENTLOG_END_PAIRED_EVENT', 'EVENTLOG_ERROR_TYPE', 'EVENTLOG_FORWARDS_READ', 'EVENTLOG_INFORMATION_TYPE', 'EVENTLOG_PAIRED_EVENT_ACTIVE', 'EVENTLOG_PAIRED_EVENT_INACTIVE', 'EVENTLOG_SEEK_READ', 'EVENTLOG_SEQUENTIAL_READ', 'EVENTLOG_START_PAIRED_EVENT', 'EVENTLOG_SUCCESS', 'EVENTLOG_WARNING_TYPE', 'EventMetadataEventChannel', 'EventMetadataEventID', 'EventMetadataEventKeyword', 'EventMetadataEventLevel', 'EventMetadataEventMessageID', 'EventMetadataEventOpcode', 'EventMetadataEventTask', 'EventMetadataEventTemplate', 'EventMetadataEventVersion', 'EvtChannelConfigAccess', 'EvtChannelConfigClassicEventlog', 'EvtChannelConfigEnabled', 'EvtChannelConfigIsolation', 'EvtChannelConfigOwningPublisher', 'EvtChannelConfigPropertyIdEND', 'EvtChannelConfigType', 'EvtChannelLoggingConfigAutoBackup', 'EvtChannelLoggingConfigLogFilePath', 'EvtChannelLoggingConfigMaxSize', 'EvtChannelLoggingConfigRetention', 'EvtChannelPublisherList', 'EvtChannelPublishingConfigBufferSize', 'EvtChannelPublishingConfigClockType', 'EvtChannelPublishingConfigControlGuid', 'EvtChannelPublishingConfigFileMax', 'EvtChannelPublishingConfigKeywords', 'EvtChannelPublishingConfigLatency', 'EvtChannelPublishingConfigLevel', 'EvtChannelPublishingConfigMaxBuffers', 'EvtChannelPublishingConfigMinBuffers', 'EvtChannelPublishingConfigSidType', 'EvtEventMetadataPropertyIdEND', 'EvtEventPath', 'EvtEventPropertyIdEND', 'EvtEventQueryIDs', 'EvtExportLogChannelPath', 'EvtExportLogFilePath', 'EvtExportLogTolerateQueryErrors', 'EvtLogAttributes', 'EvtLogCreationTime', 'EvtLogFileSize', 'EvtLogFull', 'EvtLogLastAccessTime', 'EvtLogLastWriteTime', 'EvtLogNumberOfLogRecords', 'EvtLogOldestRecordNumber', 'EvtOpenChannelPath', 'EvtOpenFilePath', 'EvtPublisherMetadataChannelReferenceFlags', 'EvtPublisherMetadataChannelReferenceID', 'EvtPublisherMetadataChannelReferenceIndex', 'EvtPublisherMetadataChannelReferenceMessageID', 'EvtPublisherMetadataChannelReferencePath', 'EvtPublisherMetadataChannelReferences', 'EvtPublisherMetadataHelpLink', 'EvtPublisherMetadataKeywordMessageID', 'EvtPublisherMetadataKeywordName', 'EvtPublisherMetadataKeywords', 'EvtPublisherMetadataKeywordValue', 'EvtPublisherMetadataLevelMessageID', 'EvtPublisherMetadataLevelName', 'EvtPublisherMetadataLevels', 'EvtPublisherMetadataLevelValue', 'EvtPublisherMetadataMessageFilePath', 'EvtPublisherMetadataOpcodeMessageID', 'EvtPublisherMetadataOpcodeName', 'EvtPublisherMetadataOpcodes', 'EvtPublisherMetadataOpcodeValue', 'EvtPublisherMetadataParameterFilePath', 'EvtPublisherMetadataPropertyIdEND', 'EvtPublisherMetadataPublisherGuid', 'EvtPublisherMetadataPublisherMessageID', 'EvtPublisherMetadataResourceFilePath', 'EvtPublisherMetadataTaskEventGuid', 'EvtPublisherMetadataTaskMessageID', 'EvtPublisherMetadataTaskName', 'EvtPublisherMetadataTasks', 'EvtPublisherMetadataTaskValue', 'EvtQueryChannelPath', 'EvtQueryFilePath', 'EvtQueryForwardDirection', 'EvtQueryReverseDirection', 'EvtQueryTolerateQueryErrors', 'EvtRenderBookmark', 'EvtRenderEventValues', 'EvtRenderEventXml', 'EvtRpcLogin', 'EvtRpcLoginAuthDefault', 'EvtRpcLoginAuthKerberos', 'EvtRpcLoginAuthNegotiate', 'EvtRpcLoginAuthNTLM', 'EvtSeekOriginMask', 'EvtSeekRelativeToBookmark', 'EvtSeekRelativeToCurrent', 'EvtSeekRelativeToFirst', 'EvtSeekRelativeToLast', 'EvtSeekStrict', 'EvtSubscribeActionDeliver', 'EvtSubscribeActionError', 'EvtSubscribeOriginMask', 'EvtSubscribeStartAfterBookmark', 'EvtSubscribeStartAtOldestRecord', 'EvtSubscribeStrict', 'EvtSubscribeToFutureEvents', 'EvtSubscribeTolerateQueryErrors', 'EvtVarTypeAnsiString', 'EvtVarTypeBinary', 'EvtVarTypeBoolean', 'EvtVarTypeByte', 'EvtVarTypeDouble', 'EvtVarTypeEvtHandle', 'EvtVarTypeEvtXml', 'EvtVarTypeFileTime', 'EvtVarTypeGuid', 'EvtVarTypeHexInt32', 'EvtVarTypeHexInt64', 'EvtVarTypeInt16', 'EvtVarTypeInt32', 'EvtVarTypeInt64', 'EvtVarTypeNull', 'EvtVarTypeSByte', 'EvtVarTypeSid', 'EvtVarTypeSingle', 'EvtVarTypeSizeT', 'EvtVarTypeString', 'EvtVarTypeSysTime', 'EvtVarTypeUInt16', 'EvtVarTypeUInt32', 'EvtVarTypeUInt64']
import typing
""""""


def ReadEventLog(Handle:typing.Any,Flags:int,Offset:int,Size:int=4096) -> typing.Any:
    """
    Reads some event log records.


Args:

      Handle(typing.Any):Handle to a an opened event log (see win32evtlog::OpenEventLog)
      Flags(int):Reading flags
      Offset(int):Record offset to read (in SEEK mode).
      Size(int):Output buffer size.Return ValueIf there are no event log records available, then an empty list is returned.

Returns:

      typing.Any:Output buffer size.
Return ValueIf there are no event log records available, then an empty list is returned.

        
    """
    pass


def ClearEventLog(handle:int,eventLogName:typing.Any) -> None:
    """
    Clears the event log


Args:

      handle(int):Handle to the event log to clear.
      eventLogName(typing.Any):The name of the event log to save to, or None

Returns:

      None
        
    """
    pass


def BackupEventLog(handle:int,eventLogName:typing.Any) -> None:
    """
    Backs up the event log


Args:

      handle(int):Handle to the event log to backup.
      eventLogName(typing.Any):The name of the event log to save to

Returns:

      None
        
    """
    pass


def CloseEventLog(handle:int) -> None:
    """
    Closes the eventlog


Args:

      handle(int):Handle to the event log to close

Returns:

      None
        
    """
    pass


def DeregisterEventSource(handle:int) -> None:
    """
    Deregisters an Event Source


Args:

      handle(int):Identifies the event log whose handle was returned by win32evtlog::RegisterEventSource

Returns:

      None
        
    """
    pass


def NotifyChangeEventLog(handle:int,handle1:int) -> None:
    """
    Lets an application receive notification when an event is written to the event log file specified by the hEventLog parameter. When the event is written to the event log file, the function causes the event object specified by the hEvent parameter to become signaled.


Args:

      handle(int):Handle to an event log file, obtained by calling win32evtlog::OpenEventLog function. When an event is written to this log file, the event specified by hEvent becomes signaled.
      handle1(int):A handle to a Win32 event. This is the event that becomes signaled when an event is written to the event log file specified by the hEventLog parameter.

Returns:

      None
        
    """
    pass


def GetNumberOfEventLogRecords(handle:int) -> int:
    """
    Returns the number of event log records.


Args:

      handle(int):Handle to the event log to query.

Returns:

      int
        
    """
    pass


def GetOldestEventLogRecord() -> int:
    """
    Returns the number of event log records.


Args:



Returns:

      int:win32evtlog.GetOldestEventLogRecord

int = GetOldestEventLogRecord()Returns the number of event log records.
Return ValueThe result is the absolute record number of the oldest record in the given event log.

        
    """
    pass


def OpenEventLog(serverName:typing.Any,sourceName:typing.Any) -> typing.Any:
    """
    Opens an event log.


Args:

      serverName(typing.Any):The server name, or None
      sourceName(typing.Any):specifies the name of the source that the returned handle will reference. The source name must be a subkey of a logfile entry under the EventLog key in the registry.

Returns:

      typing.Any
        
    """
    pass


def RegisterEventSource(serverName:typing.Any,sourceName:typing.Any) -> int:
    """
    Registers an Event Source


Args:

      serverName(typing.Any):The server name, or None
      sourceName(typing.Any):The source name

Returns:

      int
        
    """
    pass


def OpenBackupEventLog(serverName:typing.Any,fileName:typing.Any) -> typing.Any:
    """
    Opens a previously saved event log.


Args:

      serverName(typing.Any):The server name, or None
      fileName(typing.Any):The filename to open

Returns:

      typing.Any
        
    """
    pass


def ReportEvent(EventLog:typing.Any,Type:int,Category:int,EventID:int,UserSid:typing.Any,Strings:typing.Any,RawData:str) -> None:
    """
    Reports an event


Args:

      EventLog(typing.Any):Handle to an event log
      Type(int):win32con.EVENTLOG_* value
      Category(int):Source-specific event category
      EventID(int):Source-specific event identifier
      UserSid(typing.Any):Sid of current user, can be None
      Strings(typing.Any):Sequence of unicode strings to be inserted in message
      RawData(str):Binary data for event, can be None

Returns:

      None
        
    """
    pass


def EvtOpenChannelEnum(Session:typing.Any=None,Flags:int=0) -> typing.Any:
    """
    Begins an enumeration of event channels


Args:

      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtNextChannelPath(ChannelEnum:typing.Any) -> str:
    """
    Retrieves a channel path from an enumeration


Args:

      ChannelEnum(typing.Any):Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      str:Handle to an enumeration as returned by win32evtlog::EvtOpenChannelEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass


def EvtOpenLog(Path:str,Flags:int,Session:typing.Any=None) -> typing.Any:
    """
    Opens an event log or exported log archive


Args:

      Path(str):Event log name or Path of an export file
      Flags(int):EvtOpenChannelPath (1) or EvtOpenFilePath (2)
      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtClearLog(ChannelPath:str,TargetFilePath:str=None,Session:typing.Any=None,Flags:int=0) -> None:
    """
    Clears an event log and optionally exports events to an archive


Args:

      ChannelPath(str):Name of event log to be cleared
      TargetFilePath(str):Name of file in which cleared events will be archived, or None
      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass


def EvtExportLog(Path:str,TargetFilePath:str,Flags:int,Query:str=None,Session:typing.Any=None) -> None:
    """
    Exports events from a channel or log file


Args:

      Path(str):Path of a live event log channel or exported log file
      TargetFilePath(str):File to create, cannot already exist
      Flags(int):Combination of EvtExportLog* flags specifying the type of path
      Query(str):Selects specific events to export
      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      None
        
    """
    pass


def EvtArchiveExportedLog(LogFilePath:str,Locale:int,Session:typing.Any=None,Flags:int=0) -> None:
    """
    Localizes an exported event log file


Args:

      LogFilePath(str):Filename of an exported log file
      Locale(int):Locale id
      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):ReservedCommentsAccepts keyword args

Returns:

      None
        
    """
    pass


def EvtGetExtendedStatus() -> str:
    """
    Returns additional error info from last Evt* call


Args:



Returns:

      str
        
    """
    pass


def EvtQuery(Path:str,Flags:int,Query:str=None,Session:typing.Any=None) -> typing.Any:
    """
    Opens a query over a log channel or exported log file


Args:

      Path(str):Log channel or exported log file, depending on Flags
      Flags(int):Combination of EVT_QUERY_FLAGS (EvtQuery*)
      Query(str):Selects events to return, None or '*' for all events
      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtNext(ResultSet:typing.Any,Count:int,Timeout:int=-1,Flags:int=0) -> typing.Any:
    """
    Returns events from a query


Args:

      ResultSet(typing.Any):Handle to event query or subscription
      Count(int):Number of events to return
      Timeout(int):Time to wait in milliseconds, use -1 for infinite
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns a tuple of handles to events.  If no items are available, returns an empty tuple instead of raising an exception.

Returns:

      typing.Any:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns a tuple of handles to events.  If no items are available, returns 

an empty tuple instead of raising an exception.

        
    """
    pass


def EvtSeek(ResultSet:typing.Any,Position:int,Flags:int,Bookmark:typing.Any=None,Timeout:int=0) -> None:
    """
    Changes the current position in a result set


Args:

      ResultSet(typing.Any):Handle to event query or subscription
      Position(int):Offset (base from which to seek is specified by Flags)
      Flags(int):EvtSeekRelative* flag indicating seek origin
      Bookmark(typing.Any):Used as seek origin only if Flags contains EvtSeekRelativeToBookmark
      Timeout(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      None
        
    """
    pass


def EvtRender(Event:typing.Any,Flags:int) -> str:
    """
    Formats an event into XML text


Args:

      Event(typing.Any):Handle to an event or bookmark
      Flags(int):EvtRenderEventXml or EvtRenderBookmark indicating type of handleCommentsAccepts keyword argsRendering event values (Flags=EvtRenderEventValues) is not currently supported

Returns:

      str
        
    """
    pass


def EvtSubscribe(ChannelPath:str,Flags:int,SignalEvent:typing.Any=None,Callback:typing.Any=None,Context:typing.Any=None,Query:str=None,Session:typing.Any=None,Bookmark:typing.Any=None) -> typing.Any:
    """
    Requests notification for events


Args:

      ChannelPath(str):Name of an event log channel
      Flags(int):Combination of EvtSubscribe* flags determining how subscription is initiated
      SignalEvent(typing.Any):An event handle to be set when events are available (see win32event::CreateEvent)
      Callback(typing.Any):Python function to be called with each event
      Context(typing.Any):Arbitrary object to be passed to the callback function
      Query(str):XML query used to select specific events, use None or '*' for all events
      Session(typing.Any):Handle to a session on another machine, or None for local
      Bookmark(typing.Any):If Flags contains EvtSubscribeStartAfterBookmark, used as starting pointCommentsAccepts keyword argsThe method used to receive events is determined by the parameters passed in. To create a push subscription, define a callback function that will be called with each event. The function will receive 3 args: First is an integer specifying why the function was called (EvtSubscribeActionError or EvtSubscribeActionDeliver) Second is the context object passed to EvtSubscribe. Third is the handle to an event log record (if not called due to an error) If an event handle is passed in, a pull subscription is created.  The event handle will be signalled when events are available, and the subscription handle can be passed to win32evtlog::EvtNext to obtain the events.

Returns:

      typing.Any
        
    """
    pass


def EvtCreateBookmark(BookmarkXML:str=None) -> typing.Any:
    """
    Creates a bookmark


Args:

      BookmarkXML(str):XML representation of a bookmark as returned by win32evtlog::EvtRender, or None for a new bookmarkCommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtUpdateBookmark(Bookmark:typing.Any,Event:typing.Any) -> typing.Any:
    """
    Repositions a bookmark to an event


Args:

      Bookmark(typing.Any):Handle to a bookmark
      Event(typing.Any):Handle to an eventCommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtGetChannelConfigProperty(ChannelConfig:typing.Any,PropertyId:int,Flags:int=0) -> typing.Any:
    """
    Retreives channel configuration information


Args:

      ChannelConfig(typing.Any):Config handle as returned by win32evtlog::EvtOpenChannelConfig
      PropertyId(int):Property to retreive, one of EvtChannel* constants
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Any
        
    """
    pass


def EvtOpenChannelConfig(ChannelPath:str,Session:typing.Any=None,Flags:int=0) -> typing.Any:
    """
    Opens channel configuration


Args:

      ChannelPath(str):Channel to be opened
      Session(typing.Any):Session handle as returned by win32evtlog::EvtOpenSession, or None for local machine
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtOpenSession(Login:typing.Any,LoginClass:int,Timeout:int=0,Flags:int=0) -> typing.Any:
    """
    Creates a session used to access the Event Log on another machine


Args:

      Login(typing.Any):Credentials to be used to access remote machine
      LoginClass(int):Type of login to perform, EvtRpcLogin is only defined value
      Timeout(int):Reserved, use only 0
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtOpenPublisherEnum(Session:typing.Any=None,Flags:int=0) -> typing.Any:
    """
    Begins an enumeration of event publishers


Args:

      Session(typing.Any):Handle to a remote session (see win32evtlog::EvtOpenSession), or None for local machine.
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtNextPublisherId(PublisherEnum:typing.Any) -> str:
    """
    Returns the next publisher from an enumeration


Args:

      PublisherEnum(typing.Any):Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumCommentsAccepts keyword argsReturn ValueReturns None at end of enumeration

Returns:

      str:Handle to an enumeration as returned by win32evtlog::EvtOpenPublisherEnumComments

Accepts keyword args
Return ValueReturns None at end of enumeration

        
    """
    pass


def EvtOpenPublisherMetadata(PublisherIdentity:str,Session:typing.Any=None,LogFilePath:str=None,Locale:int=0,Flags:int=0) -> typing.Any:
    """
    None


Args:

      PublisherIdentity(str):Publisher id as returned by win32evtlog::EvtNextPublisherId
      Session(typing.Any):Handle to remote session, or None for local machine
      LogFilePath(str):Log file from which to retrieve publisher, or None for locally registered publisher
      Locale(int):Locale to use for retrieved properties, use 0 for current locale
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtGetPublisherMetadataProperty(PublisherMetadata:typing.Any,PropertyId:int,Flags:int=0) -> typing.Any:
    """
    Retrieves a property from an event publisher


Args:

      PublisherMetadata(typing.Any):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      PropertyId(int):Property to retreive, EvtPublisherMetadata*
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*) Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

Returns:

      typing.Any:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*) 

Some properties return a handle (type EvtVarTypeEvtHandle) which can be iterated using 

win32evtlog::EvtGetObjectArraySize and win32evtlog::EvtGetObjectArrayProperty.

        
    """
    pass


def EvtOpenEventMetadataEnum(PublisherMetadata:typing.Any,Flags:int=0) -> typing.Any:
    """
    Enumerates the events that a publisher provides


Args:

      PublisherMetadata(typing.Any):Publisher handle as returned by win32evtlog::EvtOpenPublisherMetadata
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtNextEventMetadata(EventMetadataEnum:typing.Any,Flags:int=0) -> typing.Any:
    """
    Retrieves the next item from an event metadata enumeration


Args:

      EventMetadataEnum(typing.Any):Enumeration handle as returned by win32evtlog::EvtOpenEventMetadataEnum
      Flags(int):Reserved, use only 0CommentsAccepts keyword args

Returns:

      typing.Any
        
    """
    pass


def EvtGetEventMetadataProperty(EventMetadata:typing.Any,PropertyId:int,Flags:int=0) -> typing.Any:
    """
    Retrieves a property from an event publisher


Args:

      EventMetadata(typing.Any):Event metadata handle as returned by win32evtlog::EvtNextEventMetadata
      PropertyId(int):Property to retreive, EventMetadata*
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*).

Returns:

      typing.Any:Reserved, use only 0
Comments

Accepts keyword args
Return ValueReturns the value and type of value (EvtVarType*).

        
    """
    pass


def EvtGetLogInfo(Log:typing.Any,PropertyId:int) -> typing.Any:
    """
    Retrieves log file or channel information


Args:

      Log(typing.Any):Event log handle as returned by win32evtlog::EvtOpenLog
      PropertyId(int):Property to retreive, EvtLog*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Any
        
    """
    pass


def EvtGetEventInfo(Event:typing.Any,PropertyId:int) -> typing.Any:
    """
    Retrieves information about the source of an event


Args:

      Event(typing.Any):Handle to an event
      PropertyId(int):Property to retreive, EvtEvent*CommentsAccepts keyword argsReturns the value and type of value (EvtVarType*)

Returns:

      typing.Any
        
    """
    pass


def EvtGetObjectArraySize(ObjectArray:typing.Any) -> int:
    """
    Returns the size of an array of event objects


Args:

      ObjectArray(typing.Any):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId'sCommentsAccepts keyword args

Returns:

      int
        
    """
    pass


def EvtGetObjectArrayProperty(ObjectArray:typing.Any,PropertyId:int,ArrayIndex:int,Flags:int=0) -> typing.Any:
    """
    Retrieves an item from an object array


Args:

      ObjectArray(typing.Any):Handle to an array of objects as returned by win32evtlog::EvtGetPublisherMetadataProperty for some ProperyId's
      PropertyId(int):Type of property contained in the array
      ArrayIndex(int):Zero-based index of item to retrieve
      Flags(int):Reserved, use only 0CommentsAccepts keyword argsReturn ValueReturns the value and type of value (EvtVarType*)

Returns:

      typing.Any:Reserved, use only 0
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