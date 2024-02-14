# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.dlp import (
    DatasetCreateResponse,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetGetResponse,
    DatasetUploadResponse,
    DatasetUploadPrepareResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dlp import dataset_create_params
from cloudflare.types.dlp import dataset_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.create(
            "string",
            name="string",
        )
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.create(
            "string",
            name="string",
            description="string",
            secret=True,
        )
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.create(
            "string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.create(
            "string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.create(
                "",
                name="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
            description="string",
            name="string",
        )
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.dlp.datasets.with_raw_response.update(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.list(
            "string",
        )
        assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.dlp.datasets.with_raw_response.delete(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.dlp.datasets.with_raw_response.get(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upload(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.upload(
                0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.dlp.datasets.with_raw_response.upload(
                0,
                account_id="string",
                dataset_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_prepare(self, client: Cloudflare) -> None:
        dataset = client.dlp.datasets.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload_prepare(self, client: Cloudflare) -> None:
        response = client.dlp.datasets.with_raw_response.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload_prepare(self, client: Cloudflare) -> None:
        with client.dlp.datasets.with_streaming_response.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upload_prepare(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlp.datasets.with_raw_response.upload_prepare(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.dlp.datasets.with_raw_response.upload_prepare(
                "",
                account_id="string",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.create(
            "string",
            name="string",
        )
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.create(
            "string",
            name="string",
            description="string",
            secret=True,
        )
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.create(
            "string",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.create(
            "string",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetCreateResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.create(
                "",
                name="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
            description="string",
            name="string",
        )
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetUpdateResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.update(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.update(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.list(
            "string",
        )
        assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetListResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.delete(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetGetResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.get(
                "",
                account_id="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.upload(
            0,
            account_id="string",
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetUploadResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.upload(
                0,
                account_id="",
                dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.upload(
                0,
                account_id="string",
                dataset_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_prepare(self, async_client: AsyncCloudflare) -> None:
        dataset = await async_client.dlp.datasets.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )
        assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload_prepare(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlp.datasets.with_raw_response.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload_prepare(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dlp.datasets.with_streaming_response.upload_prepare(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetUploadPrepareResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upload_prepare(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.upload_prepare(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.dlp.datasets.with_raw_response.upload_prepare(
                "",
                account_id="string",
            )