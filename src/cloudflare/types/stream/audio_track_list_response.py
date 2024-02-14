# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["AudioTrackListResponse", "AudioTrackListResponseItem"]


class AudioTrackListResponseItem(BaseModel):
    default: Optional[bool] = None
    """Denotes whether the audio track will be played by default in a player."""

    label: Optional[str] = None
    """
    A string to uniquely identify the track amongst other audio track labels for the
    specified video.
    """

    status: Optional[Literal["queued", "ready", "error"]] = None
    """Specifies the processing status of the video."""

    uid: Optional[str] = None
    """A Cloudflare-generated unique identifier for a media item."""


AudioTrackListResponse = List[AudioTrackListResponseItem]