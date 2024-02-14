# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["EdgeGetResponse", "EdgeGetResponseItem"]


class EdgeGetResponseItem(BaseModel):
    destination_conf: Optional[str] = None
    """Unique WebSocket address that will receive messages from Cloudflare’s edge."""

    fields: Optional[str] = None
    """Comma-separated list of fields."""

    filter: Optional[str] = None
    """Filters to drill down into specific events."""

    sample: Optional[int] = None
    """
    The sample parameter is the sample rate of the records set by the client:
    "sample": 1 is 100% of records "sample": 10 is 10% and so on.
    """

    session_id: Optional[str] = None
    """Unique session id of the job."""


EdgeGetResponse = List[Optional[EdgeGetResponseItem]]