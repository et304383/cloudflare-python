# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .accounts import Accounts, AsyncAccounts

from ...._compat import cached_property

from .ips import IPs, AsyncIPs

from .zones import Zones, AsyncZones

from ....types.addresses import (
    AddressMapCreateResponse,
    AddressMapUpdateResponse,
    AddressMapListResponse,
    AddressMapDeleteResponse,
    AddressMapGetResponse,
)

from typing import Type, Optional

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
from ....types.addresses import address_map_create_params
from ....types.addresses import address_map_update_params
from .accounts import (
    Accounts,
    AsyncAccounts,
    AccountsWithRawResponse,
    AsyncAccountsWithRawResponse,
    AccountsWithStreamingResponse,
    AsyncAccountsWithStreamingResponse,
)
from .ips import (
    IPs,
    AsyncIPs,
    IPsWithRawResponse,
    AsyncIPsWithRawResponse,
    IPsWithStreamingResponse,
    AsyncIPsWithStreamingResponse,
)
from .zones import (
    Zones,
    AsyncZones,
    ZonesWithRawResponse,
    AsyncZonesWithRawResponse,
    ZonesWithStreamingResponse,
    AsyncZonesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["AddressMaps", "AsyncAddressMaps"]


class AddressMaps(SyncAPIResource):
    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._client)

    @cached_property
    def ips(self) -> IPs:
        return IPs(self._client)

    @cached_property
    def zones(self) -> Zones:
        return Zones(self._client)

    @cached_property
    def with_raw_response(self) -> AddressMapsWithRawResponse:
        return AddressMapsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressMapsWithStreamingResponse:
        return AddressMapsWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapCreateResponse:
        """
        Create a new address map under the account.

        Args:
          account_identifier: Identifier

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/addressing/address_maps",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                },
                address_map_create_params.AddressMapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapCreateResponse], ResultWrapper[AddressMapCreateResponse]),
        )

    def update(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        default_sni: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapUpdateResponse:
        """
        Modify properties of an address map owned by the account.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          default_sni: If you have legacy TLS clients which do not send the TLS server name indicator,
              then you can specify one default SNI on the map. If Cloudflare receives a TLS
              handshake from a client without an SNI, it will respond with the default SNI on
              those IPs. The default SNI can be any valid zone or subdomain owned by the
              account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

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
        return self._patch(
            f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
            body=maybe_transform(
                {
                    "default_sni": default_sni,
                    "description": description,
                    "enabled": enabled,
                },
                address_map_update_params.AddressMapUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapUpdateResponse], ResultWrapper[AddressMapUpdateResponse]),
        )

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
    ) -> Optional[AddressMapListResponse]:
        """
        List all address maps owned by the account.

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
            f"/accounts/{account_identifier}/addressing/address_maps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapListResponse]], ResultWrapper[AddressMapListResponse]),
        )

    def delete(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapDeleteResponse]:
        """Delete a particular address map owned by the account.

        An Address Map must be
        disabled before it can be deleted.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

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
        return cast(
            Optional[AddressMapDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AddressMapDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapGetResponse:
        """
        Show a particular address map owned by the account.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

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
        return self._get(
            f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapGetResponse], ResultWrapper[AddressMapGetResponse]),
        )


class AsyncAddressMaps(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._client)

    @cached_property
    def ips(self) -> AsyncIPs:
        return AsyncIPs(self._client)

    @cached_property
    def zones(self) -> AsyncZones:
        return AsyncZones(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressMapsWithRawResponse:
        return AsyncAddressMapsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressMapsWithStreamingResponse:
        return AsyncAddressMapsWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapCreateResponse:
        """
        Create a new address map under the account.

        Args:
          account_identifier: Identifier

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/addressing/address_maps",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                },
                address_map_create_params.AddressMapCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapCreateResponse], ResultWrapper[AddressMapCreateResponse]),
        )

    async def update(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        default_sni: Optional[str] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapUpdateResponse:
        """
        Modify properties of an address map owned by the account.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

          default_sni: If you have legacy TLS clients which do not send the TLS server name indicator,
              then you can specify one default SNI on the map. If Cloudflare receives a TLS
              handshake from a client without an SNI, it will respond with the default SNI on
              those IPs. The default SNI can be any valid zone or subdomain owned by the
              account.

          description: An optional description field which may be used to describe the types of IPs or
              zones on the map.

          enabled: Whether the Address Map is enabled or not. Cloudflare's DNS will not respond
              with IP addresses on an Address Map until the map is enabled.

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
        return await self._patch(
            f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
            body=maybe_transform(
                {
                    "default_sni": default_sni,
                    "description": description,
                    "enabled": enabled,
                },
                address_map_update_params.AddressMapUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapUpdateResponse], ResultWrapper[AddressMapUpdateResponse]),
        )

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
    ) -> Optional[AddressMapListResponse]:
        """
        List all address maps owned by the account.

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
            f"/accounts/{account_identifier}/addressing/address_maps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[AddressMapListResponse]], ResultWrapper[AddressMapListResponse]),
        )

    async def delete(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AddressMapDeleteResponse]:
        """Delete a particular address map owned by the account.

        An Address Map must be
        disabled before it can be deleted.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

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
        return cast(
            Optional[AddressMapDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AddressMapDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        address_map_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressMapGetResponse:
        """
        Show a particular address map owned by the account.

        Args:
          account_identifier: Identifier

          address_map_identifier: Identifier

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
        return await self._get(
            f"/accounts/{account_identifier}/addressing/address_maps/{address_map_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AddressMapGetResponse], ResultWrapper[AddressMapGetResponse]),
        )


class AddressMapsWithRawResponse:
    def __init__(self, address_maps: AddressMaps) -> None:
        self._address_maps = address_maps

        self.create = to_raw_response_wrapper(
            address_maps.create,
        )
        self.update = to_raw_response_wrapper(
            address_maps.update,
        )
        self.list = to_raw_response_wrapper(
            address_maps.list,
        )
        self.delete = to_raw_response_wrapper(
            address_maps.delete,
        )
        self.get = to_raw_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AccountsWithRawResponse:
        return AccountsWithRawResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> IPsWithRawResponse:
        return IPsWithRawResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> ZonesWithRawResponse:
        return ZonesWithRawResponse(self._address_maps.zones)


class AsyncAddressMapsWithRawResponse:
    def __init__(self, address_maps: AsyncAddressMaps) -> None:
        self._address_maps = address_maps

        self.create = async_to_raw_response_wrapper(
            address_maps.create,
        )
        self.update = async_to_raw_response_wrapper(
            address_maps.update,
        )
        self.list = async_to_raw_response_wrapper(
            address_maps.list,
        )
        self.delete = async_to_raw_response_wrapper(
            address_maps.delete,
        )
        self.get = async_to_raw_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsWithRawResponse:
        return AsyncAccountsWithRawResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> AsyncIPsWithRawResponse:
        return AsyncIPsWithRawResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> AsyncZonesWithRawResponse:
        return AsyncZonesWithRawResponse(self._address_maps.zones)


class AddressMapsWithStreamingResponse:
    def __init__(self, address_maps: AddressMaps) -> None:
        self._address_maps = address_maps

        self.create = to_streamed_response_wrapper(
            address_maps.create,
        )
        self.update = to_streamed_response_wrapper(
            address_maps.update,
        )
        self.list = to_streamed_response_wrapper(
            address_maps.list,
        )
        self.delete = to_streamed_response_wrapper(
            address_maps.delete,
        )
        self.get = to_streamed_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AccountsWithStreamingResponse:
        return AccountsWithStreamingResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> IPsWithStreamingResponse:
        return IPsWithStreamingResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> ZonesWithStreamingResponse:
        return ZonesWithStreamingResponse(self._address_maps.zones)


class AsyncAddressMapsWithStreamingResponse:
    def __init__(self, address_maps: AsyncAddressMaps) -> None:
        self._address_maps = address_maps

        self.create = async_to_streamed_response_wrapper(
            address_maps.create,
        )
        self.update = async_to_streamed_response_wrapper(
            address_maps.update,
        )
        self.list = async_to_streamed_response_wrapper(
            address_maps.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            address_maps.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            address_maps.get,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsWithStreamingResponse:
        return AsyncAccountsWithStreamingResponse(self._address_maps.accounts)

    @cached_property
    def ips(self) -> AsyncIPsWithStreamingResponse:
        return AsyncIPsWithStreamingResponse(self._address_maps.ips)

    @cached_property
    def zones(self) -> AsyncZonesWithStreamingResponse:
        return AsyncZonesWithStreamingResponse(self._address_maps.zones)