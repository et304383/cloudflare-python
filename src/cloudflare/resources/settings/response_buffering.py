# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import ResponseBufferingUpdateResponse, ResponseBufferingGetResponse

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
from ...types.settings import response_buffering_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ResponseBuffering", "AsyncResponseBuffering"]


class ResponseBuffering(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponseBufferingWithRawResponse:
        return ResponseBufferingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponseBufferingWithStreamingResponse:
        return ResponseBufferingWithStreamingResponse(self)

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
    ) -> Optional[ResponseBufferingUpdateResponse]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/response_buffering",
            body=maybe_transform({"value": value}, response_buffering_update_params.ResponseBufferingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ResponseBufferingUpdateResponse]], ResultWrapper[ResponseBufferingUpdateResponse]
            ),
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
    ) -> Optional[ResponseBufferingGetResponse]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBufferingGetResponse]], ResultWrapper[ResponseBufferingGetResponse]),
        )


class AsyncResponseBuffering(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponseBufferingWithRawResponse:
        return AsyncResponseBufferingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponseBufferingWithStreamingResponse:
        return AsyncResponseBufferingWithStreamingResponse(self)

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
    ) -> Optional[ResponseBufferingUpdateResponse]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/response_buffering",
            body=maybe_transform({"value": value}, response_buffering_update_params.ResponseBufferingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ResponseBufferingUpdateResponse]], ResultWrapper[ResponseBufferingUpdateResponse]
            ),
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
    ) -> Optional[ResponseBufferingGetResponse]:
        """Enables or disables buffering of responses from the proxied server.

        Cloudflare
        may buffer the whole payload to deliver it at once to the client versus allowing
        it to be delivered in chunks. By default, the proxied server streams directly
        and is not buffered by Cloudflare. This is limited to Enterprise Zones.

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
            f"/zones/{zone_id}/settings/response_buffering",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ResponseBufferingGetResponse]], ResultWrapper[ResponseBufferingGetResponse]),
        )


class ResponseBufferingWithRawResponse:
    def __init__(self, response_buffering: ResponseBuffering) -> None:
        self._response_buffering = response_buffering

        self.update = to_raw_response_wrapper(
            response_buffering.update,
        )
        self.get = to_raw_response_wrapper(
            response_buffering.get,
        )


class AsyncResponseBufferingWithRawResponse:
    def __init__(self, response_buffering: AsyncResponseBuffering) -> None:
        self._response_buffering = response_buffering

        self.update = async_to_raw_response_wrapper(
            response_buffering.update,
        )
        self.get = async_to_raw_response_wrapper(
            response_buffering.get,
        )


class ResponseBufferingWithStreamingResponse:
    def __init__(self, response_buffering: ResponseBuffering) -> None:
        self._response_buffering = response_buffering

        self.update = to_streamed_response_wrapper(
            response_buffering.update,
        )
        self.get = to_streamed_response_wrapper(
            response_buffering.get,
        )


class AsyncResponseBufferingWithStreamingResponse:
    def __init__(self, response_buffering: AsyncResponseBuffering) -> None:
        self._response_buffering = response_buffering

        self.update = async_to_streamed_response_wrapper(
            response_buffering.update,
        )
        self.get = async_to_streamed_response_wrapper(
            response_buffering.get,
        )