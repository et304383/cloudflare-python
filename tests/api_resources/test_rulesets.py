# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import RulesetListResponse, RulesetsRulesetResponse
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRulesets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.create(
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
            account_id="string",
            zone_id="string",
            description="My ruleset to execute managed rulesets",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.with_raw_response.create(
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.with_raw_response.create(
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
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
            account_id="string",
            zone_id="string",
            description="My ruleset to execute managed rulesets",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.update(
                "",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(SyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(SyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.list(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(SyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.list(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(SyncSinglePage[RulesetListResponse], ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.with_raw_response.list(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        ruleset = client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rulesets.with_raw_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rulesets.with_streaming_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rulesets.with_raw_response.get(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )


class TestAsyncRulesets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.create(
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
            account_id="string",
            zone_id="string",
            description="My ruleset to execute managed rulesets",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.create(
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.with_raw_response.create(
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.create(
                kind="root",
                name="My ruleset",
                phase="http_request_firewall_custom",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.update(
            "2f2feab2026849078ba485f918791bdc",
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
            account_id="string",
            zone_id="string",
            description="My ruleset to execute managed rulesets",
            kind="root",
            name="My ruleset",
            phase="http_request_firewall_custom",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.update(
            "2f2feab2026849078ba485f918791bdc",
            id="2f2feab2026849078ba485f918791bdc",
            rules=[{}, {}, {}],
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.update(
                "2f2feab2026849078ba485f918791bdc",
                id="2f2feab2026849078ba485f918791bdc",
                rules=[{}, {}, {}],
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(AsyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.list(
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(AsyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.list(
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(AsyncSinglePage[RulesetListResponse], ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.list(
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(AsyncSinglePage[RulesetListResponse], ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.with_raw_response.list(
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.list(
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert ruleset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.delete(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
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
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert ruleset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.delete(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ruleset = await async_client.rulesets.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rulesets.with_raw_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ruleset = await response.parse()
        assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rulesets.with_streaming_response.get(
            "2f2feab2026849078ba485f918791bdc",
            account_id="string",
            zone_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ruleset = await response.parse()
            assert_matches_type(RulesetsRulesetResponse, ruleset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "",
                account_id="string",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_id="",
                zone_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.rulesets.with_raw_response.get(
                "2f2feab2026849078ba485f918791bdc",
                account_id="string",
                zone_id="",
            )
