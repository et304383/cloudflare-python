# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access import (
    KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse,
    KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import key_access_key_configuration_update_the_access_key_configuration_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_key_configuration_get_the_access_key_configuration(self, client: Cloudflare) -> None:
        key = client.access.keys.access_key_configuration_get_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_key_configuration_get_the_access_key_configuration(self, client: Cloudflare) -> None:
        response = client.access.keys.with_raw_response.access_key_configuration_get_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_key_configuration_get_the_access_key_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.access.keys.with_streaming_response.access_key_configuration_get_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_key_configuration_get_the_access_key_configuration(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.keys.with_raw_response.access_key_configuration_get_the_access_key_configuration(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_key_configuration_update_the_access_key_configuration(self, client: Cloudflare) -> None:
        key = client.access.keys.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        )
        assert_matches_type(KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_key_configuration_update_the_access_key_configuration(
        self, client: Cloudflare
    ) -> None:
        response = client.access.keys.with_raw_response.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_key_configuration_update_the_access_key_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.access.keys.with_streaming_response.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(
                KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_key_configuration_update_the_access_key_configuration(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.keys.with_raw_response.access_key_configuration_update_the_access_key_configuration(
                "",
                key_rotation_interval_days=30,
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_key_configuration_get_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        key = await async_client.access.keys.access_key_configuration_get_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_key_configuration_get_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.access.keys.with_raw_response.access_key_configuration_get_the_access_key_configuration(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_key_configuration_get_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.keys.with_streaming_response.access_key_configuration_get_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyAccessKeyConfigurationGetTheAccessKeyConfigurationResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_key_configuration_get_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.keys.with_raw_response.access_key_configuration_get_the_access_key_configuration(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_key_configuration_update_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        key = await async_client.access.keys.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        )
        assert_matches_type(KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_key_configuration_update_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.keys.with_raw_response.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_key_configuration_update_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.keys.with_streaming_response.access_key_configuration_update_the_access_key_configuration(
            "023e105f4ecef8ad9ca31a8372d0c353",
            key_rotation_interval_days=30,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(
                KeyAccessKeyConfigurationUpdateTheAccessKeyConfigurationResponse, key, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_key_configuration_update_the_access_key_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await (
                async_client.access.keys.with_raw_response.access_key_configuration_update_the_access_key_configuration(
                    "",
                    key_rotation_interval_days=30,
                )
            )