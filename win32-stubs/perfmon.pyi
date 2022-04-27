__all__=['', 'LoadPerfCounterTextStrings', 'UnloadPerfCounterTextStrings', 'CounterDefinition', 'ObjectType', 'PerfMonManager']
import typing
import win32typing
"""A module which wraps Performance Monitor functions."""


def LoadPerfCounterTextStrings() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def UnloadPerfCounterTextStrings() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def CounterDefinition() -> 'win32typing.PyPERF_COUNTER_DEFINITION':
    """
    None

Args:



Returns:

      win32typing.PyPERF_COUNTER_DEFINITION
        
    """
    pass
        

def ObjectType() -> 'win32typing.PyPERF_OBJECT_TYPE':
    """
    Creates a new PERF_OBJECT_TYPE object

Args:



Returns:

      win32typing.PyPERF_OBJECT_TYPE
        
    """
    pass
        

def PerfMonManager(serviceName:'str',seqPerfObTypes:'typing.List[win32typing.PyPERF_OBJECT_TYPE]',mappingName:'str'=None,eventSourceName:'str'=None) -> 'win32typing.PyPerfMonManager':
    """
    Creates a new PERF_OBJECT_TYPE object

Args:

      serviceName(str):The name of the service for which data is being provided.
      seqPerfObTypes(typing.List[win32typing.PyPERF_OBJECT_TYPE]):A sequence of objects to use in the performance monitor.  At this stage, len(seqPerfObTypes) must == 1.
      mappingName(str):The name of the mapping to open.  This must be the same as the DLL name providing the information.  If None, the serviceName is used.
      eventSourceName(str):The name used by the DLL for error messages in the registry.  If None, the serviceName is used.CommentsThe application need not be a service, but it must have an entry in the Services section of the registry.  This limits the performance monitor to being able to provide only one 'counter type', but still many counters within that type. See the documentation for the Performance Monitor API for more details.

Returns:

      win32typing.PyPerfMonManager
        
    """
    pass
        