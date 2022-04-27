__all__=['', 'CancelWaitableTimer', 'CreateEvent', 'CreateMutex', 'CreateSemaphore', 'CreateWaitableTimer', 'MsgWaitForMultipleObjects', 'MsgWaitForMultipleObjectsEx', 'OpenEvent', 'OpenMutex', 'OpenSemaphore', 'OpenWaitableTimer', 'PulseEvent', 'ReleaseMutex', 'ReleaseSemaphore', 'ResetEvent', 'SetEvent', 'SetWaitableTimer', 'WaitForMultipleObjects', 'WaitForMultipleObjectsEx', 'WaitForSingleObject', 'WaitForSingleObjectEx', 'WaitForInputIdle', 'EVENT_ALL_ACCESS', 'EVENT_MODIFY_STATE', 'INFINITE', 'MAXIMUM_WAIT_OBJECTS', 'QS_ALLEVENTS', 'QS_ALLINPUT', 'QS_HOTKEY', 'QS_INPUT', 'QS_KEY', 'QS_MOUSE', 'QS_MOUSEBUTTON', 'QS_MOUSEMOVE', 'QS_PAINT', 'QS_POSTMESSAGE', 'QS_SENDMESSAGE', 'QS_TIMER', 'SYNCHRONIZE', 'WAIT_ABANDONED', 'WAIT_ABANDONED_0', 'WAIT_FAILED', 'WAIT_IO_COMPLETION', 'WAIT_OBJECT_0', 'WAIT_TIMEOUT']
import typing
import win32typing
"""A module which provides an interface to the win32 event/wait API"""


def CancelWaitableTimer() -> 'None':
    """
    Cancels a waiting timer.

Args:



Returns:

      None
        
    """
    pass
        

def CreateEvent(EventAttributes:'win32typing.PySECURITY_ATTRIBUTES',bManualReset:'typing.Any',bInitialState:'typing.Any',Name:'str') -> 'int':
    """
    Creates a waitable event

Args:

      EventAttributes(win32typing.PySECURITY_ATTRIBUTES):The security attributes, or None
      bManualReset(typing.Any):flag for manual-reset event
      bInitialState(typing.Any):flag for initial state
      Name(str):event-object name, or NoneReturn ValueThe result is a handle to the created object

Returns:

      int:event-object name, or NoneReturn ValueThe result is a handle to the created object

        
    """
    pass
        

def CreateMutex(MutexAttributes:'win32typing.PySECURITY_ATTRIBUTES',InitialOwner:'typing.Any',Name:'str') -> 'int':
    """
    Creates a mutex

Args:

      MutexAttributes(win32typing.PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      InitialOwner(typing.Any):flag for initial ownership
      Name(str):Mutex-object name, or NoneReturn ValueThe result is a handle to the created object

Returns:

      int:Mutex-object name, or NoneReturn ValueThe result is a handle to the created object

        
    """
    pass
        

def CreateSemaphore(SemaphoreAttributes:'win32typing.PySECURITY_ATTRIBUTES',InitialCount:'typing.Any',MaximumCount:'typing.Any',SemaphoreName:'typing.Any') -> 'int':
    """
    Creates a semaphore, or opens an existing one

Args:

      SemaphoreAttributes(win32typing.PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      InitialCount(typing.Any):Initial count
      MaximumCount(typing.Any):Maximum count
      SemaphoreName(typing.Any):Semaphore-object name, or NoneWin32 API References

Returns:

      int:Search for CreateSemaphore at msdn, google or google groups.
Return ValueThe result is a handle to the object

        
    """
    pass
        

def CreateWaitableTimer(TimerAttributes:'win32typing.PySECURITY_ATTRIBUTES',ManualReset:'typing.Any',TimerName:'typing.Any') -> 'int':
    """
    Creates a waitable timer, or opens an existing one

Args:

      TimerAttributes(win32typing.PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      ManualReset(typing.Any):True for manual reset timer, or False to create a synchronization timer
      TimerName(typing.Any):Timer object name, or NoneWin32 API References

Returns:

      int:Search for CreateWaitableTimer at msdn, google or google groups.
Return ValueThe result is a handle to the object

        
    """
    pass
        

def MsgWaitForMultipleObjects(handleList:'typing.List[int]',bWaitAll:'typing.Any',milliseconds:'typing.Any',wakeMask:'typing.Any') -> 'typing.Any':
    """
    Returns when a message arrives of an event is signalled

Args:

      handleList(typing.List[int]):A sequence of handles to wait on.
      bWaitAll(typing.Any):If true, waits for all handles in the list.
      milliseconds(typing.Any):time-out interval in milliseconds
      wakeMask(typing.Any):type of input events to wait for.  One of the win32event.QS_ constants.CommentsNote that if bWaitAll is TRUE, the function will return when there is input in the queue, and all events are signalled.  This is rarely what you want! If input is waiting, the result is win32event.WAIT_OBJECT_0+len(handles))

Returns:

      typing.Any
        
    """
    pass
        

def MsgWaitForMultipleObjectsEx(handleList:'typing.List[int]',milliseconds:'typing.Any',wakeMask:'typing.Any',waitFlags:'typing.Any') -> 'typing.Any':
    """
    Returns when a message arrives of an event is signalled

Args:

      handleList(typing.List[int]):A sequence of handles to wait on.
      milliseconds(typing.Any):time-out interval in milliseconds
      wakeMask(typing.Any):type of input events to wait for
      waitFlags(typing.Any):wait flagsCommentsThis method will no longer raise a COM E_NOTIMPL exception as it is no longer dynamically loaded.

Returns:

      typing.Any
        
    """
    pass
        

def OpenEvent(desiredAccess:'typing.Any',bInheritHandle:'typing.Any',name:'str') -> 'int':
    """
    Returns a handle of an existing named event object.

Args:

      desiredAccess(typing.Any):access flag - one of win32event::EVENT_ALL_ACCESS, win32event::EVENT_MODIFY_STATE, or (NT only) win32event::SYNCHRONIZE
      bInheritHandle(typing.Any):inherit flag
      name(str):name of event to open.

Returns:

      int
        
    """
    pass
        

def OpenMutex(desiredAccess:'typing.Any',bInheritHandle:'typing.Any',name:'str') -> 'int':
    """
    Returns a handle of an existing named mutex object.

Args:

      desiredAccess(typing.Any):access flag
      bInheritHandle(typing.Any):inherit flag
      name(str):name of mutex to open.

Returns:

      int
        
    """
    pass
        

def OpenSemaphore(desiredAccess:'typing.Any',bInheritHandle:'typing.Any',name:'str') -> 'int':
    """
    Returns a handle of an existing named semaphore object.

Args:

      desiredAccess(typing.Any):access flag
      bInheritHandle(typing.Any):inherit flag
      name(str):name of semaphore to open.

Returns:

      int
        
    """
    pass
        

def OpenWaitableTimer(desiredAccess:'typing.Any',bInheritHandle:'typing.Any',timerName:'typing.Any') -> 'int':
    """
    Opens an existing named waitable timer object

Args:

      desiredAccess(typing.Any):access flag
      bInheritHandle(typing.Any):inherit flag
      timerName(typing.Any):pointer to timer object name

Returns:

      int
        
    """
    pass
        

def PulseEvent(hEvent:'int') -> 'None':
    """
    Provides a single operation that sets (to signaled) the state of the specified event object and then resets it (to nonsignaled) after releasing the appropriate number of waiting threads.

Args:

      hEvent(int):handle of event object

Returns:

      None
        
    """
    pass
        

def ReleaseMutex(hEvent:'int') -> 'None':
    """
    Releases a mutex.

Args:

      hEvent(int):handle of mutex object

Returns:

      None
        
    """
    pass
        

def ReleaseSemaphore(hEvent:'int',lReleaseCount:'typing.Any') -> 'typing.Any':
    """
    Releases a semaphore.

Args:

      hEvent(int):handle of the semaphore object
      lReleaseCount(typing.Any):amount to add to current countReturn ValueThe result is the previous count of the semaphore.

Returns:

      typing.Any:amount to add to current countReturn ValueThe result is the previous count of the semaphore.

        
    """
    pass
        

def ResetEvent(hEvent:'int') -> 'None':
    """
    Resets an event

Args:

      hEvent(int):handle of event object

Returns:

      None
        
    """
    pass
        

def SetEvent(hEvent:'int') -> 'None':
    """
    Sets an event

Args:

      hEvent(int):handle of event object

Returns:

      None
        
    """
    pass
        

def SetWaitableTimer(handle:'int',dueTime:'typing.Any',period:'typing.Any',func:'typing.Any',param:'typing.Any',resume_state:'typing.Any') -> 'None':
    """
    Sets a waitable timer.

Args:

      handle(int):handle to timer
      dueTime(typing.Any):timer due time
      period(typing.Any):timer interval
      func(typing.Any):completion routine - must be None
      param(typing.Any):completion routine parameter - must be None
      resume_state(typing.Any):resume state

Returns:

      None
        
    """
    pass
        

def WaitForMultipleObjects(handleList:'typing.List[int]',bWaitAll:'typing.Any',milliseconds:'typing.Any') -> 'typing.Any':
    """
    Returns when an event is signalled

Args:

      handleList(typing.List[int]):A sequence of handles to wait on.
      bWaitAll(typing.Any):wait flag
      milliseconds(typing.Any):time-out interval in milliseconds

Returns:

      typing.Any
        
    """
    pass
        

def WaitForMultipleObjectsEx(handleList:'typing.List[int]',bWaitAll:'typing.Any',milliseconds:'typing.Any',bAlertable:'typing.Any') -> 'typing.Any':
    """
    Returns when an event is signalled

Args:

      handleList(typing.List[int]):A sequence of handles to wait on.
      bWaitAll(typing.Any):wait flag
      milliseconds(typing.Any):time-out interval in milliseconds
      bAlertable(typing.Any):alertable wait flag.

Returns:

      typing.Any
        
    """
    pass
        

def WaitForSingleObject(hHandle:'int',milliseconds:'typing.Any') -> 'typing.Any':
    """
    Returns when an event is signalled

Args:

      hHandle(int):handle of object to wait for
      milliseconds(typing.Any):time-out interval in millisecondsReturn ValueIf the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.ValueMeaningWAIT_ABANDONEDThe specified object is a mutex object that was not released by the thread that owned the mutex object before the owning thread terminated. Ownership of the mutex object is granted to the calling thread, and the mutex is set to nonsignaled.WAIT_OBJECT_0The state of the specified object is signaled.WAIT_TIMEOUTThe time-out interval elapsed, and the object's state is nonsignaled.

Returns:

      typing.Any:time-out interval in millisecondsReturn ValueIf the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.



Value


Meaning



WAIT_ABANDONEDThe specified object is a mutex object that was not released by the thread that owned the mutex object before the owning thread terminated. Ownership of the mutex object is granted to the calling thread, and the mutex is set to nonsignaled.
WAIT_OBJECT_0The state of the specified object is signaled.
WAIT_TIMEOUTThe time-out interval elapsed, and the object's state is nonsignaled.

        
    """
    pass
        

def WaitForSingleObjectEx(hHandle:'int',milliseconds:'typing.Any',bAlertable:'typing.Any') -> 'typing.Any':
    """
    Returns when an event is signalled

Args:

      hHandle(int):handle of object to wait for
      milliseconds(typing.Any):time-out interval in milliseconds
      bAlertable(typing.Any):alertable wait flag.Return ValueSee win32event::WaitForSingleObject for return values.

Returns:

      typing.Any:alertable wait flag.Return ValueSee win32event::WaitForSingleObject for return values.

        
    """
    pass
        

def WaitForInputIdle(hProcess:'int',milliseconds:'typing.Any') -> 'typing.Any':
    """
    Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

Args:

      hProcess(int):handle of process to wait for
      milliseconds(typing.Any):time-out interval in millisecondsReturn ValueThe return value indicates wether the process is ready or wether it timed out. This value can be one of the following.ValueMeaning0The process is ready.WAIT_TIMEOUTThe time-out interval elapsed, and the process is not ready.

Returns:

      typing.Any:time-out interval in millisecondsReturn ValueThe return value indicates wether the process is ready or wether it timed out. This value can be one of the following.



Value


Meaning



0The process is ready.
WAIT_TIMEOUTThe time-out interval elapsed, and the process is not ready.

        
    """
    pass
        
EVENT_ALL_ACCESS = ...
EVENT_MODIFY_STATE = ...
INFINITE = ...
MAXIMUM_WAIT_OBJECTS = ...
QS_ALLEVENTS = ...
QS_ALLINPUT = ...
QS_HOTKEY = ...
QS_INPUT = ...
QS_KEY = ...
QS_MOUSE = ...
QS_MOUSEBUTTON = ...
QS_MOUSEMOVE = ...
QS_PAINT = ...
QS_POSTMESSAGE = ...
QS_SENDMESSAGE = ...
QS_TIMER = ...
SYNCHRONIZE = ...
WAIT_ABANDONED = ...
WAIT_ABANDONED_0 = ...
WAIT_FAILED = ...
WAIT_IO_COMPLETION = ...
WAIT_OBJECT_0 = ...
WAIT_TIMEOUT = ...
