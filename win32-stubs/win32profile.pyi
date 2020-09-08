__all__=['', 'CreateEnvironmentBlock', 'DeleteProfile', 'ExpandEnvironmentStringsForUser', 'GetAllUsersProfileDirectory', 'GetDefaultUserProfileDirectory', 'GetEnvironmentStrings', 'GetProfilesDirectory', 'GetProfileType', 'GetUserProfileDirectory', 'LoadUserProfile', 'UnloadUserProfile']
from typing import *
from win32helper.win32typing import *
"""Wraps functions for dealing with user profiles"""


def CreateEnvironmentBlock(Token:'int',Inherit:'Any') -> 'dict':
    """
    Retrieves environment variables for a user

Args:

      Token(int):User token as returned by win32security::LogonUser, use None to retrieve system variables only
      Inherit(Any):Indicates if environment of current process should be inherited

Returns:

      dict
        
    """
    pass
        

def DeleteProfile(SidString:'str',ProfilePath:'str'=None,ComputerName:'str'=None) -> 'None':
    """
    Remove profile for a user identified by string SID from specified machine.

Args:

      SidString(str):String representation of user's Sid.  See win32security::ConvertSidToStringSid.
      ProfilePath(str):Profile directory, value queried from registry if not specified
      ComputerName(str):Name of computer from which to delete profile, local machine assumed if not specified

Returns:

      None
        
    """
    pass
        

def ExpandEnvironmentStringsForUser(Token:'int',Src:'str') -> 'str':
    """
    Replaces environment variables in a string with 

per-user values

Args:

      Token(int):The logon token for a user.  Use None for system variables.
      Src(str):String containing environment variables enclosed in % signs

Returns:

      str
        
    """
    pass
        

def GetAllUsersProfileDirectory() -> 'str':
    """
    Retrieve All Users profile path

Args:



Returns:

      str
        
    """
    pass
        

def GetDefaultUserProfileDirectory() -> 'str':
    """
    Retrieve Default user profile

Args:



Returns:

      str
        
    """
    pass
        

def GetEnvironmentStrings() -> 'dict':
    """
    Retrieves environment variables for current process

Args:



Returns:

      dict
        
    """
    pass
        

def GetProfilesDirectory() -> 'str':
    """
    Retrieves directory where user profiles are stored

Args:



Returns:

      str
        
    """
    pass
        

def GetProfileType() -> 'int':
    """
    Returns type of current user's profile

Args:



Returns:

      int:win32profile.GetProfileType

int = GetProfileType()Returns type of current user's profile
Return ValueReturns a combination of PT_* flags

        
    """
    pass
        

def GetUserProfileDirectory(Token:'int') -> 'str':
    """
    Returns profile directory for a logon token

Args:

      Token(int):User token as returned by win32security::LogonUser

Returns:

      str
        
    """
    pass
        

def LoadUserProfile(hToken:'int',ProfileInfo:'PyPROFILEINFO') -> 'PyHKEY':
    """
    Loads user settings into registry

Args:

      hToken(int):Logon token as returned by win32security::LogonUser, win32security::OpenThreadToken, etc
      ProfileInfo(PyPROFILEINFO):Dictionary representing a PROFILEINFO structureCommentsSE_BACKUP_NAME and SE_RESTORE_NAME privs are required, but do not have to be enabledReturn ValueReturns a handle to user's registry key.

Returns:

      PyHKEY:Dictionary representing a PROFILEINFO structureComments

SE_BACKUP_NAME and SE_RESTORE_NAME privs are required, but do not have to be enabled
Return ValueReturns a handle to user's registry key.

        
    """
    pass
        

def UnloadUserProfile(Token:'int',Profile:'PyHKEY') -> 'None':
    """
    None

Args:

      Token(int):Logon token as returned by win32security::LogonUser, win32security::OpenProcessToken, etc
      Profile(PyHKEY):Registry handle as returned by win32profile::LoadUserProfile

Returns:

      None
        
    """
    pass
        