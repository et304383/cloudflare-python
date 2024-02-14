# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["NamespaceListResponse", "NamespaceListResponseItem"]


class NamespaceListResponseItem(BaseModel):
    id: str
    """Namespace identifier tag."""

    title: str
    """A human-readable string name for a Namespace."""

    supports_url_encoding: Optional[bool] = None
    """True if keys written on the URL will be URL-decoded before storing.

    For example, if set to "true", a key written on the URL as "%3F" will be stored
    as "?".
    """


NamespaceListResponse = List[NamespaceListResponseItem]