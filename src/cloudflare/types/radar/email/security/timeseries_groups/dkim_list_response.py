# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ......_models import BaseModel
from ......types import shared

__all__ = ["DKIMListResponse", "Serie0"]


class Serie0(BaseModel):
    fail: List[str] = FieldInfo(alias="FAIL")

    none: List[str] = FieldInfo(alias="NONE")

    pass_: List[str] = FieldInfo(alias="PASS")


class DKIMListResponse(BaseModel):
    meta: object

    serie_0: Serie0