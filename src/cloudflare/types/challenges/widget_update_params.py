# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["WidgetUpdateParams"]


class WidgetUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    domains: Required[List[str]]

    mode: Required[Literal["non-interactive", "invisible", "managed"]]
    """Widget Mode"""

    name: Required[str]
    """Human readable widget name.

    Not unique. Cloudflare suggests that you set this to a meaningful string to make
    it easier to identify your widget, and where it is used.
    """

    bot_fight_mode: bool
    """
    If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
    challenges in response to malicious bots (ENT only).
    """

    clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"]
    """
    If Turnstile is embedded on a Cloudflare site and the widget should grant
    challenge clearance, this setting can determine the clearance level to be set
    """

    offlabel: bool
    """Do not show any Cloudflare branding on the widget (ENT only)."""