# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ScanCreateResponse"]


class ScanCreateResponse(BaseModel):
    time: datetime
    """Time when url was submitted for scanning."""

    url: str
    """Canonical form of submitted URL. Use this if you want to later search by URL."""

    uuid: str
    """Scan ID."""

    visibility: str
    """Submitted visibility status."""