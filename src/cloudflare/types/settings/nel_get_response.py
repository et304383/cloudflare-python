# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["NELGetResponse", "Value"]


class Value(BaseModel):
    enabled: Optional[bool] = None


class NELGetResponse(BaseModel):
    id: Literal["nel"]
    """Zone setting identifier."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""