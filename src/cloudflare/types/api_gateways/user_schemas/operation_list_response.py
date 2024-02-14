# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "OperationListResponse",
    "OperationListResponseItem",
    "OperationListResponseItemAPIShieldOperation",
    "OperationListResponseItemAPIShieldOperationFeatures",
    "OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholds",
    "OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds",
    "OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas",
    "OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas",
    "OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas",
    "OperationListResponseItemAPIShieldBasicOperation",
]


class OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds(BaseModel):
    auth_id_tokens: Optional[int] = None
    """The total number of auth-ids seen across this calculation."""

    data_points: Optional[int] = None
    """The number of data points used for the threshold suggestion calculation."""

    last_updated: Optional[datetime] = None

    p50: Optional[int] = None
    """The p50 quantile of requests (in period_seconds)."""

    p90: Optional[int] = None
    """The p90 quantile of requests (in period_seconds)."""

    p99: Optional[int] = None
    """The p99 quantile of requests (in period_seconds)."""

    period_seconds: Optional[int] = None
    """The period over which this threshold is suggested."""

    requests: Optional[int] = None
    """The estimated number of requests covered by these calculations."""

    suggested_threshold: Optional[int] = None
    """The suggested threshold in requests done by the same auth_id or period_seconds."""


class OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholds(BaseModel):
    thresholds: Optional[
        OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds
    ] = None


class OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas(
    BaseModel
):
    parameters: Optional[List[object]] = None
    """An array containing the learned parameter schemas."""

    responses: Optional[object] = None
    """An empty response object.

    This field is required to yield a valid operation schema.
    """


class OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas(
    BaseModel
):
    last_updated: Optional[datetime] = None

    parameter_schemas: Optional[
        OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas
    ] = None
    """An operation schema object containing a response."""


class OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas(BaseModel):
    parameter_schemas: OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas


OperationListResponseItemAPIShieldOperationFeatures = Union[
    OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureThresholds,
    OperationListResponseItemAPIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas,
]


class OperationListResponseItemAPIShieldOperation(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    last_updated: datetime

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""

    operation_id: str
    """UUID identifier"""

    features: Optional[OperationListResponseItemAPIShieldOperationFeatures] = None


class OperationListResponseItemAPIShieldBasicOperation(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""


OperationListResponseItem = Union[
    OperationListResponseItemAPIShieldOperation, OperationListResponseItemAPIShieldBasicOperation
]

OperationListResponse = List[OperationListResponseItem]