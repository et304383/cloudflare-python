# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.intels import IPListIPListGetIPListsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_list_get_ip_lists(self, client: Cloudflare) -> None:
        ip_list = client.intels.ip_lists.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_list_get_ip_lists(self, client: Cloudflare) -> None:
        response = client.intels.ip_lists.with_raw_response.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_list = response.parse()
        assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_list_get_ip_lists(self, client: Cloudflare) -> None:
        with client.intels.ip_lists.with_streaming_response.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_list = response.parse()
            assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_list_get_ip_lists(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intels.ip_lists.with_raw_response.ip_list_get_ip_lists(
                "",
            )


class TestAsyncIPLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_list_get_ip_lists(self, async_client: AsyncCloudflare) -> None:
        ip_list = await async_client.intels.ip_lists.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_list_get_ip_lists(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intels.ip_lists.with_raw_response.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip_list = await response.parse()
        assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_list_get_ip_lists(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intels.ip_lists.with_streaming_response.ip_list_get_ip_lists(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip_list = await response.parse()
            assert_matches_type(Optional[IPListIPListGetIPListsResponse], ip_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_list_get_ip_lists(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intels.ip_lists.with_raw_response.ip_list_get_ip_lists(
                "",
            )