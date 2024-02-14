# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types import RateLimitUpdateResponse, RateLimitListResponse, RateLimitGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import rate_limit_update_params
from cloudflare.types import rate_limit_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRateLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rate_limit = client.rate_limits.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rate_limits.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rate_limits.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = response.parse()
            assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.rate_limits.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rate_limits.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rate_limit = client.rate_limits.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rate_limit = client.rate_limits.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rate_limits.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rate_limits.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = response.parse()
            assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.rate_limits.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rate_limit = client.rate_limits.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rate_limits.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = response.parse()
        assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rate_limits.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = response.parse()
            assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.rate_limits.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rate_limits.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRateLimits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rate_limit = await async_client.rate_limits.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rate_limits.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rate_limits.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = await response.parse()
            assert_matches_type(Optional[RateLimitUpdateResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.rate_limits.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rate_limits.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rate_limit = await async_client.rate_limits.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rate_limit = await async_client.rate_limits.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rate_limits.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rate_limits.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = await response.parse()
            assert_matches_type(Optional[RateLimitListResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.rate_limits.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rate_limit = await async_client.rate_limits.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rate_limits.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rate_limit = await response.parse()
        assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rate_limits.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rate_limit = await response.parse()
            assert_matches_type(Optional[RateLimitGetResponse], rate_limit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.rate_limits.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rate_limits.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )