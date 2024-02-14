# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users.tokens import ValueUserAPITokensRollTokenResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.tokens import value_user_api_tokens_roll_token_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_api_tokens_roll_token(self, client: Cloudflare) -> None:
        value = client.users.tokens.values.user_api_tokens_roll_token(
            {},
            body={},
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_api_tokens_roll_token(self, client: Cloudflare) -> None:
        response = client.users.tokens.values.with_raw_response.user_api_tokens_roll_token(
            {},
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_api_tokens_roll_token(self, client: Cloudflare) -> None:
        with client.users.tokens.values.with_streaming_response.user_api_tokens_roll_token(
            {},
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_api_tokens_roll_token(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.users.tokens.values.user_api_tokens_roll_token(
            {},
            body={},
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_api_tokens_roll_token(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.tokens.values.with_raw_response.user_api_tokens_roll_token(
            {},
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_api_tokens_roll_token(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.tokens.values.with_streaming_response.user_api_tokens_roll_token(
            {},
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True