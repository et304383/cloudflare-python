# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.access.users import FailedLoginZeroTrustUsersGetFailedLoginsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFailedLogins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_users_get_failed_logins(self, client: Cloudflare) -> None:
        failed_login = client.access.users.failed_logins.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_users_get_failed_logins(self, client: Cloudflare) -> None:
        response = client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        failed_login = response.parse()
        assert_matches_type(Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_users_get_failed_logins(self, client: Cloudflare) -> None:
        with client.access.users.failed_logins.with_streaming_response.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            failed_login = response.parse()
            assert_matches_type(
                Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zero_trust_users_get_failed_logins(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncFailedLogins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_users_get_failed_logins(self, async_client: AsyncCloudflare) -> None:
        failed_login = await async_client.access.users.failed_logins.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_users_get_failed_logins(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        failed_login = await response.parse()
        assert_matches_type(Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_users_get_failed_logins(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.users.failed_logins.with_streaming_response.zero_trust_users_get_failed_logins(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            failed_login = await response.parse()
            assert_matches_type(
                Optional[FailedLoginZeroTrustUsersGetFailedLoginsResponse], failed_login, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zero_trust_users_get_failed_logins(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.access.users.failed_logins.with_raw_response.zero_trust_users_get_failed_logins(
                "",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )