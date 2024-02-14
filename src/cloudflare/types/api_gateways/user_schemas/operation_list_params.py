# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["OperationListParams"]


class OperationListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    endpoint: str
    """Filter results to only include endpoints containing this pattern."""

    feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]]
    """Add feature(s) to the results.

    The feature name that is given here corresponds to the resulting feature object.
    Have a look at the top-level object description for more details on the specific
    meaning.
    """

    host: List[str]
    """Filter results to only include the specified hosts."""

    method: List[str]
    """Filter results to only include the specified HTTP methods."""

    operation_status: Literal["new", "existing"]
    """
    Filter results by whether operations exist in API Shield Endpoint Management or
    not. `new` will just return operations from the schema that do not exist in API
    Shield Endpoint Management. `existing` will just return operations from the
    schema that already exist in API Shield Endpoint Management.
    """

    page: object
    """Page number of paginated results."""

    per_page: object
    """Maximum number of results per page."""