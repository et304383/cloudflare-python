# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["ManagedHeaderListResponse", "ManagedRequestHeader", "ManagedResponseHeader"]


class ManagedRequestHeader(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""


class ManagedResponseHeader(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""


class ManagedHeaderListResponse(BaseModel):
    managed_request_headers: Optional[List[ManagedRequestHeader]] = None

    managed_response_headers: Optional[List[ManagedResponseHeader]] = None