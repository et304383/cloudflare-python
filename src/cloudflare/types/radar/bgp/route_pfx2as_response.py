# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["RoutePfx2asResponse", "Meta", "PrefixOrigin"]


class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int


class PrefixOrigin(BaseModel):
    origin: int

    peer_count: int

    prefix: str

    rpki_validation: str


class RoutePfx2asResponse(BaseModel):
    meta: Meta

    prefix_origins: List[PrefixOrigin]