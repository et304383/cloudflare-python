# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.access.apps import UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserPolicyChecks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_applications_test_access_policies(self, client: Cloudflare) -> None:
        user_policy_check = client.access.apps.user_policy_checks.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_applications_test_access_policies(self, client: Cloudflare) -> None:
        response = client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_policy_check = response.parse()
        assert_matches_type(
            UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_applications_test_access_policies(self, client: Cloudflare) -> None:
        with client.access.apps.user_policy_checks.with_streaming_response.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_policy_check = response.parse()
            assert_matches_type(
                UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_applications_test_access_policies(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="string",
                account_or_zone_id="",
            )


class TestAsyncUserPolicyChecks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_applications_test_access_policies(self, async_client: AsyncCloudflare) -> None:
        user_policy_check = await async_client.access.apps.user_policy_checks.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_applications_test_access_policies(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_policy_check = await response.parse()
        assert_matches_type(
            UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_applications_test_access_policies(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.apps.user_policy_checks.with_streaming_response.access_applications_test_access_policies(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_policy_check = await response.parse()
            assert_matches_type(
                UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse, user_policy_check, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_applications_test_access_policies(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await (
                async_client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
                    "023e105f4ecef8ad9ca31a8372d0c353",
                    account_or_zone="",
                    account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                )
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await (
                async_client.access.apps.user_policy_checks.with_raw_response.access_applications_test_access_policies(
                    "023e105f4ecef8ad9ca31a8372d0c353",
                    account_or_zone="string",
                    account_or_zone_id="",
                )
            )