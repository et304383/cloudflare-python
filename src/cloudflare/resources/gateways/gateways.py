# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from .lists import (
    Lists,
    AsyncLists,
    ListsWithRawResponse,
    AsyncListsWithRawResponse,
    ListsWithStreamingResponse,
    AsyncListsWithStreamingResponse,
)
from .rules import (
    Rules,
    AsyncRules,
    RulesWithRawResponse,
    AsyncRulesWithRawResponse,
    RulesWithStreamingResponse,
    AsyncRulesWithStreamingResponse,
)
from ...types import (
    GatewayZeroTrustAccountsCreateZeroTrustAccountResponse,
    GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .loggings import (
    Loggings,
    AsyncLoggings,
    LoggingsWithRawResponse,
    AsyncLoggingsWithRawResponse,
    LoggingsWithStreamingResponse,
    AsyncLoggingsWithStreamingResponse,
)
from ..._compat import cached_property
from .app_types import (
    AppTypes,
    AsyncAppTypes,
    AppTypesWithRawResponse,
    AsyncAppTypesWithRawResponse,
    AppTypesWithStreamingResponse,
    AsyncAppTypesWithStreamingResponse,
)
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
)
from .categories import (
    Categories,
    AsyncCategories,
    CategoriesWithRawResponse,
    AsyncCategoriesWithRawResponse,
    CategoriesWithStreamingResponse,
    AsyncCategoriesWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .lists.lists import Lists, AsyncLists
from ..._base_client import (
    make_request_options,
)
from .configurations import (
    Configurations,
    AsyncConfigurations,
    ConfigurationsWithRawResponse,
    AsyncConfigurationsWithRawResponse,
    ConfigurationsWithStreamingResponse,
    AsyncConfigurationsWithStreamingResponse,
)
from .proxy_endpoints import (
    ProxyEndpoints,
    AsyncProxyEndpoints,
    ProxyEndpointsWithRawResponse,
    AsyncProxyEndpointsWithRawResponse,
    ProxyEndpointsWithStreamingResponse,
    AsyncProxyEndpointsWithStreamingResponse,
)

__all__ = ["Gateways", "AsyncGateways"]


class Gateways(SyncAPIResource):
    @cached_property
    def categories(self) -> Categories:
        return Categories(self._client)

    @cached_property
    def app_types(self) -> AppTypes:
        return AppTypes(self._client)

    @cached_property
    def configurations(self) -> Configurations:
        return Configurations(self._client)

    @cached_property
    def lists(self) -> Lists:
        return Lists(self._client)

    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def loggings(self) -> Loggings:
        return Loggings(self._client)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpoints:
        return ProxyEndpoints(self._client)

    @cached_property
    def rules(self) -> Rules:
        return Rules(self._client)

    @cached_property
    def with_raw_response(self) -> GatewaysWithRawResponse:
        return GatewaysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewaysWithStreamingResponse:
        return GatewaysWithStreamingResponse(self)

    def zero_trust_accounts_create_zero_trust_account(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayZeroTrustAccountsCreateZeroTrustAccountResponse:
        """
        Creates a Zero Trust account with an existing Cloudflare account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GatewayZeroTrustAccountsCreateZeroTrustAccountResponse],
                ResultWrapper[GatewayZeroTrustAccountsCreateZeroTrustAccountResponse],
            ),
        )

    def zero_trust_accounts_get_zero_trust_account_information(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse:
        """
        Gets information about the current Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse],
                ResultWrapper[GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse],
            ),
        )


class AsyncGateways(AsyncAPIResource):
    @cached_property
    def categories(self) -> AsyncCategories:
        return AsyncCategories(self._client)

    @cached_property
    def app_types(self) -> AsyncAppTypes:
        return AsyncAppTypes(self._client)

    @cached_property
    def configurations(self) -> AsyncConfigurations:
        return AsyncConfigurations(self._client)

    @cached_property
    def lists(self) -> AsyncLists:
        return AsyncLists(self._client)

    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def loggings(self) -> AsyncLoggings:
        return AsyncLoggings(self._client)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpoints:
        return AsyncProxyEndpoints(self._client)

    @cached_property
    def rules(self) -> AsyncRules:
        return AsyncRules(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGatewaysWithRawResponse:
        return AsyncGatewaysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewaysWithStreamingResponse:
        return AsyncGatewaysWithStreamingResponse(self)

    async def zero_trust_accounts_create_zero_trust_account(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayZeroTrustAccountsCreateZeroTrustAccountResponse:
        """
        Creates a Zero Trust account with an existing Cloudflare account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GatewayZeroTrustAccountsCreateZeroTrustAccountResponse],
                ResultWrapper[GatewayZeroTrustAccountsCreateZeroTrustAccountResponse],
            ),
        )

    async def zero_trust_accounts_get_zero_trust_account_information(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse:
        """
        Gets information about the current Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse],
                ResultWrapper[GatewayZeroTrustAccountsGetZeroTrustAccountInformationResponse],
            ),
        )


class GatewaysWithRawResponse:
    def __init__(self, gateways: Gateways) -> None:
        self._gateways = gateways

        self.zero_trust_accounts_create_zero_trust_account = to_raw_response_wrapper(
            gateways.zero_trust_accounts_create_zero_trust_account,
        )
        self.zero_trust_accounts_get_zero_trust_account_information = to_raw_response_wrapper(
            gateways.zero_trust_accounts_get_zero_trust_account_information,
        )

    @cached_property
    def categories(self) -> CategoriesWithRawResponse:
        return CategoriesWithRawResponse(self._gateways.categories)

    @cached_property
    def app_types(self) -> AppTypesWithRawResponse:
        return AppTypesWithRawResponse(self._gateways.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self._gateways.configurations)

    @cached_property
    def lists(self) -> ListsWithRawResponse:
        return ListsWithRawResponse(self._gateways.lists)

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._gateways.locations)

    @cached_property
    def loggings(self) -> LoggingsWithRawResponse:
        return LoggingsWithRawResponse(self._gateways.loggings)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsWithRawResponse:
        return ProxyEndpointsWithRawResponse(self._gateways.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self._gateways.rules)


class AsyncGatewaysWithRawResponse:
    def __init__(self, gateways: AsyncGateways) -> None:
        self._gateways = gateways

        self.zero_trust_accounts_create_zero_trust_account = async_to_raw_response_wrapper(
            gateways.zero_trust_accounts_create_zero_trust_account,
        )
        self.zero_trust_accounts_get_zero_trust_account_information = async_to_raw_response_wrapper(
            gateways.zero_trust_accounts_get_zero_trust_account_information,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesWithRawResponse:
        return AsyncCategoriesWithRawResponse(self._gateways.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesWithRawResponse:
        return AsyncAppTypesWithRawResponse(self._gateways.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self._gateways.configurations)

    @cached_property
    def lists(self) -> AsyncListsWithRawResponse:
        return AsyncListsWithRawResponse(self._gateways.lists)

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._gateways.locations)

    @cached_property
    def loggings(self) -> AsyncLoggingsWithRawResponse:
        return AsyncLoggingsWithRawResponse(self._gateways.loggings)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsWithRawResponse:
        return AsyncProxyEndpointsWithRawResponse(self._gateways.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self._gateways.rules)


class GatewaysWithStreamingResponse:
    def __init__(self, gateways: Gateways) -> None:
        self._gateways = gateways

        self.zero_trust_accounts_create_zero_trust_account = to_streamed_response_wrapper(
            gateways.zero_trust_accounts_create_zero_trust_account,
        )
        self.zero_trust_accounts_get_zero_trust_account_information = to_streamed_response_wrapper(
            gateways.zero_trust_accounts_get_zero_trust_account_information,
        )

    @cached_property
    def categories(self) -> CategoriesWithStreamingResponse:
        return CategoriesWithStreamingResponse(self._gateways.categories)

    @cached_property
    def app_types(self) -> AppTypesWithStreamingResponse:
        return AppTypesWithStreamingResponse(self._gateways.app_types)

    @cached_property
    def configurations(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self._gateways.configurations)

    @cached_property
    def lists(self) -> ListsWithStreamingResponse:
        return ListsWithStreamingResponse(self._gateways.lists)

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._gateways.locations)

    @cached_property
    def loggings(self) -> LoggingsWithStreamingResponse:
        return LoggingsWithStreamingResponse(self._gateways.loggings)

    @cached_property
    def proxy_endpoints(self) -> ProxyEndpointsWithStreamingResponse:
        return ProxyEndpointsWithStreamingResponse(self._gateways.proxy_endpoints)

    @cached_property
    def rules(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self._gateways.rules)


class AsyncGatewaysWithStreamingResponse:
    def __init__(self, gateways: AsyncGateways) -> None:
        self._gateways = gateways

        self.zero_trust_accounts_create_zero_trust_account = async_to_streamed_response_wrapper(
            gateways.zero_trust_accounts_create_zero_trust_account,
        )
        self.zero_trust_accounts_get_zero_trust_account_information = async_to_streamed_response_wrapper(
            gateways.zero_trust_accounts_get_zero_trust_account_information,
        )

    @cached_property
    def categories(self) -> AsyncCategoriesWithStreamingResponse:
        return AsyncCategoriesWithStreamingResponse(self._gateways.categories)

    @cached_property
    def app_types(self) -> AsyncAppTypesWithStreamingResponse:
        return AsyncAppTypesWithStreamingResponse(self._gateways.app_types)

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self._gateways.configurations)

    @cached_property
    def lists(self) -> AsyncListsWithStreamingResponse:
        return AsyncListsWithStreamingResponse(self._gateways.lists)

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._gateways.locations)

    @cached_property
    def loggings(self) -> AsyncLoggingsWithStreamingResponse:
        return AsyncLoggingsWithStreamingResponse(self._gateways.loggings)

    @cached_property
    def proxy_endpoints(self) -> AsyncProxyEndpointsWithStreamingResponse:
        return AsyncProxyEndpointsWithStreamingResponse(self._gateways.proxy_endpoints)

    @cached_property
    def rules(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self._gateways.rules)
