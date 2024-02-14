# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.analytics import ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.analytics import colo_zone_analytics_deprecated_get_analytics_by_co_locations_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestColo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_analytics_deprecated_get_analytics_by_co_locations(self, client: Cloudflare) -> None:
        colo = client.analytics.colo.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_analytics_deprecated_get_analytics_by_co_locations_with_all_params(
        self, client: Cloudflare
    ) -> None:
        colo = client.analytics.colo.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
            continuous=True,
            since="2015-01-01T12:23:00Z",
            until="2015-01-02T12:23:00Z",
        )
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_analytics_deprecated_get_analytics_by_co_locations(self, client: Cloudflare) -> None:
        response = client.analytics.colo.with_raw_response.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = response.parse()
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_analytics_deprecated_get_analytics_by_co_locations(
        self, client: Cloudflare
    ) -> None:
        with client.analytics.colo.with_streaming_response.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = response.parse()
            assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_analytics_deprecated_get_analytics_by_co_locations(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.analytics.colo.with_raw_response.zone_analytics_deprecated_get_analytics_by_co_locations(
                "",
            )


class TestAsyncColo:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_analytics_deprecated_get_analytics_by_co_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        colo = await async_client.analytics.colo.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_analytics_deprecated_get_analytics_by_co_locations_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        colo = await async_client.analytics.colo.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
            continuous=True,
            since="2015-01-01T12:23:00Z",
            until="2015-01-02T12:23:00Z",
        )
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_analytics_deprecated_get_analytics_by_co_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.analytics.colo.with_raw_response.zone_analytics_deprecated_get_analytics_by_co_locations(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        colo = await response.parse()
        assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_analytics_deprecated_get_analytics_by_co_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.analytics.colo.with_streaming_response.zone_analytics_deprecated_get_analytics_by_co_locations(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            colo = await response.parse()
            assert_matches_type(ColoZoneAnalyticsDeprecatedGetAnalyticsByCoLocationsResponse, colo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_analytics_deprecated_get_analytics_by_co_locations(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.analytics.colo.with_raw_response.zone_analytics_deprecated_get_analytics_by_co_locations(
                "",
            )