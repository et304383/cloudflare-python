# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .by_tags import ByTags, AsyncByTags

from ...._compat import cached_property

from ....types.rulesets import VersionAccountRulesetsListAnAccountRulesetSVersionsResponse, VersionGetResponse

from typing import Type

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
from .by_tags import (
    ByTags,
    AsyncByTags,
    ByTagsWithRawResponse,
    AsyncByTagsWithRawResponse,
    ByTagsWithStreamingResponse,
    AsyncByTagsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    @cached_property
    def by_tags(self) -> ByTags:
        return ByTags(self._client)

    @cached_property
    def with_raw_response(self) -> VersionsWithRawResponse:
        return VersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsWithStreamingResponse:
        return VersionsWithStreamingResponse(self)

    def delete(
        self,
        ruleset_version: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an existing version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def account_rulesets_list_an_account_ruleset_s_versions(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionAccountRulesetsListAnAccountRulesetSVersionsResponse:
        """
        Fetches the versions of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VersionAccountRulesetsListAnAccountRulesetSVersionsResponse],
                ResultWrapper[VersionAccountRulesetsListAnAccountRulesetSVersionsResponse],
            ),
        )

    def get(
        self,
        ruleset_version: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionGetResponse:
        """
        Fetches a specific version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VersionGetResponse], ResultWrapper[VersionGetResponse]),
        )


class AsyncVersions(AsyncAPIResource):
    @cached_property
    def by_tags(self) -> AsyncByTags:
        return AsyncByTags(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVersionsWithRawResponse:
        return AsyncVersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsWithStreamingResponse:
        return AsyncVersionsWithStreamingResponse(self)

    async def delete(
        self,
        ruleset_version: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an existing version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def account_rulesets_list_an_account_ruleset_s_versions(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionAccountRulesetsListAnAccountRulesetSVersionsResponse:
        """
        Fetches the versions of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[VersionAccountRulesetsListAnAccountRulesetSVersionsResponse],
                ResultWrapper[VersionAccountRulesetsListAnAccountRulesetSVersionsResponse],
            ),
        )

    async def get(
        self,
        ruleset_version: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionGetResponse:
        """
        Fetches a specific version of an account or zone ruleset.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          ruleset_version: The version of the ruleset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not ruleset_version:
            raise ValueError(f"Expected a non-empty value for `ruleset_version` but received {ruleset_version!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VersionGetResponse], ResultWrapper[VersionGetResponse]),
        )


class VersionsWithRawResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.account_rulesets_list_an_account_ruleset_s_versions = to_raw_response_wrapper(
            versions.account_rulesets_list_an_account_ruleset_s_versions,
        )
        self.get = to_raw_response_wrapper(
            versions.get,
        )

    @cached_property
    def by_tags(self) -> ByTagsWithRawResponse:
        return ByTagsWithRawResponse(self._versions.by_tags)


class AsyncVersionsWithRawResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.account_rulesets_list_an_account_ruleset_s_versions = async_to_raw_response_wrapper(
            versions.account_rulesets_list_an_account_ruleset_s_versions,
        )
        self.get = async_to_raw_response_wrapper(
            versions.get,
        )

    @cached_property
    def by_tags(self) -> AsyncByTagsWithRawResponse:
        return AsyncByTagsWithRawResponse(self._versions.by_tags)


class VersionsWithStreamingResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.account_rulesets_list_an_account_ruleset_s_versions = to_streamed_response_wrapper(
            versions.account_rulesets_list_an_account_ruleset_s_versions,
        )
        self.get = to_streamed_response_wrapper(
            versions.get,
        )

    @cached_property
    def by_tags(self) -> ByTagsWithStreamingResponse:
        return ByTagsWithStreamingResponse(self._versions.by_tags)


class AsyncVersionsWithStreamingResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.account_rulesets_list_an_account_ruleset_s_versions = async_to_streamed_response_wrapper(
            versions.account_rulesets_list_an_account_ruleset_s_versions,
        )
        self.get = async_to_streamed_response_wrapper(
            versions.get,
        )

    @cached_property
    def by_tags(self) -> AsyncByTagsWithStreamingResponse:
        return AsyncByTagsWithStreamingResponse(self._versions.by_tags)