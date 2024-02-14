# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users import AuditLogAuditLogsGetUserAuditLogsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users import audit_log_audit_logs_get_user_audit_logs_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuditLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_audit_logs_get_user_audit_logs(self, client: Cloudflare) -> None:
        audit_log = client.users.audit_logs.audit_logs_get_user_audit_logs()
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_audit_logs_get_user_audit_logs_with_all_params(self, client: Cloudflare) -> None:
        audit_log = client.users.audit_logs.audit_logs_get_user_audit_logs(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "ip": "17.168.228.63",
                "email": "alice@example.com",
            },
            before=parse_datetime("2019-04-30T01:12:20Z"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_datetime("2019-04-30T01:12:20Z"),
            zone={"name": "example.com"},
        )
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_audit_logs_get_user_audit_logs(self, client: Cloudflare) -> None:
        response = client.users.audit_logs.with_raw_response.audit_logs_get_user_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = response.parse()
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_audit_logs_get_user_audit_logs(self, client: Cloudflare) -> None:
        with client.users.audit_logs.with_streaming_response.audit_logs_get_user_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = response.parse()
            assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuditLogs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_audit_logs_get_user_audit_logs(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.users.audit_logs.audit_logs_get_user_audit_logs()
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_audit_logs_get_user_audit_logs_with_all_params(self, async_client: AsyncCloudflare) -> None:
        audit_log = await async_client.users.audit_logs.audit_logs_get_user_audit_logs(
            id="f174be97-19b1-40d6-954d-70cd5fbd52db",
            action={"type": "add"},
            actor={
                "ip": "17.168.228.63",
                "email": "alice@example.com",
            },
            before=parse_datetime("2019-04-30T01:12:20Z"),
            direction="desc",
            export=True,
            hide_user_logs=True,
            page=50,
            per_page=25,
            since=parse_datetime("2019-04-30T01:12:20Z"),
            zone={"name": "example.com"},
        )
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_audit_logs_get_user_audit_logs(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.audit_logs.with_raw_response.audit_logs_get_user_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        audit_log = await response.parse()
        assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_audit_logs_get_user_audit_logs(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.audit_logs.with_streaming_response.audit_logs_get_user_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            audit_log = await response.parse()
            assert_matches_type(AuditLogAuditLogsGetUserAuditLogsResponse, audit_log, path=["response"])

        assert cast(Any, response.is_closed) is True