# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["ClientCertificateClientCertificateForAZoneListClientCertificatesParams"]


class ClientCertificateClientCertificateForAZoneListClientCertificatesParams(TypedDict, total=False):
    limit: int
    """Limit to the number of records returned."""

    offset: int
    """Offset the results"""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of records per page."""

    status: Literal["all", "active", "pending_reactivation", "pending_revocation", "revoked"]
    """Client Certitifcate Status to filter results by."""