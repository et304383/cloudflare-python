# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasParams"]


class SchemaAPIShieldEndpointManagementGetOperationsAndFeaturesAsOpenAPISchemasParams(TypedDict, total=False):
    feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]]
    """Add feature(s) to the results.

    The feature name that is given here corresponds to the resulting feature object.
    Have a look at the top-level object description for more details on the specific
    meaning.
    """

    host: List[str]
    """Receive schema only for the given host(s)."""