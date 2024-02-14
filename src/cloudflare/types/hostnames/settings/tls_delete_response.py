# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["TLSDeleteResponse"]


class TLSDeleteResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the tls setting was originally created for this hostname."""

    hostname: Optional[str] = None
    """The hostname for which the tls settings are set."""

    status: Optional[object] = None

    updated_at: Optional[datetime] = None
    """This is the time the tls setting was updated."""

    value: Optional[object] = None