__all__=['', 'NetGetJoinInformation', 'NetGroupGetInfo', 'NetGroupGetUsers', 'NetGroupSetUsers', 'NetGroupSetInfo', 'NetGroupAdd', 'NetGroupAddUser', 'NetGroupDel', 'NetGroupDelUser', 'NetGroupEnum', 'NetGroupAdd', 'NetLocalGroupAddMembers', 'NetLocalGroupDelMembers', 'NetGroupDel', 'NetGroupEnum', 'NetGroupGetInfo', 'NetLocalGroupGetMembers', 'NetGroupSetInfo', 'NetLocalGroupSetMembers', 'NetMessageBufferSend', 'NetMessageNameAdd', 'NetMessageNameDel', 'NetMessageNameEnum', 'NetServerEnum', 'NetServerGetInfo', 'NetServerSetInfo', 'NetShareAdd', 'NetShareDel', 'NetShareCheck', 'NetShareEnum', 'NetShareGetInfo', 'NetShareSetInfo', 'NetUserAdd', 'NetUserChangePassword', 'NetUserEnum', 'NetUserGetGroups', 'NetUserGetInfo', 'NetUserGetLocalGroups', 'NetUserSetInfo', 'NetUserDel', 'NetUserModalsGet', 'NetUserModalsSet', 'NetWkstaUserEnum', 'NetWkstaGetInfo', 'NetWkstaSetInfo', 'NetWkstaTransportEnum', 'NetWkstaTransportAdd', 'NetWkstaTransportDel', 'NetServerDiskEnum', 'NetUseAdd', 'NetUseDel', 'NetUseEnum', 'NetUseGetInfo', 'NetGetAnyDCName', 'NetGetDCName', 'NetSessionEnum', 'NetSessionDel', 'NetSessionGetInfo', 'NetFileEnum', 'NetFileClose', 'NetFileGetInfo', 'NetStatisticsGet', 'NetServerComputerNameAdd', 'NetServerComputerNameDel', 'NetValidateName', 'NetValidatePasswordPolicy']
import typing
import win32typing
"""A module encapsulating the Windows Network API."""


def NetGetJoinInformation() -> 'typing.Tuple[str, typing.Any]':
    """
    Retrieves join status information for the specified 

computer.

Args:



Returns:

      typing.Tuple[str, typing.Any]
        
    """
    pass
        

def NetGroupGetInfo(server:'typing.Union[str]',groupname:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about a particular group on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group name
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetGroupGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyGROUP_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetGroupGetUsers(server:'typing.Union[str]',groupName:'typing.Union[str]',level:'typing.Any',resumeHandle:'typing.Any'=0,prefLen:'typing.Any'=4096) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Enumerates the users in a group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupName(typing.Union[str]):The name of the local group.
      level(typing.Any):The level of data required.
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetGroupGetUsers at msdn, google or google groups.
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
        

def NetGroupSetUsers(server:'typing.Union[str]',group:'typing.Union[str]',level:'typing.Any',members:'typing.Tuple[typing.Any, typing.Any]') -> 'None':
    """
    Sets the members of a local group.  Any existing members not listed are 

removed.

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      level(typing.Any):The level of information in the data. Must be 0
      members(typing.Tuple[typing.Any, typing.Any]):The list of new members to add.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupSetInfo(server:'typing.Union[str]',groupname:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about a particular group account on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group name
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Creates a new group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupAddUser(server:'typing.Union[str]',group:'typing.Union[str]',username:'typing.Union[str]') -> 'None':
    """
    Adds a user to the group

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      username(typing.Union[str]):The user to add to the group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDel(server:'typing.Union[str]',groupname:'typing.Union[str]') -> 'None':
    """
    Deletes a group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDelUser(server:'typing.Union[str]',group:'typing.Union[str]',username:'typing.Union[str]') -> 'None':
    """
    Deletes a user from the group

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      username(typing.Union[str]):The user to delete from the group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Enumerates all groups.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The level of data required.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetGroupEnum at msdn, google or google groups.
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
        

def NetGroupAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Creates a new group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupAddMembers(server:'typing.Union[str]',group:'typing.Union[str]',level:'typing.Any',members:'typing.Tuple[typing.Any, typing.Any]') -> 'None':
    """
    Adds users to a local group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      level(typing.Any):The level of information in the data.
      members(typing.Tuple[typing.Any, typing.Any]):The new members to add.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupDelMembers(server:'typing.Union[str]',group:'typing.Union[str]',members:'typing.List[str]') -> 'None':
    """
    Deletes users from a local group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      members(typing.List[str]):A list of strings with fully qualified user names to delete from a local group.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupDel(server:'typing.Union[str]',groupname:'typing.Union[str]') -> 'None':
    """
    Deletes a group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetGroupEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Enumerates all groups.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The level of data required.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetGroupEnum at msdn, google or google groups.
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
        

def NetGroupGetInfo(server:'typing.Union[str]',groupname:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about a particular group on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group name
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetGroupGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyGROUP_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetLocalGroupGetMembers(server:'typing.Union[str]',groupName:'typing.Union[str]',level:'typing.Any',resumeHandle:'typing.Any'=0,prefLen:'typing.Any'=4096) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Enumerates the members in a local 

group.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupName(typing.Union[str]):The name of the local group.
      level(typing.Any):The level of data required.
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetLocalGroupGetMembers at msdn, google or google groups.
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
        

def NetGroupSetInfo(server:'typing.Union[str]',groupname:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about a particular group account on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      groupname(typing.Union[str]):The group name
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the group data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetLocalGroupSetMembers(server:'typing.Union[str]',group:'typing.Union[str]',level:'typing.Any',members:'typing.Tuple[typing.Any, typing.Any]') -> 'None':
    """
    Sets the members of a local group. Any existing members not listed 

are removed.

Args:

      server(typing.Union[str]):The name of the server, or None.
      group(typing.Union[str]):The group name
      level(typing.Any):The level of information in the data.
      members(typing.Tuple[typing.Any, typing.Any]):The list of new members to add.Win32 API References

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
        

def NetMessageNameAdd(server:'typing.Union[typing.Any]',msgname:'typing.Union[typing.Any]') -> 'None':
    """
    Adds a message alias for specified machine

Args:

      server(typing.Union[typing.Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None
      msgname(typing.Union[typing.Any]):Message alias to add, 15 characters max

Returns:

      None
        
    """
    pass
        

def NetMessageNameDel(server:'typing.Union[typing.Any]',msgname:'typing.Union[typing.Any]') -> 'None':
    """
    Removes a message alias for specified machine

Args:

      server(typing.Union[typing.Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None
      msgname(typing.Union[typing.Any]):Message alias to delete for specified machine

Returns:

      None
        
    """
    pass
        

def NetMessageNameEnum(Server:'typing.Union[typing.Any]') -> 'None':
    """
    Lists aliases for a computer

Args:

      Server(typing.Union[typing.Any]):Name of server on which to execute - leading backslashes required on NT - local machine used if None

Returns:

      None
        
    """
    pass
        

def NetServerEnum(server:'typing.Union[str]',level:'typing.Any',_type:'typing.Any',prefLen:'typing.Any',domain:'typing.Union[str]'=None,resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Retrieves information about each server of a 

particular type

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The level of data required.
      _type(typing.Any):Type of server to return - one of the SV_TYPE_* constants.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      domain(typing.Union[str]):The domain to enumerate, or None for the current domain.
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetServerEnum at msdn, google or google groups.
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
        

def NetServerGetInfo(server:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about a particular server.

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetServerGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PySERVER_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetServerSetInfo(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about a particular server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Creates a new share.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data.  Must be level 2 or 502.
      data(typing.Any):A dictionary holding the share data, in the format of SHARE_INFO_*Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareDel(server:'typing.Union[str]',shareName:'typing.Union[str]',reserved:'typing.Any'=0) -> 'None':
    """
    Deletes a share

Args:

      server(typing.Union[str]):The name of the server, or None.
      shareName(typing.Union[str]):The share name
      reserved(typing.Any):Must be zero.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetShareCheck(server:'typing.Union[str]',deviceName:'typing.Union[str]') -> 'typing.Tuple[typing.Any, typing.Any]':
    """
    Checks if server is sharing a device

Args:

      server(typing.Union[str]):The name of the server, or None.
      deviceName(typing.Union[str]):The share nameWin32 API References

Returns:

      typing.Tuple[typing.Any, typing.Any]:Search for NetShareCheck at msdn, google or google groups.
Return ValueThe result is (1, type-of-device) if device is shared, (0, None) if it is not shared.

        
    """
    pass
        

def NetShareEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',serverName:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Retrieves information about each shared resource 

on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The level of data required.
      prefLen(typing.Any):The preferred length of the data buffer.Alternative Parameters
      serverName(typing.Any):The name of the server on which the call should execute, or None for the local computer.CommentsIf the old style is used, the result is a list of [(shareName, type, remarks), ...]Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetShareEnum 

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
        

def NetShareGetInfo(server:'typing.Union[str]',netname:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about a particular share on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      netname(typing.Union[str]):The network name
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetShareGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PySHARE_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetShareSetInfo(server:'typing.Union[str]',netname:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about a particular share on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      netname(typing.Union[str]):The network name
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Creates a new user.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the user data in the format of PyUSER_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserChangePassword(server:'typing.Union[str]',username:'typing.Union[str]',oldPassword:'typing.Union[str]',newPassword:'typing.Union[str]') -> 'None':
    """
    Changes the password for a user.

Args:

      server(typing.Union[str]):The name of the server, or None.
      username(typing.Union[str]):The user name, or None for the current username.
      oldPassword(typing.Union[str]):The old password
      newPassword(typing.Union[str]):The new passwordCommentsA server or domain can be configured to require that a user log on to change the password on a user account. If that is the case, you need administrator or account operator access to change the password for another user acount. If logging on is not required, you can change the password for any user account, so long as you know the current password.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserEnum(server:'typing.Union[str]',level:'typing.Any',arg:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Enumerates all users.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The level of data required.
      arg(typing.Any):The types of accounts to enumerate.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetUserEnum at msdn, google or google groups.
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
        

def NetUserGetGroups(serverName:'str',userName:'str') -> 'typing.List[typing.Tuple[typing.Any, typing.Any]]':
    """
    Returns a list of groups,attributes for all groups 

for the user.

Args:

      serverName(str):The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.
      userName(str):The name of the user to search for in each group account. To Do This needs to be extended to support the new model, while not breaking existing code.  A default arg would be perfect.Return ValueAlways makes the level 1 call and returns all data. Data return format is a Python List.  Each "Item" is a tuple of (groupname, attributes).  "(s,i)" respectively.  In NT 4 the attributes seem to be hardcoded to 7. Earlier version of NT have not been tested.

Returns:

      typing.List[typing.Tuple[typing.Any, typing.Any]]:The name of the user to search for in each group account. To Do This needs to be extended to support the new model, while 

not breaking existing code.  A default arg would be perfect.
Return ValueAlways makes the level 1 call and returns all data. 

Data return format is a Python List.  Each "Item" 

is a tuple of (groupname, attributes).  "(s,i)" respectively.  In NT 4 the attributes seem to be hardcoded to 7. 

Earlier version of NT have not been tested.

        
    """
    pass
        

def NetUserGetInfo(server:'typing.Union[str]',username:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about a particular user account on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      username(typing.Union[str]):The user name
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetUserGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyUSER_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetUserGetLocalGroups(serverName:'str',userName:'str',flags:'typing.Any') -> 'typing.List[typing.Any]':
    """
    Retrieves a list of local groups to which a specified user 

belongs.

Args:

      serverName(str):The name of the remote server on which the function is to execute. None or an empty string specifies the server program running on the local computer.
      userName(str):The name of the user to search for in each group account. This parameter can be of the form &ltUserName&gt, in which case the username is expected to be found on servername. The user name can also be of the form &ltDomainName&gt\\&ltUserName&gt in which case &ltDomainName&gt is associated with servername and &ltUserName&gt is expected to be to be found on that domain.
      flags(typing.Any):Flags for the call. To Do This needs to be extended to support the new model, while not breaking existing code.  A default arg would be perfect.

Returns:

      typing.List[typing.Any]
        
    """
    pass
        

def NetUserSetInfo(server:'typing.Union[str]',username:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about a particular user account on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      username(typing.Union[str]):The user name
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the user data in the format of PyUSER_INFO_*Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUserDel(server:'typing.Union[str]',username:'typing.Union[str]') -> 'None':
    """
    Deletes a user.

Args:

      server(typing.Union[str]):The name of the server, or None.
      username(typing.Union[str]):The user nameWin32 API References

Returns:

      None
        
    """
    pass
        

def NetUserModalsGet(server:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves global user information on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the dataWin32 API References

Returns:

      typing.Any:Search for NetUserModalsGet at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyUSER_MODALS_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetUserModalsSet(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets global user parameters on a server.

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the data in the format of PyUSER_MODALS_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaUserEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Retrieves information about all users 

currently logged on to the workstation.

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The level of data required.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetWkstaUserEnum at msdn, google or google groups.
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
        

def NetWkstaGetInfo(server:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves information about the configuration elements for a workstation

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.Win32 API References

Returns:

      typing.Any:Search for NetWkstaGetInfo at msdn, google or google groups.
Return ValueThe result will be a dictionary in one of the PyWKSTA_INFO_* 

formats, depending on the level parameter.

        
    """
    pass
        

def NetWkstaSetInfo(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Sets information about the configuration elements for a workstation

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaTransportEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Retrieves information about transport 

protocols that are currently managed by the redirector

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The level of data required.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetWkstaTransportEnum at msdn, google or google groups.
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
        

def NetWkstaTransportAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    binds the redirector to a transport

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the share data.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetWkstaTransportDel(server:'typing.Union[str]',TransportName:'typing.Union[str]',ucond:'typing.Any'=0) -> 'None':
    """
    unbinds the transport protocol from redirector

Args:

      server(typing.Union[str]):The name of the server, or None.
      TransportName(typing.Union[str]):The name of the transport to delete.
      ucond(typing.Any):Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCEWin32 API References

Returns:

      None
        
    """
    pass
        

def NetServerDiskEnum(server:'typing.Union[str]',level:'typing.Any') -> 'typing.Any':
    """
    Retrieves the list of disk drives on a server.

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The level of data required. Must be 0.Win32 API References

Returns:

      typing.Any:Search for NetServerDiskEnum at msdn, google or google groups.
Return ValueThe result is a list of drives on the server

        
    """
    pass
        

def NetUseAdd(server:'typing.Union[str]',level:'typing.Any',data:'typing.Any') -> 'None':
    """
    Establishes connection between local or NULL device name and a shared resource through 

redirector

Args:

      server(typing.Union[str]):The name of the server, or None.
      level(typing.Any):The information level contained in the data
      data(typing.Any):A dictionary holding the share data in the format of PyUSE_INFO_*.Win32 API References

Returns:

      None
        
    """
    pass
        

def NetUseDel(server:'typing.Union[str]',useName:'typing.Union[str]',forceCond:'typing.Any'=0) -> 'None':
    """
    Ends connection to a shared resource.

Args:

      server(typing.Union[str]):The name of the server, or None.
      useName(typing.Union[str]):The share name
      forceCond(typing.Any):Level of force to use. Can be USE_FORCE or USE_NOFORCE or USE_LOTS_OF_FORCEWin32 API References

Returns:

      None
        
    """
    pass
        

def NetUseEnum(server:'typing.Union[str]',level:'typing.Any',prefLen:'typing.Any',resumeHandle:'typing.Any'=0) -> 'typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]':
    """
    Retrieves information about transport protocols that 

are currently managed by the redirector

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      level(typing.Any):The level of data required. Currently levels 0, 1 and 2 are supported.
      prefLen(typing.Any):The preferred length of the data buffer.Win32 API References
      resumeHandle(typing.Any):A resume handle.  See the return description for more information.

Returns:

      typing.Tuple[typing.Any, typing.Any, typing.Any, typing.Any]:Search for NetUseEnum at msdn, google or google groups.
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
        

def NetUseGetInfo(server:'typing.Union[str]',usename:'typing.Union[str]',level:'typing.Any'=0) -> 'typing.Any':
    """
    Retrieves information about the configuration elements for a workstation

Args:

      server(typing.Union[str]):The name of the server to execute on, or None.
      usename(typing.Union[str]):The name of the locally mapped resource.
      level(typing.Any):The information level contained in the data. NOTE: levels 302 and 402 don't seem to work correctly. They return error 124. So currently these info levels are not available.Win32 API References

Returns:

      typing.Any:Search for NetUseGetInfo at msdn, google or google groups.
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
        

def NetSessionEnum(level:'typing.Any',server:'typing.Union[str]'=None,client:'typing.Union[str]'=None,username:'typing.Union[str]'=None) -> 'typing.Tuple[typing.Any, ...]':
    """
    Returns network sessions for a server, limited to single client and/or 

user if specified.

Args:

      level(typing.Any):Level of information requested, currently accepts 0, 1, 2, 10, and 502
      server(typing.Union[str]):The name of the server for which to list sessions, local machine assumed if None
      client(typing.Union[str]):Name of client computer, or None to list all computer sessions
      username(typing.Union[str]):User name, or None to list all connected usersReturn ValueReturns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified

Returns:

      typing.Tuple[typing.Any, ...]:User name, or None to list all connected users
Return ValueReturns a sequence of dictionaries representing SESSION_INFO_* structs, depending on level specified

        
    """
    pass
        

def NetSessionDel(server:'typing.Union[str]',client:'typing.Union[str]'=None,username:'typing.Union[str]'=None) -> 'None':
    """
    Disconnects network connections on a server

Args:

      server(typing.Union[str]):The name of the server on which to operate, local machine assumed if None or blank
      client(typing.Union[str]):Name of client computer, or None
      username(typing.Union[str]):User name, or None for all connected usersReturn ValueReturns None on success

Returns:

      None:User name, or None for all connected users
Return ValueReturns None on success

        
    """
    pass
        

def NetSessionGetInfo(level:'typing.Any',server:'typing.Union[str]',client:'typing.Union[str]',username:'typing.Union[str]') -> 'typing.Any':
    """
    Returns information for a network session from specified client

Args:

      level(typing.Any):Level of information requested, currently accepts 0, 1, 2, 10, and 502
      server(typing.Union[str]):The name of the server on which to operate, None or blank assumes local machine
      client(typing.Union[str]):Name of client computer
      username(typing.Union[str]):User that established sessionReturn ValueReturns a dictionary representing a SESSION_INFO_* struct, depending on level specified

Returns:

      typing.Any:User that established sessionReturn ValueReturns a dictionary representing a SESSION_INFO_* struct, depending on level specified

        
    """
    pass
        

def NetFileEnum(level:'typing.Any',servername:'typing.Union[str]'=None,basepath:'typing.Union[str]'=None,username:'typing.Union[str]'=None) -> 'typing.Tuple[typing.Any, ...]':
    """
    Lists remotely opened resources on a server

Args:

      level(typing.Any):Level of information, 2 or 3 supported
      servername(typing.Union[str]):The name of the server for which to list open resources, local machine assumed if None
      basepath(typing.Union[str]):If specified, limits returned list to files on given path
      username(typing.Union[str]):User that opened resource, or None to list open files for all usersReturn ValueReturns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified

Returns:

      typing.Tuple[typing.Any, ...]:User that opened resource, or None to list open files for all users
Return ValueReturns a sequence of dictionaries representing FILE_INFO_* structs, depending on level specified

        
    """
    pass
        

def NetFileClose(servername:'typing.Union[str]',fileid:'typing.Any') -> 'None':
    """
    Closes an open network resource on a server

Args:

      servername(typing.Union[str]):Name of server on which to operate, local machine assumed if None
      fileid(typing.Any):Id of opened resource, as returned by win32net::NetFileEnum

Returns:

      None
        
    """
    pass
        

def NetFileGetInfo(level:'typing.Any',servername:'typing.Union[str]',fileid:'typing.Any') -> 'typing.Any':
    """
    Returns information about an open network resource

Args:

      level(typing.Any):Level of information to return, 2 or 3 supported
      servername(typing.Union[str]):Server on which resource is open, local machine assumed if None
      fileid(typing.Any):Id of opened resource, as returned by win32net::NetFileEnum

Returns:

      typing.Any
        
    """
    pass
        

def NetStatisticsGet(server:'typing.Union[str]',service:'typing.Union[str]',level:'typing.Any',options:'typing.Any') -> 'typing.Any':
    """
    Retrieves network statistics for specified service on specified machine

Args:

      server(typing.Union[str]):Name of server/workstation to retrieve statistics for (None or blank uses local).
      service(typing.Union[str]):SERVICE_SERVER or SERVICE_WORKSTATION
      level(typing.Any):Only 0 currently supported.
      options(typing.Any):Must be zero.Return ValueThe result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct

Returns:

      typing.Any:Must be zero.Return ValueThe result is a dictionary representing a STAT_SERVER_0 or STAT_WORKSTATION_0 struct

        
    """
    pass
        

def NetServerComputerNameAdd(ServerName:'typing.Union[str]',EmulatedDomainName:'typing.Union[str]',EmulatedServerName:'typing.Union[str]') -> 'None':
    """
    Adds an additional network name for a server

Args:

      ServerName(typing.Union[str]):Name of server that will receive additional name
      EmulatedDomainName(typing.Union[str]):Domain under which to add the new server name, can be None
      EmulatedServerName(typing.Union[str]):New network name that server will respond toReturn ValueReturns none on success

Returns:

      None:New network name that server will respond toReturn ValueReturns none on success

        
    """
    pass
        

def NetServerComputerNameDel(ServerName:'typing.Union[str]',EmulatedServerName:'typing.Union[str]') -> 'None':
    """
    None

Args:

      ServerName(typing.Union[str]):Name of server on which to operate
      EmulatedServerName(typing.Union[str]):Network name to be removedReturn ValueReturns none on success

Returns:

      None:Network name to be removedReturn ValueReturns none on success

        
    """
    pass
        

def NetValidateName(Server:'typing.Union[str]',Name:'typing.Union[str]',NameType:'typing.Any',Account:'typing.Union[str]'=None,Password:'typing.Union[str]'=None) -> 'None':
    """
    Checks that domain/machine/workgroup name is valid for given context

Args:

      Server(typing.Union[str]):Name of server on which to execute (None or blank uses local)
      Name(typing.Union[str]):Machine, domain, or workgroup name to validate
      NameType(typing.Any):Type of name to validate - from NETSETUP_NAME_TYPE enum (win32net.NetSetup*)
      Account(typing.Union[str]):Account name to use while validating, current security context is used if not specified
      Password(typing.Union[str]):Password for AccountCommentsIf Account and Password aren't passed, current logon credentials are usedWill raise NotImplementedError if not available on this platform.Return ValueReturns none if valid, exception if not

Returns:

      None:Password for Account
Comments

If Account and Password aren't passed, current logon credentials are used

Will raise NotImplementedError if not available on this platform.
Return ValueReturns none if valid, exception if not

        
    """
    pass
        

def NetValidatePasswordPolicy(Server:'typing.Union[str]',Qualifier:'typing.Any',ValidationType:'typing.Any',arg:'typing.Union[typing.Any]') -> 'None':
    """
    Allows an application to check 

password compliance against an application-provided account database and 

verify that passwords meet the complexity, aging, minimum length, and 

history reuse requirements of a password policy.

Args:

      Server(typing.Union[str]):Name of server on which to execute (None or blank uses local)
      Qualifier(typing.Any):Reserved, must be None
      ValidationType(typing.Any):The type of password validation to perform
      arg(typing.Union[typing.Any]):Depends on the ValidationType param - either a PyNET_VALIDATE_AUTHENTICATION_INPUT_ARG,  PyNET_VALIDATE_PASSWORD_CHANGE_INPUT_ARG or PyNET_VALIDATE_PASSWORD_RESET_INPUT_ARG tuple or dict.CommentsWill raise NotImplementedError if not available on this platform, or raise win32net.error if the function fails.Return ValueReturns a tuple of (PyNET_VALIDATE_PERSISTED_FIELDS, int) with the integer being the ValidationResult.

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
        