# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .available_alerts import AvailableAlerts, AsyncAvailableAlerts

from ...._compat import cached_property

from .destinations.destinations import Destinations, AsyncDestinations

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .available_alerts import (
    AvailableAlerts,
    AsyncAvailableAlerts,
    AvailableAlertsWithRawResponse,
    AsyncAvailableAlertsWithRawResponse,
    AvailableAlertsWithStreamingResponse,
    AsyncAvailableAlertsWithStreamingResponse,
)
from .destinations import (
    Destinations,
    AsyncDestinations,
    DestinationsWithRawResponse,
    AsyncDestinationsWithRawResponse,
    DestinationsWithStreamingResponse,
    AsyncDestinationsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["V3", "AsyncV3"]


class V3(SyncAPIResource):
    @cached_property
    def available_alerts(self) -> AvailableAlerts:
        return AvailableAlerts(self._client)

    @cached_property
    def destinations(self) -> Destinations:
        return Destinations(self._client)

    @cached_property
    def with_raw_response(self) -> V3WithRawResponse:
        return V3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3WithStreamingResponse:
        return V3WithStreamingResponse(self)


class AsyncV3(AsyncAPIResource):
    @cached_property
    def available_alerts(self) -> AsyncAvailableAlerts:
        return AsyncAvailableAlerts(self._client)

    @cached_property
    def destinations(self) -> AsyncDestinations:
        return AsyncDestinations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3WithRawResponse:
        return AsyncV3WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3WithStreamingResponse:
        return AsyncV3WithStreamingResponse(self)


class V3WithRawResponse:
    def __init__(self, v3: V3) -> None:
        self._v3 = v3

    @cached_property
    def available_alerts(self) -> AvailableAlertsWithRawResponse:
        return AvailableAlertsWithRawResponse(self._v3.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self._v3.destinations)


class AsyncV3WithRawResponse:
    def __init__(self, v3: AsyncV3) -> None:
        self._v3 = v3

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsWithRawResponse:
        return AsyncAvailableAlertsWithRawResponse(self._v3.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self._v3.destinations)


class V3WithStreamingResponse:
    def __init__(self, v3: V3) -> None:
        self._v3 = v3

    @cached_property
    def available_alerts(self) -> AvailableAlertsWithStreamingResponse:
        return AvailableAlertsWithStreamingResponse(self._v3.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self._v3.destinations)


class AsyncV3WithStreamingResponse:
    def __init__(self, v3: AsyncV3) -> None:
        self._v3 = v3

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsWithStreamingResponse:
        return AsyncAvailableAlertsWithStreamingResponse(self._v3.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self._v3.destinations)