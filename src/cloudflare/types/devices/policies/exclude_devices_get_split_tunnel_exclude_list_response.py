# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ExcludeDevicesGetSplitTunnelExcludeListResponse", "ExcludeDevicesGetSplitTunnelExcludeListResponseItem"]


class ExcludeDevicesGetSplitTunnelExcludeListResponseItem(BaseModel):
    address: str
    """The address in CIDR format to exclude from the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""

    host: Optional[str] = None
    """The domain name to exclude from the tunnel.

    If `host` is present, `address` must not be present.
    """


ExcludeDevicesGetSplitTunnelExcludeListResponse = List[ExcludeDevicesGetSplitTunnelExcludeListResponseItem]