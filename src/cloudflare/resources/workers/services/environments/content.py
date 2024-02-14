# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.workers.services.environments import ContentUpdateResponse, content_update_params

from typing import Type, List

from ....._types import FileTypes

from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
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
from .....types.workers.services.environments import content_update_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Content", "AsyncContent"]


class Content(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentWithRawResponse:
        return ContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentWithStreamingResponse:
        return ContentWithStreamingResponse(self)

    def update(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: content_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentUpdateResponse:
        """
        Put script content from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content",
            body=maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ContentUpdateResponse], ResultWrapper[ContentUpdateResponse]),
        )

    def get(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get script content from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncContent(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentWithRawResponse:
        return AsyncContentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentWithStreamingResponse:
        return AsyncContentWithStreamingResponse(self)

    async def update(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: content_update_params.Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentUpdateResponse:
        """
        Put script content from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be
              present. This should be referenced either in the metadata as `main_module`
              (esm)/`body_part` (service worker) or as a header `CF-WORKER-MAIN-MODULE-PART`
              (esm) /`CF-WORKER-BODY-PART` (service worker) by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        body = deepcopy_minimal(
            {
                "any_part_name": any_part_name,
                "metadata": metadata,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["<any part name>", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content",
            body=maybe_transform(body, content_update_params.ContentUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ContentUpdateResponse], ResultWrapper[ContentUpdateResponse]),
        )

    async def get(
        self,
        environment_name: str,
        *,
        account_id: str,
        service_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get script content from a worker with an environment

        Args:
          account_id: Identifier

          service_name: Name of Worker to bind to

          environment_name: Optional environment if the Worker utilizes one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not service_name:
            raise ValueError(f"Expected a non-empty value for `service_name` but received {service_name!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/services/{service_name}/environments/{environment_name}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ContentWithRawResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.update = to_raw_response_wrapper(
            content.update,
        )
        self.get = to_custom_raw_response_wrapper(
            content.get,
            BinaryAPIResponse,
        )


class AsyncContentWithRawResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.update = async_to_raw_response_wrapper(
            content.update,
        )
        self.get = async_to_custom_raw_response_wrapper(
            content.get,
            AsyncBinaryAPIResponse,
        )


class ContentWithStreamingResponse:
    def __init__(self, content: Content) -> None:
        self._content = content

        self.update = to_streamed_response_wrapper(
            content.update,
        )
        self.get = to_custom_streamed_response_wrapper(
            content.get,
            StreamedBinaryAPIResponse,
        )


class AsyncContentWithStreamingResponse:
    def __init__(self, content: AsyncContent) -> None:
        self._content = content

        self.update = async_to_streamed_response_wrapper(
            content.update,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            content.get,
            AsyncStreamedBinaryAPIResponse,
        )