# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["GroupWAFRuleGroupsListWAFRuleGroupsParams"]


class GroupWAFRuleGroupsListWAFRuleGroupsParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned rule groups."""

    match: Literal["any", "all"]
    """When set to `all`, all the search requirements must match.

    When set to `any`, only one of the search requirements has to match.
    """

    mode: Literal["on", "off"]
    """The state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """

    order: Literal["mode", "rules_count"]
    """The field used to sort returned rule groups."""

    page: float
    """The page number of paginated results."""

    per_page: float
    """The number of rule groups per page."""