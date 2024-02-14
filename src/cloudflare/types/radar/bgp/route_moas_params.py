# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["RouteMoasParams"]


class RouteMoasParams(TypedDict, total=False):
    format: Literal["JSON", "CSV"]
    """Format results are returned in."""

    invalid_only: bool
    """Lookup only RPKI invalid MOASes"""

    origin: int
    """Lookup MOASes originated by the given ASN"""

    prefix: str
    """Lookup MOASes by prefix"""