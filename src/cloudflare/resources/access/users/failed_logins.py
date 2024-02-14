# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.access.users import FailedLoginZeroTrustUsersGetFailedLoginsResponse

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["FailedLogins", "AsyncFailedLogins"]


class FailedLogins(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FailedLoginsWithRawResponse:
        return FailedLoginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FailedLoginsWithStreamingResponse:
        return FailedLoginsWithStreamingResponse(self)

    def zero_trust_users_get_failed_logins(
        self,
        id: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse]:
        """
        Get all failed login attempts for a single user.

        Args:
          identifier: Identifier

          id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{identifier}/access/users/{id}/failed_logins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse]],
                ResultWrapper[FailedLoginZeroTrustUsersGetFailedLoginsResponse],
            ),
        )


class AsyncFailedLogins(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFailedLoginsWithRawResponse:
        return AsyncFailedLoginsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFailedLoginsWithStreamingResponse:
        return AsyncFailedLoginsWithStreamingResponse(self)

    async def zero_trust_users_get_failed_logins(
        self,
        id: str,
        *,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse]:
        """
        Get all failed login attempts for a single user.

        Args:
          identifier: Identifier

          id: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{identifier}/access/users/{id}/failed_logins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse]],
                ResultWrapper[FailedLoginZeroTrustUsersGetFailedLoginsResponse],
            ),
        )


class FailedLoginsWithRawResponse:
    def __init__(self, failed_logins: FailedLogins) -> None:
        self._failed_logins = failed_logins

        self.zero_trust_users_get_failed_logins = to_raw_response_wrapper(
            failed_logins.zero_trust_users_get_failed_logins,
        )


class AsyncFailedLoginsWithRawResponse:
    def __init__(self, failed_logins: AsyncFailedLogins) -> None:
        self._failed_logins = failed_logins

        self.zero_trust_users_get_failed_logins = async_to_raw_response_wrapper(
            failed_logins.zero_trust_users_get_failed_logins,
        )


class FailedLoginsWithStreamingResponse:
    def __init__(self, failed_logins: FailedLogins) -> None:
        self._failed_logins = failed_logins

        self.zero_trust_users_get_failed_logins = to_streamed_response_wrapper(
            failed_logins.zero_trust_users_get_failed_logins,
        )


class AsyncFailedLoginsWithStreamingResponse:
    def __init__(self, failed_logins: AsyncFailedLogins) -> None:
        self._failed_logins = failed_logins

        self.zero_trust_users_get_failed_logins = async_to_streamed_response_wrapper(
            failed_logins.zero_trust_users_get_failed_logins,
        )