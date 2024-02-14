# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse",
    "UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItem",
    "UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItemConfiguration",
]


class UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItemConfiguration(BaseModel):
    target: Optional[str] = None
    """The configuration target for this rule.

    You must set the target to `ua` for User Agent Blocking rules.
    """

    value: Optional[str] = None
    """The exact user agent string to match.

    This value will be compared to the received `User-Agent` HTTP header value.
    """


class UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItem(BaseModel):
    id: Optional[str] = None
    """The unique identifier of the User Agent Blocking rule."""

    configuration: Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItemConfiguration] = None
    """The configuration object for the current rule."""

    description: Optional[str] = None
    """An informative summary of the rule."""

    mode: Optional[Literal["block", "challenge", "js_challenge", "managed_challenge"]] = None
    """The action to apply to a matched request."""

    paused: Optional[bool] = None
    """When true, indicates that the rule is currently paused."""


UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse = List[
    UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponseItem
]