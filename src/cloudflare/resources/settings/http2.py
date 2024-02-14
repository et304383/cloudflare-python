# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import HTTP2UpdateResponse, HTTP2GetResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.settings import http2_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["HTTP2", "AsyncHTTP2"]


class HTTP2(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTTP2WithRawResponse:
        return HTTP2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTTP2WithStreamingResponse:
        return HTTP2WithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTP2UpdateResponse]:
        """
        Value of the HTTP2 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP2 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/http2",
            body=maybe_transform({"value": value}, http2_update_params.HTTP2UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2UpdateResponse]], ResultWrapper[HTTP2UpdateResponse]),
        )

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
    ) -> Optional[HTTP2GetResponse]:
        """
        Value of the HTTP2 setting.

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
            f"/zones/{zone_id}/settings/http2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2GetResponse]], ResultWrapper[HTTP2GetResponse]),
        )


class AsyncHTTP2(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTTP2WithRawResponse:
        return AsyncHTTP2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTTP2WithStreamingResponse:
        return AsyncHTTP2WithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HTTP2UpdateResponse]:
        """
        Value of the HTTP2 setting.

        Args:
          zone_id: Identifier

          value: Value of the HTTP2 setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/http2",
            body=maybe_transform({"value": value}, http2_update_params.HTTP2UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2UpdateResponse]], ResultWrapper[HTTP2UpdateResponse]),
        )

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
    ) -> Optional[HTTP2GetResponse]:
        """
        Value of the HTTP2 setting.

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
            f"/zones/{zone_id}/settings/http2",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[HTTP2GetResponse]], ResultWrapper[HTTP2GetResponse]),
        )


class HTTP2WithRawResponse:
    def __init__(self, http2: HTTP2) -> None:
        self._http2 = http2

        self.update = to_raw_response_wrapper(
            http2.update,
        )
        self.get = to_raw_response_wrapper(
            http2.get,
        )


class AsyncHTTP2WithRawResponse:
    def __init__(self, http2: AsyncHTTP2) -> None:
        self._http2 = http2

        self.update = async_to_raw_response_wrapper(
            http2.update,
        )
        self.get = async_to_raw_response_wrapper(
            http2.get,
        )


class HTTP2WithStreamingResponse:
    def __init__(self, http2: HTTP2) -> None:
        self._http2 = http2

        self.update = to_streamed_response_wrapper(
            http2.update,
        )
        self.get = to_streamed_response_wrapper(
            http2.get,
        )


class AsyncHTTP2WithStreamingResponse:
    def __init__(self, http2: AsyncHTTP2) -> None:
        self._http2 = http2

        self.update = async_to_streamed_response_wrapper(
            http2.update,
        )
        self.get = async_to_streamed_response_wrapper(
            http2.get,
        )