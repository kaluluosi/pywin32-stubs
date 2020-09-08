__all__=['NetGetJoinInformation', 'NetGroupGetInfo', 'NetGroupGetUsers', 'NetGroupSetUsers', 'NetGroupSetInfo', 'NetGroupAdd', 'NetGroupAddUser', 'NetGroupDel', 'NetGroupDelUser', 'NetGroupEnum', 'NetGroupAdd', 'NetLocalGroupAddMembers', 'NetLocalGroupDelMembers', 'NetGroupDel', 'NetGroupEnum', 'NetGroupGetInfo', 'NetLocalGroupGetMembers', 'NetGroupSetInfo', 'NetLocalGroupSetMembers', 'NetMessageBufferSend', 'NetMessageNameAdd', 'NetMessageNameDel', 'NetMessageNameEnum', 'NetServerEnum', 'NetServerGetInfo', 'NetServerSetInfo', 'NetShareAdd', 'NetShareDel', 'NetShareCheck', 'NetShareEnum', 'NetShareGetInfo', 'NetShareSetInfo', 'NetUserAdd', 'NetUserChangePassword', 'NetUserEnum', 'NetUserGetGroups', 'NetUserGetInfo', 'NetUserGetLocalGroups', 'NetUserSetInfo', 'NetUserDel', 'NetUserModalsGet', 'NetUserModalsSet', 'NetWkstaUserEnum', 'NetWkstaGetInfo', 'NetWkstaSetInfo', 'NetWkstaTransportEnum', 'NetWkstaTransportAdd', 'NetWkstaTransportDel', 'NetServerDiskEnum', 'NetUseAdd', 'NetUseDel', 'NetUseEnum', 'NetUseGetInfo', 'NetGetAnyDCName', 'NetGetDCName', 'NetSessionEnum', 'NetSessionDel', 'NetSessionGetInfo', 'NetFileEnum', 'NetFileClose', 'NetFileGetInfo', 'NetStatisticsGet', 'NetServerComputerNameAdd', 'NetServerComputerNameDel', 'NetValidateName', 'NetValidatePasswordPolicy']
from typing import *
from .win32typing import *
"""A module encapsulating the Windows Network API."""


def NetGetJoinInformation() -> 'Tuple[str, int]':
    """
    Retrieves join status information for the specified 

computer.

Args:



Returns:

      Tuple[str, int]
        
    """
    pass
        

def NetGroupGetInfo(server:'Union[str]',groupname:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about a particular group on a server.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group name
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetGroupGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyGROUP_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetGroupGetUsers(server:'Union[str]',groupName:'Union[str]',level:'int',resumeHandle:'int'=0,prefLen:'int'=4096) -> 'Tuple[Any, Any, Any, Any]':
    """
    Enumerates the users in a group.

Args:

      server(Union[str]):The name of the server, or None.
      groupName(Union[str]):The name of the local group.
      level(int):The level of data required.
      resumeHandle(int):A resume handle.  See the return description for more information.
      prefLen(int):The preferred length of the data buffer.Win32 API References

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetGroupGetUsers at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyGROUP_USERS_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetGroupSetUsers(server:'Union[str]',group:'Union[str]',level:'int',members:'Tuple[Any, Any]') -> 'None':
    """
    Sets the members of a local group.  Any existing members not listed are 

removed.

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      level(int):The level of information in the data. Must be 0
      members(Tuple[Any, Any]):The list of new members to add.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupSetInfo(server:'Union[str]',groupname:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about a particular group account on a server.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group name
      level(int):The information level contained in the data
      data(Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Creates a new group.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupAddUser(server:'Union[str]',group:'Union[str]',username:'Union[str]') -> 'None':
    """
    Adds a user to the group

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      username(Union[str]):The user to add to the group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDel(server:'Union[str]',groupname:'Union[str]') -> 'None':
    """
    Deletes a group.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDelUser(server:'Union[str]',group:'Union[str]',username:'Union[str]') -> 'None':
    """
    Deletes a user from the group

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      username(Union[str]):The user to delete from the group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupEnum(server:'Union[str]',level:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Enumerates all groups.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The level of data required.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetGroupEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyGROUP_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetGroupAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Creates a new group.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupAddMembers(server:'Union[str]',group:'Union[str]',level:'int',members:'Tuple[Any, Any]') -> 'None':
    """
    Adds users to a local group.

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      level(int):The level of information in the data.
      members(Tuple[Any, Any]):The new members to add.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupDelMembers(server:'Union[str]',group:'Union[str]',members:'List[str]') -> 'None':
    """
    Deletes users from a local group.

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      members(List[str]):A list of strings with fully qualified user names to delete from a local group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDel(server:'Union[str]',groupname:'Union[str]') -> 'None':
    """
    Deletes a group.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupEnum(server:'Union[str]',level:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Enumerates all groups.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The level of data required.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetGroupEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyGROUP_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetGroupGetInfo(server:'Union[str]',groupname:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about a particular group on a server.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group name
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetGroupGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyGROUP_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetLocalGroupGetMembers(server:'Union[str]',groupName:'Union[str]',level:'int',resumeHandle:'int'=0,prefLen:'int'=4096) -> 'Tuple[Any, Any, Any, Any]':
    """
    Enumerates the members in a local 

group.

Args:

      server(Union[str]):The name of the server, or None.
      groupName(Union[str]):The name of the local group.
      level(int):The level of data required.
      resumeHandle(int):A resume handle.  See the return description for more information.
      prefLen(int):The preferred length of the data buffer.Win32 API References

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetLocalGroupGetMembers at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyLOCALGROUP_MEMBERS_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetGroupSetInfo(server:'Union[str]',groupname:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about a particular group account on a server.

Args:

      server(Union[str]):The name of the server, or None.
      groupname(Union[str]):The group name
      level(int):The information level contained in the data
      data(Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupSetMembers(server:'Union[str]',group:'Union[str]',level:'int',members:'Tuple[Any, Any]') -> 'None':
    """
    Sets the members of a local group. Any existing members not listed 

are removed.

Args:

      server(Union[str]):The name of the server, or None.
      group(Union[str]):The group name
      level(int):The level of information in the data.
      members(Tuple[Any, Any]):The list of new members to add.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetMessageBufferSend(domain:'str',userName:'str',fromName:'str',message:'str') -> 'None':
    """
    sends a string to a registered message alias.

Args:

      domain(str):Specifies the name of the remote server on which the function is to execute. None or empty string the local computer.
      userName(str):Specifies the message name to which the message buffer should be sent.
      fromName(str):The user the message is to come from, or None for the current user.
      message(str):The message textWin32 API References

Returns:

      None
        
    """
    pass
        

def NetMessageNameAdd(server:'Union[str, Any]',msgname:'Union[str, Any]') -> 'None':
    """
    Adds a message alias for specified machine

Args:

      server(Union[str, Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None
      msgname(Union[str, Any]):Message alias to add, 15 characters max

Returns:

      None
        
    """
    pass
        

def NetMessageNameDel(server:'Union[str, Any]',msgname:'Union[str, Any]') -> 'None':
    """
    Removes a message alias for specified machine

Args:

      server(Union[str, Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None
      msgname(Union[str, Any]):Message alias to delete for specified machine

Returns:

      None
        
    """
    pass
        

def NetMessageNameEnum(Server:'Union[str, Any]') -> 'None':
    """
    Lists aliases for a computer

Args:

      Server(Union[str, Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None

Returns:

      None
        
    """
    pass
        

def NetServerEnum(server:'Union[str]',level:'int',type:'int',prefLen:'int',domain:'Union[str]'=None,resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about each server of a 

particular type

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The level of data required.
      type(int):Type of server to return - one of the SV_TYPE_* constants.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      domain(Union[str]):The domain to enumerate, or None for the current domain.
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetServerEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PySERVER_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetServerGetInfo(server:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about a particular server.

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetServerGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PySERVER_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetServerSetInfo(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about a particular server.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Creates a new share.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data.  Must be level 2 or 502.
      data(Any):A dictionary holding the share data, in the format of SHARE_INFO_*Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareDel(server:'Union[str]',shareName:'Union[str]',reserved:'int'=0) -> 'None':
    """
    Deletes a share

Args:

      server(Union[str]):The name of the server, or None.
      shareName(Union[str]):The share name
      reserved(int):Must be zero.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareCheck(server:'Union[str]',deviceName:'Union[str]') -> 'Tuple[Any, type]':
    """
    Checks if server is sharing a device

Args:

      server(Union[str]):The name of the server, or None.
      deviceName(Union[str]):The share nameWin32 API References

Returns:

      Tuple[Any, type]:Search for NetShareCheck at msdn, google or google groups.
Return ValueThe result is (1, type-of-device) if device is shared, (0, None) if it is not shared.

        
    """
    pass
        

def NetShareEnum(server:'Union[str]',level:'int',prefLen:'int',serverName:'Any',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about each shared resource 

on a server.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The level of data required.
      prefLen(int):The preferred length of the data buffer.Alternative Parameters
      serverName(Any):The name of the server on which the call should execute, or None for the local computer.CommentsIf the old style is used, the result is a list of [(shareName, type, remarks), ...]Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetShareEnum 

param 1 is not declared as const :-( at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PySHARE_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetShareGetInfo(server:'Union[str]',netname:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about a particular share on a server.

Args:

      server(Union[str]):The name of the server, or None.
      netname(Union[str]):The network name
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetShareGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PySHARE_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetShareSetInfo(server:'Union[str]',netname:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about a particular share on a server.

Args:

      server(Union[str]):The name of the server, or None.
      netname(Union[str]):The network name
      level(int):The information level contained in the data
      data(Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Creates a new user.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the user data in the format of PyUSER_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserChangePassword(server:'Union[str]',username:'Union[str]',oldPassword:'Union[str]',newPassword:'Union[str]') -> 'None':
    """
    Changes the password for a user.

Args:

      server(Union[str]):The name of the server, or None.
      username(Union[str]):The user name, or None for the current username.
      oldPassword(Union[str]):The old password
      newPassword(Union[str]):The new passwordCommentsA server or domain can be configured to require that a user log on to change the password on a user account. If that is the case, you need administrator or account operator access to change the password for another user acount. If logging on is not required, you can change the password for any user account, so long as you know the current password.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserEnum(server:'Union[str]',level:'int',filter:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Enumerates all users.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The level of data required.
      filter(int):The types of accounts to enumerate.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetUserEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyUSER_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetUserGetGroups(serverName:'str',userName:'str') -> 'List[Any]':
    """
    Returns a list of groups,attributes for all groups 

for the user.

Args:

      serverName(str):The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.
      userName(str):The name of the user to search for in each group account. To Do This needs to be extended to support the new model, while not breaking existing code.  A default arg would be perfect.Return ValueAlways makes the level 1 call and returns all data. Data return format is a Python List.  Each "Item" is a tuple of (groupname, attributes).  "(s,i)" respectively.  In NT 4 the attributes seem to be hardcoded to 7. Earlier version of NT have not been tested.

Returns:

      List[Any]:The name of the user to search for in each group account. To Do This needs to be extended to support the new model, while 

not breaking existing code.  A default arg would be perfect.
Return ValueAlways makes the level 1 call and returns all data. 

Data return format is a Python List.  Each "Item" 

is a tuple of (groupname, attributes).  "(s,i)" respectively.  In NT 4 the attributes seem to be hardcoded to 7. 

Earlier version of NT have not been tested.

        
    """
    pass
        

def NetUserGetInfo(server:'Union[str]',username:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about a particular user account on a server.

Args:

      server(Union[str]):The name of the server, or None.
      username(Union[str]):The user name
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetUserGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyUSER_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetUserGetLocalGroups(serverName:'str',userName:'str',flags:'int') -> 'List[Any]':
    """
    Retrieves a list of local groups to which a specified user 

belongs.

Args:

      serverName(str):The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.
      userName(str):The name of the user to search for in each group account. This parameter can be of the form &ltUserName&gt, in which case the username is expected to be found on servername. The user name can also be of the form &ltDomainName&gt\\&ltUserName&gt in which case &ltDomainName&gt is associated with servername and &ltUserName&gt is expected to be to be found on that domain.
      flags(int):Flags for the call. To Do This needs to be extended to support the new model, while not breaking existing code.  A default arg would be perfect.

Returns:

      List[Any]
        
    """
    pass
        

def NetUserSetInfo(server:'Union[str]',username:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about a particular user account on a server.

Args:

      server(Union[str]):The name of the server, or None.
      username(Union[str]):The user name
      level(int):The information level contained in the data
      data(Any):A dictionary holding the user data in the format of PyUSER_INFO_*Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserDel(server:'Union[str]',username:'Union[str]') -> 'None':
    """
    Deletes a user.

Args:

      server(Union[str]):The name of the server, or None.
      username(Union[str]):The user nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetUserModalsGet(server:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves global user information on a server.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the dataWin32 API References

Returns:

      dict:Search for NetUserModalsGet at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyUSER_MODALS_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetUserModalsSet(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets global user parameters on a server.

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the data in the format of PyUSER_MODALS_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaUserEnum(server:'Union[str]',level:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about all users 

currently logged on to the workstation.

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The level of data required.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetWkstaUserEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyWKSTA_USER_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetWkstaGetInfo(server:'Union[str]',level:'int') -> 'dict':
    """
    Retrieves information about the configuration elements for a workstation

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.Win32 API References

Returns:

      dict:Search for NetWkstaGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyWKSTA_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetWkstaSetInfo(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Sets information about the configuration elements for a workstation

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaTransportEnum(server:'Union[str]',level:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about transport 

protocols that are currently managed by the redirector

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The level of data required.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetWkstaTransportEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyWKSTA_TRANSPORT_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetWkstaTransportAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    binds the redirector to a transport

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaTransportDel(server:'Union[str]',TransportName:'Union[str]',ucond:'int'=0) -> 'None':
    """
    unbinds the transport protocol from redirector

Args:

      server(Union[str]):The name of the server, or None.
      TransportName(Union[str]):The name of the transport to delete.
      ucond(int):Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCEWin32 API References

Returns:

      None
        
    """
    pass
        

def NetServerDiskEnum(server:'Union[str]',level:'int') -> 'list':
    """
    Retrieves the list of disk drives on a server.

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The level of data required. Must be 0.Win32 API References

Returns:

      list:Search for NetServerDiskEnum at msdn, google or google groups.
Return ValueThe result is a list of drives on the server

        
    """
    pass
        

def NetUseAdd(server:'Union[str]',level:'int',data:'Any') -> 'None':
    """
    Establishes connection between local or NULL device name and a shared resource through 

redirector

Args:

      server(Union[str]):The name of the server, or None.
      level(int):The information level contained in the data
      data(Any):A dictionary holding the share data in the format of PyUSE_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUseDel(server:'Union[str]',useName:'Union[str]',forceCond:'int'=0) -> 'None':
    """
    Ends connection to a shared resource.

Args:

      server(Union[str]):The name of the server, or None.
      useName(Union[str]):The share name
      forceCond(int):Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCEWin32 API References

Returns:

      None
        
    """
    pass
        

def NetUseEnum(server:'Union[str]',level:'int',prefLen:'int',resumeHandle:'int'=0) -> 'Tuple[Any, Any, Any, Any]':
    """
    Retrieves information about transport protocols that 

are currently managed by the redirector

Args:

      server(Union[str]):The name of the server to execute on, or None.
      level(int):The level of data required. Currently levels 0, 1 and 2 are supported.
      prefLen(int):The preferred length of the data buffer.Win32 API References
      resumeHandle(int):A resume handle.  See the return description for more information.

Returns:

      Tuple[Any, Any, Any, Any]:Search for NetUseEnum at msdn, google or google groups.
Return ValueThe result is a list of items read (with each item being a dictionary of format 

PyUSE_INFO_*, depending on the level parameter), 

the total available, and a new "resume handle".  The first time you call 

this function, you should pass zero for the resume handle.  If more data 

is available than what was returned, a new non-zero resume handle will be 

returned, which can be used to call the function again to fetch more data. 

This process may repeat, each time with a new resume handle, until zero is 

returned for the new handle, indicating all the data has been read.

        
    """
    pass
        

def NetUseGetInfo(server:'Union[str]',usename:'Union[str]',level:'int'=0) -> 'dict':
    """
    Retrieves information about the configuration elements for a workstation

Args:

      server(Union[str]):The name of the server to execute on, or None.
      usename(Union[str]):The name of the locally mapped resource.
      level(int):The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.Win32 API References

Returns:

      dict:Search for NetUseGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyUSE_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetGetAnyDCName(server:'str'=None,domain:'str'=None) -> 'str':
    """
    Returns the name of any domain controller trusted by the specified 

server.

Args:

      server(str):Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.
      domain(str):Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.

Returns:

      str
        
    """
    pass
        

def NetGetDCName(server:'str'=None,domain:'str'=None) -> 'str':
    """
    Returns the name of the primary domain controller (PDC).

Args:

      server(str):Specifies the name of the remote server on which the function is to execute. If this parameter is None, the local computer is used.
      domain(str):Specifies the name of the domain. If this parameter is None, the name of the domain controller for the primary domain is used.

Returns:

      str
        
    """
    pass
        

def NetSessionEnum(level:'int',server:'Union[str]'=None,client:'Union[str]'=None,username:'Union[str]'=None) -> 'Tuple[dict, ...]':
    """
    Returns network sessions for a server, limited to single client and/or 

user if specified.

Args:

      level(int):Level of information requested, currently accepts 0, 1, 2, 10, and 502
      server(Union[str]):The name of the server for which to list sessions, local machine assumed if None
      client(Union[str]):Name of client computer, or None to list all computer sessions
      username(Union[str]):User name, or None to list all connected usersReturn ValueReturns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified

Returns:

      Tuple[dict, ...]:User name, or None to list all connected users
Return ValueReturns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified

        
    """
    pass
        

def NetSessionDel(server:'Union[str]',client:'Union[str]'=None,username:'Union[str]'=None) -> 'None':
    """
    Disconnects network connections on a server

Args:

      server(Union[str]):The name of the server on which to operate, local machine assumed if None or blank
      client(Union[str]):Name of client computer, or None
      username(Union[str]):User name, or None for all connected usersReturn ValueReturns None on success

Returns:

      None:User name, or None for all connected users
Return ValueReturns None on success

        
    """
    pass
        

def NetSessionGetInfo(level:'int',server:'Union[str]',client:'Union[str]',username:'Union[str]') -> 'dict':
    """
    Returns information for a network session from specified client

Args:

      level(int):Level of information requested, currently accepts 0, 1, 2, 10, and 502
      server(Union[str]):The name of the server on which to operate, None or blank assumes local machine
      client(Union[str]):Name of client computer
      username(Union[str]):User that established sessionReturn ValueReturns a dictionary representing a SESSION_INFO_* struct, depending on level specified

Returns:

      dict:User that established sessionReturn ValueReturns a dictionary representing a SESSION_INFO_* struct, depending on level specified

        
    """
    pass
        

def NetFileEnum(level:'int',servername:'Union[str]'=None,basepath:'Union[str]'=None,username:'Union[str]'=None) -> 'Tuple[dict, ...]':
    """
    Lists remotely opened resources on a server

Args:

      level(int):Level of information, 2 or 3 supported
      servername(Union[str]):The name of the server for which to list open resources, local machine assumed if None
      basepath(Union[str]):If specified, limits returned list to files on given path
      username(Union[str]):User that opened resource, or None to list open files for all usersReturn ValueReturns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified

Returns:

      Tuple[dict, ...]:User that opened resource, or None to list open files for all users
Return ValueReturns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified

        
    """
    pass
        

def NetFileClose(servername:'Union[str]',fileid:'int') -> 'None':
    """
    Closes an open network resource on a server

Args:

      servername(Union[str]):Name of server on which to operate, local machine assumed if None
      fileid(int):Id of opened resource, as returned by win32net::NetFileEnum

Returns:

      None
        
    """
    pass
        

def NetFileGetInfo(level:'int',servername:'Union[str]',fileid:'int') -> 'dict':
    """
    Returns information about an open network resource

Args:

      level(int):Level of information to return, 2 or 3 supported
      servername(Union[str]):Server on which resource is open, local machine assumed if None
      fileid(int):Id of opened resource, as returned by win32net::NetFileEnum

Returns:

      dict
        
    """
    pass
        

def NetStatisticsGet(server:'Union[str]',service:'Union[str]',level:'int',options:'int') -> 'dict':
    """
    Retrieves network statistics for specified service on specified machine

Args:

      server(Union[str]):Name of server/workstation to retrieve statistics for (None or blank uses local).
      service(Union[str]):SERVICE_SERVER or SERVICE_WORKSTATION
      level(int):Only 0 currently supported.
      options(int):Must be zero.Return ValueThe result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct

Returns:

      dict:Must be zero.Return ValueThe result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct

        
    """
    pass
        

def NetServerComputerNameAdd(ServerName:'Union[str]',EmulatedDomainName:'Union[str]',EmulatedServerName:'Union[str]') -> 'None':
    """
    Adds an additional network name for a server

Args:

      ServerName(Union[str]):Name of server that will receive additional name
      EmulatedDomainName(Union[str]):Domain under which to add the new server name, can be None
      EmulatedServerName(Union[str]):New network name that server will respond toReturn ValueReturns none on success

Returns:

      None:New network name that server will respond toReturn ValueReturns none on success

        
    """
    pass
        

def NetServerComputerNameDel(ServerName:'Union[str]',EmulatedServerName:'Union[str]') -> 'None':
    """
    None

Args:

      ServerName(Union[str]):Name of server on which to operate
      EmulatedServerName(Union[str]):Network name to be removedReturn ValueReturns none on success

Returns:

      None:Network name to be removedReturn ValueReturns none on success

        
    """
    pass
        

def NetValidateName(Server:'Union[str]',Name:'Union[str]',NameType:'int',Account:'Union[str]'=None,Password:'Union[str]'=None) -> 'None':
    """
    Checks that domain/machine/workgroup name is valid for given context

Args:

      Server(Union[str]):Name of server on which to execute (None or blank uses local)
      Name(Union[str]):Machine, domain, or workgroup name to validate
      NameType(int):Type of name to validate - from NETSETUP_NAME_TYPE enum (win32net.NetSetup*)
      Account(Union[str]):Account name to use while validating, current security context is used if not specified
      Password(Union[str]):Password for AccountCommentsIf Account and Password aren't passed, current logon credentials are usedWill raise NotImplementedError if not available on this platform.Return ValueReturns none if valid, exception if not

Returns:

      None:Password for Account
Comments

If Account and Password aren't passed, current logon credentials are used

Will raise NotImplementedError if not available on this platform.
Return ValueReturns none if valid, exception if not

        
    """
    pass
        

def NetValidatePasswordPolicy(Server:'Union[str]',Qualifier:'None',ValidationType:'int',arg:'Union[dict, tuple]') -> 'None':
    """
    Allows an application to check 

password compliance against an application-provided account database and 

verify that passwords meet the complexity, aging, minimum length, and 

history reuse requirements of a password policy.

Args:

      Server(Union[str]):Name of server on which to execute (None or blank uses local)
      Qualifier(None):Reserved, must be None
      ValidationType(int):The type of password validation to perform
      arg(Union[dict, tuple]):Depends on the ValidationType param - either a PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG,  PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG or PyNET_VALIDATE_PASSWORD_RESET_INPUT_ARG tuple or dict.CommentsWill raise NotImplementedError if not available on this platform, or raise win32net.error if the function fails.Return ValueReturns a tuple of (PyNET_VALIDATE_PERSISTED_FIELDS, int) with the integer being the ValidationResult.

Returns:

      None:Depends on the ValidationType param - either 

a PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG,  PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG 

or PyNET_VALIDATE_PASSWORD_RESET_INPUT_ARG

 tuple or dict.Comments

Will raise NotImplementedError if not available on this platform, or 

raise win32net.error if the function fails.
Return ValueReturns a tuple of (PyNET_VALIDATE_PERSISTED_FIELDS, int) with 

the integer being the ValidationResult.

        
    """
    pass
        