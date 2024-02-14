# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.workers.deployments.by_scripts import DetailGetResponse

from typing import Type

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

__all__ = ["Details", "AsyncDetails"]


class Details(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsWithRawResponse:
        return DetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsWithStreamingResponse:
        return DetailsWithStreamingResponse(self)

    def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        script_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailGetResponse:
        """
        Get Deployment Detail

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DetailGetResponse], ResultWrapper[DetailGetResponse]),
        )


class AsyncDetails(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsWithRawResponse:
        return AsyncDetailsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsWithStreamingResponse:
        return AsyncDetailsWithStreamingResponse(self)

    async def get(
        self,
        deployment_id: str,
        *,
        account_id: str,
        script_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailGetResponse:
        """
        Get Deployment Detail

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_id:
            raise ValueError(f"Expected a non-empty value for `script_id` but received {script_id!r}")
        if not deployment_id:
            raise ValueError(f"Expected a non-empty value for `deployment_id` but received {deployment_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/deployments/by-script/{script_id}/detail/{deployment_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DetailGetResponse], ResultWrapper[DetailGetResponse]),
        )


class DetailsWithRawResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.get = to_raw_response_wrapper(
            details.get,
        )


class AsyncDetailsWithRawResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.get = async_to_raw_response_wrapper(
            details.get,
        )


class DetailsWithStreamingResponse:
    def __init__(self, details: Details) -> None:
        self._details = details

        self.get = to_streamed_response_wrapper(
            details.get,
        )


class AsyncDetailsWithStreamingResponse:
    def __init__(self, details: AsyncDetails) -> None:
        self._details = details

        self.get = async_to_streamed_response_wrapper(
            details.get,
        )