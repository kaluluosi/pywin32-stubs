__all__=['', 'CreateTransaction', 'RollbackTransaction', 'RollbackTransactionAsync', 'CommitTransaction', 'CommitTransactionAsync', 'GetTransactionId', 'OpenTransaction']
from typing import *
from win32helper.win32typing import *
"""Module wrapping Kernal Transaction Manager functions, as used with 

transacted NTFS and transacted registry functions."""


def CreateTransaction(TransactionAttributes:'PySECURITY_ATTRIBUTES'=None,UOW:'PyIID'=None,CreateOptions:'int'=0,IsolationLevel:'int'=0,IsolationFlags:'int'=0,Timeout:'int'=0,Description:'str'=None) -> 'int':
    """
    Creates a transaction

Args:

      TransactionAttributes(PySECURITY_ATTRIBUTES):Security and inheritance for the transaction, can be None
      UOW(PyIID):Reserved, use only None
      CreateOptions(int):TRANSACTION_DO_NOT_PROMOTE is only defined flag
      IsolationLevel(int):Reserved, use only 0
      IsolationFlags(int):Reserved, use only 0
      Timeout(int):Abort timeout in milliseconds
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
        

def GetTransactionId(TransactionHandle:'int') -> 'PyIID':
    """
    Returns the transaction's GUID

Args:

      TransactionHandle(int):Handle to a transaction

Returns:

      PyIID
        
    """
    pass
        

def OpenTransaction(DesiredAccess:'int',TransactionId:'PyIID') -> 'int':
    """
    Creates a handle to an existing transaction

Args:

      DesiredAccess(int):Combination of TRANSACTION_* access rights
      TransactionId(PyIID):GUID identifying the transaction

Returns:

      int
        
    """
    pass
        