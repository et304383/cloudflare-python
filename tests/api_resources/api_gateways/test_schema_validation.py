# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.api_gateways.settings import APIShieldZoneSchemaValidationSettings

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import schema_validation_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemaValidation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateways.schema_validation.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        schema_validation = client.api_gateways.schema_validation.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            validation_default_mitigation_action="block",
            validation_override_mitigation_action="none",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.api_gateways.schema_validation.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = response.parse()
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.api_gateways.schema_validation.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = response.parse()
            assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.schema_validation.with_raw_response.update(
                "",
            )


class TestAsyncSchemaValidation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateways.schema_validation.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        schema_validation = await async_client.api_gateways.schema_validation.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            validation_default_mitigation_action="block",
            validation_override_mitigation_action="none",
        )
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.api_gateways.schema_validation.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema_validation = await response.parse()
        assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.api_gateways.schema_validation.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema_validation = await response.parse()
            assert_matches_type(APIShieldZoneSchemaValidationSettings, schema_validation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.schema_validation.with_raw_response.update(
                "",
            )