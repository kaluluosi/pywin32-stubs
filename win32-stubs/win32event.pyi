__all__=['', 'CancelWaitableTimer', 'CreateEvent', 'CreateMutex', 'CreateSemaphore', 'CreateWaitableTimer', 'MsgWaitForMultipleObjects', 'MsgWaitForMultipleObjectsEx', 'OpenEvent', 'OpenMutex', 'OpenSemaphore', 'OpenWaitableTimer', 'PulseEvent', 'ReleaseMutex', 'ReleaseSemaphore', 'ResetEvent', 'SetEvent', 'SetWaitableTimer', 'WaitForMultipleObjects', 'WaitForMultipleObjectsEx', 'WaitForSingleObject', 'WaitForSingleObjectEx', 'WaitForInputIdle', 'EVENT_ALL_ACCESS', 'EVENT_MODIFY_STATE', 'INFINITE', 'MAXIMUM_WAIT_OBJECTS', 'QS_ALLEVENTS', 'QS_ALLINPUT', 'QS_HOTKEY', 'QS_INPUT', 'QS_KEY', 'QS_MOUSE', 'QS_MOUSEBUTTON', 'QS_MOUSEMOVE', 'QS_PAINT', 'QS_POSTMESSAGE', 'QS_SENDMESSAGE', 'QS_TIMER', 'SYNCHRONIZE', 'WAIT_ABANDONED', 'WAIT_ABANDONED_0', 'WAIT_FAILED', 'WAIT_IO_COMPLETION', 'WAIT_OBJECT_0', 'WAIT_TIMEOUT']
from typing import *
from win32helper.win32typing import *
"""A module which provides an interface to the win32 event/wait API"""


def CancelWaitableTimer() -> 'None':
    """
    Cancels a waiting timer.

Args:



Returns:

      None
        
    """
    pass
        

def CreateEvent(EventAttributes:'PySECURITY_ATTRIBUTES',bManualReset:'bool',bInitialState:'bool',Name:'str') -> 'int':
    """
    Creates a waitable event

Args:

      EventAttributes(PySECURITY_ATTRIBUTES):The security attributes, or None
      bManualReset(bool):flag for manual-reset event
      bInitialState(bool):flag for initial state
      Name(str):event-object name, or NoneReturn ValueThe result is a handle to the created object

Returns:

      int:event-object name, or NoneReturn ValueThe result is a handle to the created object

        
    """
    pass
        

def CreateMutex(MutexAttributes:'PySECURITY_ATTRIBUTES',InitialOwner:'bool',Name:'str') -> 'int':
    """
    Creates a mutex

Args:

      MutexAttributes(PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      InitialOwner(bool):flag for initial ownership
      Name(str):Mutex-object name, or NoneReturn ValueThe result is a handle to the created object

Returns:

      int:Mutex-object name, or NoneReturn ValueThe result is a handle to the created object

        
    """
    pass
        

def CreateSemaphore(SemaphoreAttributes:'PySECURITY_ATTRIBUTES',InitialCount:'int',MaximumCount:'int',SemaphoreName:'str') -> 'int':
    """
    Creates a semaphore, or opens an existing one

Args:

      SemaphoreAttributes(PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      InitialCount(int):Initial count
      MaximumCount(int):Maximum count
      SemaphoreName(str):Semaphore-object name, or NoneWin32 API References

Returns:

      int:Search for CreateSemaphore at msdn, google or google groups.
Return ValueThe result is a handle to the object

        
    """
    pass
        

def CreateWaitableTimer(TimerAttributes:'PySECURITY_ATTRIBUTES',ManualReset:'bool',TimerName:'str') -> 'int':
    """
    Creates a waitable timer, or opens an existing one

Args:

      TimerAttributes(PySECURITY_ATTRIBUTES):Specifies inheritance and security descriptor for object, or None for defaults
      ManualReset(bool):True for manual reset timer, or False to create a synchronization timer
      TimerName(str):Timer object name, or NoneWin32 API References

Returns:

      int:Search for CreateWaitableTimer at msdn, google or google groups.
Return ValueThe result is a handle to the object

        
    """
    pass
        

def MsgWaitForMultipleObjects(handleList:'List[int]',bWaitAll:'bool',milliseconds:'int',wakeMask:'int') -> 'int':
    """
    Returns when a message arrives of an event is signalled

Args:

      handleList(List[int]):A sequence of handles to wait on.
      bWaitAll(bool):If true, waits for all handles in the list.
      milliseconds(int):time-out interval in milliseconds
      wakeMask(int):type of input events to wait for.  One of the win32event.QS_ constants.CommentsNote that if bWaitAll is TRUE, the function will return when there is input in the queue, and all events are signalled.  This is rarely what you want! If input is waiting, the result is win32event.WAIT_OBJECT_0+len(handles))

Returns:

      int
        
    """
    pass
        

def MsgWaitForMultipleObjectsEx(handleList:'List[int]',milliseconds:'int',wakeMask:'int',waitFlags:'int') -> 'int':
    """
    Returns when a message arrives of an event is signalled

Args:

      handleList(List[int]):A sequence of handles to wait on.
      milliseconds(int):time-out interval in milliseconds
      wakeMask(int):type of input events to wait for
      waitFlags(int):wait flagsCommentsThis method will no longer raise a COM E_NOTIMPL exception as it is no longer dynamically loaded.

Returns:

      int
        
    """
    pass
        

def OpenEvent(desiredAccess:'int',bInheritHandle:'bool',name:'str') -> 'int':
    """
    Returns a handle of an existing named event object.

Args:

      desiredAccess(int):access flag - one of win32event::EVENT_ALL_ACCESS, win32event::EVENT_MODIFY_STATE, or (NT only) win32event::SYNCHRONIZE
      bInheritHandle(bool):inherit flag
      name(str):name of event to open.

Returns:

      int
        
    """
    pass
        

def OpenMutex(desiredAccess:'int',bInheritHandle:'bool',name:'str') -> 'int':
    """
    Returns a handle of an existing named mutex object.

Args:

      desiredAccess(int):access flag
      bInheritHandle(bool):inherit flag
      name(str):name of mutex to open.

Returns:

      int
        
    """
    pass
        

def OpenSemaphore(desiredAccess:'int',bInheritHandle:'bool',name:'str') -> 'int':
    """
    Returns a handle of an existing named semaphore object.

Args:

      desiredAccess(int):access flag
      bInheritHandle(bool):inherit flag
      name(str):name of semaphore to open.

Returns:

      int
        
    """
    pass
        

def OpenWaitableTimer(desiredAccess:'int',bInheritHandle:'bool',timerName:'str') -> 'int':
    """
    Opens an existing named waitable timer object

Args:

      desiredAccess(int):access flag
      bInheritHandle(bool):inherit flag
      timerName(str):pointer to timer object name

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
        

def ReleaseSemaphore(hEvent:'int',lReleaseCount:'int') -> 'int':
    """
    Releases a semaphore.

Args:

      hEvent(int):handle of the semaphore object
      lReleaseCount(int):amount to add to current countReturn ValueThe result is the previous count of the semaphore.

Returns:

      int:amount to add to current countReturn ValueThe result is the previous count of the semaphore.

        
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
        

def SetWaitableTimer(handle:'int',dueTime:'Any',period:'int',func:'Any',param:'Any',resume_state:'bool') -> 'None':
    """
    Sets a waitable timer.

Args:

      handle(int):handle to timer
      dueTime(Any):timer due time
      period(int):timer interval
      func(Any):completion routine - must be None
      param(Any):completion routine parameter - must be None
      resume_state(bool):resume state

Returns:

      None
        
    """
    pass
        

def WaitForMultipleObjects(handleList:'List[int]',bWaitAll:'bool',milliseconds:'int') -> 'int':
    """
    Returns when an event is signalled

Args:

      handleList(List[int]):A sequence of handles to wait on.
      bWaitAll(bool):wait flag
      milliseconds(int):time-out interval in milliseconds

Returns:

      int
        
    """
    pass
        

def WaitForMultipleObjectsEx(handleList:'List[int]',bWaitAll:'bool',milliseconds:'int',bAlertable:'bool') -> 'int':
    """
    Returns when an event is signalled

Args:

      handleList(List[int]):A sequence of handles to wait on.
      bWaitAll(bool):wait flag
      milliseconds(int):time-out interval in milliseconds
      bAlertable(bool):alertable wait flag.

Returns:

      int
        
    """
    pass
        

def WaitForSingleObject(hHandle:'int',milliseconds:'int') -> 'int':
    """
    Returns when an event is signalled

Args:

      hHandle(int):handle of object to wait for
      milliseconds(int):time-out interval in millisecondsReturn ValueIf the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.ValueMeaningWAIT_ABANDONEDThe specified object is a mutex object that was not released by the thread that owned the mutex object before the owning thread terminated. Ownership of the mutex object is granted to the calling thread, and the mutex is set to nonsignaled.WAIT_OBJECT_0The state of the specified object is signaled.WAIT_TIMEOUTThe time-out interval elapsed, and the object's state is nonsignaled.

Returns:

      int:time-out interval in millisecondsReturn ValueIf the function succeeds, the return value indicates the event that caused the function to return. This value can be one of the following.



Value


Meaning



WAIT_ABANDONEDThe specified object is a mutex object that was not released by the thread that owned the mutex object before the owning thread terminated. Ownership of the mutex object is granted to the calling thread, and the mutex is set to nonsignaled.
WAIT_OBJECT_0The state of the specified object is signaled.
WAIT_TIMEOUTThe time-out interval elapsed, and the object's state is nonsignaled.

        
    """
    pass
        

def WaitForSingleObjectEx(hHandle:'int',milliseconds:'int',bAlertable:'bool') -> 'int':
    """
    Returns when an event is signalled

Args:

      hHandle(int):handle of object to wait for
      milliseconds(int):time-out interval in milliseconds
      bAlertable(bool):alertable wait flag.Return ValueSee win32event::WaitForSingleObject for return values.

Returns:

      int:alertable wait flag.Return ValueSee win32event::WaitForSingleObject for return values.

        
    """
    pass
        

def WaitForInputIdle(hProcess:'int',milliseconds:'int') -> 'int':
    """
    Waits until the given process is waiting for user input with no input pending, or until the time-out interval has elapsed

Args:

      hProcess(int):handle of process to wait for
      milliseconds(int):time-out interval in millisecondsReturn ValueThe return value indicates wether the process is ready or wether it timed out. This value can be one of the following.ValueMeaning0The process is ready.WAIT_TIMEOUTThe time-out interval elapsed, and the process is not ready.

Returns:

      int:time-out interval in millisecondsReturn ValueThe return value indicates wether the process is ready or wether it timed out. This value can be one of the following.



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