# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = [
    "PageruleListResponse",
    "PageruleListResponseItem",
    "PageruleListResponseItemAction",
    "PageruleListResponseItemActionValue",
    "PageruleListResponseItemTarget",
    "PageruleListResponseItemTargetConstraint",
]


class PageruleListResponseItemActionValue(BaseModel):
    type: Optional[Literal["temporary", "permanent"]] = None
    """The response type for the URL redirect."""

    url: Optional[str] = None
    """
    The URL to redirect the request to. Notes: ${num} refers to the position of '\\**'
    in the constraint value.
    """


class PageruleListResponseItemAction(BaseModel):
    modified_on: Optional[datetime] = None
    """The timestamp of when the override was last modified."""

    name: Optional[Literal["forward_url"]] = None
    """The type of route."""

    value: Optional[PageruleListResponseItemActionValue] = None


class PageruleListResponseItemTargetConstraint(BaseModel):
    operator: Literal["matches", "contains", "equals", "not_equal", "not_contain"]
    """
    The matches operator can use asterisks and pipes as wildcard and 'or' operators.
    """

    value: str
    """The URL pattern to match against the current request.

    The pattern may contain up to four asterisks ('\\**') as placeholders.
    """


class PageruleListResponseItemTarget(BaseModel):
    constraint: PageruleListResponseItemTargetConstraint
    """String constraint."""

    target: Literal["url"]
    """A target based on the URL of the request."""


class PageruleListResponseItem(BaseModel):
    id: str
    """Identifier"""

    actions: List[PageruleListResponseItemAction]
    """The set of actions to perform if the targets of this rule match the request.

    Actions can redirect to another URL or override settings, but not both.
    """

    created_on: datetime
    """The timestamp of when the Page Rule was created."""

    modified_on: datetime
    """The timestamp of when the Page Rule was last modified."""

    priority: int
    """
    The priority of the rule, used to define which Page Rule is processed over
    another. A higher number indicates a higher priority. For example, if you have a
    catch-all Page Rule (rule A: `/images/*`) but want a more specific Page Rule to
    take precedence (rule B: `/images/special/*`), specify a higher priority for
    rule B so it overrides rule A.
    """

    status: Literal["active", "disabled"]
    """The status of the Page Rule."""

    targets: List[PageruleListResponseItemTarget]
    """The rule targets to evaluate on each request."""


PageruleListResponse = List[PageruleListResponseItem]