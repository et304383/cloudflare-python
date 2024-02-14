# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import RulesetCreateResponse, RulesetUpdateResponse, RulesetListResponse, RulesetGetResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import ruleset_create_params
from cloudflare.types import ruleset_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRulesets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            description="My ruleset to execute managed rulesets",
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.with_raw_response.create(
                "abf9b32d38c5f572afde3336ec0ce302",
                account_or_zone="",
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.with_raw_response.create(
                "",
                account_or_zone="string",
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            description="My ruleset to execute managed rulesets",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        )
        assert_matches_type(RulesetListResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetListResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetListResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.with_raw_response.list(
                "abf9b32d38c5f572afde3336ec0ce302",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.with_raw_response.list(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )


class TestAsyncRulesets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            description="My ruleset to execute managed rulesets",
        )
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.create(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetCreateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.with_raw_response.create(
                "abf9b32d38c5f572afde3336ec0ce302",
                account_or_zone="",
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.create(
                "",
                account_or_zone="string",
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
                {
                    "action": "block",
                    "action_parameters": {
                        "response": {
                            "content": '{\n  "success": false,\n  "error": "you have been blocked"\n}',
                            "content_type": "application/json",
                            "status_code": 400,
                        }
                    },
                    "description": "Block when the IP address is not 1.1.1.1",
                    "enabled": True,
                    "expression": "ip.src ne 1.1.1.1",
                    "id": "3a03d665bac047339bb530ecb439a90d",
                    "logging": {"enabled": True},
                    "ref": "my_ref",
                },
            ],
            description="My ruleset to execute managed rulesets",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
        )
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.update(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetUpdateResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        )
        assert_matches_type(RulesetListResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetListResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.list(
            "abf9b32d38c5f572afde3336ec0ce302",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetListResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.with_raw_response.list(
                "abf9b32d38c5f572afde3336ec0ce302",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.list(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_or_zone="string",
            account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetGetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="abf9b32d38c5f572afde3336ec0ce302",
            )