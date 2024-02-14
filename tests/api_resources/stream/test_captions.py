# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.stream import (
    CaptionUpdateResponse,
    CaptionDeleteResponse,
    CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import caption_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCaptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        caption = client.stream.captions.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )
        assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.captions.with_raw_response.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = response.parse()
        assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.captions.with_streaming_response.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = response.parse()
            assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.with_raw_response.update(
                "tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.with_raw_response.update(
                "tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        caption = client.stream.captions.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.captions.with_raw_response.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = response.parse()
        assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.captions.with_streaming_response.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = response.parse()
            assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.with_raw_response.delete(
                "tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.with_raw_response.delete(
                "tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            client.stream.captions.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_subtitles_captions_list_captions_or_subtitles(self, client: Cloudflare) -> None:
        caption = client.stream.captions.stream_subtitles_captions_list_captions_or_subtitles(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_subtitles_captions_list_captions_or_subtitles(self, client: Cloudflare) -> None:
        response = client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = response.parse()
        assert_matches_type(CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_subtitles_captions_list_captions_or_subtitles(self, client: Cloudflare) -> None:
        with client.stream.captions.with_streaming_response.stream_subtitles_captions_list_captions_or_subtitles(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = response.parse()
            assert_matches_type(
                CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_subtitles_captions_list_captions_or_subtitles(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCaptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        caption = await async_client.stream.captions.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )
        assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.with_raw_response.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = await response.parse()
        assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.with_streaming_response.update(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
            file="@/Users/kyle/Desktop/tr.vtt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = await response.parse()
            assert_matches_type(CaptionUpdateResponse, caption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.with_raw_response.update(
                "tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.with_raw_response.update(
                "tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
                file="@/Users/kyle/Desktop/tr.vtt",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        caption = await async_client.stream.captions.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )
        assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.captions.with_raw_response.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = await response.parse()
        assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.captions.with_streaming_response.delete(
            "tr",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="ea95132c15732412d22c1476fa83f27a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = await response.parse()
            assert_matches_type(CaptionDeleteResponse, caption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.with_raw_response.delete(
                "tr",
                account_id="",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.with_raw_response.delete(
                "tr",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `language` but received ''"):
            await async_client.stream.captions.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="ea95132c15732412d22c1476fa83f27a",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_subtitles_captions_list_captions_or_subtitles(
        self, async_client: AsyncCloudflare
    ) -> None:
        caption = await async_client.stream.captions.stream_subtitles_captions_list_captions_or_subtitles(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_subtitles_captions_list_captions_or_subtitles(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        caption = await response.parse()
        assert_matches_type(CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_subtitles_captions_list_captions_or_subtitles(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.captions.with_streaming_response.stream_subtitles_captions_list_captions_or_subtitles(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            caption = await response.parse()
            assert_matches_type(
                CaptionStreamSubtitlesCaptionsListCaptionsOrSubtitlesResponse, caption, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_subtitles_captions_list_captions_or_subtitles(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.captions.with_raw_response.stream_subtitles_captions_list_captions_or_subtitles(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )