# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["BucketListParams"]


class BucketListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor received during the last List Buckets call.

    R2 buckets are paginated using cursors instead of page numbers.
    """

    direction: Literal["asc", "desc"]
    """Direction to order buckets"""

    name_contains: str
    """Bucket names to filter by.

    Only buckets with this phrase in their name will be returned.
    """

    order: Literal["name"]
    """Field to order buckets by"""

    per_page: float
    """Maximum number of buckets to return in a single call"""

    start_after: str
    """Bucket name to start searching after. Buckets are ordered lexicographically."""