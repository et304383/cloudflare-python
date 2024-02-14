# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["OriginTLSClientAuthListResponse", "OriginTLSClientAuthListResponseItem"]


class OriginTLSClientAuthListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The zone's leaf certificate."""

    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""

    private_key: Optional[str] = None
    """The zone's private key."""


OriginTLSClientAuthListResponse = List[OriginTLSClientAuthListResponseItem]