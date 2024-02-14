# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["AseListResponse", "Top0"]


class Top0(BaseModel):
    client_asn: float = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    value: str


class AseListResponse(BaseModel):
    top_0: List[Top0]