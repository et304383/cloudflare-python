# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.magic_transit import (
    GRETunnelGetResponse,
    GRETunnelListResponse,
    GRETunnelCreateResponse,
    GRETunnelDeleteResponse,
    GRETunnelUpdateResponse,
    gre_tunnel_create_params,
    gre_tunnel_update_params,
)

__all__ = ["GRETunnels", "AsyncGRETunnels"]


class GRETunnels(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GRETunnelsWithRawResponse:
        return GRETunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GRETunnelsWithStreamingResponse:
        return GRETunnelsWithStreamingResponse(self)

    def create(
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
    ) -> GRETunnelCreateResponse:
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
            body=maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
        )

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
    ) -> GRETunnelUpdateResponse:
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
                gre_tunnel_update_params.GRETunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelUpdateResponse], ResultWrapper[GRETunnelUpdateResponse]),
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
    ) -> GRETunnelListResponse:
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
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
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
    ) -> GRETunnelDeleteResponse:
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
            cast_to=cast(Type[GRETunnelDeleteResponse], ResultWrapper[GRETunnelDeleteResponse]),
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
    ) -> GRETunnelGetResponse:
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
            cast_to=cast(Type[GRETunnelGetResponse], ResultWrapper[GRETunnelGetResponse]),
        )


class AsyncGRETunnels(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGRETunnelsWithRawResponse:
        return AsyncGRETunnelsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGRETunnelsWithStreamingResponse:
        return AsyncGRETunnelsWithStreamingResponse(self)

    async def create(
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
    ) -> GRETunnelCreateResponse:
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
            body=maybe_transform(body, gre_tunnel_create_params.GRETunnelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelCreateResponse], ResultWrapper[GRETunnelCreateResponse]),
        )

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
    ) -> GRETunnelUpdateResponse:
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
                gre_tunnel_update_params.GRETunnelUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[GRETunnelUpdateResponse], ResultWrapper[GRETunnelUpdateResponse]),
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
    ) -> GRETunnelListResponse:
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
            cast_to=cast(Type[GRETunnelListResponse], ResultWrapper[GRETunnelListResponse]),
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
    ) -> GRETunnelDeleteResponse:
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
            cast_to=cast(Type[GRETunnelDeleteResponse], ResultWrapper[GRETunnelDeleteResponse]),
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
    ) -> GRETunnelGetResponse:
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
            cast_to=cast(Type[GRETunnelGetResponse], ResultWrapper[GRETunnelGetResponse]),
        )


class GRETunnelsWithRawResponse:
    def __init__(self, gre_tunnels: GRETunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.update = to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.list = to_raw_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_raw_response_wrapper(
            gre_tunnels.get,
        )


class AsyncGRETunnelsWithRawResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_raw_response_wrapper(
            gre_tunnels.create,
        )
        self.update = async_to_raw_response_wrapper(
            gre_tunnels.update,
        )
        self.list = async_to_raw_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_raw_response_wrapper(
            gre_tunnels.get,
        )


class GRETunnelsWithStreamingResponse:
    def __init__(self, gre_tunnels: GRETunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.update = to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.list = to_streamed_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = to_streamed_response_wrapper(
            gre_tunnels.get,
        )


class AsyncGRETunnelsWithStreamingResponse:
    def __init__(self, gre_tunnels: AsyncGRETunnels) -> None:
        self._gre_tunnels = gre_tunnels

        self.create = async_to_streamed_response_wrapper(
            gre_tunnels.create,
        )
        self.update = async_to_streamed_response_wrapper(
            gre_tunnels.update,
        )
        self.list = async_to_streamed_response_wrapper(
            gre_tunnels.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gre_tunnels.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            gre_tunnels.get,
        )