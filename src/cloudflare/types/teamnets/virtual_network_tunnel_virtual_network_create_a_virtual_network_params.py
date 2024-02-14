# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkParams"]


class VirtualNetworkTunnelVirtualNetworkCreateAVirtualNetworkParams(TypedDict, total=False):
    name: Required[str]
    """A user-friendly name for the virtual network."""

    comment: str
    """Optional remark describing the virtual network."""

    is_default: bool
    """If `true`, this virtual network is the default for the account."""