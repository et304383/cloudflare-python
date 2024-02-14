# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["GroupWAFRuleGroupsListWAFRuleGroupsResponse", "GroupWAFRuleGroupsListWAFRuleGroupsResponseItem"]


class GroupWAFRuleGroupsListWAFRuleGroupsResponseItem(BaseModel):
    id: str
    """The unique identifier of the rule group."""

    description: Optional[str] = None
    """An informative summary of what the rule group does."""

    mode: Literal["on", "off"]
    """The state of the rules contained in the rule group.

    When `on`, the rules in the group are configurable/usable.
    """

    name: str
    """The name of the rule group."""

    rules_count: float
    """The number of rules in the current rule group."""

    allowed_modes: Optional[List[Literal["on", "off"]]] = None
    """The available states for the rule group."""

    modified_rules_count: Optional[float] = None
    """
    The number of rules within the group that have been modified from their default
    configuration.
    """

    package_id: Optional[str] = None
    """The unique identifier of a WAF package."""


GroupWAFRuleGroupsListWAFRuleGroupsResponse = List[GroupWAFRuleGroupsListWAFRuleGroupsResponseItem]