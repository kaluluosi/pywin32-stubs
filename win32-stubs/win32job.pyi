from pywintypes import *
__all__=['AssignProcessToJobObject', 'CreateJobObject', 'OpenJobObject', 'TerminateJobObject', 'UserHandleGrantAccess', 'IsProcessInJob', 'QueryInformationJobObject', 'SetInformationJobObject', 'JOB_OBJECT_ALL_ACCESS', 'JOB_OBJECT_ASSIGN_PROCESS', 'JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS', 'JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS', 'JOB_OBJECT_LIMIT_ACTIVE_PROCESS', 'JOB_OBJECT_LIMIT_AFFINITY', 'JOB_OBJECT_LIMIT_BREAKAWAY_OK', 'JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION', 'JOB_OBJECT_LIMIT_JOB_MEMORY', 'JOB_OBJECT_LIMIT_JOB_TIME', 'JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE', 'JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME', 'JOB_OBJECT_LIMIT_PRIORITY_CLASS', 'JOB_OBJECT_LIMIT_PROCESS_MEMORY', 'JOB_OBJECT_LIMIT_PROCESS_TIME', 'JOB_OBJECT_LIMIT_SCHEDULING_CLASS', 'JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK', 'JOB_OBJECT_LIMIT_VALID_FLAGS', 'JOB_OBJECT_LIMIT_WORKINGSET', 'JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS', 'JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT', 'JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO', 'JOB_OBJECT_MSG_END_OF_JOB_TIME', 'JOB_OBJECT_MSG_END_OF_PROCESS_TIME', 'JOB_OBJECT_MSG_EXIT_PROCESS', 'JOB_OBJECT_MSG_JOB_MEMORY_LIMIT', 'JOB_OBJECT_MSG_NEW_PROCESS', 'JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT', 'JOB_OBJECT_POST_AT_END_OF_JOB', 'JOB_OBJECT_QUERY', 'JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS', 'JOB_OBJECT_SECURITY_FILTER_TOKENS', 'JOB_OBJECT_SECURITY_NO_ADMIN', 'JOB_OBJECT_SECURITY_ONLY_TOKEN', 'JOB_OBJECT_SECURITY_RESTRICTED_TOKEN', 'JOB_OBJECT_SECURITY_VALID_FLAGS', 'JOB_OBJECT_SET_ATTRIBUTES', 'JOB_OBJECT_SET_SECURITY_ATTRIBUTES', 'JOB_OBJECT_TERMINATE', 'JOB_OBJECT_TERMINATE_AT_END_OF_JOB', 'JOB_OBJECT_UI_VALID_FLAGS', 'JOB_OBJECT_UILIMIT_ALL', 'JOB_OBJECT_UILIMIT_DESKTOP', 'JOB_OBJECT_UILIMIT_DISPLAYSETTINGS', 'JOB_OBJECT_UILIMIT_EXITWINDOWS', 'JOB_OBJECT_UILIMIT_GLOBALATOMS', 'JOB_OBJECT_UILIMIT_HANDLES', 'JOB_OBJECT_UILIMIT_NONE', 'JOB_OBJECT_UILIMIT_READCLIPBOARD', 'JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS', 'JOB_OBJECT_UILIMIT_WRITECLIPBOARD', 'JobObjectAssociateCompletionPortInformation', 'JobObjectBasicAccountingInformation', 'JobObjectBasicAndIoAccountingInformation', 'JobObjectBasicLimitInformation', 'JobObjectBasicProcessIdList', 'JobObjectBasicUIRestrictions', 'JobObjectEndOfJobTimeInformation', 'JobObjectExtendedLimitInformation', 'JobObjectJobSetInformation', 'JobObjectSecurityLimitInformation', 'MaxJobObjectInfoClass']
import typing
"""An interface to the win32 Process and Thread API's, 

available in Windows 2000 and later."""


def AssignProcessToJobObject(hJob:typing.Any,hProcess:typing.Any) -> None:
    """
    Associates a process with an existing job object.


Args:

      hJob(typing.Any):
      hProcess(typing.Any):

Returns:

      None
        
    """
    pass


def CreateJobObject(jobAttributes:typing.Any,name:typing.Any) -> None:
    """
    Creates or opens a job object.


Args:

      jobAttributes(typing.Any):
      name(typing.Any):

Returns:

      None
        
    """
    pass


def OpenJobObject(desiredAccess:int,inheritHandles:bool,name:typing.Any) -> None:
    """
    Opens an existing job object.


Args:

      desiredAccess(int):
      inheritHandles(bool):
      name(typing.Any):

Returns:

      None
        
    """
    pass


def TerminateJobObject(hJob:typing.Any,exitCode:int) -> None:
    """
    Terminates all processes currently associated with the job.


Args:

      hJob(typing.Any):
      exitCode(int):

Returns:

      None
        
    """
    pass


def UserHandleGrantAccess(hUserHandle:typing.Any,hJob:typing.Any,grant:bool) -> None:
    """
    Grants or denies access to a handle to a User object to a job that has a user-interface restriction.


Args:

      hUserHandle(typing.Any):
      hJob(typing.Any):
      grant(bool):

Returns:

      None
        
    """
    pass


def IsProcessInJob(hProcess:typing.Any,hJob:typing.Any) -> typing.Any:
    """
    Determines if the process is running in the specified job.


Args:

      hProcess(typing.Any):Handle to a process
      hJob(typing.Any):Handle to a job, use None to check if process is part of any jobCommentsFunction is only available on WinXP and later

Returns:

      typing.Any
        
    """
    pass


def QueryInformationJobObject(Job:typing.Any,JobObjectInfoClass:int) -> dict:
    """
    Retrieves limit and job state information from the job object.


Args:

      Job(typing.Any):Handle to a job, use None for job that calling process is part of
      JobObjectInfoClass(int):The type of data required, one of JobObject* valuesJobObjectInfoClassType of information returnedJobObjectBasicAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_ACCOUNTING_INFORMATION structJobObjectBasicAndIoAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION structJobObjectBasicLimitInformationReturns a dict representing a JOBOBJECT_BASIC_LIMIT_INFORMATION structJobObjectExtendedLimitInformationReturns a dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION structJobObjectEndOfJobTimeInformationReturns a dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION structJobObjectBasicUIRestrictionsReturns a dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS structJobObjectBasicProcessIdListReturns a sequence of pids of processes assigned to the jobJobObjectJobSetInformationReturns a dict representing a JOBOBJECT_JOBSET_INFORMATION struct (not documented on MSDN)JobObjectSecurityLimitInformationJOBOBJECT_SECURITY_LIMIT_INFORMATION Not implementedJobObjectAssociateCompletionPortInformationJOBOBJECT_ASSOCIATE_COMPLETION_PORT Not implementedReturn ValueThe type of the returned information is dependent on the class requested

Returns:

      dict:The type of data required, one of JobObject* values


JobObjectInfoClass


Type of information returned



JobObjectBasicAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_ACCOUNTING_INFORMATION struct
JobObjectBasicAndIoAccountingInformationReturns a dict representing a JOBOBJECT_BASIC_AND_IO_ACCOUNTING_INFORMATION struct
JobObjectBasicLimitInformationReturns a dict representing a JOBOBJECT_BASIC_LIMIT_INFORMATION struct
JobObjectExtendedLimitInformationReturns a dict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION struct
JobObjectEndOfJobTimeInformationReturns a dict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION struct
JobObjectBasicUIRestrictionsReturns a dict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS struct
JobObjectBasicProcessIdListReturns a sequence of pids of processes assigned to the job
JobObjectJobSetInformationReturns a dict representing a JOBOBJECT_JOBSET_INFORMATION struct (not documented on MSDN)
JobObjectSecurityLimitInformationJOBOBJECT_SECURITY_LIMIT_INFORMATION Not implemented
JobObjectAssociateCompletionPortInformationJOBOBJECT_ASSOCIATE_COMPLETION_PORT Not implemented
Return ValueThe type of the returned information is dependent on the class requested

        
    """
    pass


def SetInformationJobObject(Job:typing.Any,JobObjectInfoClass:int,JobObjectInfo:dict) -> None:
    """
    Sets quotas and limits for a job


Args:

      Job(typing.Any):Handle to a job
      JobObjectInfoClass(int):The type of data required, one of JobObject* values
      JobObjectInfo(dict):Dictionary containing info to be set, as returned by win32job::QueryInformationJobObjectJobObjectInfoClassType of information to be setJobObjectBasicLimitInformationA JOBOBJECT_BASIC_LIMIT_INFORMATION dictJobObjectExtendedLimitInformationdict representing a JOBOBJECT_EXTENDED_LIMIT_INFORMATION structJobObjectEndOfJobTimeInformationdict representing a JOBOBJECT_END_OF_JOB_TIME_INFORMATION structJobObjectBasicUIRestrictionsdict representing a JOBOBJECT_BASIC_UI_RESTRICTIONS structJobObjectJobSetInformationInput is a JOBOBJECT_JOBSET_INFORMATION dict - Not implementedJobObjectSecurityLimitInformationInput is a JOBOBJECT_SECURITY_LIMIT_INFORMATION dict - Not implementedJobObjectAssociateCompletionPortInformationInput is a JOBOBJECT_ASSOCIATE_COMPLETION_PORT dict - Not implemented

Returns:

      None
        
    """
    pass

JOB_OBJECT_ALL_ACCESS = ...
JOB_OBJECT_ASSIGN_PROCESS = ...
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS = ...
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS = ...
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = ...
JOB_OBJECT_LIMIT_AFFINITY = ...
JOB_OBJECT_LIMIT_BREAKAWAY_OK = ...
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION = ...
JOB_OBJECT_LIMIT_JOB_MEMORY = ...
JOB_OBJECT_LIMIT_JOB_TIME = ...
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = ...
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME = ...
JOB_OBJECT_LIMIT_PRIORITY_CLASS = ...
JOB_OBJECT_LIMIT_PROCESS_MEMORY = ...
JOB_OBJECT_LIMIT_PROCESS_TIME = ...
JOB_OBJECT_LIMIT_SCHEDULING_CLASS = ...
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK = ...
JOB_OBJECT_LIMIT_VALID_FLAGS = ...
JOB_OBJECT_LIMIT_WORKINGSET = ...
JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS = ...
JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT = ...
JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO = ...
JOB_OBJECT_MSG_END_OF_JOB_TIME = ...
JOB_OBJECT_MSG_END_OF_PROCESS_TIME = ...
JOB_OBJECT_MSG_EXIT_PROCESS = ...
JOB_OBJECT_MSG_JOB_MEMORY_LIMIT = ...
JOB_OBJECT_MSG_NEW_PROCESS = ...
JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT = ...
JOB_OBJECT_POST_AT_END_OF_JOB = ...
JOB_OBJECT_QUERY = ...
JOB_OBJECT_RESERVED_LIMIT_VALID_FLAGS = ...
JOB_OBJECT_SECURITY_FILTER_TOKENS = ...
JOB_OBJECT_SECURITY_NO_ADMIN = ...
JOB_OBJECT_SECURITY_ONLY_TOKEN = ...
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN = ...
JOB_OBJECT_SECURITY_VALID_FLAGS = ...
JOB_OBJECT_SET_ATTRIBUTES = ...
JOB_OBJECT_SET_SECURITY_ATTRIBUTES = ...
JOB_OBJECT_TERMINATE = ...
JOB_OBJECT_TERMINATE_AT_END_OF_JOB = ...
JOB_OBJECT_UI_VALID_FLAGS = ...
JOB_OBJECT_UILIMIT_ALL = ...
JOB_OBJECT_UILIMIT_DESKTOP = ...
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS = ...
JOB_OBJECT_UILIMIT_EXITWINDOWS = ...
JOB_OBJECT_UILIMIT_GLOBALATOMS = ...
JOB_OBJECT_UILIMIT_HANDLES = ...
JOB_OBJECT_UILIMIT_NONE = ...
JOB_OBJECT_UILIMIT_READCLIPBOARD = ...
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS = ...
JOB_OBJECT_UILIMIT_WRITECLIPBOARD = ...
JobObjectAssociateCompletionPortInformation = ...
JobObjectBasicAccountingInformation = ...
JobObjectBasicAndIoAccountingInformation = ...
JobObjectBasicLimitInformation = ...
JobObjectBasicProcessIdList = ...
JobObjectBasicUIRestrictions = ...
JobObjectEndOfJobTimeInformation = ...
JobObjectExtendedLimitInformation = ...
JobObjectJobSetInformation = ...
JobObjectSecurityLimitInformation = ...
MaxJobObjectInfoClass = ...