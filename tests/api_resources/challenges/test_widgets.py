# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.challenges import (
    WidgetCreateResponse,
    WidgetUpdateResponse,
    WidgetListResponse,
    WidgetDeleteResponse,
    WidgetGetResponse,
    WidgetRotateSecretResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.challenges import widget_create_params
from cloudflare.types.challenges import widget_update_params
from cloudflare.types.challenges import widget_list_params
from cloudflare.types.challenges import widget_rotate_secret_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWidgets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
            bot_fight_mode=True,
            clearance_level="interactive",
            offlabel=True,
            region="world",
        )
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.create(
                "",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
            bot_fight_mode=True,
            clearance_level="interactive",
            offlabel=True,
        )
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.update(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.challenges.widgets.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.delete(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.challenges.widgets.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.get(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.challenges.widgets.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_rotate_secret(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_rotate_secret_with_all_params(self, client: Cloudflare) -> None:
        widget = client.challenges.widgets.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            invalidate_immediately=True,
        )
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_rotate_secret(self, client: Cloudflare) -> None:
        response = client.challenges.widgets.with_raw_response.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = response.parse()
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_rotate_secret(self, client: Cloudflare) -> None:
        with client.challenges.widgets.with_streaming_response.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = response.parse()
            assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_rotate_secret(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.challenges.widgets.with_raw_response.rotate_secret(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            client.challenges.widgets.with_raw_response.rotate_secret(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWidgets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
            bot_fight_mode=True,
            clearance_level="interactive",
            offlabel=True,
            region="world",
        )
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetCreateResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.create(
                "",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
            bot_fight_mode=True,
            clearance_level="interactive",
            offlabel=True,
        )
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.update(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
            mode="invisible",
            name="blog.cloudflare.com login form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetUpdateResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.update(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.challenges.widgets.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                domains=["203.0.113.1", "cloudflare.com", "blog.example.com"],
                mode="invisible",
                name="blog.cloudflare.com login form",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="id",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetListResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.delete(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetDeleteResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.delete(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.challenges.widgets.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.get(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetGetResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.get(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.challenges.widgets.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_rotate_secret_with_all_params(self, async_client: AsyncCloudflare) -> None:
        widget = await async_client.challenges.widgets.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            invalidate_immediately=True,
        )
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.challenges.widgets.with_raw_response.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        widget = await response.parse()
        assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        async with async_client.challenges.widgets.with_streaming_response.rotate_secret(
            "0x4AAF00AAAABn0R22HWm-YUc",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            widget = await response.parse()
            assert_matches_type(Optional[WidgetRotateSecretResponse], widget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.challenges.widgets.with_raw_response.rotate_secret(
                "0x4AAF00AAAABn0R22HWm-YUc",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sitekey` but received ''"):
            await async_client.challenges.widgets.with_raw_response.rotate_secret(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )