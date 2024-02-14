# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneParams"]


class OperationAPIShieldEndpointManagementGetInformationAboutAllOperationsOnAZoneParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]
    """Direction to order results."""

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

    order: Literal["method", "host", "endpoint", "thresholds.$key"]
    """Field to order by.

    When requesting a feature, the feature keys are available for ordering as well,
    e.g., `thresholds.suggested_threshold`.
    """

    page: object
    """Page number of paginated results."""

    per_page: float
    """Number of results to return per page"""