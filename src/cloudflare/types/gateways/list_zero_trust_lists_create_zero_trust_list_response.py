# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ListZeroTrustListsCreateZeroTrustListResponse", "Item"]


class Item(BaseModel):
    created_at: Optional[datetime] = None

    value: Optional[str] = None
    """The value of the item in a list."""


class ListZeroTrustListsCreateZeroTrustListResponse(BaseModel):
    id: Optional[str] = None
    """API Resource UUID tag."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the list."""

    items: Optional[List[Item]] = None
    """The items in the list."""

    name: Optional[str] = None
    """The name of the list."""

    type: Optional[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]] = None
    """The type of list."""

    updated_at: Optional[datetime] = None