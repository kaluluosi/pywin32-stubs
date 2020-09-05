from pywintypes import *
__all__=['STARTUPINFO', 'beginthreadex', 'CreateRemoteThread', 'CreateProcess', 'CreateProcessAsUser', 'GetCurrentProcess', 'GetProcessVersion', 'GetCurrentProcessId', 'GetStartupInfo', 'GetPriorityClass', 'GetExitCodeThread', 'GetExitCodeProcess', 'GetWindowThreadProcessId', 'SetThreadPriority', 'GetThreadPriority', 'GetProcessPriorityBoost', 'SetProcessPriorityBoost', 'GetThreadPriorityBoost', 'SetThreadPriorityBoost', 'GetThreadIOPendingFlag', 'GetThreadTimes', 'GetProcessId', 'SetPriorityClass', 'AttachThreadInput', 'SetThreadIdealProcessor', 'GetProcessAffinityMask', 'SetProcessAffinityMask', 'SetThreadAffinityMask', 'SuspendThread', 'ResumeThread', 'TerminateProcess', 'ExitProcess', 'EnumProcesses', 'EnumProcessModules', 'EnumProcessModulesEx', 'GetModuleFileNameEx', 'GetProcessMemoryInfo', 'GetProcessTimes', 'GetProcessIoCounters', 'GetProcessWindowStation', 'GetProcessWorkingSetSize', 'SetProcessWorkingSetSize', 'GetProcessShutdownParameters', 'SetProcessShutdownParameters', 'GetGuiResources', 'IsWow64Process', 'ABOVE_NORMAL_PRIORITY_CLASS', 'BELOW_NORMAL_PRIORITY_CLASS', 'CREATE_BREAKAWAY_FROM_JOB', 'CREATE_DEFAULT_ERROR_MODE', 'CREATE_NEW_CONSOLE', 'CREATE_NEW_PROCESS_GROUP', 'CREATE_NO_WINDOW', 'CREATE_PRESERVE_CODE_AUTHZ_LEVEL', 'CREATE_SEPARATE_WOW_VDM', 'CREATE_SHARED_WOW_VDM', 'CREATE_SUSPENDED', 'CREATE_UNICODE_ENVIRONMENT', 'DEBUG_ONLY_THIS_PROCESS', 'DEBUG_PROCESS', 'DETACHED_PROCESS', 'HIGH_PRIORITY_CLASS', 'IDLE_PRIORITY_CLASS', 'LIST_MODULES_32BIT', 'LIST_MODULES_64BIT', 'LIST_MODULES_ALL', 'LIST_MODULES_DEFAULT', 'MAXIMUM_PROCESSORS', 'NORMAL_PRIORITY_CLASS', 'REALTIME_PRIORITY_CLASS', 'STARTF_FORCEOFFFEEDBACK', 'STARTF_FORCEONFEEDBACK', 'STARTF_RUNFULLSCREEN', 'STARTF_USECOUNTCHARS', 'STARTF_USEFILLATTRIBUTE', 'STARTF_USEPOSITION', 'STARTF_USESHOWWINDOW', 'STARTF_USESIZE', 'STARTF_USESTDHANDLES', 'THREAD_MODE_BACKGROUND_BEGIN', 'THREAD_MODE_BACKGROUND_BEGIN', 'THREAD_MODE_BACKGROUND_END', 'THREAD_MODE_BACKGROUND_END', 'THREAD_PRIORITY_ABOVE_NORMAL', 'THREAD_PRIORITY_BELOW_NORMAL', 'THREAD_PRIORITY_HIGHEST', 'THREAD_PRIORITY_IDLE', 'THREAD_PRIORITY_LOWEST', 'THREAD_PRIORITY_NORMAL', 'THREAD_PRIORITY_TIME_CRITICAL']
import typing
"""An interface to the win32 Process and Thread API's"""


def STARTUPINFO() -> typing.Any:
    """
    Creates a new STARTUPINFO object.


Args:



Returns:

      typing.Any
        
    """
    pass


def beginthreadex(sa:typing.Any,stackSize:int,entryPoint:typing.Any,args:tuple,flags:int) -> typing.Any:
    """
    Creates a new thread


Args:

      sa(typing.Any):The security attributes, or None
      stackSize(int):Stack size for the new thread, or zero for the default size.
      entryPoint(typing.Any):The thread function.
      args(tuple):Args passed to the function.
      flags(int):Can be CREATE_SUSPENDED so thread doesn't run immediatelyReturn ValueThe result is a tuple of the thread handle and thread ID.

Returns:

      typing.Any:Can be CREATE_SUSPENDED so thread doesn't run immediatelyReturn ValueThe result is a tuple of the thread handle and thread ID.

        
    """
    pass


def CreateRemoteThread(hprocess:typing.Any,sa:typing.Any,stackSize:int,entryPoint:typing.Any,Parameter:int,flags:int) -> typing.Any:
    """
    creates a thread that runs in 

the virtual address space of another process.


Args:

      hprocess(typing.Any):The handle to the remote process.
      sa(typing.Any):The security attributes, or None
      stackSize(int):Stack size for the new thread, or zero for the default size.
      entryPoint(typing.Any):The thread function's address.
      Parameter(int):Arg passed to the function in the form of a void pointer
      flags(int):Return ValueThe result is a tuple of the thread handle and thread ID.

Returns:

      typing.Any:Return ValueThe result is a tuple of the thread handle and thread ID.

        
    """
    pass


def CreateProcess(appName:str,commandLine:str,processAttributes:typing.Any,threadAttributes:typing.Any,bInheritHandles:int,dwCreationFlags:int,newEnvironment:Union[None,typing.Any],currentDirectory:str,startupinfo:typing.Any) -> typing.Any:
    """
    Creates a new process and its primary thread. The new process executes the specified executable file.


Args:

      appName(str):name of executable module, or None
      commandLine(str):command line string, or None
      processAttributes(typing.Any):process security attributes, or None
      threadAttributes(typing.Any):thread security attributes, or None
      bInheritHandles(int):handle inheritance flag
      dwCreationFlags(int):creation flags.  May be a combination of the following values from the win32con module:ValueMeaningCREATE_BREAKAWAY_FROM_JOBWindows 2000: The child processes of a process associated with a job are not associated with the job. If the calling process is not associated with a job, this flag has no effect. If the calling process is associated with a job, the job must set the JOB_OBJECT_LIMIT_BREAKAWAY_OK limit or CreateProcess will fail.CREATE_DEFAULT_ERROR_MODEThe new process does not inherit the error mode of the calling process. Instead, CreateProcess gives the new process the current default error mode. An application sets the current default error mode by calling SetErrorMode. This flag is particularly useful for multi-threaded shell applications that run with hard errors disabled. The default behavior for CreateProcess is for the new process to inherit the error mode of the caller. Setting this flag changes that default behavior.CREATE_FORCE_DOSWindows NT/2000: This flag is valid only when starting a 16-bit bound application. If set, the system will force the application to run as an MS-DOS-based application rather than as an OS/2-based application.CREATE_NEW_CONSOLEThe new process has a new console, instead of inheriting the parent's console. This flag cannot be used with the DETACHED_PROCESS flag.CREATE_NEW_PROCESS_GROUPThe new process is the root process of a new process group. The process group includes all processes that are descendants of this root process. The process identifier of the new process group is the same as the process identifier, which is returned in the lpProcessInformation parameter. Process groups are used by the GenerateConsoleCtrlEvent function to enable sending a CTRL+C or CTRL+BREAK signal to a group of console processes.CREATE_NO_WINDOWWindows NT/2000: This flag is valid only when starting a console application. If set, the console application is run without a console window.CREATE_SEPARATE_WOW_VDMWindows NT/2000: This flag is valid only when starting a 16-bit Windows-based application. If set, the new process runs in a private Virtual DOS Machine (VDM). By default, all 16-bit Windows-based applications run as threads in a single, shared VDM. The advantage of running separately is that a crash only terminates the single VDM; any other programs running in distinct VDMs continue to function normally. Also, 16-bit Windows-based applications that are run in separate VDMs have separate input queues. That means that if one application stops responding momentarily, applications in separate VDMs continue to receive input. The disadvantage of running separately is that it takes significantly more memory to do so. You should use this flag only if the user requests that 16-bit applications should run in them own VDM.CREATE_SHARED_WOW_VDMWindows NT/2000: The flag is valid only when starting a 16-bit Windows-based application. If the DefaultSeparateVDM switch in the Windows section of WIN.INI is TRUE, this flag causes the CreateProcess function to override the switch and run the new process in the shared Virtual DOS Machine.CREATE_SUSPENDEDThe primary thread of the new process is created in a suspended state, and does not run until the ResumeThread function is called.CREATE_UNICODE_ENVIRONMENTIndicates the format of the lpEnvironment parameter. If this flag is set, the environment block pointed to by lpEnvironment uses Unicode characters. Otherwise, the environment block uses ANSI characters.DEBUG_PROCESSIf this flag is set, the calling process is treated as a debugger, and the new process is debugged. The system notifies the debugger of all debug events that occur in the process being debugged. If you create a process with this flag set, only the calling thread (the thread that called CreateProcess) can call the WaitForDebugEvent function. Windows 95/98: This flag is not valid if the new process is a 16-bit application.DEBUG_ONLY_THIS_PROCESSIf this flag is not set and the calling process is being debugged, the new process becomes another process being debugged by the calling process's debugger. If the calling process is not a process being debugged, no debugging-related actions occur.DETACHED_PROCESSFor console processes, the new process does not have access to the console of the parent process. The new process can call the AllocConsole function at a later time to create a new console. This flag cannot be used with the CREATE_NEW_CONSOLE flag.ABOVE_NORMAL_PRIORITY_CLASSWindows 2000: Indicates a process that has priority higher than NORMAL_PRIORITY_CLASS but lower than HIGH_PRIORITY_CLASS.BELOW_NORMAL_PRIORITY_CLASSWindows 2000: Indicates a process that has priority higher than IDLE_PRIORITY_CLASS but lower than NORMAL_PRIORITY_CLASS.HIGH_PRIORITY_CLASSIndicates a process that performs time-critical tasks. The threads of a high-priority class process preempt the threads of normal-priority or idle-priority class processes. An example is the Task List, which must respond quickly when called by the user, regardless of the load on the system. Use extreme care when using the high-priority class, because a CPU-bound application with a high-priority class can use nearly all available cycles.IDLE_PRIORITY_CLASSIndicates a process whose threads run only when the system is idle and are preempted by the threads of any process running in a higher priority class. An example is a screen saver. The idle priority class is inherited by child processes.NORMAL_PRIORITY_CLASSIndicates a normal process with no special scheduling needs.REALTIME_PRIORITY_CLASSIndicates a process that has the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes performing important tasks. For example, a real-time process that executes for more than a very brief interval can cause disk caches not to flush or cause the mouse to be unresponsive.
      newEnvironment(None,typing.Any):A dictionary of string or Unicode pairs to define the environment for the process, or None to inherit the current environment.
      currentDirectory(str):current directory name, or None
      startupinfo(typing.Any):a STARTUPINFO object that specifies how the main window for the new process should appear.CommentsThe result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

Returns:

      typing.Any
        
    """
    pass


def CreateProcessAsUser(hToken:typing.Any,appName:str,commandLine:str,processAttributes:typing.Any,threadAttributes:typing.Any,bInheritHandles:int,dwCreationFlags:int,newEnvironment:None,currentDirectory:str,startupinfo:typing.Any) -> typing.Any:
    """
    Creates a new process in the context of the specified user.


Args:

      hToken(typing.Any):Handle to a token that represents a logged-on user
      appName(str):name of executable module, or None
      commandLine(str):command line string, or None
      processAttributes(typing.Any):process security attributes, or None
      threadAttributes(typing.Any):thread security attributes, or None
      bInheritHandles(int):handle inheritance flag
      dwCreationFlags(int):creation flags
      newEnvironment(None):A dictionary of stringor Unicode pairs to define the environment for the process, or None to inherit the current environment.
      currentDirectory(str):current directory name, or None
      startupinfo(typing.Any):a STARTUPINFO object that specifies how the main window for the new process should appear.CommentsThe result is a tuple of (hProcess, hThread, dwProcessId, dwThreadId)

Returns:

      typing.Any
        
    """
    pass


def GetCurrentProcess() -> int:
    """
    Retrieves a pseudo handle for the current process.


Args:



Returns:

      int
        
    """
    pass


def GetProcessVersion(processId:int) -> int:
    """
    Obtains the major and minor version numbers of the system on which a specified process expects to run.


Args:

      processId(int):identifier specifying the process of interest.

Returns:

      int
        
    """
    pass


def GetCurrentProcessId() -> int:
    """
    Retrieves the process identifier of the calling process.


Args:



Returns:

      int
        
    """
    pass


def GetStartupInfo() -> typing.Any:
    """
    Retrieves the contents of the STARTUPINFO structure that was specified when the calling process was created.


Args:



Returns:

      typing.Any
        
    """
    pass


def GetPriorityClass(handle:typing.Any) -> int:
    """
    None


Args:

      handle(typing.Any):handle to the thread

Returns:

      int
        
    """
    pass


def GetExitCodeThread(handle:typing.Any) -> int:
    """
    None


Args:

      handle(typing.Any):handle to the thread

Returns:

      int
        
    """
    pass


def GetExitCodeProcess(handle:typing.Any) -> int:
    """
    None


Args:

      handle(typing.Any):handle to the process

Returns:

      int
        
    """
    pass


def GetWindowThreadProcessId(hwnd:int) -> typing.Any:
    """
    Retrieves the identifier of the thread and process that created the specified window.


Args:

      hwnd(int):handle to the windowReturn ValueThe result is a tuple of (threadId, processId)

Returns:

      typing.Any:handle to the windowReturn ValueThe result is a tuple of (threadId, processId)

        
    """
    pass


def SetThreadPriority(handle:typing.Any,nPriority:int) -> None:
    """
    None


Args:

      handle(typing.Any):handle to the thread
      nPriority(int):thread priority level

Returns:

      None
        
    """
    pass


def GetThreadPriority(handle:typing.Any) -> int:
    """
    None


Args:

      handle(typing.Any):handle to the thread

Returns:

      int
        
    """
    pass


def GetProcessPriorityBoost(Process:typing.Any) -> bool:
    """
    Determines if dynamic priority adjustment is enabled for a process


Args:

      Process(typing.Any):Handle to a process

Returns:

      bool
        
    """
    pass


def SetProcessPriorityBoost(Process:typing.Any,DisablePriorityBoost:typing.Any) -> None:
    """
    Enables or disables dynamic priority adjustment for a process


Args:

      Process(typing.Any):Handle to a process
      DisablePriorityBoost(typing.Any):True to disable or False to enable

Returns:

      None
        
    """
    pass


def GetThreadPriorityBoost(Thread:typing.Any) -> bool:
    """
    Determines if dynamic priority adjustment is enabled for a thread


Args:

      Thread(typing.Any):Handle to a thread

Returns:

      bool
        
    """
    pass


def SetThreadPriorityBoost(Thread:typing.Any,DisablePriorityBoost:typing.Any) -> None:
    """
    Enables or disables dynamic priority adjustment for a thread


Args:

      Thread(typing.Any):Handle to a thread
      DisablePriorityBoost(typing.Any):True to disable or False to enable

Returns:

      None
        
    """
    pass


def GetThreadIOPendingFlag(Thread:typing.Any) -> bool:
    """
    Determines if thread has any outstanding IO requests


Args:

      Thread(typing.Any):Handle to a thread

Returns:

      bool
        
    """
    pass


def GetThreadTimes(Thread:typing.Any) -> dict:
    """
    Returns a thread's time statistics


Args:

      Thread(typing.Any):Handle to a thread

Returns:

      dict
        
    """
    pass


def GetProcessId(Process:typing.Any) -> int:
    """
    Returns the Pid for a process handle


Args:

      Process(typing.Any):Handle to a process

Returns:

      int
        
    """
    pass


def SetPriorityClass(handle:typing.Any,dwPriorityClass:int) -> None:
    """
    None


Args:

      handle(typing.Any):handle to the process
      dwPriorityClass(int):priority class value

Returns:

      None
        
    """
    pass


def AttachThreadInput(idAttach:int,idAttachTo:int,Attach:bool) -> None:
    """
    Attaches or detaches the input of two threads


Args:

      idAttach(int):The id of a thread
      idAttachTo(int):The id of the thread to which it will be attached
      Attach(bool):Indicates whether thread should be attached or detached

Returns:

      None
        
    """
    pass


def SetThreadIdealProcessor(handle:typing.Any,dwIdealProcessor:int) -> int:
    """
    Used to specify a preferred processor for a thread. The system schedules threads on their preferred processors whenever possible.


Args:

      handle(typing.Any):handle to the thread of interest
      dwIdealProcessor(int):ideal processor number

Returns:

      int
        
    """
    pass


def GetProcessAffinityMask(hProcess:typing.Any) -> typing.Any:
    """
    Gets a processor affinity mask for a specified process


Args:

      hProcess(typing.Any):handle to the process of interestReturn ValueThe result is a tuple of (process affinity mask, system affinity mask)

Returns:

      typing.Any:handle to the process of interestReturn ValueThe result is a tuple of (process affinity mask, system affinity mask)

        
    """
    pass


def SetProcessAffinityMask(hProcess:typing.Any,mask:int) -> None:
    """
    Sets a processor affinity mask for a specified process.


Args:

      hProcess(typing.Any):handle to the process of interest
      mask(int):a processor affinity maskCommentsThis function does not exist on all platforms.

Returns:

      None
        
    """
    pass


def SetThreadAffinityMask(hThread:typing.Any,ThreadAffinityMask:int) -> int:
    """
    Sets a processor affinity mask for a specified thread.


Args:

      hThread(typing.Any):handle to the thread of interest
      ThreadAffinityMask(int):a processor affinity mask

Returns:

      int
        
    """
    pass


def SuspendThread(handle:typing.Any) -> int:
    """
    Suspends the specified thread.


Args:

      handle(typing.Any):handle to the threadReturn ValueThe return value is the thread's previous suspend count

Returns:

      int:handle to the threadReturn ValueThe return value is the thread's previous suspend count

        
    """
    pass


def ResumeThread(handle:typing.Any) -> int:
    """
    Resumes the specified thread. When the suspend count is decremented to zero, the execution of the thread is resumed.


Args:

      handle(typing.Any):handle to the threadReturn ValueThe return value is the thread's previous suspend count

Returns:

      int:handle to the threadReturn ValueThe return value is the thread's previous suspend count

        
    """
    pass


def TerminateProcess(handle:typing.Any,exitCode:int) -> None:
    """
    Terminates the specified process and all of its threads.


Args:

      handle(typing.Any):handle to the process
      exitCode(int):The exit code for the process.

Returns:

      None
        
    """
    pass


def ExitProcess(exitCode:int) -> None:
    """
    Ends a process and all its threads


Args:

      exitCode(int):Specifies the exit code for the process, and for all threads that are terminated as a result of this callCommentsExitProcess is the preferred method of ending a process. This function provides a clean process shutdown. This includes calling the entry-point function of all attached dynamic-link libraries (DLLs) with a value indicating that the process is detaching from the DLL. If a process terminates by calling win32process::TerminateProcess, the DLLs that the process is attached to are not notified of the process termination.

Returns:

      None
        
    """
    pass


def EnumProcesses() -> typing.Any:
    """
    Returns Pids for currently running processes


Args:



Returns:

      typing.Any
        
    """
    pass


def EnumProcessModules(hProcess:typing.Any) -> typing.Any:
    """
    Lists loaded modules for a process handle


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess

Returns:

      typing.Any
        
    """
    pass


def EnumProcessModulesEx(hProcess:typing.Any,FilterFlag:int) -> typing.Any:
    """
    Lists 32 or 64-bit modules load by a process


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess
      FilterFlag(int):Controls whether 32 or 64-bit modules are returnedCommentsRequires Vista or later

Returns:

      typing.Any
        
    """
    pass


def GetModuleFileNameEx(hProcess:typing.Any,hModule:typing.Any) -> typing.Any:
    """
    Return name of module loaded by another process (uses process handle, not pid)


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess
      hModule(typing.Any):Module handle

Returns:

      typing.Any
        
    """
    pass


def GetProcessMemoryInfo(hProcess:typing.Any) -> dict:
    """
    Returns process memory statistics as a dict representing a PROCESS_MEMORY_COUNTERS struct


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess

Returns:

      dict
        
    """
    pass


def GetProcessTimes(hProcess:typing.Any) -> dict:
    """
    Retrieve time statics for a process by handle.  (KernelTime and UserTime in 100 nanosecond units)


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess

Returns:

      dict
        
    """
    pass


def GetProcessIoCounters(hProcess:typing.Any) -> dict:
    """
    Return I/O statistics for a process as a dictionary representing an IO_COUNTERS struct.


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess

Returns:

      dict
        
    """
    pass


def GetProcessWindowStation() -> None:
    """
    Returns a handle to the window station for the calling process


Args:



Returns:

      None
        
    """
    pass


def GetProcessWorkingSetSize(hProcess:typing.Any) -> typing.Any:
    """
    Returns min and max working set sizes for a process by handle


Args:

      hProcess(typing.Any):Process handle as returned by win32api::OpenProcess

Returns:

      typing.Any
        
    """
    pass


def SetProcessWorkingSetSize(hProcess:typing.Any,MinimumWorkingSetSize:int,MaximumWorkingSetSize:int) -> None:
    """
    Sets minimum and maximum working set sizes for a process


Args:

      hProcess(typing.Any):Process handle as returned by OpenProcess
      MinimumWorkingSetSize(int):Minimum number of bytes to keep in physical memory
      MaximumWorkingSetSize(int):Maximum number of bytes to keep in physical memoryCommentsSet both min and max to -1 to have process swapped out completely

Returns:

      None
        
    """
    pass


def GetProcessShutdownParameters() -> typing.Any:
    """
    Retrieves shutdown priority and flags for current process


Args:



Returns:

      typing.Any
        
    """
    pass


def SetProcessShutdownParameters(Level:int,Flags:int) -> None:
    """
    Sets shutdown priority and flags for current process


Args:

      Level(int):Priority, higher means earlier
      Flags(int):Currently only SHUTDOWN_NORETRY validCommentsRanges are 000-0FF Reserved by windows, 100-1FF Last, 200-2FF Middle, 300-3FF First, 400-4FF Reserved by windows

Returns:

      None
        
    """
    pass


def GetGuiResources(Process:typing.Any,Flags:int) -> int:
    """
    Returns the number of GDI or user object handles held by a process


Args:

      Process(typing.Any):Handle to a process as returned by win32api::OpenProcess
      Flags(int):GR_GDIOBJECTS or GR_USEROBJECTS (from win32con)CommentsAvailable on Win2k and up

Returns:

      int
        
    """
    pass


def IsWow64Process(Process:typing.Any=None) -> bool:
    """
    Determines whether the specified process is running under WOW64.


Args:

      Process(typing.Any):Handle to a process as returned by win32api::OpenProcess, win32api::GetCurrentProcess, etc, or will use the current process handle if None (the default) is passed.Return ValueIf this function is not provided by the operating system, the return value is False (ie, a NotImplemented exception will never be thrown). However, if the function exists but fails, a win32process.error exception is thrown as normal.

Returns:

      bool:Handle to a process as returned by 

win32api::OpenProcess, win32api::GetCurrentProcess, etc, or 

will use the current process handle if None (the default) is passed.
Return ValueIf this function is not provided by the operating system, the 

return value is False (ie, a NotImplemented exception will never be thrown). 

However, if the function exists but fails, a win32process.error exception 

is thrown as normal.

        
    """
    pass

ABOVE_NORMAL_PRIORITY_CLASS = ...
BELOW_NORMAL_PRIORITY_CLASS = ...
CREATE_BREAKAWAY_FROM_JOB = ...
CREATE_DEFAULT_ERROR_MODE = ...
CREATE_NEW_CONSOLE = ...
CREATE_NEW_PROCESS_GROUP = ...
CREATE_NO_WINDOW = ...
CREATE_PRESERVE_CODE_AUTHZ_LEVEL = ...
CREATE_SEPARATE_WOW_VDM = ...
CREATE_SHARED_WOW_VDM = ...
CREATE_SUSPENDED = ...
CREATE_UNICODE_ENVIRONMENT = ...
DEBUG_ONLY_THIS_PROCESS = ...
DEBUG_PROCESS = ...
DETACHED_PROCESS = ...
HIGH_PRIORITY_CLASS = ...
IDLE_PRIORITY_CLASS = ...
LIST_MODULES_32BIT = ...
LIST_MODULES_64BIT = ...
LIST_MODULES_ALL = ...
LIST_MODULES_DEFAULT = ...
MAXIMUM_PROCESSORS = ...
NORMAL_PRIORITY_CLASS = ...
REALTIME_PRIORITY_CLASS = ...
STARTF_FORCEOFFFEEDBACK = ...
STARTF_FORCEONFEEDBACK = ...
STARTF_RUNFULLSCREEN = ...
STARTF_USECOUNTCHARS = ...
STARTF_USEFILLATTRIBUTE = ...
STARTF_USEPOSITION = ...
STARTF_USESHOWWINDOW = ...
STARTF_USESIZE = ...
STARTF_USESTDHANDLES = ...
THREAD_MODE_BACKGROUND_BEGIN = ...
THREAD_MODE_BACKGROUND_BEGIN = ...
THREAD_MODE_BACKGROUND_END = ...
THREAD_MODE_BACKGROUND_END = ...
THREAD_PRIORITY_ABOVE_NORMAL = ...
THREAD_PRIORITY_BELOW_NORMAL = ...
THREAD_PRIORITY_HIGHEST = ...
THREAD_PRIORITY_IDLE = ...
THREAD_PRIORITY_LOWEST = ...
THREAD_PRIORITY_NORMAL = ...
THREAD_PRIORITY_TIME_CRITICAL = ...