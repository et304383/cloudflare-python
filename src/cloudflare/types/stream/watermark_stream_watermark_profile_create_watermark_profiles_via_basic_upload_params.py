# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadParams"]


class WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadParams(TypedDict, total=False):
    file: Required[str]
    """The image file to upload."""

    name: str
    """A short description of the watermark profile."""

    opacity: float
    """The translucency of the image.

    A value of `0.0` makes the image completely transparent, and `1.0` makes the
    image completely opaque. Note that if the image is already semi-transparent,
    setting this to `1.0` will not make the image completely opaque.
    """

    padding: float
    """
    The whitespace between the adjacent edges (determined by position) of the video
    and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded
    video width or length, as determined by the algorithm.
    """

    position: str
    """The location of the image.

    Valid positions are: `upperRight`, `upperLeft`, `lowerLeft`, `lowerRight`, and
    `center`. Note that `center` ignores the `padding` parameter.
    """

    scale: float
    """The size of the image relative to the overall size of the video.

    This parameter will adapt to horizontal and vertical videos automatically. `0.0`
    indicates no scaling (use the size of the image as-is), and `1.0 `fills the
    entire video.
    """