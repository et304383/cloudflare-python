# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import (
    MembershipUpdateResponse,
    MembershipDeleteResponse,
    MembershipGetResponse,
    MembershipUserSAccountMembershipsListMembershipsResponse,
    membership_user_s_account_memberships_list_memberships_params,
)

from typing_extensions import Literal

from typing import Type, Optional

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import membership_update_params
from ..types import membership_user_s_account_memberships_list_memberships_params
from .._wrappers import ResultWrapper
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
from typing import cast
from typing import cast

__all__ = ["Memberships", "AsyncMemberships"]


class Memberships(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsWithRawResponse:
        return MembershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsWithStreamingResponse:
        return MembershipsWithStreamingResponse(self)

    def update(
        self,
        membership_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipUpdateResponse:
        """
        Accept or reject this account invitation.

        Args:
          membership_id: Membership identifier tag.

          status: Whether to accept or reject this account invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return cast(
            MembershipUpdateResponse,
            self._put(
                f"/memberships/{membership_id}",
                body=maybe_transform({"status": status}, membership_update_params.MembershipUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MembershipUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipDeleteResponse:
        """
        Remove the associated member from an account.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return self._delete(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MembershipDeleteResponse], ResultWrapper[MembershipDeleteResponse]),
        )

    def get(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipGetResponse:
        """
        Get a specific membership.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return cast(
            MembershipGetResponse,
            self._get(
                f"/memberships/{membership_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MembershipGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_s_account_memberships_list_memberships(
        self,
        *,
        account: membership_user_s_account_memberships_list_memberships_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "account.name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipUserSAccountMembershipsListMembershipsResponse]:
        """
        List memberships of accounts the user can access.

        Args:
          direction: Direction to order memberships.

          name: Account name

          order: Field to order memberships by.

          page: Page number of paginated results.

          per_page: Number of memberships per page.

          status: Status of this membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/memberships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    membership_user_s_account_memberships_list_memberships_params.MembershipUserSAccountMembershipsListMembershipsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MembershipUserSAccountMembershipsListMembershipsResponse]],
                ResultWrapper[MembershipUserSAccountMembershipsListMembershipsResponse],
            ),
        )


class AsyncMemberships(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsWithRawResponse:
        return AsyncMembershipsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsWithStreamingResponse:
        return AsyncMembershipsWithStreamingResponse(self)

    async def update(
        self,
        membership_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipUpdateResponse:
        """
        Accept or reject this account invitation.

        Args:
          membership_id: Membership identifier tag.

          status: Whether to accept or reject this account invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return cast(
            MembershipUpdateResponse,
            await self._put(
                f"/memberships/{membership_id}",
                body=maybe_transform({"status": status}, membership_update_params.MembershipUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MembershipUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipDeleteResponse:
        """
        Remove the associated member from an account.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return await self._delete(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[MembershipDeleteResponse], ResultWrapper[MembershipDeleteResponse]),
        )

    async def get(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipGetResponse:
        """
        Get a specific membership.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return cast(
            MembershipGetResponse,
            await self._get(
                f"/memberships/{membership_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MembershipGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_s_account_memberships_list_memberships(
        self,
        *,
        account: membership_user_s_account_memberships_list_memberships_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "account.name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipUserSAccountMembershipsListMembershipsResponse]:
        """
        List memberships of accounts the user can access.

        Args:
          direction: Direction to order memberships.

          name: Account name

          order: Field to order memberships by.

          page: Page number of paginated results.

          per_page: Number of memberships per page.

          status: Status of this membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/memberships",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    membership_user_s_account_memberships_list_memberships_params.MembershipUserSAccountMembershipsListMembershipsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[MembershipUserSAccountMembershipsListMembershipsResponse]],
                ResultWrapper[MembershipUserSAccountMembershipsListMembershipsResponse],
            ),
        )


class MembershipsWithRawResponse:
    def __init__(self, memberships: Memberships) -> None:
        self._memberships = memberships

        self.update = to_raw_response_wrapper(
            memberships.update,
        )
        self.delete = to_raw_response_wrapper(
            memberships.delete,
        )
        self.get = to_raw_response_wrapper(
            memberships.get,
        )
        self.user_s_account_memberships_list_memberships = to_raw_response_wrapper(
            memberships.user_s_account_memberships_list_memberships,
        )


class AsyncMembershipsWithRawResponse:
    def __init__(self, memberships: AsyncMemberships) -> None:
        self._memberships = memberships

        self.update = async_to_raw_response_wrapper(
            memberships.update,
        )
        self.delete = async_to_raw_response_wrapper(
            memberships.delete,
        )
        self.get = async_to_raw_response_wrapper(
            memberships.get,
        )
        self.user_s_account_memberships_list_memberships = async_to_raw_response_wrapper(
            memberships.user_s_account_memberships_list_memberships,
        )


class MembershipsWithStreamingResponse:
    def __init__(self, memberships: Memberships) -> None:
        self._memberships = memberships

        self.update = to_streamed_response_wrapper(
            memberships.update,
        )
        self.delete = to_streamed_response_wrapper(
            memberships.delete,
        )
        self.get = to_streamed_response_wrapper(
            memberships.get,
        )
        self.user_s_account_memberships_list_memberships = to_streamed_response_wrapper(
            memberships.user_s_account_memberships_list_memberships,
        )


class AsyncMembershipsWithStreamingResponse:
    def __init__(self, memberships: AsyncMemberships) -> None:
        self._memberships = memberships

        self.update = async_to_streamed_response_wrapper(
            memberships.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            memberships.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            memberships.get,
        )
        self.user_s_account_memberships_list_memberships = async_to_streamed_response_wrapper(
            memberships.user_s_account_memberships_list_memberships,
        )