# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZoneSettingAdvancedDDoS

__all__ = ["AdvancedDDoS", "AsyncAdvancedDDoS"]


class AdvancedDDoS(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvancedDDoSWithRawResponse:
        return AdvancedDDoSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvancedDDoSWithStreamingResponse:
        return AdvancedDDoSWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneSettingAdvancedDDoS]:
        """
        Advanced protection from Distributed Denial of Service (DDoS) attacks on your
        website. This is an uneditable value that is 'on' in the case of Business and
        Enterprise zones.

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
            f"/zones/{zone_id}/settings/advanced_ddos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingAdvancedDDoS]], ResultWrapper[ZoneSettingAdvancedDDoS]),
        )


class AsyncAdvancedDDoS(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvancedDDoSWithRawResponse:
        return AsyncAdvancedDDoSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvancedDDoSWithStreamingResponse:
        return AsyncAdvancedDDoSWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneSettingAdvancedDDoS]:
        """
        Advanced protection from Distributed Denial of Service (DDoS) attacks on your
        website. This is an uneditable value that is 'on' in the case of Business and
        Enterprise zones.

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
            f"/zones/{zone_id}/settings/advanced_ddos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingAdvancedDDoS]], ResultWrapper[ZoneSettingAdvancedDDoS]),
        )


class AdvancedDDoSWithRawResponse:
    def __init__(self, advanced_ddos: AdvancedDDoS) -> None:
        self._advanced_ddos = advanced_ddos

        self.get = to_raw_response_wrapper(
            advanced_ddos.get,
        )


class AsyncAdvancedDDoSWithRawResponse:
    def __init__(self, advanced_ddos: AsyncAdvancedDDoS) -> None:
        self._advanced_ddos = advanced_ddos

        self.get = async_to_raw_response_wrapper(
            advanced_ddos.get,
        )


class AdvancedDDoSWithStreamingResponse:
    def __init__(self, advanced_ddos: AdvancedDDoS) -> None:
        self._advanced_ddos = advanced_ddos

        self.get = to_streamed_response_wrapper(
            advanced_ddos.get,
        )


class AsyncAdvancedDDoSWithStreamingResponse:
    def __init__(self, advanced_ddos: AsyncAdvancedDDoS) -> None:
        self._advanced_ddos = advanced_ddos

        self.get = async_to_streamed_response_wrapper(
            advanced_ddos.get,
        )
