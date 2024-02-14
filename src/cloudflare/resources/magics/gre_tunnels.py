# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.magics import (
    GreTunnelUpdateResponse,
    GreTunnelDeleteResponse,
    GreTunnelGetResponse,
    GreTunnelMagicGreTunnelsCreateGreTunnelsResponse,
    GreTunnelMagicGreTunnelsListGreTunnelsResponse,
    GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse,
    gre_tunnel_update_params,
)

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
from ...types.magics import gre_tunnel_update_params
from ...types.magics import gre_tunnel_magic_gre_tunnels_create_gre_tunnels_params
from ...types.magics import gre_tunnel_magic_gre_tunnels_update_multiple_gre_tunnels_params
from ..._wrappers import ResultWrapper
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

__all__ = ["GreTunnels", "AsyncGreTunnels"]


class GreTunnels(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreTunnelsWithRawResponse:
        return GreTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreTunnelsWithStreamingResponse:
        return GreTunnelsWithStreamingResponse(self)

    def update(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        cloudflare_gre_endpoint: str,
        customer_gre_endpoint: str,
        interface_address: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        health_check: gre_tunnel_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        mtu: int | NotGiven = NOT_GIVEN,
        ttl: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelUpdateResponse:
        """Updates a specific GRE tunnel.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          cloudflare_gre_endpoint: The IP address assigned to the Cloudflare side of the GRE tunnel.

          customer_gre_endpoint: The IP address assigned to the customer side of the GRE tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the tunnel. The name cannot contain spaces or special characters,
              must be 15 characters or less, and cannot share a name with another GRE tunnel.

          description: An optional description of the GRE tunnel.

          mtu: Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value
              is 576.

          ttl: Time To Live (TTL) in number of hops of the GRE tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            body=maybe_transform(
                {
                    "cloudflare_gre_endpoint": cloudflare_gre_endpoint,
                    "customer_gre_endpoint": customer_gre_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "description": description,
                    "health_check": health_check,
                    "mtu": mtu,
                    "ttl": ttl,
                },
                gre_tunnel_update_params.GreTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelUpdateResponse], ResultWrapper[GreTunnelUpdateResponse]),
        )

    def delete(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelDeleteResponse:
        """Disables and removes a specific static GRE tunnel.

        Use `?validate_only=true` as
        an optional query parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._delete(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelDeleteResponse], ResultWrapper[GreTunnelDeleteResponse]),
        )

    def get(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelGetResponse:
        """
        Lists informtion for a specific GRE tunnel.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelGetResponse], ResultWrapper[GreTunnelGetResponse]),
        )

    def magic_gre_tunnels_create_gre_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsCreateGreTunnelsResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            body=maybe_transform(
                body,
                gre_tunnel_magic_gre_tunnels_create_gre_tunnels_params.GreTunnelMagicGreTunnelsCreateGreTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsCreateGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsCreateGreTunnelsResponse],
            ),
        )

    def magic_gre_tunnels_list_gre_tunnels(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsListGreTunnelsResponse:
        """
        Lists GRE tunnels associated with an account.

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
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsListGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsListGreTunnelsResponse],
            ),
        )

    def magic_gre_tunnels_update_multiple_gre_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse:
        """Updates multiple GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._put(
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            body=maybe_transform(
                body,
                gre_tunnel_magic_gre_tunnels_update_multiple_gre_tunnels_params.GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse],
            ),
        )


class AsyncGreTunnels(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreTunnelsWithRawResponse:
        return AsyncGreTunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreTunnelsWithStreamingResponse:
        return AsyncGreTunnelsWithStreamingResponse(self)

    async def update(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        cloudflare_gre_endpoint: str,
        customer_gre_endpoint: str,
        interface_address: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        health_check: gre_tunnel_update_params.HealthCheck | NotGiven = NOT_GIVEN,
        mtu: int | NotGiven = NOT_GIVEN,
        ttl: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelUpdateResponse:
        """Updates a specific GRE tunnel.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          cloudflare_gre_endpoint: The IP address assigned to the Cloudflare side of the GRE tunnel.

          customer_gre_endpoint: The IP address assigned to the customer side of the GRE tunnel.

          interface_address: A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
              of the tunnel. Select the subnet from the following private IP space:
              10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.

          name: The name of the tunnel. The name cannot contain spaces or special characters,
              must be 15 characters or less, and cannot share a name with another GRE tunnel.

          description: An optional description of the GRE tunnel.

          mtu: Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value
              is 576.

          ttl: Time To Live (TTL) in number of hops of the GRE tunnel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            body=maybe_transform(
                {
                    "cloudflare_gre_endpoint": cloudflare_gre_endpoint,
                    "customer_gre_endpoint": customer_gre_endpoint,
                    "interface_address": interface_address,
                    "name": name,
                    "description": description,
                    "health_check": health_check,
                    "mtu": mtu,
                    "ttl": ttl,
                },
                gre_tunnel_update_params.GreTunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelUpdateResponse], ResultWrapper[GreTunnelUpdateResponse]),
        )

    async def delete(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelDeleteResponse:
        """Disables and removes a specific static GRE tunnel.

        Use `?validate_only=true` as
        an optional query parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelDeleteResponse], ResultWrapper[GreTunnelDeleteResponse]),
        )

    async def get(
        self,
        tunnel_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelGetResponse:
        """
        Lists informtion for a specific GRE tunnel.

        Args:
          account_identifier: Identifier

          tunnel_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not tunnel_identifier:
            raise ValueError(f"Expected a non-empty value for `tunnel_identifier` but received {tunnel_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/magic/gre_tunnels/{tunnel_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GreTunnelGetResponse], ResultWrapper[GreTunnelGetResponse]),
        )

    async def magic_gre_tunnels_create_gre_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsCreateGreTunnelsResponse:
        """Creates new GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            body=maybe_transform(
                body,
                gre_tunnel_magic_gre_tunnels_create_gre_tunnels_params.GreTunnelMagicGreTunnelsCreateGreTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsCreateGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsCreateGreTunnelsResponse],
            ),
        )

    async def magic_gre_tunnels_list_gre_tunnels(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsListGreTunnelsResponse:
        """
        Lists GRE tunnels associated with an account.

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
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsListGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsListGreTunnelsResponse],
            ),
        )

    async def magic_gre_tunnels_update_multiple_gre_tunnels(
        self,
        account_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse:
        """Updates multiple GRE tunnels.

        Use `?validate_only=true` as an optional query
        parameter to only run validation without persisting changes.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._put(
            f"/accounts/{account_identifier}/magic/gre_tunnels",
            body=maybe_transform(
                body,
                gre_tunnel_magic_gre_tunnels_update_multiple_gre_tunnels_params.GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse],
                ResultWrapper[GreTunnelMagicGreTunnelsUpdateMultipleGreTunnelsResponse],
            ),
        )


class GreTunnelsWithRawResponse:
    def __init__(self, gre_tunnels: GreTunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.update = to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.delete = to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_raw_response_wrapper(
            gre_tunnels.get,
        )
        self.magic_gre_tunnels_create_gre_tunnels = to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_create_gre_tunnels,
        )
        self.magic_gre_tunnels_list_gre_tunnels = to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_list_gre_tunnels,
        )
        self.magic_gre_tunnels_update_multiple_gre_tunnels = to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels,
        )


class AsyncGreTunnelsWithRawResponse:
    def __init__(self, gre_tunnels: AsyncGreTunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.update = async_to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.delete = async_to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            gre_tunnels.get,
        )
        self.magic_gre_tunnels_create_gre_tunnels = async_to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_create_gre_tunnels,
        )
        self.magic_gre_tunnels_list_gre_tunnels = async_to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_list_gre_tunnels,
        )
        self.magic_gre_tunnels_update_multiple_gre_tunnels = async_to_raw_response_wrapper(
            gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels,
        )


class GreTunnelsWithStreamingResponse:
    def __init__(self, gre_tunnels: GreTunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.update = to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.delete = to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_streamed_response_wrapper(
            gre_tunnels.get,
        )
        self.magic_gre_tunnels_create_gre_tunnels = to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_create_gre_tunnels,
        )
        self.magic_gre_tunnels_list_gre_tunnels = to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_list_gre_tunnels,
        )
        self.magic_gre_tunnels_update_multiple_gre_tunnels = to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels,
        )


class AsyncGreTunnelsWithStreamingResponse:
    def __init__(self, gre_tunnels: AsyncGreTunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.update = async_to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            gre_tunnels.get,
        )
        self.magic_gre_tunnels_create_gre_tunnels = async_to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_create_gre_tunnels,
        )
        self.magic_gre_tunnels_list_gre_tunnels = async_to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_list_gre_tunnels,
        )
        self.magic_gre_tunnels_update_multiple_gre_tunnels = async_to_streamed_response_wrapper(
            gre_tunnels.magic_gre_tunnels_update_multiple_gre_tunnels,
        )