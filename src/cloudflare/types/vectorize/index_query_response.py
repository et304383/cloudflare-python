# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndexQueryResponse", "Match"]


class Match(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    metadata: Optional[object] = None

    score: Optional[float] = None
    """The score of the vector according to the index's distance metric"""

    values: Optional[List[float]] = None


class IndexQueryResponse(BaseModel):
    count: Optional[int] = None
    """Specifies the count of vectors returned by the search"""

    matches: Optional[List[Match]] = None
    """Array of vectors matched by the search"""