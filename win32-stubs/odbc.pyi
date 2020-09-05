from pywintypes import *
__all__=['odbc', 'SQLDataSources']
import typing
"""A Python wrapper around the ODBC API."""


def odbc(connectionString:str) -> typing.Any:
    """
    Creates an ODBC connection


Args:

      connectionString(str):An ODBC connection string. For backwards-compatibility, this parameter can be of the form DSN[/username[/password]] (e.g. "myDSN/myUserName/myPassword"). Alternatively, a full ODBC connection string can be used (e.g., "Driver={SQL Server};Server=(local);Database=myDatabase").

Returns:

      typing.Any
        
    """
    pass


def SQLDataSources(direction:int) -> typing.Any:
    """
    Enumerates ODBC data sources


Args:

      direction(int):One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

Returns:

      typing.Any:One of SQL_FETCH_* flags indicating how to retrieve data sourcesReturn ValueThe result is None when SQL_NO_DATA is returned from ODBC.

        
    """
    pass
