__all__=['odbc', 'SQLDataSources']
from typing import *
from .win32typing import *
"""A Python wrapper around the ODBC API."""


def odbc(connectionString:'str') -> 'connection':
    """
    Creates an ODBC connection

Args:

      connectionString(str):An ODBC connection string. For backwards-compatibility, this parameter can be of the form DSN[/username[/password]] (e.g. "myDSN/myUserName/myPassword"). Alternatively, a full ODBC connection string can be used (e.g., "Driver={SQL Server};Server=(local);Database=myDatabase").

Returns:

      connection
        
    """
    pass
        

def SQLDataSources(direction:'int') -> 'Tuple[Any, Union[Any, None]]':
    """
    Enumerates ODBC data sources

Args:

      direction(int):One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

Returns:

      Tuple[Any, Union[Any, None]]:One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

        
    """
    pass
        