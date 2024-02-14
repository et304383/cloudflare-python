# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.alerting.v3.destinations import (
    PagerdutyCreateTokenResponse,
    PagerdutyDeleteAllResponse,
    PagerdutyLinkResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPagerduty:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_token(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.v3.destinations.pagerduty.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_token(self, client: Cloudflare) -> None:
        response = client.alerting.v3.destinations.pagerduty.with_raw_response.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_token(self, client: Cloudflare) -> None:
        with client.alerting.v3.destinations.pagerduty.with_streaming_response.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_token(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3.destinations.pagerduty.with_raw_response.create_token(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_all(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.v3.destinations.pagerduty.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_all(self, client: Cloudflare) -> None:
        response = client.alerting.v3.destinations.pagerduty.with_raw_response.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_all(self, client: Cloudflare) -> None:
        with client.alerting.v3.destinations.pagerduty.with_streaming_response.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_all(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3.destinations.pagerduty.with_raw_response.delete_all(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_link(self, client: Cloudflare) -> None:
        pagerduty = client.alerting.v3.destinations.pagerduty.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_link(self, client: Cloudflare) -> None:
        response = client.alerting.v3.destinations.pagerduty.with_raw_response.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_link(self, client: Cloudflare) -> None:
        with client.alerting.v3.destinations.pagerduty.with_streaming_response.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_link(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3.destinations.pagerduty.with_raw_response.link(
                "8c71e667571b4f61b94d9e4b12158038",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.alerting.v3.destinations.pagerduty.with_raw_response.link(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPagerduty:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_token(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.v3.destinations.pagerduty.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3.destinations.pagerduty.with_raw_response.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3.destinations.pagerduty.with_streaming_response.create_token(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(PagerdutyCreateTokenResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_token(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3.destinations.pagerduty.with_raw_response.create_token(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.v3.destinations.pagerduty.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3.destinations.pagerduty.with_raw_response.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3.destinations.pagerduty.with_streaming_response.delete_all(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(Optional[PagerdutyDeleteAllResponse], pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3.destinations.pagerduty.with_raw_response.delete_all(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_link(self, async_client: AsyncCloudflare) -> None:
        pagerduty = await async_client.alerting.v3.destinations.pagerduty.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3.destinations.pagerduty.with_raw_response.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3.destinations.pagerduty.with_streaming_response.link(
            "8c71e667571b4f61b94d9e4b12158038",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(PagerdutyLinkResponse, pagerduty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_link(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3.destinations.pagerduty.with_raw_response.link(
                "8c71e667571b4f61b94d9e4b12158038",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.alerting.v3.destinations.pagerduty.with_raw_response.link(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )