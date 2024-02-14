# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.quality.speed import HistogramGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.quality.speed import histogram_get_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistogram:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        histogram = client.radar.quality.speed.histogram.get()
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        histogram = client.radar.quality.speed.histogram.get(
            asn=["string", "string", "string"],
            bucket_size=0,
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            location=["string", "string", "string"],
            metric_group="BANDWIDTH",
            name=["string", "string", "string"],
        )
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.radar.quality.speed.histogram.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        histogram = response.parse()
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.radar.quality.speed.histogram.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            histogram = response.parse()
            assert_matches_type(HistogramGetResponse, histogram, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistogram:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        histogram = await async_client.radar.quality.speed.histogram.get()
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        histogram = await async_client.radar.quality.speed.histogram.get(
            asn=["string", "string", "string"],
            bucket_size=0,
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            location=["string", "string", "string"],
            metric_group="BANDWIDTH",
            name=["string", "string", "string"],
        )
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.speed.histogram.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        histogram = await response.parse()
        assert_matches_type(HistogramGetResponse, histogram, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.speed.histogram.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            histogram = await response.parse()
            assert_matches_type(HistogramGetResponse, histogram, path=["response"])

        assert cast(Any, response.is_closed) is True