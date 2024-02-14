# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.settings import H2PrioritizationUpdateResponse, H2PrioritizationGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import h2_prioritization_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestH2Prioritization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        h2_prioritization = client.settings.h2_prioritization.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        h2_prioritization = client.settings.h2_prioritization.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.settings.h2_prioritization.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h2_prioritization = response.parse()
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.settings.h2_prioritization.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h2_prioritization = response.parse()
            assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.h2_prioritization.with_raw_response.update(
                "",
                value={
                    "id": "h2_prioritization",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        h2_prioritization = client.settings.h2_prioritization.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.h2_prioritization.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h2_prioritization = response.parse()
        assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.h2_prioritization.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h2_prioritization = response.parse()
            assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.h2_prioritization.with_raw_response.get(
                "",
            )


class TestAsyncH2Prioritization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        h2_prioritization = await async_client.settings.h2_prioritization.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        h2_prioritization = await async_client.settings.h2_prioritization.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.h2_prioritization.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h2_prioritization = await response.parse()
        assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.h2_prioritization.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "h2_prioritization",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h2_prioritization = await response.parse()
            assert_matches_type(Optional[H2PrioritizationUpdateResponse], h2_prioritization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.h2_prioritization.with_raw_response.update(
                "",
                value={
                    "id": "h2_prioritization",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        h2_prioritization = await async_client.settings.h2_prioritization.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.h2_prioritization.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        h2_prioritization = await response.parse()
        assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.h2_prioritization.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            h2_prioritization = await response.parse()
            assert_matches_type(Optional[H2PrioritizationGetResponse], h2_prioritization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.h2_prioritization.with_raw_response.get(
                "",
            )