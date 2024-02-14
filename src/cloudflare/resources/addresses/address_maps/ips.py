# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.addresses.address_maps import IPUpdateResponse, IPDeleteResponse

from typing import Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["IPs", "AsyncIPs"]


class IPs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self)

    def update(
        self,
        ip_address: str,
        *,
        account_identifier: str,
        address_map_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPUpdateResponse]:
        """
        Add an IP from a prefix owned by the account to a particular address map.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not address_map_identifier:
            raise ValueError(
                f"Expected a non-empty value for `address_map_identifier` but received {address_map_identifier!r}"
            )
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return cast(
            Optional[IPUpdateResponse],
            self._put(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        ip_address: str,
        *,
        account_identifier: str,
        address_map_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPDeleteResponse]:
        """
        Remove an IP from a particular address map.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not address_map_identifier:
            raise ValueError(
                f"Expected a non-empty value for `address_map_identifier` but received {address_map_identifier!r}"
            )
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return cast(
            Optional[IPDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncIPs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self)

    async def update(
        self,
        ip_address: str,
        *,
        account_identifier: str,
        address_map_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPUpdateResponse]:
        """
        Add an IP from a prefix owned by the account to a particular address map.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not address_map_identifier:
            raise ValueError(
                f"Expected a non-empty value for `address_map_identifier` but received {address_map_identifier!r}"
            )
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return cast(
            Optional[IPUpdateResponse],
            await self._put(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        ip_address: str,
        *,
        account_identifier: str,
        address_map_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IPDeleteResponse]:
        """
        Remove an IP from a particular address map.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          ip_address: An IPv4 or IPv6 address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not address_map_identifier:
            raise ValueError(
                f"Expected a non-empty value for `address_map_identifier` but received {address_map_identifier!r}"
            )
        if not ip_address:
            raise ValueError(f"Expected a non-empty value for `ip_address` but received {ip_address!r}")
        return cast(
            Optional[IPDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}/ips/{ip_address}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IPDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class IPsWithRawResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.update = to_raw_response_wrapper(
            ips.update,
        )
        self.delete = to_raw_response_wrapper(
            ips.delete,
        )


class AsyncIPsWithRawResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.update = async_to_raw_response_wrapper(
            ips.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ips.delete,
        )


class IPsWithStreamingResponse:
    def __init__(self, ips: IPs) -> None:
        self._ips = ips

        self.update = to_streamed_response_wrapper(
            ips.update,
        )
        self.delete = to_streamed_response_wrapper(
            ips.delete,
        )


class AsyncIPsWithStreamingResponse:
    def __init__(self, ips: AsyncIPs) -> None:
        self._ips = ips

        self.update = async_to_streamed_response_wrapper(
            ips.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ips.delete,
        )