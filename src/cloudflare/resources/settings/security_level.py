# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import SecurityLevelUpdateResponse, SecurityLevelGetResponse

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
from ...types.settings import security_level_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SecurityLevel", "AsyncSecurityLevel"]


class SecurityLevel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityLevelWithRawResponse:
        return SecurityLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityLevelWithStreamingResponse:
        return SecurityLevelWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityLevelUpdateResponse]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            body=maybe_transform({"value": value}, security_level_update_params.SecurityLevelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevelUpdateResponse]], ResultWrapper[SecurityLevelUpdateResponse]),
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
    ) -> Optional[SecurityLevelGetResponse]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevelGetResponse]], ResultWrapper[SecurityLevelGetResponse]),
        )


class AsyncSecurityLevel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityLevelWithRawResponse:
        return AsyncSecurityLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityLevelWithStreamingResponse:
        return AsyncSecurityLevelWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SecurityLevelUpdateResponse]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            body=maybe_transform({"value": value}, security_level_update_params.SecurityLevelUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevelUpdateResponse]], ResultWrapper[SecurityLevelUpdateResponse]),
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
    ) -> Optional[SecurityLevelGetResponse]:
        """
        Choose the appropriate security profile for your website, which will
        automatically adjust each of the security settings. If you choose to customize
        an individual security setting, the profile will become Custom.
        (https://support.cloudflare.com/hc/en-us/articles/200170056).

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
            f"/zones/{zone_id}/settings/security_level",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SecurityLevelGetResponse]], ResultWrapper[SecurityLevelGetResponse]),
        )


class SecurityLevelWithRawResponse:
    def __init__(self, security_level: SecurityLevel) -> None:
        self._security_level = security_level

        self.update = to_raw_response_wrapper(
            security_level.update,
        )
        self.get = to_raw_response_wrapper(
            security_level.get,
        )


class AsyncSecurityLevelWithRawResponse:
    def __init__(self, security_level: AsyncSecurityLevel) -> None:
        self._security_level = security_level

        self.update = async_to_raw_response_wrapper(
            security_level.update,
        )
        self.get = async_to_raw_response_wrapper(
            security_level.get,
        )


class SecurityLevelWithStreamingResponse:
    def __init__(self, security_level: SecurityLevel) -> None:
        self._security_level = security_level

        self.update = to_streamed_response_wrapper(
            security_level.update,
        )
        self.get = to_streamed_response_wrapper(
            security_level.get,
        )


class AsyncSecurityLevelWithStreamingResponse:
    def __init__(self, security_level: AsyncSecurityLevel) -> None:
        self._security_level = security_level

        self.update = async_to_streamed_response_wrapper(
            security_level.update,
        )
        self.get = async_to_streamed_response_wrapper(
            security_level.get,
        )