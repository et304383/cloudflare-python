# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.users.load_balancers.pools import HealthLoadBalancerPoolsPoolHealthDetailsResponse

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Health", "AsyncHealth"]


class Health(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthWithRawResponse:
        return HealthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthWithStreamingResponse:
        return HealthWithStreamingResponse(self)

    def load_balancer_pools_pool_health_details(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthLoadBalancerPoolsPoolHealthDetailsResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            HealthLoadBalancerPoolsPoolHealthDetailsResponse,
            self._get(
                f"/user/load_balancers/pools/{identifier}/health",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[HealthLoadBalancerPoolsPoolHealthDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncHealth(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthWithRawResponse:
        return AsyncHealthWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthWithStreamingResponse:
        return AsyncHealthWithStreamingResponse(self)

    async def load_balancer_pools_pool_health_details(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HealthLoadBalancerPoolsPoolHealthDetailsResponse:
        """
        Fetch the latest pool health status for a single pool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return cast(
            HealthLoadBalancerPoolsPoolHealthDetailsResponse,
            await self._get(
                f"/user/load_balancers/pools/{identifier}/health",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[HealthLoadBalancerPoolsPoolHealthDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class HealthWithRawResponse:
    def __init__(self, health: Health) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = to_raw_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class AsyncHealthWithRawResponse:
    def __init__(self, health: AsyncHealth) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = async_to_raw_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class HealthWithStreamingResponse:
    def __init__(self, health: Health) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = to_streamed_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )


class AsyncHealthWithStreamingResponse:
    def __init__(self, health: AsyncHealth) -> None:
        self._health = health

        self.load_balancer_pools_pool_health_details = async_to_streamed_response_wrapper(
            health.load_balancer_pools_pool_health_details,
        )