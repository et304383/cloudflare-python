# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.images import (
    Image,
    V1ListResponse,
    V1DeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        v1 = client.images.v1.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.create(
                account_id="",
                file={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        v1 = client.images.v1.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.create(
                account_id="",
                url="https://example.com/path/to/logo.png",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        v1 = client.images.v1.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        v1 = client.images.v1.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=10,
        )
        assert_matches_type(SyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(SyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(SyncV4PagePagination[V1ListResponse], v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        v1 = client.images.v1.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.delete(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        v1 = client.images.v1.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        v1 = client.images.v1.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={},
            require_signed_urls=True,
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.edit(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        v1 = client.images.v1.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.images.v1.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.images.v1.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncV1:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.create(
                account_id="",
                file={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="https://example.com/path/to/logo.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.create(
                account_id="",
                url="https://example.com/path/to/logo.png",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=10,
        )
        assert_matches_type(AsyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(AsyncV4PagePagination[V1ListResponse], v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(AsyncV4PagePagination[V1ListResponse], v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DeleteResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DeleteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.delete(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={},
            require_signed_urls=True,
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.edit(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.edit(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1.with_raw_response.edit(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        v1 = await async_client.images.v1.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.images.v1.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(Image, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.images.v1.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(Image, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.with_raw_response.get(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
