# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.spectrums.analytics.events import SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.spectrums.analytics.events import summary_spectrum_analytics_summary_get_analytics_summary_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummaries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_analytics_summary_get_analytics_summary(self, client: Cloudflare) -> None:
        summary = client.spectrums.analytics.events.summaries.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_analytics_summary_get_analytics_summary_with_all_params(self, client: Cloudflare) -> None:
        summary = client.spectrums.analytics.events.summaries.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dimensions=["event", "appID"],
            filters="event==disconnect%20AND%20coloName!=SFO",
            metrics=["count", "bytesIngress"],
            since=parse_datetime("2014-01-02T02:20:00Z"),
            sort=["+count", "-bytesIngress"],
            until=parse_datetime("2014-01-02T03:20:00Z"),
        )
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_spectrum_analytics_summary_get_analytics_summary(self, client: Cloudflare) -> None:
        response = client.spectrums.analytics.events.summaries.with_raw_response.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_spectrum_analytics_summary_get_analytics_summary(self, client: Cloudflare) -> None:
        with client.spectrums.analytics.events.summaries.with_streaming_response.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(
                Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_spectrum_analytics_summary_get_analytics_summary(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.analytics.events.summaries.with_raw_response.spectrum_analytics_summary_get_analytics_summary(
                "",
            )


class TestAsyncSummaries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_analytics_summary_get_analytics_summary(self, async_client: AsyncCloudflare) -> None:
        summary = (
            await async_client.spectrums.analytics.events.summaries.spectrum_analytics_summary_get_analytics_summary(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_analytics_summary_get_analytics_summary_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        summary = (
            await async_client.spectrums.analytics.events.summaries.spectrum_analytics_summary_get_analytics_summary(
                "023e105f4ecef8ad9ca31a8372d0c353",
                dimensions=["event", "appID"],
                filters="event==disconnect%20AND%20coloName!=SFO",
                metrics=["count", "bytesIngress"],
                since=parse_datetime("2014-01-02T02:20:00Z"),
                sort=["+count", "-bytesIngress"],
                until=parse_datetime("2014-01-02T03:20:00Z"),
            )
        )
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_spectrum_analytics_summary_get_analytics_summary(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.spectrums.analytics.events.summaries.with_raw_response.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(
            Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_spectrum_analytics_summary_get_analytics_summary(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.spectrums.analytics.events.summaries.with_streaming_response.spectrum_analytics_summary_get_analytics_summary(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(
                Optional[SummarySpectrumAnalyticsSummaryGetAnalyticsSummaryResponse], summary, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_spectrum_analytics_summary_get_analytics_summary(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.analytics.events.summaries.with_raw_response.spectrum_analytics_summary_get_analytics_summary(
                "",
            )