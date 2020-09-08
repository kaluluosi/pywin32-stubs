__all__=['', 'HrInstallService', 'HrInstallMailboxAgent', 'HrCreateMailboxAgentProfile', 'HrCreateGatewayProfile', 'HrMailboxAgentExists', 'HrAdminProgramExists', 'HrRemoveMailboxAgent', 'HrRemoveProfile', 'HrEnumOrganizations', 'HrEnumSites', 'HrEnumContainers', 'HrEnumSiteAdmins', 'HrGetServiceAccountName']
from typing import *
from win32helper.win32typing import *
"""An COM interface to Exchange's DAPI"""


def HrInstallService() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def HrInstallMailboxAgent() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def HrCreateMailboxAgentProfile(serviceName:'str',profile:'str') -> 'None':
    """
    None

Args:

      serviceName(str):The name of the service.
      profile(str):The profile.

Returns:

      None
        
    """
    pass
        

def HrCreateGatewayProfile(serviceName:'str',profile:'str') -> 'None':
    """
    None

Args:

      serviceName(str):The name of the service.
      profile(str):The profile.

Returns:

      None
        
    """
    pass
        

def HrMailboxAgentExists(server:'str',siteDN:'str',rdn:'str') -> 'None':
    """
    None

Args:

      server(str):The name of the server
      siteDN(str):Contains the distinguished name (DN) of the site.
      rdn(str):RDN of the site where the mailbox agent might exist.

Returns:

      None
        
    """
    pass
        

def HrAdminProgramExists() -> 'None':
    """
    None

Args:



Returns:

      None
        
    """
    pass
        

def HrRemoveMailboxAgent(server:'str',siteDN:'str',rdn:'str') -> 'None':
    """
    Removes a Mailbox Agent

Args:

      server(str):The name of the server
      siteDN(str):Contains the distinguished name (DN) of the site.
      rdn(str):RDN of the site where the mailbox agent exists.

Returns:

      None
        
    """
    pass
        

def HrRemoveProfile(profile:'str') -> 'None':
    """
    Removes a profile

Args:

      profile(str):The profile to delete.

Returns:

      None
        
    """
    pass
        

def HrEnumOrganizations(rootDN:'str',server:'str') -> 'List[str]':
    """
    Lists the names of the organizations on the server.

Args:

      rootDN(str):Contains the distinguished name (DN) of the directory information tree (DIT) root.
      server(str):The name of the server

Returns:

      List[str]
        
    """
    pass
        

def HrEnumSites(server:'str',organizationDN:'str') -> 'List[str]':
    """
    Lists the names of the sites in an organization.

Args:

      server(str):The name of the server
      organizationDN(str):Contains the distinguished name (DN) of the organization.

Returns:

      List[str]
        
    """
    pass
        

def HrEnumContainers(server:'str',siteDN:'str',fSubtree:'int') -> 'List[str]':
    """
    Lists the names of the containers on the server

Args:

      server(str):The name of the server
      siteDN(str):Distinguished name (DN) of the site.
      fSubtree(int):

Returns:

      List[str]
        
    """
    pass
        

def HrEnumSiteAdmins(server:'str',siteDN:'str') -> 'List[str]':
    """
    Lists the administrators for a site.

Args:

      server(str):The name of the server
      siteDN(str):Distinguished name (DN) of the site.

Returns:

      List[str]
        
    """
    pass
        

def HrGetServiceAccountName(serviceName:'str',serviceName1:'str') -> 'str':
    """
    Obtains the account name for a service.

Args:

      serviceName(str):The name of the service
      serviceName1(str):The name of the service

Returns:

      str
        
    """
    pass
        