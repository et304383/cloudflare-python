# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zones.settings import ZoneSettingBrotli, brotli_edit_params

__all__ = ["Brotli", "AsyncBrotli"]


class Brotli(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrotliWithRawResponse:
        return BrotliWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrotliWithStreamingResponse:
        return BrotliWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneSettingBrotli]:
        """
        When the client requesting an asset supports the Brotli compression algorithm,
        Cloudflare will serve a Brotli compressed version of the asset.

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
            f"/zones/{zone_id}/settings/brotli",
            body=maybe_transform({"value": value}, brotli_edit_params.BrotliEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingBrotli]], ResultWrapper[ZoneSettingBrotli]),
        )

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
    ) -> Optional[ZoneSettingBrotli]:
        """
        When the client requesting an asset supports the Brotli compression algorithm,
        Cloudflare will serve a Brotli compressed version of the asset.

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
            f"/zones/{zone_id}/settings/brotli",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingBrotli]], ResultWrapper[ZoneSettingBrotli]),
        )


class AsyncBrotli(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrotliWithRawResponse:
        return AsyncBrotliWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrotliWithStreamingResponse:
        return AsyncBrotliWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["off", "on"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZoneSettingBrotli]:
        """
        When the client requesting an asset supports the Brotli compression algorithm,
        Cloudflare will serve a Brotli compressed version of the asset.

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
            f"/zones/{zone_id}/settings/brotli",
            body=await async_maybe_transform({"value": value}, brotli_edit_params.BrotliEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingBrotli]], ResultWrapper[ZoneSettingBrotli]),
        )

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
    ) -> Optional[ZoneSettingBrotli]:
        """
        When the client requesting an asset supports the Brotli compression algorithm,
        Cloudflare will serve a Brotli compressed version of the asset.

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
            f"/zones/{zone_id}/settings/brotli",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZoneSettingBrotli]], ResultWrapper[ZoneSettingBrotli]),
        )


class BrotliWithRawResponse:
    def __init__(self, brotli: Brotli) -> None:
        self._brotli = brotli

        self.edit = to_raw_response_wrapper(
            brotli.edit,
        )
        self.get = to_raw_response_wrapper(
            brotli.get,
        )


class AsyncBrotliWithRawResponse:
    def __init__(self, brotli: AsyncBrotli) -> None:
        self._brotli = brotli

        self.edit = async_to_raw_response_wrapper(
            brotli.edit,
        )
        self.get = async_to_raw_response_wrapper(
            brotli.get,
        )


class BrotliWithStreamingResponse:
    def __init__(self, brotli: Brotli) -> None:
        self._brotli = brotli

        self.edit = to_streamed_response_wrapper(
            brotli.edit,
        )
        self.get = to_streamed_response_wrapper(
            brotli.get,
        )


class AsyncBrotliWithStreamingResponse:
    def __init__(self, brotli: AsyncBrotli) -> None:
        self._brotli = brotli

        self.edit = async_to_streamed_response_wrapper(
            brotli.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            brotli.get,
        )
