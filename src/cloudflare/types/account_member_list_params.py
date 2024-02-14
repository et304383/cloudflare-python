# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["AccountMemberListParams"]


class AccountMemberListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """Direction to order results."""

    order: Literal["user.first_name", "user.last_name", "user.email", "status"]
    """Field to order results by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""

    status: Literal["accepted", "pending", "rejected"]
    """A member's status in the account."""