# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.waiting_rooms import PreviewCreateResponse

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
from ...types.waiting_rooms import preview_create_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Previews", "AsyncPreviews"]


class Previews(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self)

    def create(
        self,
        zone_identifier: str,
        *,
        custom_html: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewCreateResponse:
        """Creates a waiting room page preview.

        Upload a custom waiting room page for
        preview. You will receive a preview URL in the form
        `http://waitingrooms.dev/preview/<uuid>`. You can use the following query
        parameters to change the state of the preview:

        1. `force_queue`: Boolean indicating if all users will be queued in the waiting
           room and no one will be let into the origin website (also known as queueAll).
        2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently
           full and not accepting new users at the moment.
        3. `queueing_method`: The queueing method currently used by the waiting room.
           - **fifo** indicates a FIFO queue.
           - **random** indicates a Random queue.
           - **passthrough** indicates a Passthrough queue. Keep in mind that the
             waiting room page will only be displayed if `force_queue=true` or
             `event=prequeueing` — for other cases the request will pass through to the
             origin. For our preview, this will be a fake origin website returning
             "Welcome".
           - **reject** indicates a Reject queue.
        4. `event`: Used to preview a waiting room event.
           - **none** indicates no event is occurring.
           - **prequeueing** indicates that an event is prequeueing (between
             `prequeue_start_time` and `event_start_time`).
           - **started** indicates that an event has started (between `event_start_time`
             and `event_end_time`).
        5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users
           in the prequeue when it starts. This can only be set to **true** if an event
           is active (`event` is not **none**).

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6.
        `waitTime`: Non-zero, positive integer indicating the estimated wait time in
        minutes. The default value is 10 minutes.

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated
        wait time as 50 minutes.

        Args:
          zone_identifier: Identifier

          custom_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/waiting_rooms/preview",
            body=maybe_transform({"custom_html": custom_html}, preview_create_params.PreviewCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewCreateResponse], ResultWrapper[PreviewCreateResponse]),
        )


class AsyncPreviews(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self)

    async def create(
        self,
        zone_identifier: str,
        *,
        custom_html: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewCreateResponse:
        """Creates a waiting room page preview.

        Upload a custom waiting room page for
        preview. You will receive a preview URL in the form
        `http://waitingrooms.dev/preview/<uuid>`. You can use the following query
        parameters to change the state of the preview:

        1. `force_queue`: Boolean indicating if all users will be queued in the waiting
           room and no one will be let into the origin website (also known as queueAll).
        2. `queue_is_full`: Boolean indicating if the waiting room's queue is currently
           full and not accepting new users at the moment.
        3. `queueing_method`: The queueing method currently used by the waiting room.
           - **fifo** indicates a FIFO queue.
           - **random** indicates a Random queue.
           - **passthrough** indicates a Passthrough queue. Keep in mind that the
             waiting room page will only be displayed if `force_queue=true` or
             `event=prequeueing` — for other cases the request will pass through to the
             origin. For our preview, this will be a fake origin website returning
             "Welcome".
           - **reject** indicates a Reject queue.
        4. `event`: Used to preview a waiting room event.
           - **none** indicates no event is occurring.
           - **prequeueing** indicates that an event is prequeueing (between
             `prequeue_start_time` and `event_start_time`).
           - **started** indicates that an event has started (between `event_start_time`
             and `event_end_time`).
        5. `shuffle_at_event_start`: Boolean indicating if the event will shuffle users
           in the prequeue when it starts. This can only be set to **true** if an event
           is active (`event` is not **none**).

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?force_queue=false&queue_is_full=false&queueing_method=random&event=started&shuffle_at_event_start=true` 6.
        `waitTime`: Non-zero, positive integer indicating the estimated wait time in
        minutes. The default value is 10 minutes.

        For example, you can make a request to
        `http://waitingrooms.dev/preview/<uuid>?waitTime=50` to configure the estimated
        wait time as 50 minutes.

        Args:
          zone_identifier: Identifier

          custom_html: Only available for the Waiting Room Advanced subscription. This is a template
              html file that will be rendered at the edge. If no custom_page_html is provided,
              the default waiting room will be used. The template is based on mustache (
              https://mustache.github.io/ ). There are several variables that are evaluated by
              the Cloudflare edge:

              1. {{`waitTimeKnown`}} Acts like a boolean value that indicates the behavior to
                 take when wait time is not available, for instance when queue_all is
                 **true**.
              2. {{`waitTimeFormatted`}} Estimated wait time for the user. For example, five
                 minutes. Alternatively, you can use:
              3. {{`waitTime`}} Number of minutes of estimated wait for a user.
              4. {{`waitTimeHours`}} Number of hours of estimated wait for a user
                 (`Math.floor(waitTime/60)`).
              5. {{`waitTimeHourMinutes`}} Number of minutes above the `waitTimeHours` value
                 (`waitTime%60`).
              6. {{`queueIsFull`}} Changes to **true** when no more people can be added to the
                 queue.

              To view the full list of variables, look at the `cfWaitingRoom` object described
              under the `json_response_enabled` property in other Waiting Room API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/waiting_rooms/preview",
            body=maybe_transform({"custom_html": custom_html}, preview_create_params.PreviewCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PreviewCreateResponse], ResultWrapper[PreviewCreateResponse]),
        )


class PreviewsWithRawResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.create = to_raw_response_wrapper(
            previews.create,
        )


class AsyncPreviewsWithRawResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.create = async_to_raw_response_wrapper(
            previews.create,
        )


class PreviewsWithStreamingResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.create = to_streamed_response_wrapper(
            previews.create,
        )


class AsyncPreviewsWithStreamingResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.create = async_to_streamed_response_wrapper(
            previews.create,
        )