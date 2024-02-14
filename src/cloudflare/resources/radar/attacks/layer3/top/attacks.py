# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ......_compat import cached_property

from ......types.radar.attacks.layer3.top import AttackListResponse

from typing import Type, List, Union

from datetime import datetime

from typing_extensions import Literal

from ......_response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from ......types.radar.attacks.layer3.top import attack_list_params
from ......_wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Attacks", "AsyncAttacks"]


class Attacks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttacksWithRawResponse:
        return AttacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttacksWithStreamingResponse:
        return AttacksWithStreamingResponse(self)

    def list(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        limit_per_location: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttackListResponse:
        """Get the top attacks from origin to target location.

        Values are a percentage out
        of the total layer 3 attacks (with billing country). You can optionally limit
        the number of attacks per origin/target location (useful if all the top attacks
        are from or to the same location).

        Args:
          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          limit_direction: Array of attack origin/target location attack limits. Together with
              `limitPerLocation`, limits how many objects will be fetched per origin/target
              location.

          limit_per_location: Limit the number of attacks per origin/target (refer to `limitDirection`
              parameter) location.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer3/top/attacks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "limit_direction": limit_direction,
                        "limit_per_location": limit_per_location,
                        "location": location,
                        "name": name,
                        "protocol": protocol,
                    },
                    attack_list_params.AttackListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AttackListResponse], ResultWrapper[AttackListResponse]),
        )


class AsyncAttacks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttacksWithRawResponse:
        return AsyncAttacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttacksWithStreamingResponse:
        return AsyncAttacksWithStreamingResponse(self)

    async def list(
        self,
        *,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        limit_direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        limit_per_location: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttackListResponse:
        """Get the top attacks from origin to target location.

        Values are a percentage out
        of the total layer 3 attacks (with billing country). You can optionally limit
        the number of attacks per origin/target location (useful if all the top attacks
        are from or to the same location).

        Args:
          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit: Limit the number of objects in the response.

          limit_direction: Array of attack origin/target location attack limits. Together with
              `limitPerLocation`, limits how many objects will be fetched per origin/target
              location.

          limit_per_location: Limit the number of attacks per origin/target (refer to `limitDirection`
              parameter) location.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer3/top/attacks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "ip_version": ip_version,
                        "limit": limit,
                        "limit_direction": limit_direction,
                        "limit_per_location": limit_per_location,
                        "location": location,
                        "name": name,
                        "protocol": protocol,
                    },
                    attack_list_params.AttackListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[AttackListResponse], ResultWrapper[AttackListResponse]),
        )


class AttacksWithRawResponse:
    def __init__(self, attacks: Attacks) -> None:
        self._attacks = attacks

        self.list = to_raw_response_wrapper(
            attacks.list,
        )


class AsyncAttacksWithRawResponse:
    def __init__(self, attacks: AsyncAttacks) -> None:
        self._attacks = attacks

        self.list = async_to_raw_response_wrapper(
            attacks.list,
        )


class AttacksWithStreamingResponse:
    def __init__(self, attacks: Attacks) -> None:
        self._attacks = attacks

        self.list = to_streamed_response_wrapper(
            attacks.list,
        )


class AsyncAttacksWithStreamingResponse:
    def __init__(self, attacks: AsyncAttacks) -> None:
        self._attacks = attacks

        self.list = async_to_streamed_response_wrapper(
            attacks.list,
        )