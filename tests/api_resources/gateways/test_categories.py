# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.gateways import CategoryZeroTrustGatewayCategoriesListCategoriesResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_categories_list_categories(self, client: Cloudflare) -> None:
        category = client.gateways.categories.zero_trust_gateway_categories_list_categories(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_categories_list_categories(self, client: Cloudflare) -> None:
        response = client.gateways.categories.with_raw_response.zero_trust_gateway_categories_list_categories(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(
            Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_categories_list_categories(self, client: Cloudflare) -> None:
        with client.gateways.categories.with_streaming_response.zero_trust_gateway_categories_list_categories(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(
                Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zero_trust_gateway_categories_list_categories(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.gateways.categories.with_raw_response.zero_trust_gateway_categories_list_categories(
                "",
            )


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_categories_list_categories(self, async_client: AsyncCloudflare) -> None:
        category = await async_client.gateways.categories.zero_trust_gateway_categories_list_categories(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_categories_list_categories(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.gateways.categories.with_raw_response.zero_trust_gateway_categories_list_categories(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(
            Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_categories_list_categories(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.categories.with_streaming_response.zero_trust_gateway_categories_list_categories(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(
                Optional[CategoryZeroTrustGatewayCategoriesListCategoriesResponse], category, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zero_trust_gateway_categories_list_categories(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.gateways.categories.with_raw_response.zero_trust_gateway_categories_list_categories(
                "",
            )