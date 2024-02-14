# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["VariantDeleteResponse"]


class VariantDeleteResponse(BaseModel):
    id: Literal["variants"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""