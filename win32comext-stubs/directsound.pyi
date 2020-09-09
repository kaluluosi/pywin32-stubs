__all__=['', 'DirectSoundCreate', 'DirectSoundEnumerate', 'DirectSoundCaptureCreate', 'DirectSoundCaptureEnumerate', 'DSCAPS', 'DSBCAPS', 'DSCCAPS', 'DSCBCAPS', 'DSBUFFERDESC', 'DSCBUFFERDESC', 'DS3DMODE_DISABLE', 'DS3DMODE_HEADRELATIVE', 'DS3DMODE_NORMAL', 'DSBCAPS_CTRL3D', 'DSBCAPS_CTRLFREQUENCY', 'DSBCAPS_CTRLPAN', 'DSBCAPS_CTRLPOSITIONNOTIFY', 'DSBCAPS_CTRLVOLUME', 'DSBCAPS_GETCURRENTPOSITION2', 'DSBCAPS_GLOBALFOCUS', 'DSBCAPS_LOCHARDWARE', 'DSBCAPS_LOCSOFTWARE', 'DSBCAPS_MUTE3DATMAXDISTANCE', 'DSBCAPS_PRIMARYBUFFER', 'DSBCAPS_STATIC', 'DSBCAPS_STICKYFOCUS', 'DSBLOCK_ENTIREBUFFER', 'DSBLOCK_FROMWRITECURSOR', 'DSBPLAY_LOOPING', 'DSBSTATUS_BUFFERLOST', 'DSBSTATUS_LOOPING', 'DSBSTATUS_PLAYING', 'DSCAPS_CERTIFIED', 'DSCAPS_CONTINUOUSRATE', 'DSCAPS_EMULDRIVER', 'DSCAPS_PRIMARY16BIT', 'DSCAPS_PRIMARY8BIT', 'DSCAPS_PRIMARYMONO', 'DSCAPS_PRIMARYSTEREO', 'DSCAPS_SECONDARY16BIT', 'DSCAPS_SECONDARY8BIT', 'DSCAPS_SECONDARYMONO', 'DSCAPS_SECONDARYSTEREO', 'DSCBCAPS_WAVEMAPPED', 'DSCCAPS_EMULDRIVER', 'DSSCL_EXCLUSIVE', 'DSSCL_NORMAL', 'DSSCL_PRIORITY', 'DSSCL_WRITEPRIMARY', 'DSSPEAKER_GEOMETRY_MAX', 'DSSPEAKER_GEOMETRY_MIN', 'DSSPEAKER_GEOMETRY_NARROW', 'DSSPEAKER_GEOMETRY_WIDE', 'DSSPEAKER_HEADPHONE', 'DSSPEAKER_MONO', 'DSSPEAKER_QUAD', 'DSSPEAKER_STEREO', 'DSSPEAKER_SURROUND']
import typing
from win32helper import win32typing
""""""


def DirectSoundCreate(guid:'win32typing.PyIID'=None,unk:'typing.Any'=None) -> 'win32typing.PyIUnknown':
    """
    Creates and initializes a new object that supports the 

IDirectSound interface.

Args:

      guid(win32typing.PyIID):Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundEnumerate, or None for the default device.
      unk(typing.Any):The IUnknown for COM aggregation.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def DirectSoundEnumerate() -> 'typing.Any':
    """
    Enumerates DirectSound drivers installed in the system.

Args:



Returns:

      typing.Any
        
    """
    pass
        

def DirectSoundCaptureCreate(guid:'win32typing.PyIID'=None,unk:'typing.Any'=None) -> 'win32typing.PyIUnknown':
    """
    Creates and initializes a new object that supports the 

IDirectSoundCapture interface.

Args:

      guid(win32typing.PyIID):Address of the GUID that identifies the sound device. The value of this parameter must be one of the GUIDs returned by DirectSoundCaptureEnumerate, or None for the default device.
      unk(typing.Any):The IUnknown for COM aggregation.

Returns:

      win32typing.PyIUnknown
        
    """
    pass
        

def DirectSoundCaptureEnumerate() -> 'typing.Any':
    """
    Enumerates DirectSoundCapture drivers installed in the 

system.

Args:



Returns:

      typing.Any
        
    """
    pass
        

def DSCAPS() -> 'win32typing.PyDSCAPS':
    """
    Creates a new PyDSCAPS object.

Args:



Returns:

      win32typing.PyDSCAPS
        
    """
    pass
        

def DSBCAPS() -> 'win32typing.PyDSBCAPS':
    """
    Creates a new PyDSBCAPS object

Args:



Returns:

      win32typing.PyDSBCAPS
        
    """
    pass
        

def DSCCAPS() -> 'win32typing.PyDSCCAPS':
    """
    Creates a new PyDSCCAPS object

Args:



Returns:

      win32typing.PyDSCCAPS
        
    """
    pass
        

def DSCBCAPS() -> 'win32typing.PyDSCBCAPS':
    """
    Creates a new PyDSCBCAPS object

Args:



Returns:

      win32typing.PyDSCBCAPS
        
    """
    pass
        

def DSBUFFERDESC() -> 'win32typing.PyDSBUFFERDESC':
    """
    Creates a new PyDSBUFFERDESC object

Args:



Returns:

      win32typing.PyDSBUFFERDESC
        
    """
    pass
        

def DSCBUFFERDESC() -> 'win32typing.PyDSCBUFFERDESC':
    """
    Creates a new PyDSCBUFFERDESC object

Args:



Returns:

      win32typing.PyDSCBUFFERDESC
        
    """
    pass
        
DS3DMODE_DISABLE = ...
DS3DMODE_HEADRELATIVE = ...
DS3DMODE_NORMAL = ...
DSBCAPS_CTRL3D = ...
DSBCAPS_CTRLFREQUENCY = ...
DSBCAPS_CTRLPAN = ...
DSBCAPS_CTRLPOSITIONNOTIFY = ...
DSBCAPS_CTRLVOLUME = ...
DSBCAPS_GETCURRENTPOSITION2 = ...
DSBCAPS_GLOBALFOCUS = ...
DSBCAPS_LOCHARDWARE = ...
DSBCAPS_LOCSOFTWARE = ...
DSBCAPS_MUTE3DATMAXDISTANCE = ...
DSBCAPS_PRIMARYBUFFER = ...
DSBCAPS_STATIC = ...
DSBCAPS_STICKYFOCUS = ...
DSBLOCK_ENTIREBUFFER = ...
DSBLOCK_FROMWRITECURSOR = ...
DSBPLAY_LOOPING = ...
DSBSTATUS_BUFFERLOST = ...
DSBSTATUS_LOOPING = ...
DSBSTATUS_PLAYING = ...
DSCAPS_CERTIFIED = ...
DSCAPS_CONTINUOUSRATE = ...
DSCAPS_EMULDRIVER = ...
DSCAPS_PRIMARY16BIT = ...
DSCAPS_PRIMARY8BIT = ...
DSCAPS_PRIMARYMONO = ...
DSCAPS_PRIMARYSTEREO = ...
DSCAPS_SECONDARY16BIT = ...
DSCAPS_SECONDARY8BIT = ...
DSCAPS_SECONDARYMONO = ...
DSCAPS_SECONDARYSTEREO = ...
DSCBCAPS_WAVEMAPPED = ...
DSCCAPS_EMULDRIVER = ...
DSSCL_EXCLUSIVE = ...
DSSCL_NORMAL = ...
DSSCL_PRIORITY = ...
DSSCL_WRITEPRIMARY = ...
DSSPEAKER_GEOMETRY_MAX = ...
DSSPEAKER_GEOMETRY_MIN = ...
DSSPEAKER_GEOMETRY_NARROW = ...
DSSPEAKER_GEOMETRY_WIDE = ...
DSSPEAKER_HEADPHONE = ...
DSSPEAKER_MONO = ...
DSSPEAKER_QUAD = ...
DSSPEAKER_STEREO = ...
DSSPEAKER_SURROUND = ...