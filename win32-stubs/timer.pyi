from pywintypes import *
__all__=['set_timer', 'kill_timer']
import typing
"""Extension that wraps Win32 Timer functions"""


def set_timer(Elapse:int,TimerFunc:typing.Any) -> int:
    """
    Creates a timer that executes a callback function


Args:

      Elapse(int):Timer period, in milliseconds
      TimerFunc(typing.Any):Callback function.  Will be called with with 2 int args: (timer_id, time)CommentsUses the SetTimer function.Return ValueReturns the id of the timer, which can be passed to kill_timer to stop it.

Returns:

      int:Callback function.  Will be called with with 2 int 

args: (timer_id, time)Comments

Uses the SetTimer function.
Return ValueReturns the id of the timer, which can be passed to kill_timer to stop it.

        
    """
    pass


def kill_timer(IDEvent:int) -> typing.Any:
    """
    Creates a timer that executes a callback function


Args:

      IDEvent(int):Timer id as returned by timer::set_timerCommentsUses the KillTimer API function.

Returns:

      typing.Any
        
    """
    pass
