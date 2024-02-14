# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["WidgetGetResponse"]


class WidgetGetResponse(BaseModel):
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

    created_on: datetime
    """When the widget was created."""

    domains: List[str]

    mode: Literal["non-interactive", "invisible", "managed"]
    """Widget Mode"""

    modified_on: datetime
    """When the widget was modified."""

    name: str
    """Human readable widget name.

    Not unique. Cloudflare suggests that you set this to a meaningful string to make
    it easier to identify your widget, and where it is used.
    """

    offlabel: bool
    """Do not show any Cloudflare branding on the widget (ENT only)."""

    region: Literal["world"]
    """Region where this widget can be used."""

    secret: str
    """Secret key for this widget."""

    sitekey: str
    """Widget item identifier tag."""