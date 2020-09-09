__all__=['', 'odbc', 'SQLDataSources']
import typing
from win32helper import win32typing
"""A Python wrapper around the ODBC API."""


def odbc(connectionString:'str') -> 'win32typing.connection':
    """
    Creates an ODBC connection

Args:

      connectionString(str):An ODBC connection string. For backwards-compatibility, this parameter can be of the form DSN[/username[/password]] (e.g. "myDSN/myUserName/myPassword"). Alternatively, a full ODBC connection string can be used (e.g., "Driver={SQL Server};Server=(local);Database=myDatabase").

Returns:

      win32typing.connection
        
    """
    pass
        

def SQLDataSources(direction:'typing.Any') -> 'typing.Tuple[typing.Any, typing.Union[typing.Any]]':
    """
    Enumerates ODBC data sources

Args:

      direction(typing.Any):One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

Returns:

      typing.Tuple[typing.Any, typing.Union[typing.Any]]:One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

        
    """
    pass
        