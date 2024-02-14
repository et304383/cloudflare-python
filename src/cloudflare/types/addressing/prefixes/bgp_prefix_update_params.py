# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["BGPPrefixUpdateParams", "OnDemand"]


class BGPPrefixUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    prefix_identifier: Required[str]
    """Identifier"""

    on_demand: OnDemand


class OnDemand(TypedDict, total=False):
    advertised: bool