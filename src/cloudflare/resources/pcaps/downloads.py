# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
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
from ..._wrappers import ResultWrapper

__all__ = ["Downloads", "AsyncDownloads"]


class Downloads(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self)

    def list(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Download PCAP information into a file.

        Response is a binary PCAP file.

        Args:
          account_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/pcaps/{identifier}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncDownloads(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self)

    async def list(
        self,
        identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Download PCAP information into a file.

        Response is a binary PCAP file.

        Args:
          account_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/pcaps/{identifier}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class DownloadsWithRawResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.list = to_custom_raw_response_wrapper(
            downloads.list,
            BinaryAPIResponse,
        )


class AsyncDownloadsWithRawResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.list = async_to_custom_raw_response_wrapper(
            downloads.list,
            AsyncBinaryAPIResponse,
        )


class DownloadsWithStreamingResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.list = to_custom_streamed_response_wrapper(
            downloads.list,
            StreamedBinaryAPIResponse,
        )


class AsyncDownloadsWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.list = async_to_custom_streamed_response_wrapper(
            downloads.list,
            AsyncStreamedBinaryAPIResponse,
        )