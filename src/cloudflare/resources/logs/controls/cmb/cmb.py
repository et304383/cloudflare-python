# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .configs import Configs, AsyncConfigs

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Cmb", "AsyncCmb"]


class Cmb(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> CmbWithRawResponse:
        return CmbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmbWithStreamingResponse:
        return CmbWithStreamingResponse(self)


class AsyncCmb(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmbWithRawResponse:
        return AsyncCmbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmbWithStreamingResponse:
        return AsyncCmbWithStreamingResponse(self)


class CmbWithRawResponse:
    def __init__(self, cmb: Cmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._cmb.configs)


class AsyncCmbWithRawResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._cmb.configs)


class CmbWithStreamingResponse:
    def __init__(self, cmb: Cmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._cmb.configs)


class AsyncCmbWithStreamingResponse:
    def __init__(self, cmb: AsyncCmb) -> None:
        self._cmb = cmb

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._cmb.configs)