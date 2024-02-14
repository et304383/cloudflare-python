# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .iqi.iqi import Iqi, AsyncIqi

from ...._compat import cached_property

from .speed.speed import Speed, AsyncSpeed

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
from .iqi import (
    Iqi,
    AsyncIqi,
    IqiWithRawResponse,
    AsyncIqiWithRawResponse,
    IqiWithStreamingResponse,
    AsyncIqiWithStreamingResponse,
)
from .speed import (
    Speed,
    AsyncSpeed,
    SpeedWithRawResponse,
    AsyncSpeedWithRawResponse,
    SpeedWithStreamingResponse,
    AsyncSpeedWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Quality", "AsyncQuality"]


class Quality(SyncAPIResource):
    @cached_property
    def iqi(self) -> Iqi:
        return Iqi(self._client)

    @cached_property
    def speed(self) -> Speed:
        return Speed(self._client)

    @cached_property
    def with_raw_response(self) -> QualityWithRawResponse:
        return QualityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QualityWithStreamingResponse:
        return QualityWithStreamingResponse(self)


class AsyncQuality(AsyncAPIResource):
    @cached_property
    def iqi(self) -> AsyncIqi:
        return AsyncIqi(self._client)

    @cached_property
    def speed(self) -> AsyncSpeed:
        return AsyncSpeed(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncQualityWithRawResponse:
        return AsyncQualityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQualityWithStreamingResponse:
        return AsyncQualityWithStreamingResponse(self)


class QualityWithRawResponse:
    def __init__(self, quality: Quality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IqiWithRawResponse:
        return IqiWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedWithRawResponse:
        return SpeedWithRawResponse(self._quality.speed)


class AsyncQualityWithRawResponse:
    def __init__(self, quality: AsyncQuality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIqiWithRawResponse:
        return AsyncIqiWithRawResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedWithRawResponse:
        return AsyncSpeedWithRawResponse(self._quality.speed)


class QualityWithStreamingResponse:
    def __init__(self, quality: Quality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> IqiWithStreamingResponse:
        return IqiWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> SpeedWithStreamingResponse:
        return SpeedWithStreamingResponse(self._quality.speed)


class AsyncQualityWithStreamingResponse:
    def __init__(self, quality: AsyncQuality) -> None:
        self._quality = quality

    @cached_property
    def iqi(self) -> AsyncIqiWithStreamingResponse:
        return AsyncIqiWithStreamingResponse(self._quality.iqi)

    @cached_property
    def speed(self) -> AsyncSpeedWithStreamingResponse:
        return AsyncSpeedWithStreamingResponse(self._quality.speed)