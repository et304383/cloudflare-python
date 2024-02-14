# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.waiting_rooms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleWaitingRoomCreateWaitingRoomRuleResponse,
    RuleWaitingRoomListWaitingRoomRulesResponse,
    RuleWaitingRoomReplaceWaitingRoomRulesResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.waiting_rooms import rule_update_params
from cloudflare.types.waiting_rooms import rule_waiting_room_create_waiting_room_rule_params
from cloudflare.types.waiting_rooms import rule_waiting_room_replace_waiting_room_rules_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_create_waiting_room_rule(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_create_waiting_room_rule_with_all_params(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_create_waiting_room_rule(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_create_waiting_room_rule(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_create_waiting_room_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.waiting_room_create_waiting_room_rule(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_list_waiting_room_rules(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_list_waiting_room_rules(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_list_waiting_room_rules(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_list_waiting_room_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.waiting_room_list_waiting_room_rules(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waiting_room_replace_waiting_room_rules(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )
        assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waiting_room_replace_waiting_room_rules(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waiting_room_replace_waiting_room_rules(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waiting_room_replace_waiting_room_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.waiting_room_replace_waiting_room_rules(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.update(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.delete(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_create_waiting_room_rule(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_create_waiting_room_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.waiting_rooms.rules.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_create_waiting_room_rule(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_create_waiting_room_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.waiting_room_create_waiting_room_rule(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_create_waiting_room_rule(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.waiting_room_create_waiting_room_rule(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_list_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_list_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_list_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.waiting_room_list_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleWaitingRoomListWaitingRoomRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_list_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.waiting_room_list_waiting_room_rules(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waiting_room_replace_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )
        assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waiting_room_replace_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waiting_room_replace_waiting_room_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.waiting_room_replace_waiting_room_rules(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
                {
                    "action": "bypass_waiting_room",
                    "expression": "ip.src in {10.20.30.40}",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waiting_room_replace_waiting_room_rules(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.waiting_room_replace_waiting_room_rules(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                body=[
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                    {
                        "action": "bypass_waiting_room",
                        "expression": "ip.src in {10.20.30.40}",
                    },
                ],
            )