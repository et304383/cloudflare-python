# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["AsePrefixesResponse", "Asn", "Meta"]


class Asn(BaseModel):
    asn: int

    country: str

    name: str

    pfxs_count: int


class Meta(BaseModel):
    data_time: str

    query_time: str

    total_peers: int


class AsePrefixesResponse(BaseModel):
    asns: List[Asn]

    meta: Meta