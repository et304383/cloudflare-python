# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import OriginPostQuantumEncryptionUpdateResponse, OriginPostQuantumEncryptionGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import origin_post_quantum_encryption_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginPostQuantumEncryptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        origin_post_quantum_encryption = client.origin_post_quantum_encryptions.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        )
        assert_matches_type(
            OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.origin_post_quantum_encryptions.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_post_quantum_encryption = response.parse()
        assert_matches_type(
            OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.origin_post_quantum_encryptions.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_post_quantum_encryption = response.parse()
            assert_matches_type(
                OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.origin_post_quantum_encryptions.with_raw_response.update(
                "",
                value="preferred",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        origin_post_quantum_encryption = client.origin_post_quantum_encryptions.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.origin_post_quantum_encryptions.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_post_quantum_encryption = response.parse()
        assert_matches_type(OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.origin_post_quantum_encryptions.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_post_quantum_encryption = response.parse()
            assert_matches_type(
                OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.origin_post_quantum_encryptions.with_raw_response.get(
                "",
            )


class TestAsyncOriginPostQuantumEncryptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        origin_post_quantum_encryption = await async_client.origin_post_quantum_encryptions.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        )
        assert_matches_type(
            OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_post_quantum_encryptions.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_post_quantum_encryption = await response.parse()
        assert_matches_type(
            OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_post_quantum_encryptions.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="preferred",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_post_quantum_encryption = await response.parse()
            assert_matches_type(
                OriginPostQuantumEncryptionUpdateResponse, origin_post_quantum_encryption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.origin_post_quantum_encryptions.with_raw_response.update(
                "",
                value="preferred",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        origin_post_quantum_encryption = await async_client.origin_post_quantum_encryptions.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_post_quantum_encryptions.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_post_quantum_encryption = await response.parse()
        assert_matches_type(OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_post_quantum_encryptions.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_post_quantum_encryption = await response.parse()
            assert_matches_type(
                OriginPostQuantumEncryptionGetResponse, origin_post_quantum_encryption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.origin_post_quantum_encryptions.with_raw_response.get(
                "",
            )