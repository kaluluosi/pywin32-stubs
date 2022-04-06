__all__=['', 'OleCreate', 'OleLoadPicture', 'OleLoadPicturePath', 'OleSetContainedObject', 'OleTranslateAccelerator', 'EMBDHLP_CREATENOW', 'EMBDHLP_DELAYCREATE', 'EMBDHLP_INPROC_HANDLER', 'EMBDHLP_INPROC_SERVER', 'OLECLOSE_NOSAVE', 'OLECLOSE_PROMPTSAVE', 'OLECLOSE_SAVEIFDIRTY', 'OLECMDF_ENABLED', 'OLECMDF_LATCHED', 'OLECMDF_NINCHED', 'OLECMDF_SUPPORTED', 'OLECMDTEXTF_NAME', 'OLECMDTEXTF_NONE', 'OLECMDTEXTF_STATUS', 'OLECREATE_LEAVERUNNING', 'OLEIVERB_DISCARDUNDOSTATE', 'OLEIVERB_HIDE', 'OLEIVERB_INPLACEACTIVATE', 'OLEIVERB_OPEN', 'OLEIVERB_PRIMARY', 'OLEIVERB_SHOW', 'OLEIVERB_UIACTIVATE']
import typing
import win32typing
"""A module, encapsulating the ActiveX Control interfaces"""


def OleCreate(clsid:'typing.Any',clsid1:'typing.Any',obCLSID:'win32typing.PyIID',obIID:'win32typing.PyIID',renderopt:'typing.Any',obFormatEtc:'typing.Any',obOleClientSite:'win32typing.PyIOleClientSite',obStorage:'win32typing.PyIStorage') -> 'win32typing.PyIOleObject':
    """
    Creates a new embedded object identified by a CLSID.

Args:

      clsid(typing.Any):A CLSID in string or native format
      clsid1(typing.Any):A IID in string or native format
      obCLSID(win32typing.PyIID):The PyIID CLSID for the OLE object to create.
      obIID(win32typing.PyIID):The PyIID for the interface to return.
      renderopt(typing.Any):The DWORD renderopt for redering the Display.
      obFormatEtc(typing.Any):The FORMATETC structure.
      obOleClientSite(win32typing.PyIOleClientSite):The PyIOleClientSite interface to the container.
      obStorage(win32typing.PyIStorage):The PyIStorage interface.

Returns:

      win32typing.PyIOleObject
        
    """
    pass
        

def OleLoadPicture(stream:'win32typing.PyIStream',size:'typing.Any',runMode:'typing.Any',arg:'win32typing.PyIID',arg1:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Creates a new picture object and initializes it from the contents 

of a stream.

Args:

      stream(win32typing.PyIStream):The stream that contains picture's data.
      size(typing.Any):Number of bytes read from the stream
      runMode(typing.Any):The opposite of the initial value of the KeepOriginalFormat property. If TRUE, KeepOriginalFormat is set to FALSE and vice-versa.
      arg(win32typing.PyIID):The identifier of the interface describing the type of interface pointer to return
      arg1(win32typing.PyIID):The IID to use for the return object - use only if pythoncom does not support the native interface requested.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def OleLoadPicturePath(url_or_path:'typing.Union[typing.Any, str]',unk:'typing.Any',reserved:'typing.Any',clr:'typing.Any',arg:'win32typing.PyIID',arg1:'win32typing.PyIID') -> 'win32typing.PyIUnknown':
    """
    Creates a new picture object and initializes it from the 

contents of a stream.

Args:

      url_or_path(typing.Union[typing.Any, str]):The path or url to the file you want to open.
      unk(typing.Any):The IUnknown for COM aggregation.
      reserved(typing.Any):reserved
      clr(typing.Any):The color you want to reserve to be transparent.
      arg(win32typing.PyIID):The identifier of the interface describing the type of interface pointer to return
      arg1(win32typing.PyIID):The IID to use for the return object - use only if pythoncom does not support the native interface requested.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def OleSetContainedObject(unk:'win32typing.PyIUnknown',fContained:'typing.Any') -> 'None':
    """
    Notifies an object embedded in an OLE container to ensure correct 

reference.

Args:

      unk(win32typing.PyIUnknown):The object
      fContained(typing.Any):

Returns:

      None
        
    """
    pass
        

def OleTranslateAccelerator(frame:'win32typing.PyIOleInPlaceFrame',frame_info:'typing.Any',msg:'win32typing.PyMSG') -> 'None':
    """
    Called by the object application, allows an object's container to 

translate accelerators according to the container's accelerator table.

Args:

      frame(win32typing.PyIOleInPlaceFrame):frame to send keystrokes to.
      frame_info(typing.Any):
      msg(win32typing.PyMSG):

Returns:

      None
        
    """
    pass
        
EMBDHLP_CREATENOW = ...
EMBDHLP_DELAYCREATE = ...
EMBDHLP_INPROC_HANDLER = ...
EMBDHLP_INPROC_SERVER = ...
OLECLOSE_NOSAVE = ...
OLECLOSE_PROMPTSAVE = ...
OLECLOSE_SAVEIFDIRTY = ...
OLECMDF_ENABLED = ...
OLECMDF_LATCHED = ...
OLECMDF_NINCHED = ...
OLECMDF_SUPPORTED = ...
OLECMDTEXTF_NAME = ...
OLECMDTEXTF_NONE = ...
OLECMDTEXTF_STATUS = ...
OLECREATE_LEAVERUNNING = ...
OLEIVERB_DISCARDUNDOSTATE = ...
OLEIVERB_HIDE = ...
OLEIVERB_INPLACEACTIVATE = ...
OLEIVERB_OPEN = ...
OLEIVERB_PRIMARY = ...
OLEIVERB_SHOW = ...
OLEIVERB_UIACTIVATE = ...
