# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.settings import RocketLoaderUpdateResponse, RocketLoaderGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import rocket_loader_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRocketLoader:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rocket_loader = client.settings.rocket_loader.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rocket_loader = client.settings.rocket_loader.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.settings.rocket_loader.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rocket_loader = response.parse()
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.settings.rocket_loader.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rocket_loader = response.parse()
            assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.rocket_loader.with_raw_response.update(
                "",
                value={
                    "id": "rocket_loader",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rocket_loader = client.settings.rocket_loader.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.rocket_loader.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rocket_loader = response.parse()
        assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.rocket_loader.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rocket_loader = response.parse()
            assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.rocket_loader.with_raw_response.get(
                "",
            )


class TestAsyncRocketLoader:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rocket_loader = await async_client.settings.rocket_loader.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rocket_loader = await async_client.settings.rocket_loader.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.rocket_loader.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rocket_loader = await response.parse()
        assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.rocket_loader.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value={
                "id": "rocket_loader",
                "value": "on",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rocket_loader = await response.parse()
            assert_matches_type(Optional[RocketLoaderUpdateResponse], rocket_loader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.rocket_loader.with_raw_response.update(
                "",
                value={
                    "id": "rocket_loader",
                    "value": "on",
                },
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rocket_loader = await async_client.settings.rocket_loader.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.rocket_loader.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rocket_loader = await response.parse()
        assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.rocket_loader.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rocket_loader = await response.parse()
            assert_matches_type(Optional[RocketLoaderGetResponse], rocket_loader, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.rocket_loader.with_raw_response.get(
                "",
            )