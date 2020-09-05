from pywintypes import *
__all__=['LoadPerfCounterTextStrings', 'UnloadPerfCounterTextStrings', 'CounterDefinition', 'ObjectType', 'PerfMonManager']
import typing
"""A module which wraps Performance Monitor functions."""


def LoadPerfCounterTextStrings() -> None:
    """
    None


Args:



Returns:

      None
        
    """
    pass


def UnloadPerfCounterTextStrings() -> None:
    """
    None


Args:



Returns:

      None
        
    """
    pass


def CounterDefinition() -> typing.Any:
    """
    None


Args:



Returns:

      typing.Any
        
    """
    pass


def ObjectType() -> typing.Any:
    """
    Creates a new PERF_OBJECT_TYPE object


Args:



Returns:

      typing.Any
        
    """
    pass


def PerfMonManager(serviceName:typing.Any,seqPerfObTypes:typing.Any,mappingName:typing.Any=None,eventSourceName:typing.Any=None) -> typing.Any:
    """
    Creates a new PERF_OBJECT_TYPE object


Args:

      serviceName(typing.Any):The name of the service for which data is being provided.
      seqPerfObTypes(typing.Any):A sequence of objects to use in the performance monitor.  At this stage, len(seqPerfObTypes) must == 1.
      mappingName(typing.Any):The name of the mapping to open.  This must be the same as the DLL name providing the information.  If None, the serviceName is used.
      eventSourceName(typing.Any):The name used by the DLL for error messages in the registry.  If None, the serviceName is used.CommentsThe application need not be a service, but it must have an entry in the Services section of the registry.  This limits the performance monitor to being able to provide only one 'counter type', but still many counters within that type. See the documentation for the Performance Monitor API for more details.

Returns:

      typing.Any
        
    """
    pass
