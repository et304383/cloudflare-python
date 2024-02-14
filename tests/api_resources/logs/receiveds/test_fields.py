# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.logs.receiveds import FieldLogsReceivedListFieldsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_logs_received_list_fields(self, client: Cloudflare) -> None:
        field = client.logs.receiveds.fields.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_logs_received_list_fields(self, client: Cloudflare) -> None:
        response = client.logs.receiveds.fields.with_raw_response.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_logs_received_list_fields(self, client: Cloudflare) -> None:
        with client.logs.receiveds.fields.with_streaming_response.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_logs_received_list_fields(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.logs.receiveds.fields.with_raw_response.logs_received_list_fields(
                "",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_logs_received_list_fields(self, async_client: AsyncCloudflare) -> None:
        field = await async_client.logs.receiveds.fields.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_logs_received_list_fields(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.receiveds.fields.with_raw_response.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_logs_received_list_fields(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.receiveds.fields.with_streaming_response.logs_received_list_fields(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldLogsReceivedListFieldsResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_logs_received_list_fields(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.logs.receiveds.fields.with_raw_response.logs_received_list_fields(
                "",
            )