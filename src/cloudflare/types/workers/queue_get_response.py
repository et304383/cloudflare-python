# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["QueueGetResponse"]


class QueueGetResponse(BaseModel):
    consumers: Optional[object] = None

    consumers_total_count: Optional[object] = None

    created_on: Optional[object] = None

    modified_on: Optional[object] = None

    producers: Optional[object] = None

    producers_total_count: Optional[object] = None

    queue_id: Optional[object] = None

    queue_name: Optional[str] = None