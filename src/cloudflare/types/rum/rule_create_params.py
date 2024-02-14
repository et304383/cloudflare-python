# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["RuleCreateParams"]


class RuleCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    host: str

    inclusive: bool
    """Whether the rule includes or excludes traffic from being measured."""

    is_paused: bool
    """Whether the rule is paused or not."""

    paths: List[str]