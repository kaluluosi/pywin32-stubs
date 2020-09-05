from pywintypes import *
__all__=['CreateTransaction', 'RollbackTransaction', 'RollbackTransactionAsync', 'CommitTransaction', 'CommitTransactionAsync', 'GetTransactionId', 'OpenTransaction']
import typing
"""Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions."""


def CreateTransaction(TransactionAttributes:typing.Any=None,UOW:typing.Any=None,CreateOptions:int=0,IsolationLevel:int=0,IsolationFlags:int=0,Timeout:int=0,Description:typing.Any=None) -> int:
    """
    Creates a transaction


Args:

      TransactionAttributes(typing.Any):Security and inheritance for the transaction, can be None
      UOW(typing.Any):Reserved, use only None
      CreateOptions(int):TRANSACTION_DO_NOT_PROMOTE is only defined flag
      IsolationLevel(int):Reserved, use only 0
      IsolationFlags(int):Reserved, use only 0
      Timeout(int):Abort timeout in milliseconds
      Description(typing.Any):Text description of transaction, can be NoneWin32 API References

Returns:

      int
        
    """
    pass


def RollbackTransaction(TransactionHandle:typing.Any) -> None:
    """
    Rolls back a transaction


Args:

      TransactionHandle(typing.Any):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass


def RollbackTransactionAsync(TransactionHandle:typing.Any) -> None:
    """
    Rolls back a transaction asynchronously


Args:

      TransactionHandle(typing.Any):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass


def CommitTransaction(TransactionHandle:typing.Any) -> None:
    """
    Commits a transaction


Args:

      TransactionHandle(typing.Any):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass


def CommitTransactionAsync(TransactionHandle:typing.Any) -> None:
    """
    Commits a transaction asynchronously


Args:

      TransactionHandle(typing.Any):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass


def GetTransactionId(TransactionHandle:typing.Any) -> typing.Any:
    """
    Returns the transaction's GUID


Args:

      TransactionHandle(typing.Any):Handle to a transaction

Returns:

      typing.Any
        
    """
    pass


def OpenTransaction(DesiredAccess:int,TransactionId:typing.Any) -> int:
    """
    Creates a handle to an existing transaction


Args:

      DesiredAccess(int):Combination of TRANSACTION_* access rights
      TransactionId(typing.Any):GUID identifying the transaction

Returns:

      int
        
    """
    pass
