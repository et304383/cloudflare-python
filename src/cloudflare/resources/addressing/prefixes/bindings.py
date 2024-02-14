# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.addressing.prefixes import (
    BindingCreateResponse,
    BindingListResponse,
    BindingDeleteResponse,
    BindingGetResponse,
)

from typing import Type

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
from ....types.addressing.prefixes import binding_create_params
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

__all__ = ["Bindings", "AsyncBindings"]


class Bindings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self)

    def create(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        cidr: str | NotGiven = NOT_GIVEN,
        service_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingCreateResponse:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "service_id": service_id,
                },
                binding_create_params.BindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingCreateResponse], ResultWrapper[BindingCreateResponse]),
        )

    def list(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingListResponse:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingListResponse], ResultWrapper[BindingListResponse]),
        )

    def delete(
        self,
        binding_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          binding_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not binding_identifier:
            raise ValueError(f"Expected a non-empty value for `binding_identifier` but received {binding_identifier!r}")
        return cast(
            BindingDeleteResponse,
            self._delete(
                f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BindingDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        binding_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingGetResponse:
        """
        Fetch a single Service Binding

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          binding_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not binding_identifier:
            raise ValueError(f"Expected a non-empty value for `binding_identifier` but received {binding_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingGetResponse], ResultWrapper[BindingGetResponse]),
        )


class AsyncBindings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self)

    async def create(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        cidr: str | NotGiven = NOT_GIVEN,
        service_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingCreateResponse:
        """
        Creates a new Service Binding, routing traffic to IPs within the given CIDR to a
        service running on Cloudflare's network. **Note:** This API may only be used on
        prefixes currently configured with a Magic Transit service binding, and only
        allows creating service bindings for the Cloudflare CDN or Cloudflare Spectrum.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          cidr: IP Prefix in Classless Inter-Domain Routing format.

          service_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings",
            body=maybe_transform(
                {
                    "cidr": cidr,
                    "service_id": service_id,
                },
                binding_create_params.BindingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingCreateResponse], ResultWrapper[BindingCreateResponse]),
        )

    async def list(
        self,
        prefix_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingListResponse:
        """List the Cloudflare services this prefix is currently bound to.

        Traffic sent to
        an address within an IP prefix will be routed to the Cloudflare service of the
        most-specific Service Binding matching the address. **Example:** binding
        `192.0.2.0/24` to Cloudflare Magic Transit and `192.0.2.1/32` to the Cloudflare
        CDN would route traffic for `192.0.2.1` to the CDN, and traffic for all other
        IPs in the prefix to Cloudflare Magic Transit.

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingListResponse], ResultWrapper[BindingListResponse]),
        )

    async def delete(
        self,
        binding_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingDeleteResponse:
        """
        Delete a Service Binding

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          binding_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not binding_identifier:
            raise ValueError(f"Expected a non-empty value for `binding_identifier` but received {binding_identifier!r}")
        return cast(
            BindingDeleteResponse,
            await self._delete(
                f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BindingDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        binding_identifier: str,
        *,
        account_identifier: str,
        prefix_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BindingGetResponse:
        """
        Fetch a single Service Binding

        Args:
          account_identifier: Identifier

          prefix_identifier: Identifier

          binding_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not prefix_identifier:
            raise ValueError(f"Expected a non-empty value for `prefix_identifier` but received {prefix_identifier!r}")
        if not binding_identifier:
            raise ValueError(f"Expected a non-empty value for `binding_identifier` but received {binding_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/addressing/prefixes/{prefix_identifier}/bindings/{binding_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[BindingGetResponse], ResultWrapper[BindingGetResponse]),
        )


class BindingsWithRawResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.create = to_raw_response_wrapper(
            bindings.create,
        )
        self.list = to_raw_response_wrapper(
            bindings.list,
        )
        self.delete = to_raw_response_wrapper(
            bindings.delete,
        )
        self.get = to_raw_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithRawResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.create = async_to_raw_response_wrapper(
            bindings.create,
        )
        self.list = async_to_raw_response_wrapper(
            bindings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bindings.delete,
        )
        self.get = async_to_raw_response_wrapper(
            bindings.get,
        )


class BindingsWithStreamingResponse:
    def __init__(self, bindings: Bindings) -> None:
        self._bindings = bindings

        self.create = to_streamed_response_wrapper(
            bindings.create,
        )
        self.list = to_streamed_response_wrapper(
            bindings.list,
        )
        self.delete = to_streamed_response_wrapper(
            bindings.delete,
        )
        self.get = to_streamed_response_wrapper(
            bindings.get,
        )


class AsyncBindingsWithStreamingResponse:
    def __init__(self, bindings: AsyncBindings) -> None:
        self._bindings = bindings

        self.create = async_to_streamed_response_wrapper(
            bindings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            bindings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bindings.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            bindings.get,
        )