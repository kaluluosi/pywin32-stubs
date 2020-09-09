__all__=['', 'OpenPrinter', 'GetPrinter', 'SetPrinter', 'ClosePrinter', 'AddPrinterConnection', 'DeletePrinterConnection', 'EnumPrinters', 'GetDefaultPrinter', 'GetDefaultPrinterW', 'SetDefaultPrinter', 'SetDefaultPrinterW', 'StartDocPrinter', 'EndDocPrinter', 'AbortPrinter', 'StartPagePrinter', 'EndPagePrinter', 'StartDoc', 'EndDoc', 'AbortDoc', 'StartPage', 'EndPage', 'WritePrinter', 'EnumJobs', 'GetJob', 'SetJob', 'DocumentProperties', 'EnumPrintProcessors', 'EnumPrintProcessorDatatypes', 'EnumPrinterDrivers', 'EnumForms', 'AddForm', 'DeleteForm', 'GetForm', 'SetForm', 'AddJob', 'ScheduleJob', 'DeviceCapabilities', 'GetDeviceCaps', 'EnumMonitors', 'EnumPorts', 'GetPrintProcessorDirectory', 'GetPrinterDriverDirectory', 'AddPrinter', 'DeletePrinter', 'DeletePrinterDriver', 'DeletePrinterDriverEx', 'FlushPrinter']
import typing
from win32helper import win32typing
"""A module encapsulating the Windows printing API."""


def OpenPrinter(printer:'str',Defaults:'typing.Any'=None) -> 'win32typing.PyPrinterHANDLE':
    """
    Retrieves a handle to a printer.

Args:

      printer(str):Printer or print server name.  Use None to open local print server.
      Defaults(typing.Any):PRINTER_DEFAULTS dict, or None

Returns:

      win32typing.PyPrinterHANDLE
        
    """
    pass
        

def GetPrinter(hPrinter:'win32typing.PyPrinterHANDLE',Level:'typing.Any'=2) -> 'typing.Any':
    """
    Retrieves information about a printer

Args:

      hPrinter(win32typing.PyPrinterHANDLE):handle to printer object as returned by win32print::OpenPrinter
      Level(typing.Any):Level of data returned (1,2,3,4,5,7,8,9)CommentsOriginal implementation used level 2 only and returned a tuple Pass single arg as indicator to use old behaviour for backward compatibilityReturn ValueReturns a dictionary containing PRINTER_INFO_* data for level, or returns a tuple of PRINTER_INFO_2 data if no level is passed in.

Returns:

      typing.Any:Level of data returned (1,2,3,4,5,7,8,9)
Comments

Original implementation used level 2 only and returned a tuple 

Pass single arg as indicator to use old behaviour for backward compatibility
Return ValueReturns a dictionary containing PRINTER_INFO_* data for level, or 

returns a tuple of PRINTER_INFO_2 data if no level is passed in.

        
    """
    pass
        

def SetPrinter(hPrinter:'win32typing.PyPrinterHANDLE',Level:'typing.Any',pPrinter:'typing.Any',Command:'typing.Any') -> 'None':
    """
    Change printer configuration and status

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      Level(typing.Any):Level of data contained in pPrinter
      pPrinter(typing.Any):PRINTER_INFO_* dict as returned by win32print::GetPrinter, can be None if level is 0
      Command(typing.Any):Command to send to printer - one of the PRINTER_CONTROL_* constants, or 0CommentsIf Level is 0 and Command is PRINTER_CONTROL_SET_STATUS, pPrinter should be an integer, and is interpreted as the new printer status to set (one of the PRINTER_STATUS_* constants).

Returns:

      None
        
    """
    pass
        

def ClosePrinter(hPrinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Closes a handle to a printer.

Args:

      hPrinter(win32typing.PyPrinterHANDLE):handle to printer object

Returns:

      None
        
    """
    pass
        

def AddPrinterConnection(printer:'str') -> 'typing.Any':
    """
    Connects to remote printer

Args:

      printer(str):printer to connect to (eg: \\server\\printer).

Returns:

      typing.Any
        
    """
    pass
        

def DeletePrinterConnection(printer:'str') -> 'typing.Any':
    """
    Removes connection to remote printer

Args:

      printer(str):printer to disconnect from (eg: \\server\\printer).

Returns:

      typing.Any
        
    """
    pass
        

def EnumPrinters(flags:'typing.Any',name:'str'=None,level:'typing.Any'=1) -> 'typing.Any':
    """
    Enumerates printers, print servers, domains and print providers.

Args:

      flags(typing.Any):types of printer objects to enumerate (combination of PRINTER_ENUM_* constants).
      name(str):name of printer object.
      level(typing.Any):type of printer info structure (Levels 1,2,4,5 supported)CommentsUse Flags=PRINTER_ENUM_NAME, Name=None, Level=1 to enumerate print providers. Use Flags=PRINTER_ENUM_NAME, Name=\\servername, Level=2 or 5 to list printers on another server. See MSDN docs for EnumPrinters for other specific combinationsReturn ValueLevel 1 returns a tuple of tuples for backward compatibility. Each individual element is a tuple of (flags, description, name, comment) All other levels return a tuple of dictionaries representing PRINTER_INFO_* structures

Returns:

      typing.Any:type of printer info structure (Levels 1,2,4,5 supported)
Comments

Use Flags=PRINTER_ENUM_NAME, Name=None, Level=1 to enumerate print providers. 

Use Flags=PRINTER_ENUM_NAME, Name=\\servername, Level=2 or 5 to list printers on another server. 

See MSDN docs for EnumPrinters for other specific combinations
Return ValueLevel 1 returns a tuple of tuples for backward compatibility. 

Each individual element is a tuple of (flags, description, name, comment) 

All other levels return a tuple of dictionaries representing PRINTER_INFO_* structures

        
    """
    pass
        

def GetDefaultPrinter() -> 'str':
    """
    Returns the default printer.

Args:



Returns:

      str
        
    """
    pass
        

def GetDefaultPrinterW() -> 'str':
    """
    Returns the default printer.

Args:



Returns:

      str
        
    """
    pass
        

def SetDefaultPrinter(printer:'str') -> 'typing.Any':
    """
    Sets the default printer.

Args:

      printer(str):printer to set as defaultCommentsThis function uses the pre-win2k method of WriteProfileString rather than the SetDefaultPrinter API function

Returns:

      typing.Any
        
    """
    pass
        

def SetDefaultPrinterW(Printer:'str') -> 'typing.Any':
    """
    Sets the default printer

Args:

      Printer(str):Name of printer, can be None to use first available printerCommentsUnlike win32print::SetDefaultPrinter, this method calls the SetDefaultPrinter API function.

Returns:

      typing.Any
        
    """
    pass
        

def StartDocPrinter(hprinter:'win32typing.PyPrinterHANDLE',_tuple:'typing.Any',level:'typing.Any'=1) -> 'typing.Any':
    """
    Notifies the print spooler that a document is to be spooled for printing. To 

be used before using WritePrinter. Returns the Jobid of the started job.

Args:

      hprinter(win32typing.PyPrinterHANDLE):handle to printer (from win32print::OpenPrinter)
      _tuple(typing.Any):A tuple corresponding to the level parameter.CommentsFor level 1, the tuple is:Items[0] string : docNameSpecifies the name of the document.[1] string : outputFileSpecifies the name of an output file. To print to a printer, set this to None.[2] string : dataTypeIdentifies the type of data used to record the document, such as "raw" or "emf", used to record the print job. This member can be None. If it is not None, the StartDoc function passes it to the printer driver. Note that the printer driver might ignore the requested data type.
      level(typing.Any):type of docinfo structure (only docinfo level 1 supported)

Returns:

      typing.Any
        
    """
    pass
        

def EndDocPrinter(hPrinter:'win32typing.PyPrinterHANDLE') -> 'typing.Any':
    """
    The EndDocPrinter function ends a print job for the specified printer. To be 

used after using WritePrinter.

Args:

      hPrinter(win32typing.PyPrinterHANDLE):handle to printer (from win32print::OpenPrinter)

Returns:

      typing.Any
        
    """
    pass
        

def AbortPrinter(hPrinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Deletes spool file for a printer

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Handle to printer as returned by win32print::OpenPrinter

Returns:

      None
        
    """
    pass
        

def StartPagePrinter(hprinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Notifies the print spooler that a page is to be printed on specified printer

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter

Returns:

      None
        
    """
    pass
        

def EndPagePrinter(hprinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Ends a page in a print job

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter

Returns:

      None
        
    """
    pass
        

def StartDoc(hdc:'int',docinfo:'typing.Any') -> 'typing.Any':
    """
    Starts spooling a print job on a printer device context

Args:

      hdc(int):Printer device context handle as returned by win32gui::CreateDC
      docinfo(typing.Any):DOCINFO tuple specifying print job parametersReturn ValueOn success, returns the job id of the print job

Returns:

      typing.Any:DOCINFO tuple specifying print job parametersReturn ValueOn success, returns the job id of the print job

        
    """
    pass
        

def EndDoc(hdc:'int') -> 'None':
    """
    Stops spooling a print job on a printer device context

Args:

      hdc(int):Printer device context handle as returned by win32gui::CreateDC

Returns:

      None
        
    """
    pass
        

def AbortDoc(hdc:'int') -> 'None':
    """
    Cancels a print job

Args:

      hdc(int):Printer device context handle as returned by win32gui::CreateDC

Returns:

      None
        
    """
    pass
        

def StartPage(hdc:'int') -> 'None':
    """
    Starts a page on a printer device context

Args:

      hdc(int):Printer device context handle as returned by win32gui::CreateDC

Returns:

      None
        
    """
    pass
        

def EndPage(hdc:'int') -> 'None':
    """
    Ends a page on a printer device context

Args:

      hdc(int):Printer device context handle as returned by win32gui::CreateDC

Returns:

      None
        
    """
    pass
        

def WritePrinter(hprinter:'win32typing.PyPrinterHANDLE',buf:'str') -> 'typing.Any':
    """
    Copies the specified bytes to the specified printer. 

Suitable for copying raw Postscript or HPGL files to a printer. 

StartDocPrinter and EndDocPrinter should be called before and after.

Args:

      hprinter(win32typing.PyPrinterHANDLE):Handle to printer as returned by win32print::OpenPrinter.
      buf(str):String or buffer containing data to send to printer. Embedded NULL bytes are allowed.Return ValueReturns number of bytes written to printer.

Returns:

      typing.Any:String or buffer containing data to send to printer. Embedded 

NULL bytes are allowed.Return ValueReturns number of bytes written to printer.

        
    """
    pass
        

def EnumJobs(hPrinter:'win32typing.PyPrinterHANDLE',FirstJob:'typing.Any',NoJobs:'typing.Any',Level:'typing.Any'=1) -> 'typing.Any':
    """
    Enumerates print jobs on specified printer.

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Handle of printer.
      FirstJob(typing.Any):location of first job in print queue to enumerate.
      NoJobs(typing.Any):Number of jobs to enumerate.
      Level(typing.Any):Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).Return ValueReturns a sequence of dictionaries representing JOB_INFO_* structures, depending on level

Returns:

      typing.Any:Level of information to return (JOB_INFO_1, JOB_INFO_2, 

JOB_INFO_3 supported).
Return ValueReturns a sequence of dictionaries representing JOB_INFO_* structures, depending on level

        
    """
    pass
        

def GetJob(hPrinter:'win32typing.PyPrinterHANDLE',JobID:'typing.Any',Level:'typing.Any'=1) -> 'typing.Any':
    """
    Returns dictionary of information about a specified print job.

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Handle to a printer as returned by win32print::OpenPrinter.
      JobID(typing.Any):Job Identifier.
      Level(typing.Any):Level of information to return (JOB_INFO_1, JOB_INFO_2, JOB_INFO_3 supported).Return ValueReturns a dict representing a JOB_INFO_* struct, depending on level

Returns:

      typing.Any:Level of information to return (JOB_INFO_1, JOB_INFO_2, 

JOB_INFO_3 supported).
Return ValueReturns a dict representing a JOB_INFO_* struct, depending on level

        
    """
    pass
        

def SetJob(hPrinter:'win32typing.PyPrinterHANDLE',JobID:'typing.Any',Level:'typing.Any',JobInfo:'typing.Any',Command:'typing.Any') -> 'typing.Any':
    """
    Pause, cancel, resume, set priority levels on a print job.

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Handle of printer.
      JobID(typing.Any):Job Identifier.
      Level(typing.Any):Level of information in JobInfo dict (0, 1, 2, and 3 are supported).
      JobInfo(typing.Any):JOB_INFO_* Dictionary as returned by win32print::GetJob or win32print::EnumJobs (can be None if Level is 0).
      Command(typing.Any):Job command value (JOB_CONTROL_*).CommentsIf printer is not opened with at least PRINTER_ACCESS_ADMINISTER access, 'Position' member of JOB_INFO_1 and JOB_INFO_2 must be set to JOB_POSITION_UNSPECIFIED

Returns:

      typing.Any
        
    """
    pass
        

def DocumentProperties(HWnd:'int',hPrinter:'win32typing.PyPrinterHANDLE',DeviceName:'str',DevModeOutput:'win32typing.PyDEVMODE',DevModeInput:'win32typing.PyDEVMODE',Mode:'typing.Any') -> 'typing.Any':
    """
    Changes printer configuration for a printer

Args:

      HWnd(int):Parent window handle to use if DM_IN_PROMPT is specified to display printer dialog
      hPrinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      DeviceName(str):Name of printer
      DevModeOutput(win32typing.PyDEVMODE):PyDEVMODE object that receives modified info, can be None if DM_OUT_BUFFER not specified
      DevModeInput(win32typing.PyDEVMODE):PyDEVMODE that specifies initial configuration, can be None if DM_IN_BUFFER not specified
      Mode(typing.Any):A combination of DM_IN_BUFFER, DM_OUT_BUFFER, and DM_IN_PROMPT - pass 0 to retrieve driver data sizeReturn ValueIf DM_IN_PROMPT is specified, returned value will be IDOK or IDCANCEL

Returns:

      typing.Any:A combination of DM_IN_BUFFER, DM_OUT_BUFFER, and DM_IN_PROMPT - pass 0 to retrieve driver data 

sizeReturn ValueIf DM_IN_PROMPT is specified, returned value will be IDOK or IDCANCEL

        
    """
    pass
        

def EnumPrintProcessors(Server:'typing.Union[str]'=None,Environment:'typing.Union[str]'=None) -> 'typing.Tuple[str, ...]':
    """
    List printer processors for specified server and 

environment

Args:

      Server(typing.Union[str]):Name of print server, use None for local machine
      Environment(typing.Union[str]):Environment - eg 'Windows NT x86' - use None for current client environment

Returns:

      typing.Tuple[str, ...]
        
    """
    pass
        

def EnumPrintProcessorDatatypes(ServerName:'typing.Union[str]',PrintProcessorName:'typing.Union[str]') -> 'typing.Tuple[str, ...]':
    """
    List data types that specified print provider 

recognizes

Args:

      ServerName(typing.Union[str]):Name of print server, use None for local machine
      PrintProcessorName(typing.Union[str]):Name of print processor

Returns:

      typing.Tuple[str, ...]
        
    """
    pass
        

def EnumPrinterDrivers(Server:'typing.Union[str, typing.Any]'=None,Environment:'typing.Union[str, typing.Any]'=None,Level:'typing.Any'=1) -> 'typing.Tuple[typing.Any, ...]':
    """
    Lists installed printer drivers

Args:

      Server(typing.Union[str, typing.Any]):Name of print server, use None for local machine
      Environment(typing.Union[str, typing.Any]):Environment - eg 'Windows NT x86' - use None for current client environment
      Level(typing.Any):Level of information to return, 1-6 (not all levels are supported on all platforms)CommentsOn Win2k and up, 'all' can be passed for environmentReturn ValueReturns a sequence of dictionaries representing DRIVER_INFO_* structures

Returns:

      typing.Tuple[typing.Any, ...]:Level of information to return, 1-6 (not all levels are supported on all platforms)
Comments

On Win2k and up, 'all' can be passed for environment
Return ValueReturns a sequence of dictionaries representing DRIVER_INFO_* structures

        
    """
    pass
        

def EnumForms(hprinter:'win32typing.PyPrinterHANDLE') -> 'typing.Tuple[win32typing.FORM_INFO_1, ...]':
    """
    Lists forms for a printer

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinterReturn ValueReturns a sequence of dictionaries representing FORM_INFO_1 structures

Returns:

      typing.Tuple[win32typing.FORM_INFO_1, ...]:Printer handle as returned by win32print::OpenPrinterReturn ValueReturns a sequence of dictionaries representing FORM_INFO_1 structures

        
    """
    pass
        

def AddForm(hprinter:'win32typing.PyPrinterHANDLE',Form:'typing.Any') -> 'None':
    """
    Adds a form for a printer

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      Form(typing.Any):FORM_INFO_1 dictionaryReturn ValueReturns None on success, throws an exception otherwise

Returns:

      None:FORM_INFO_1 dictionaryReturn ValueReturns None on success, throws an exception otherwise

        
    """
    pass
        

def DeleteForm(hprinter:'win32typing.PyPrinterHANDLE',FormName:'str') -> 'None':
    """
    Deletes a form defined for a printer

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      FormName(str):Name of form to be deletedReturn ValueReturns None on success, throws an exception otherwise

Returns:

      None:Name of form to be deletedReturn ValueReturns None on success, throws an exception otherwise

        
    """
    pass
        

def GetForm(hprinter:'win32typing.PyPrinterHANDLE',FormName:'str') -> 'None':
    """
    Retrieves information about a form defined for a printer

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      FormName(str):Name of form for which to retrieve infoReturn ValueReturns a FORM_INFO_1 dict

Returns:

      None:Name of form for which to retrieve infoReturn ValueReturns a FORM_INFO_1 dict

        
    """
    pass
        

def SetForm(hprinter:'win32typing.PyPrinterHANDLE',FormName:'str',Form:'typing.Any') -> 'None':
    """
    Change information for a form

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      FormName(str):Name of form
      Form(typing.Any):FORM_INFO_1 dictionaryReturn ValueReturns None on success

Returns:

      None:FORM_INFO_1 dictionaryReturn ValueReturns None on success

        
    """
    pass
        

def AddJob(hprinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Add a job to be spooled to a printer queue

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinterReturn ValueReturns the file name to which data should be written and the job id of the new job

Returns:

      None:Printer handle as returned by win32print::OpenPrinterReturn ValueReturns the file name to which data should be written and the job id of the new job

        
    """
    pass
        

def ScheduleJob(hprinter:'win32typing.PyPrinterHANDLE',JobId:'typing.Any') -> 'None':
    """
    Schedules a spooled job to be printed

Args:

      hprinter(win32typing.PyPrinterHANDLE):Printer handle as returned by win32print::OpenPrinter
      JobId(typing.Any):Job Id as returned by win32print::AddJob

Returns:

      None
        
    """
    pass
        

def DeviceCapabilities(Device:'str',Port:'str',Capability:'typing.Any',DEVMODE:'win32typing.PyDEVMODE'=None) -> 'None':
    """
    Queries a printer for its capabilities

Args:

      Device(str):Name of printer
      Port(str):Port that printer is using
      Capability(typing.Any):Type of capability to return - DC_* constant
      DEVMODE(win32typing.PyDEVMODE):If present, function returns values from it, otherwise the printer defaults are usedCapabilityReturned valueDC_MINEXTENTDictionary containing minimum paper width and heightDC_MAXEXTENTDictionary containing maximum paper width and heightDC_ENUMRESOLUTIONSSequence of dictionaries containing x and y resolutions in DPIDC_PAPERSReturns a sequence of ints, DMPAPER_* constantsDC_BINSReturns a sequence of ints, DMBIN_* constantsDC_NUPSequence of ints containing supported logical page per physical page settingsDC_MEDIATYPESSequence of ints, DMMEDIA_* constantsDC_PAPERNAMESSequence of stringsDC_MEDIATYPENAMESSequence of stringsDC_MEDIAREADYSequence of stringsDC_FILEDEPENDENCIESSequence of stringsDC_PERSONALITYSequence of stringsDC_BINNAMESSequence of stringsDC_PAPERSIZESequence of dicts containing paper sizes, in 1/10 millimeter unitsAll othersOutput is an int

Returns:

      None
        
    """
    pass
        

def GetDeviceCaps(hdc:'int',Index:'typing.Any') -> 'typing.Any':
    """
    Retrieves device-specific parameters and settings

Args:

      hdc(int):Handle to a printer or display device context
      Index(typing.Any):The capability to return.  See MSDN for valid values.CommentsCan also be used for Display DCs in addition to printer DCsWin32 API References

Returns:

      typing.Any
        
    """
    pass
        

def EnumMonitors(Name:'typing.Union[str, typing.Any]',Level:'typing.Any') -> 'typing.Tuple[typing.Any, ...]':
    """
    Lists installed printer port monitors

Args:

      Name(typing.Union[str, typing.Any]):Name of server, use None for local machine
      Level(typing.Any):Level of information to return, 1 and 2 supportedReturn ValueReturns a sequence of dicts representing MONITOR_INFO_* structures depending on level

Returns:

      typing.Tuple[typing.Any, ...]:Level of information to return, 1 and 2 supportedReturn ValueReturns a sequence of dicts representing MONITOR_INFO_* structures depending on level

        
    """
    pass
        

def EnumPorts(Name:'typing.Union[str, typing.Any]',Level:'typing.Any') -> 'typing.Tuple[typing.Any, ...]':
    """
    Lists printer port on a server

Args:

      Name(typing.Union[str, typing.Any]):Name of server, use None for local machine
      Level(typing.Any):Level of information to return, 1 and 2 supportedReturn ValueReturns a sequence of dicts representing PORT_INFO_* structures depending on level

Returns:

      typing.Tuple[typing.Any, ...]:Level of information to return, 1 and 2 supportedReturn ValueReturns a sequence of dicts representing PORT_INFO_* structures depending on level

        
    """
    pass
        

def GetPrintProcessorDirectory(Name:'typing.Union[str, typing.Any]',Environment:'typing.Union[str, typing.Any]') -> 'str':
    """
    Returns the directory where print processor files 

reside

Args:

      Name(typing.Union[str, typing.Any]):Name of server, use None for local machine
      Environment(typing.Union[str, typing.Any]):Environment - eg 'Windows NT x86' - use None for current client environment

Returns:

      str
        
    """
    pass
        

def GetPrinterDriverDirectory(Name:'typing.Union[str, typing.Any]',Environment:'typing.Union[str, typing.Any]') -> 'str':
    """
    Returns the directory where printer drivers are 

installed

Args:

      Name(typing.Union[str, typing.Any]):Name of server, use None for local machine
      Environment(typing.Union[str, typing.Any]):Environment - eg 'Windows NT x86' - use None for current client environment

Returns:

      str
        
    """
    pass
        

def AddPrinter(Name:'str',Level:'typing.Any',pPrinter:'typing.Any') -> 'win32typing.PyPrinterHANDLE':
    """
    Installs a printer on a server

Args:

      Name(str):Name of server on which to install printer, None indicates local machine
      Level(typing.Any):Level of data contained in pPrinter, only level 2 currently supported
      pPrinter(typing.Any):PRINTER_INFO_2 dict as returned by win32print::GetPrinterCommentspPrinterName, pPortName, pDriverName, and pPrintProcessor are requiredReturn ValueReturns a handle to the new printer

Returns:

      win32typing.PyPrinterHANDLE:PRINTER_INFO_2 dict as returned by win32print::GetPrinterComments

pPrinterName, pPortName, pDriverName, and pPrintProcessor are required
Return ValueReturns a handle to the new printer

        
    """
    pass
        

def DeletePrinter(hPrinter:'win32typing.PyPrinterHANDLE') -> 'None':
    """
    Deletes an existing printer

Args:

      hPrinter(win32typing.PyPrinterHANDLE):Handle to printer as returned by win32print::OpenPrinter or win32print::AddPrinterCommentsPrinter handle must be opened for PRINTER_ACCESS_ADMINISTER If there are any pending print jobs for the printer, actual deletion does not happen until they are done

Returns:

      None
        
    """
    pass
        

def DeletePrinterDriver(Server:'typing.Union[str]',Environment:'typing.Union[str]',DriverName:'typing.Union[str]') -> 'None':
    """
    Removes the specified printer driver from a server

Args:

      Server(typing.Union[str]):Name of print server, use None for local machine
      Environment(typing.Union[str]):Environment - eg 'Windows NT x86' - use None for current client environment
      DriverName(typing.Union[str]):Name of driver to removeCommentsDoes not delete associated driver files - use win32print::DeletePrinterDriverEx if this is required

Returns:

      None
        
    """
    pass
        

def DeletePrinterDriverEx(Server:'typing.Union[str]',Environment:'typing.Union[str]',DriverName:'typing.Union[str]',DeleteFlag:'typing.Any',VersionFlag:'typing.Any') -> 'None':
    """
    Deletes a printer driver and its associated files

Args:

      Server(typing.Union[str]):Name of print server, use None for local machine
      Environment(typing.Union[str]):Environment - eg 'Windows NT x86' - use None for current client environment
      DriverName(typing.Union[str]):Name of driver to remove
      DeleteFlag(typing.Any):Combination of DPD_DELETE_SPECIFIC_VERSION, DPD_DELETE_UNUSED_FILES, and DPD_DELETE_ALL_FILES
      VersionFlag(typing.Any):Can be 0,1,2, or 3.  Only used if DPD_DELETE_SPECIFIC_VERSION is specified in DeleteFlag

Returns:

      None
        
    """
    pass
        

def FlushPrinter(Printer:'win32typing.PyPrinterHANDLE',Buf:'typing.Any',Sleep:'typing.Any') -> 'typing.Any':
    """
    Clears printer from error state if WritePrinter fails

Args:

      Printer(win32typing.PyPrinterHANDLE):Handle to a printer
      Buf(typing.Any):Data to be sent to printer
      Sleep(typing.Any):Number of milliseconds to suspend printerReturn ValueReturns the number of bytes actually written to the printer

Returns:

      typing.Any:Number of milliseconds to suspend printerReturn ValueReturns the number of bytes actually written to the printer

        
    """
    pass
        