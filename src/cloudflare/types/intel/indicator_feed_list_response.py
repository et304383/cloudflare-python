# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndicatorFeedListResponse", "IndicatorFeedListResponseItem"]


class IndicatorFeedListResponseItem(BaseModel):
    id: Optional[int] = None
    """The unique identifier for the indicator feed"""

    created_on: Optional[datetime] = None
    """The date and time when the data entry was created"""

    description: Optional[str] = None
    """The description of the example test"""

    modified_on: Optional[datetime] = None
    """The date and time when the data entry was last modified"""

    name: Optional[str] = None
    """The name of the indicator feed"""


IndicatorFeedListResponse = List[IndicatorFeedListResponseItem]