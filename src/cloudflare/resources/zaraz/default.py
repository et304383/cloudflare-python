# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.zaraz import DefaultGetResponse

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Default", "AsyncDefault"]


class Default(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultWithRawResponse:
        return DefaultWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultWithStreamingResponse:
        return DefaultWithStreamingResponse(self)

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGetResponse:
        """
        Gets default Zaraz configuration for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DefaultGetResponse], ResultWrapper[DefaultGetResponse]),
        )


class AsyncDefault(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultWithRawResponse:
        return AsyncDefaultWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultWithStreamingResponse:
        return AsyncDefaultWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultGetResponse:
        """
        Gets default Zaraz configuration for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/default",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DefaultGetResponse], ResultWrapper[DefaultGetResponse]),
        )


class DefaultWithRawResponse:
    def __init__(self, default: Default) -> None:
        self._default = default

        self.get = to_raw_response_wrapper(
            default.get,
        )


class AsyncDefaultWithRawResponse:
    def __init__(self, default: AsyncDefault) -> None:
        self._default = default

        self.get = async_to_raw_response_wrapper(
            default.get,
        )


class DefaultWithStreamingResponse:
    def __init__(self, default: Default) -> None:
        self._default = default

        self.get = to_streamed_response_wrapper(
            default.get,
        )


class AsyncDefaultWithStreamingResponse:
    def __init__(self, default: AsyncDefault) -> None:
        self._default = default

        self.get = async_to_streamed_response_wrapper(
            default.get,
        )