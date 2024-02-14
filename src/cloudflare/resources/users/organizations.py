# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.users import (
    OrganizationDeleteResponse,
    OrganizationGetResponse,
    OrganizationUserSOrganizationsListOrganizationsResponse,
)

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.users import organization_user_s_organizations_list_organizations_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Organizations", "AsyncOrganizations"]


class Organizations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self)

    def delete(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationDeleteResponse:
        """
        Removes association to an organization.

        Args:
          organization_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return self._delete(
            f"/user/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDeleteResponse,
        )

    def get(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationGetResponse:
        """
        Gets a specific organization the user is associated with.

        Args:
          organization_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return cast(
            OrganizationGetResponse,
            self._get(
                f"/user/organizations/{organization_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OrganizationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_s_organizations_list_organizations(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["member", "invited"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrganizationUserSOrganizationsListOrganizationsResponse]:
        """
        Lists organizations the user is associated with.

        Args:
          direction: Direction to order organizations.

          match: Whether to match all search requirements or at least one (any).

          name: Organization name.

          order: Field to order organizations by.

          page: Page number of paginated results.

          per_page: Number of organizations per page.

          status: Whether the user is a member of the organization or has an inivitation pending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    organization_user_s_organizations_list_organizations_params.OrganizationUserSOrganizationsListOrganizationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OrganizationUserSOrganizationsListOrganizationsResponse]],
                ResultWrapper[OrganizationUserSOrganizationsListOrganizationsResponse],
            ),
        )


class AsyncOrganizations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self)

    async def delete(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationDeleteResponse:
        """
        Removes association to an organization.

        Args:
          organization_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return await self._delete(
            f"/user/organizations/{organization_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationDeleteResponse,
        )

    async def get(
        self,
        organization_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationGetResponse:
        """
        Gets a specific organization the user is associated with.

        Args:
          organization_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organization_id:
            raise ValueError(f"Expected a non-empty value for `organization_id` but received {organization_id!r}")
        return cast(
            OrganizationGetResponse,
            await self._get(
                f"/user/organizations/{organization_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OrganizationGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_s_organizations_list_organizations(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["member", "invited"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrganizationUserSOrganizationsListOrganizationsResponse]:
        """
        Lists organizations the user is associated with.

        Args:
          direction: Direction to order organizations.

          match: Whether to match all search requirements or at least one (any).

          name: Organization name.

          order: Field to order organizations by.

          page: Page number of paginated results.

          per_page: Number of organizations per page.

          status: Whether the user is a member of the organization or has an inivitation pending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/organizations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    organization_user_s_organizations_list_organizations_params.OrganizationUserSOrganizationsListOrganizationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OrganizationUserSOrganizationsListOrganizationsResponse]],
                ResultWrapper[OrganizationUserSOrganizationsListOrganizationsResponse],
            ),
        )


class OrganizationsWithRawResponse:
    def __init__(self, organizations: Organizations) -> None:
        self._organizations = organizations

        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )
        self.get = to_raw_response_wrapper(
            organizations.get,
        )
        self.user_s_organizations_list_organizations = to_raw_response_wrapper(
            organizations.user_s_organizations_list_organizations,
        )


class AsyncOrganizationsWithRawResponse:
    def __init__(self, organizations: AsyncOrganizations) -> None:
        self._organizations = organizations

        self.delete = async_to_raw_response_wrapper(
            organizations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            organizations.get,
        )
        self.user_s_organizations_list_organizations = async_to_raw_response_wrapper(
            organizations.user_s_organizations_list_organizations,
        )


class OrganizationsWithStreamingResponse:
    def __init__(self, organizations: Organizations) -> None:
        self._organizations = organizations

        self.delete = to_streamed_response_wrapper(
            organizations.delete,
        )
        self.get = to_streamed_response_wrapper(
            organizations.get,
        )
        self.user_s_organizations_list_organizations = to_streamed_response_wrapper(
            organizations.user_s_organizations_list_organizations,
        )


class AsyncOrganizationsWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizations) -> None:
        self._organizations = organizations

        self.delete = async_to_streamed_response_wrapper(
            organizations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            organizations.get,
        )
        self.user_s_organizations_list_organizations = async_to_streamed_response_wrapper(
            organizations.user_s_organizations_list_organizations,
        )