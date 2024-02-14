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

__all__ = ["URLScannerScanParams"]


class URLScannerScanParams(TypedDict, total=False):
    account_scans: bool
    """Return only scans created by account."""

    date_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter scans requested before date (inclusive)."""

    date_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter scans requested after date (inclusive)."""

    hostname: str
    """Filter scans by hostname of _any_ request made by the webpage."""

    limit: int
    """Limit the number of objects in the response."""

    next_cursor: str
    """Pagination cursor to get the next set of results."""

    page_hostname: str
    """Filter scans by main page hostname ."""

    page_path: str
    """Filter scans by exact match URL path (also supports suffix search)."""

    page_url: str
    """Filter scans by exact match to scanned URL (_after redirects_)"""

    path: str
    """Filter scans by url path of _any_ request made by the webpage."""

    scan_id: Annotated[str, PropertyInfo(alias="scanId")]
    """Scan uuid"""

    url: str
    """Filter scans by exact match URL of _any_ request made by the webpage"""