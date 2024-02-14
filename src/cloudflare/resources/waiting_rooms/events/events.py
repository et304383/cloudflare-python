# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .details import Details, AsyncDetails

from ...._compat import cached_property

from ....types.waiting_rooms import (
    EventUpdateResponse,
    EventDeleteResponse,
    EventGetResponse,
    EventWaitingRoomCreateEventResponse,
    EventWaitingRoomListEventsResponse,
)

from typing import Type, Optional

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
from ....types.waiting_rooms import event_update_params
from ....types.waiting_rooms import event_waiting_room_create_event_params
from .details import (
    Details,
    AsyncDetails,
    DetailsWithRawResponse,
    AsyncDetailsWithRawResponse,
    DetailsWithStreamingResponse,
    AsyncDetailsWithStreamingResponse,
)
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

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    @cached_property
    def details(self) -> Details:
        return Details(self._client)

    @cached_property
    def with_raw_response(self) -> EventsWithRawResponse:
        return EventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsWithStreamingResponse:
        return EventsWithStreamingResponse(self)

    def update(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventUpdateResponse:
        """
        Updates a configured event for a waiting room.

        Args:
          zone_identifier: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventUpdateResponse], ResultWrapper[EventUpdateResponse]),
        )

    def delete(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventDeleteResponse:
        """
        Deletes an event for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._delete(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventDeleteResponse], ResultWrapper[EventDeleteResponse]),
        )

    def get(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventGetResponse:
        """
        Fetches a single configured event for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventGetResponse], ResultWrapper[EventGetResponse]),
        )

    def waiting_room_create_event(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventWaitingRoomCreateEventResponse:
        """Only available for the Waiting Room Advanced subscription.

        Creates an event for
        a waiting room. An event takes place during a specified period of time,
        temporarily changing the behavior of a waiting room. While the event is active,
        some of the properties in the event's configuration may either override or
        inherit from the waiting room's configuration. Note that events cannot overlap
        with each other, so only one event can be active at a time.

        Args:
          zone_identifier: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_waiting_room_create_event_params.EventWaitingRoomCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventWaitingRoomCreateEventResponse], ResultWrapper[EventWaitingRoomCreateEventResponse]),
        )

    def waiting_room_list_events(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EventWaitingRoomListEventsResponse]:
        """
        Lists events for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EventWaitingRoomListEventsResponse]], ResultWrapper[EventWaitingRoomListEventsResponse]
            ),
        )


class AsyncEvents(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetails:
        return AsyncDetails(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        return AsyncEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsWithStreamingResponse:
        return AsyncEventsWithStreamingResponse(self)

    async def update(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventUpdateResponse:
        """
        Updates a configured event for a waiting room.

        Args:
          zone_identifier: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_update_params.EventUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventUpdateResponse], ResultWrapper[EventUpdateResponse]),
        )

    async def delete(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventDeleteResponse:
        """
        Deletes an event for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventDeleteResponse], ResultWrapper[EventDeleteResponse]),
        )

    async def get(
        self,
        event_id: object,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventGetResponse:
        """
        Fetches a single configured event for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventGetResponse], ResultWrapper[EventGetResponse]),
        )

    async def waiting_room_create_event(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        event_end_time: str,
        event_start_time: str,
        name: str,
        custom_page_html: Optional[str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        disable_session_renewal: Optional[bool] | NotGiven = NOT_GIVEN,
        new_users_per_minute: Optional[int] | NotGiven = NOT_GIVEN,
        prequeue_start_time: Optional[str] | NotGiven = NOT_GIVEN,
        queueing_method: Optional[str] | NotGiven = NOT_GIVEN,
        session_duration: Optional[int] | NotGiven = NOT_GIVEN,
        shuffle_at_event_start: bool | NotGiven = NOT_GIVEN,
        suspended: bool | NotGiven = NOT_GIVEN,
        total_active_users: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventWaitingRoomCreateEventResponse:
        """Only available for the Waiting Room Advanced subscription.

        Creates an event for
        a waiting room. An event takes place during a specified period of time,
        temporarily changing the behavior of a waiting room. While the event is active,
        some of the properties in the event's configuration may either override or
        inherit from the waiting room's configuration. Note that events cannot overlap
        with each other, so only one event can be active at a time.

        Args:
          zone_identifier: Identifier

          event_end_time: An ISO 8601 timestamp that marks the end of the event.

          event_start_time: An ISO 8601 timestamp that marks the start of the event. At this time, queued
              users will be processed with the event's configuration. The start time must be
              at least one minute before `event_end_time`.

          name: A unique name to identify the event. Only alphanumeric characters, hyphens and
              underscores are allowed.

          custom_page_html: If set, the event will override the waiting room's `custom_page_html` property
              while it is active. If null, the event will inherit it.

          description: A note that you can use to add more details about the event.

          disable_session_renewal: If set, the event will override the waiting room's `disable_session_renewal`
              property while it is active. If null, the event will inherit it.

          new_users_per_minute: If set, the event will override the waiting room's `new_users_per_minute`
              property while it is active. If null, the event will inherit it. This can only
              be set if the event's `total_active_users` property is also set.

          prequeue_start_time: An ISO 8601 timestamp that marks when to begin queueing all users before the
              event starts. The prequeue must start at least five minutes before
              `event_start_time`.

          queueing_method: If set, the event will override the waiting room's `queueing_method` property
              while it is active. If null, the event will inherit it.

          session_duration: If set, the event will override the waiting room's `session_duration` property
              while it is active. If null, the event will inherit it.

          shuffle_at_event_start: If enabled, users in the prequeue will be shuffled randomly at the
              `event_start_time`. Requires that `prequeue_start_time` is not null. This is
              useful for situations when many users will join the event prequeue at the same
              time and you want to shuffle them to ensure fairness. Naturally, it makes the
              most sense to enable this feature when the `queueing_method` during the event
              respects ordering such as **fifo**, or else the shuffling may be unnecessary.

          suspended: Suspends or allows an event. If set to `true`, the event is ignored and traffic
              will be handled based on the waiting room configuration.

          total_active_users: If set, the event will override the waiting room's `total_active_users` property
              while it is active. If null, the event will inherit it. This can only be set if
              the event's `new_users_per_minute` property is also set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events",
            body=maybe_transform(
                {
                    "event_end_time": event_end_time,
                    "event_start_time": event_start_time,
                    "name": name,
                    "custom_page_html": custom_page_html,
                    "description": description,
                    "disable_session_renewal": disable_session_renewal,
                    "new_users_per_minute": new_users_per_minute,
                    "prequeue_start_time": prequeue_start_time,
                    "queueing_method": queueing_method,
                    "session_duration": session_duration,
                    "shuffle_at_event_start": shuffle_at_event_start,
                    "suspended": suspended,
                    "total_active_users": total_active_users,
                },
                event_waiting_room_create_event_params.EventWaitingRoomCreateEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EventWaitingRoomCreateEventResponse], ResultWrapper[EventWaitingRoomCreateEventResponse]),
        )

    async def waiting_room_list_events(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EventWaitingRoomListEventsResponse]:
        """
        Lists events for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EventWaitingRoomListEventsResponse]], ResultWrapper[EventWaitingRoomListEventsResponse]
            ),
        )


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.update = to_raw_response_wrapper(
            events.update,
        )
        self.delete = to_raw_response_wrapper(
            events.delete,
        )
        self.get = to_raw_response_wrapper(
            events.get,
        )
        self.waiting_room_create_event = to_raw_response_wrapper(
            events.waiting_room_create_event,
        )
        self.waiting_room_list_events = to_raw_response_wrapper(
            events.waiting_room_list_events,
        )

    @cached_property
    def details(self) -> DetailsWithRawResponse:
        return DetailsWithRawResponse(self._events.details)


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.update = async_to_raw_response_wrapper(
            events.update,
        )
        self.delete = async_to_raw_response_wrapper(
            events.delete,
        )
        self.get = async_to_raw_response_wrapper(
            events.get,
        )
        self.waiting_room_create_event = async_to_raw_response_wrapper(
            events.waiting_room_create_event,
        )
        self.waiting_room_list_events = async_to_raw_response_wrapper(
            events.waiting_room_list_events,
        )

    @cached_property
    def details(self) -> AsyncDetailsWithRawResponse:
        return AsyncDetailsWithRawResponse(self._events.details)


class EventsWithStreamingResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.update = to_streamed_response_wrapper(
            events.update,
        )
        self.delete = to_streamed_response_wrapper(
            events.delete,
        )
        self.get = to_streamed_response_wrapper(
            events.get,
        )
        self.waiting_room_create_event = to_streamed_response_wrapper(
            events.waiting_room_create_event,
        )
        self.waiting_room_list_events = to_streamed_response_wrapper(
            events.waiting_room_list_events,
        )

    @cached_property
    def details(self) -> DetailsWithStreamingResponse:
        return DetailsWithStreamingResponse(self._events.details)


class AsyncEventsWithStreamingResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.update = async_to_streamed_response_wrapper(
            events.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            events.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            events.get,
        )
        self.waiting_room_create_event = async_to_streamed_response_wrapper(
            events.waiting_room_create_event,
        )
        self.waiting_room_list_events = async_to_streamed_response_wrapper(
            events.waiting_room_list_events,
        )

    @cached_property
    def details(self) -> AsyncDetailsWithStreamingResponse:
        return AsyncDetailsWithStreamingResponse(self._events.details)