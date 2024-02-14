# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.stream import (
    ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse,
    clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params,
)

from typing import Type, List

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
from ...types.stream import clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Clips", "AsyncClips"]


class Clips(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClipsWithRawResponse:
        return ClipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClipsWithStreamingResponse:
        return ClipsWithStreamingResponse(self)

    def stream_video_clipping_clip_videos_given_a_start_and_end_time(
        self,
        account_id: str,
        *,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params.Watermark
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse:
        """
        Clips a video based on the specified start and end times provided in seconds.

        Args:
          account_id: The account identifier tag.

          clipped_from_video_uid: The unique video identifier (UID).

          end_time_seconds: Specifies the end time for the video clip in seconds.

          start_time_seconds: Specifies the start time for the video clip in seconds.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

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
            f"/accounts/{account_id}/stream/clip",
            body=maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "require_signed_urls": require_signed_urls,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params.ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse],
                ResultWrapper[ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse],
            ),
        )


class AsyncClips(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClipsWithRawResponse:
        return AsyncClipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClipsWithStreamingResponse:
        return AsyncClipsWithStreamingResponse(self)

    async def stream_video_clipping_clip_videos_given_a_start_and_end_time(
        self,
        account_id: str,
        *,
        clipped_from_video_uid: str,
        end_time_seconds: int,
        start_time_seconds: int,
        allowed_origins: List[str] | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        max_duration_seconds: int | NotGiven = NOT_GIVEN,
        require_signed_urls: bool | NotGiven = NOT_GIVEN,
        thumbnail_timestamp_pct: float | NotGiven = NOT_GIVEN,
        watermark: clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params.Watermark
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse:
        """
        Clips a video based on the specified start and end times provided in seconds.

        Args:
          account_id: The account identifier tag.

          clipped_from_video_uid: The unique video identifier (UID).

          end_time_seconds: Specifies the end time for the video clip in seconds.

          start_time_seconds: Specifies the start time for the video clip in seconds.

          allowed_origins: Lists the origins allowed to display the video. Enter allowed origin domains in
              an array and use `*` for wildcard subdomains. Empty arrays allow the video to be
              viewed on any origin.

          creator: A user-defined identifier for the media creator.

          max_duration_seconds: The maximum duration in seconds for a video upload. Can be set for a video that
              is not yet uploaded to limit its duration. Uploads that exceed the specified
              duration will fail during processing. A value of `-1` means the value is
              unknown.

          require_signed_urls: Indicates whether the video can be a accessed using the UID. When set to `true`,
              a signed token must be generated with a signing key to view the video.

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
            f"/accounts/{account_id}/stream/clip",
            body=maybe_transform(
                {
                    "clipped_from_video_uid": clipped_from_video_uid,
                    "end_time_seconds": end_time_seconds,
                    "start_time_seconds": start_time_seconds,
                    "allowed_origins": allowed_origins,
                    "creator": creator,
                    "max_duration_seconds": max_duration_seconds,
                    "require_signed_urls": require_signed_urls,
                    "thumbnail_timestamp_pct": thumbnail_timestamp_pct,
                    "watermark": watermark,
                },
                clip_stream_video_clipping_clip_videos_given_a_start_and_end_time_params.ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse],
                ResultWrapper[ClipStreamVideoClippingClipVideosGivenAStartAndEndTimeResponse],
            ),
        )


class ClipsWithRawResponse:
    def __init__(self, clips: Clips) -> None:
        self._clips = clips

        self.stream_video_clipping_clip_videos_given_a_start_and_end_time = to_raw_response_wrapper(
            clips.stream_video_clipping_clip_videos_given_a_start_and_end_time,
        )


class AsyncClipsWithRawResponse:
    def __init__(self, clips: AsyncClips) -> None:
        self._clips = clips

        self.stream_video_clipping_clip_videos_given_a_start_and_end_time = async_to_raw_response_wrapper(
            clips.stream_video_clipping_clip_videos_given_a_start_and_end_time,
        )


class ClipsWithStreamingResponse:
    def __init__(self, clips: Clips) -> None:
        self._clips = clips

        self.stream_video_clipping_clip_videos_given_a_start_and_end_time = to_streamed_response_wrapper(
            clips.stream_video_clipping_clip_videos_given_a_start_and_end_time,
        )


class AsyncClipsWithStreamingResponse:
    def __init__(self, clips: AsyncClips) -> None:
        self._clips = clips

        self.stream_video_clipping_clip_videos_given_a_start_and_end_time = async_to_streamed_response_wrapper(
            clips.stream_video_clipping_clip_videos_given_a_start_and_end_time,
        )