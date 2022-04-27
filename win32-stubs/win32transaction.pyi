__all__=['', 'CreateTransaction', 'RollbackTransaction', 'RollbackTransactionAsync', 'CommitTransaction', 'CommitTransactionAsync', 'GetTransactionId', 'OpenTransaction']
import typing
import win32typing
"""Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions."""


def CreateTransaction(TransactionAttributes:'win32typing.PySECURITY_ATTRIBUTES'=None,UOW:'win32typing.PyIID'=None,CreateOptions:'typing.Any'=0,IsolationLevel:'typing.Any'=0,IsolationFlags:'typing.Any'=0,Timeout:'typing.Any'=0,Description:'str'=None) -> 'int':
    """
    Creates a transaction

Args:

      TransactionAttributes(win32typing.PySECURITY_ATTRIBUTES):Security and inheritance for the transaction, can be None
      UOW(win32typing.PyIID):Reserved, use only None
      CreateOptions(typing.Any):TRANSACTION_DO_NOT_PROMOTE is only defined flag
      IsolationLevel(typing.Any):Reserved, use only 0
      IsolationFlags(typing.Any):Reserved, use only 0
      Timeout(typing.Any):Abort timeout in milliseconds
      Description(str):Text description of transaction, can be NoneWin32 API References

Returns:

      int
        
    """
    pass
        

def RollbackTransaction(TransactionHandle:'int') -> 'None':
    """
    Rolls back a transaction

Args:

      TransactionHandle(int):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass
        

def RollbackTransactionAsync(TransactionHandle:'int') -> 'None':
    """
    Rolls back a transaction asynchronously

Args:

      TransactionHandle(int):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass
        

def CommitTransaction(TransactionHandle:'int') -> 'None':
    """
    Commits a transaction

Args:

      TransactionHandle(int):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass
        

def CommitTransactionAsync(TransactionHandle:'int') -> 'None':
    """
    Commits a transaction asynchronously

Args:

      TransactionHandle(int):Handle to a transactionWin32 API References

Returns:

      None
        
    """
    pass
        

def GetTransactionId(TransactionHandle:'int') -> 'win32typing.PyIID':
    """
    Returns the transaction's GUID

Args:

      TransactionHandle(int):Handle to a transaction

Returns:

      win32typing.PyIID
        
    """
    pass
        

def OpenTransaction(DesiredAccess:'typing.Any',TransactionId:'win32typing.PyIID') -> 'int':
    """
    Creates a handle to an existing transaction

Args:

      DesiredAccess(typing.Any):Combination of TRANSACTION_* access rights
      TransactionId(win32typing.PyIID):GUID identifying the transaction

Returns:

      int
        
    """
    pass
        