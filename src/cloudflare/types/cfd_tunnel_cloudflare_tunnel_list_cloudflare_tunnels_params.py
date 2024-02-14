# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Union

from datetime import datetime

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CfdTunnelCloudflareTunnelListCloudflareTunnelsParams"]


class CfdTunnelCloudflareTunnelListCloudflareTunnelsParams(TypedDict, total=False):
    exclude_prefix: str

    existed_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, include only tunnels that were created (and not deleted) before
    this time.
    """

    include_prefix: str

    is_deleted: bool
    """If `true`, only include deleted tunnels.

    If `false`, exclude deleted tunnels. If empty, all tunnels will be included.
    """

    name: str
    """A user-friendly name for the tunnel."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    was_active_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    was_inactive_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]