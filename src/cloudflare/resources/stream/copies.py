# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    CopyStreamVideosUploadVideosFromAURLResponse,
    copy_stream_videos_upload_videos_from_a_url_params,
)

from typing import Type, List, Union

from datetime import datetime

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
from ...types.stream import copy_stream_videos_upload_videos_from_a_url_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Copies", "AsyncCopies"]


class Copies(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CopiesWithRawResponse:
        return CopiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopiesWithStreamingResponse:
        return CopiesWithStreamingResponse(self)

    def stream_videos_upload_videos_from_a_url(
        self,
        account_id: str,
        *,
        url: str,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: copy_stream_videos_upload_videos_from_a_url_params.Watermark | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CopyStreamVideosUploadVideosFromAURLResponse:
        """
        Uploads a video to Stream from a provided URL.

        Args:
          account_id: The account identifier tag.

          url: A video's URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/stream/copy",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                copy_stream_videos_upload_videos_from_a_url_params.CopyStreamVideosUploadVideosFromAURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CopyStreamVideosUploadVideosFromAURLResponse],
                ResultWrapper[CopyStreamVideosUploadVideosFromAURLResponse],
            ),
        )


class AsyncCopies(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCopiesWithRawResponse:
        return AsyncCopiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopiesWithStreamingResponse:
        return AsyncCopiesWithStreamingResponse(self)

    async def stream_videos_upload_videos_from_a_url(
        self,
        account_id: str,
        *,
        url: str,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        meta: object | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        scheduled_deletion: Union[str, datetime] | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: copy_stream_videos_upload_videos_from_a_url_params.Watermark | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CopyStreamVideosUploadVideosFromAURLResponse:
        """
        Uploads a video to Stream from a provided URL.

        Args:
          account_id: The account identifier tag.

          url: A video's URL. The server must be publicly routable and support `HTTP HEAD`
              requests and `HTTP GET` range requests. The server should respond to `HTTP HEAD`
              requests with a `content-range` header that includes the size of the file.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          meta: A user modifiable key-value store used to reference other systems of record for
              managing videos.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

          scheduled_deletion: Indicates the date and time at which the video will be deleted. Omit the field
              to indicate no change, or include with a `null` value to remove an existing
              scheduled deletion. If specified, must be at least 30 days from upload time.

          thumbnail_timestamp_pct: The timestamp for a thumbnail image calculated as a percentage value of the
              video's duration. To convert from a second-wise timestamp to a percentage,
              divide the desired timestamp by the total duration of the video. If this value
              is not set, the default thumbnail image is taken from 0s of the video.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/copy",
            body=maybe_transform(
                {
                    "url": url,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "meta": meta,
                    "require_signed_urls": require_signed_urls,
                    "scheduled_deletion": scheduled_deletion,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                copy_stream_videos_upload_videos_from_a_url_params.CopyStreamVideosUploadVideosFromAURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CopyStreamVideosUploadVideosFromAURLResponse],
                ResultWrapper[CopyStreamVideosUploadVideosFromAURLResponse],
            ),
        )


class CopiesWithRawResponse:
    def __init__(self, copies: Copies) -> None:
        self._copies = copies

        self.stream_videos_upload_videos_from_a_url = to_raw_response_wrapper(
            copies.stream_videos_upload_videos_from_a_url,
        )


class AsyncCopiesWithRawResponse:
    def __init__(self, copies: AsyncCopies) -> None:
        self._copies = copies

        self.stream_videos_upload_videos_from_a_url = async_to_raw_response_wrapper(
            copies.stream_videos_upload_videos_from_a_url,
        )


class CopiesWithStreamingResponse:
    def __init__(self, copies: Copies) -> None:
        self._copies = copies

        self.stream_videos_upload_videos_from_a_url = to_streamed_response_wrapper(
            copies.stream_videos_upload_videos_from_a_url,
        )


class AsyncCopiesWithStreamingResponse:
    def __init__(self, copies: AsyncCopies) -> None:
        self._copies = copies

        self.stream_videos_upload_videos_from_a_url = async_to_streamed_response_wrapper(
            copies.stream_videos_upload_videos_from_a_url,
        )