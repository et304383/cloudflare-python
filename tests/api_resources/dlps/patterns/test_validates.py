# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.dlps.patterns import ValidateDLPPatternValidationValidatePatternResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dlps.patterns import validate_dlp_pattern_validation_validate_pattern_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_dlp_pattern_validation_validate_pattern(self, client: Cloudflare) -> None:
        validate = client.dlps.patterns.validates.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )
        assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_dlp_pattern_validation_validate_pattern(self, client: Cloudflare) -> None:
        response = client.dlps.patterns.validates.with_raw_response.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_dlp_pattern_validation_validate_pattern(self, client: Cloudflare) -> None:
        with client.dlps.patterns.validates.with_streaming_response.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_dlp_pattern_validation_validate_pattern(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dlps.patterns.validates.with_raw_response.dlp_pattern_validation_validate_pattern(
                "",
                regex="^4[0-9]{6,}$",
            )


class TestAsyncValidates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_dlp_pattern_validation_validate_pattern(self, async_client: AsyncCloudflare) -> None:
        validate = await async_client.dlps.patterns.validates.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )
        assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_dlp_pattern_validation_validate_pattern(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dlps.patterns.validates.with_raw_response.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_dlp_pattern_validation_validate_pattern(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.dlps.patterns.validates.with_streaming_response.dlp_pattern_validation_validate_pattern(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regex="^4[0-9]{6,}$",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateDLPPatternValidationValidatePatternResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_dlp_pattern_validation_validate_pattern(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dlps.patterns.validates.with_raw_response.dlp_pattern_validation_validate_pattern(
                "",
                regex="^4[0-9]{6,}$",
            )