# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from typing import Type

from ...types.zaraz import PublishCreateResponse

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
from ...types.zaraz import publish_create_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Publish", "AsyncPublish"]


class Publish(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PublishWithRawResponse:
        return PublishWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PublishWithStreamingResponse:
        return PublishWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Publish current Zaraz preview configuration for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz configuration description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/settings/zaraz/publish",
            body=maybe_transform(body, publish_create_params.PublishCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncPublish(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPublishWithRawResponse:
        return AsyncPublishWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPublishWithStreamingResponse:
        return AsyncPublishWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Publish current Zaraz preview configuration for a zone.

        Args:
          zone_id: Identifier

          body: Zaraz configuration description.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/settings/zaraz/publish",
            body=maybe_transform(body, publish_create_params.PublishCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class PublishWithRawResponse:
    def __init__(self, publish: Publish) -> None:
        self._publish = publish

        self.create = to_raw_response_wrapper(
            publish.create,
        )


class AsyncPublishWithRawResponse:
    def __init__(self, publish: AsyncPublish) -> None:
        self._publish = publish

        self.create = async_to_raw_response_wrapper(
            publish.create,
        )


class PublishWithStreamingResponse:
    def __init__(self, publish: Publish) -> None:
        self._publish = publish

        self.create = to_streamed_response_wrapper(
            publish.create,
        )


class AsyncPublishWithStreamingResponse:
    def __init__(self, publish: AsyncPublish) -> None:
        self._publish = publish

        self.create = async_to_streamed_response_wrapper(
            publish.create,
        )