# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .bulks import Bulks, AsyncBulks

from ...._compat import cached_property

from ....types.intels import DomainDomainIntelligenceGetDomainDetailsResponse

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
from ....types.intels import domain_domain_intelligence_get_domain_details_params
from .bulks import (
    Bulks,
    AsyncBulks,
    BulksWithRawResponse,
    AsyncBulksWithRawResponse,
    BulksWithStreamingResponse,
    AsyncBulksWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Domains", "AsyncDomains"]


class Domains(SyncAPIResource):
    @cached_property
    def bulks(self) -> Bulks:
        return Bulks(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsWithRawResponse:
        return DomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsWithStreamingResponse:
        return DomainsWithStreamingResponse(self)

    def domain_intelligence_get_domain_details(
        self,
        account_id: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainDomainIntelligenceGetDomainDetailsResponse:
        """
        Get Domain Details

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain},
                    domain_domain_intelligence_get_domain_details_params.DomainDomainIntelligenceGetDomainDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainDomainIntelligenceGetDomainDetailsResponse],
                ResultWrapper[DomainDomainIntelligenceGetDomainDetailsResponse],
            ),
        )


class AsyncDomains(AsyncAPIResource):
    @cached_property
    def bulks(self) -> AsyncBulks:
        return AsyncBulks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsWithRawResponse:
        return AsyncDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsWithStreamingResponse:
        return AsyncDomainsWithStreamingResponse(self)

    async def domain_intelligence_get_domain_details(
        self,
        account_id: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainDomainIntelligenceGetDomainDetailsResponse:
        """
        Get Domain Details

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/domain",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"domain": domain},
                    domain_domain_intelligence_get_domain_details_params.DomainDomainIntelligenceGetDomainDetailsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[DomainDomainIntelligenceGetDomainDetailsResponse],
                ResultWrapper[DomainDomainIntelligenceGetDomainDetailsResponse],
            ),
        )


class DomainsWithRawResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.domain_intelligence_get_domain_details = to_raw_response_wrapper(
            domains.domain_intelligence_get_domain_details,
        )

    @cached_property
    def bulks(self) -> BulksWithRawResponse:
        return BulksWithRawResponse(self._domains.bulks)


class AsyncDomainsWithRawResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.domain_intelligence_get_domain_details = async_to_raw_response_wrapper(
            domains.domain_intelligence_get_domain_details,
        )

    @cached_property
    def bulks(self) -> AsyncBulksWithRawResponse:
        return AsyncBulksWithRawResponse(self._domains.bulks)


class DomainsWithStreamingResponse:
    def __init__(self, domains: Domains) -> None:
        self._domains = domains

        self.domain_intelligence_get_domain_details = to_streamed_response_wrapper(
            domains.domain_intelligence_get_domain_details,
        )

    @cached_property
    def bulks(self) -> BulksWithStreamingResponse:
        return BulksWithStreamingResponse(self._domains.bulks)


class AsyncDomainsWithStreamingResponse:
    def __init__(self, domains: AsyncDomains) -> None:
        self._domains = domains

        self.domain_intelligence_get_domain_details = async_to_streamed_response_wrapper(
            domains.domain_intelligence_get_domain_details,
        )

    @cached_property
    def bulks(self) -> AsyncBulksWithStreamingResponse:
        return AsyncBulksWithStreamingResponse(self._domains.bulks)