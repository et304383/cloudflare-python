# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from datetime import datetime

from typing import List, Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["DatasetListResponse", "DatasetListResponseItem", "DatasetListResponseItemUpload"]


class DatasetListResponseItemUpload(BaseModel):
    num_cells: int

    status: Literal["empty", "uploading", "failed", "complete"]

    version: int


class DatasetListResponseItem(BaseModel):
    id: str

    created_at: datetime

    name: str

    num_cells: int

    secret: bool

    status: Literal["empty", "uploading", "failed", "complete"]

    updated_at: datetime

    uploads: List[DatasetListResponseItemUpload]

    description: Optional[str] = None


DatasetListResponse = List[DatasetListResponseItem]