# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateway import AuditSSHSettingUpdateResponse, AuditSSHSettingGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateway import audit_ssh_setting_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditSSHSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.gateway.audit_ssh_settings.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.gateway.audit_ssh_settings.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
            seed_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateway.audit_ssh_settings.with_raw_response.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = response.parse()
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateway.audit_ssh_settings.with_streaming_response.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = response.parse()
            assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        audit_ssh_setting = client.gateway.audit_ssh_settings.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateway.audit_ssh_settings.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = response.parse()
        assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateway.audit_ssh_settings.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = response.parse()
            assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditSSHSettings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.gateway.audit_ssh_settings.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.gateway.audit_ssh_settings.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
            seed_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateway.audit_ssh_settings.with_raw_response.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = await response.parse()
        assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateway.audit_ssh_settings.with_streaming_response.update(
            "699d98642c564d2e855e9661899b7252",
            public_key="1pyl6I1tL7xfJuFYVzXlUW8uXXlpxegHXBzGCBKaSFA=",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = await response.parse()
            assert_matches_type(AuditSSHSettingUpdateResponse, audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        audit_ssh_setting = await async_client.gateway.audit_ssh_settings.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateway.audit_ssh_settings.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_ssh_setting = await response.parse()
        assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateway.audit_ssh_settings.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_ssh_setting = await response.parse()
            assert_matches_type(AuditSSHSettingGetResponse, audit_ssh_setting, path=["response"])

        assert cast(Any, response.is_closed) is True