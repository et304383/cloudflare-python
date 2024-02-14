# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel import SinkholeListResponse

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

__all__ = ["Sinkholes", "AsyncSinkholes"]


class Sinkholes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SinkholesWithRawResponse:
        return SinkholesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SinkholesWithStreamingResponse:
        return SinkholesWithStreamingResponse(self)

    def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SinkholeListResponse:
        """
        List sinkholes owned by this account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/intel/sinkholes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SinkholeListResponse], ResultWrapper[SinkholeListResponse]),
        )


class AsyncSinkholes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSinkholesWithRawResponse:
        return AsyncSinkholesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSinkholesWithStreamingResponse:
        return AsyncSinkholesWithStreamingResponse(self)

    async def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SinkholeListResponse:
        """
        List sinkholes owned by this account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/intel/sinkholes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[SinkholeListResponse], ResultWrapper[SinkholeListResponse]),
        )


class SinkholesWithRawResponse:
    def __init__(self, sinkholes: Sinkholes) -> None:
        self._sinkholes = sinkholes

        self.list = to_raw_response_wrapper(
            sinkholes.list,
        )


class AsyncSinkholesWithRawResponse:
    def __init__(self, sinkholes: AsyncSinkholes) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_raw_response_wrapper(
            sinkholes.list,
        )


class SinkholesWithStreamingResponse:
    def __init__(self, sinkholes: Sinkholes) -> None:
        self._sinkholes = sinkholes

        self.list = to_streamed_response_wrapper(
            sinkholes.list,
        )


class AsyncSinkholesWithStreamingResponse:
    def __init__(self, sinkholes: AsyncSinkholes) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_streamed_response_wrapper(
            sinkholes.list,
        )