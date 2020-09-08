__all__=['', 'OleCreate', 'OleLoadPicture', 'OleLoadPicturePath', 'OleSetContainedObject', 'OleTranslateAccelerator', 'EMBDHLP_CREATENOW', 'EMBDHLP_DELAYCREATE', 'EMBDHLP_INPROC_HANDLER', 'EMBDHLP_INPROC_SERVER', 'OLECLOSE_NOSAVE', 'OLECLOSE_PROMPTSAVE', 'OLECLOSE_SAVEIFDIRTY', 'OLECMDF_ENABLED', 'OLECMDF_LATCHED', 'OLECMDF_NINCHED', 'OLECMDF_SUPPORTED', 'OLECMDTEXTF_NAME', 'OLECMDTEXTF_NONE', 'OLECMDTEXTF_STATUS', 'OLECREATE_LEAVERUNNING', 'OLEIVERB_DISCARDUNDOSTATE', 'OLEIVERB_HIDE', 'OLEIVERB_INPLACEACTIVATE', 'OLEIVERB_OPEN', 'OLEIVERB_PRIMARY', 'OLEIVERB_SHOW', 'OLEIVERB_UIACTIVATE']
from typing import *
from win32helper.win32typing import *
"""A module, encapsulating the ActiveX Control interfaces"""


def OleCreate(clsid:'Any',clsid1:'Any',obCLSID:'PyIID',obIID:'PyIID',renderopt:'Any',obFormatEtc:'Any',obOleClientSite:'PyIOleClientSite',obStorage:'PyIStorage') -> 'PyIOleObject':
    """
    Creates a new embedded object identified by a CLSID.

Args:

      clsid(Any):A CLSID in string or native format
      clsid1(Any):A IID in string or native format
      obCLSID(PyIID):The PyIID CLSID for the OLE object to create.
      obIID(PyIID):The PyIID for the interface to return.
      renderopt(Any):The DWORD renderopt for redering the Display.
      obFormatEtc(Any):The FORMATETC structure.
      obOleClientSite(PyIOleClientSite):The PyIOleClientSite interface to the container.
      obStorage(PyIStorage):The PyIStorage interface.

Returns:

      PyIOleObject
        
    """
    pass
        

def OleLoadPicture(stream:'PyIStream',size:'int',runMode:'int',arg:'PyIID',arg1:'PyIID') -> 'PyIUnknown':
    """
    Creates a new picture object and initializes it from the contents 

of a stream.

Args:

      stream(PyIStream):The stream that contains picture's data.
      size(int):Number of bytes read from the stream
      runMode(int):The opposite of the initial value of the KeepOriginalFormat property. If TRUE, KeepOriginalFormat is set to FALSE and vice-versa.
      arg(PyIID):The identifier of the interface describing the type of interface pointer to return
      arg1(PyIID):The IID to use for the return object - use only if pythoncom does not support the native interface requested.

Returns:

      PyIUnknown
        
    """
    pass
        

def OleLoadPicturePath(url_or_path:'Union[str, Any]',unk:'Any',reserved:'int',clr:'int',arg:'PyIID',arg1:'PyIID') -> 'PyIUnknown':
    """
    Creates a new picture object and initializes it from the 

contents of a stream.

Args:

      url_or_path(Union[str, Any]):The path or url to the file you want to open.
      unk(Any):The IUnknown for COM aggregation.
      reserved(int):reserved
      clr(int):The color you want to reserve to be transparent.
      arg(PyIID):The identifier of the interface describing the type of interface pointer to return
      arg1(PyIID):The IID to use for the return object - use only if pythoncom does not support the native interface requested.

Returns:

      PyIUnknown
        
    """
    pass
        

def OleSetContainedObject(unk:'PyIUnknown',fContained:'int') -> 'None':
    """
    Notifies an object embedded in an OLE container to ensure correct 

reference.

Args:

      unk(PyIUnknown):The object
      fContained(int):

Returns:

      None
        
    """
    pass
        

def OleTranslateAccelerator(frame:'PyIOleInPlaceFrame',frame_info:'Any',msg:'PyMSG') -> 'None':
    """
    Called by the object application, allows an object's container to 

translate accelerators according to the container's accelerator table.

Args:

      frame(PyIOleInPlaceFrame):frame to send keystrokes to.
      frame_info(Any):
      msg(PyMSG):

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