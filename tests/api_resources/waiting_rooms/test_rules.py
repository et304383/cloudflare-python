# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.waiting_rooms import (
    WaitingroomRule,
    RuleEditResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.create(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.create(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.update(
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
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.update(
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
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.update(
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
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.update(
                "",
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

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[WaitingroomRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncSinglePage[WaitingroomRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncSinglePage[WaitingroomRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.list(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.list(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        rule = client.waiting_rooms.rules.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.waiting_rooms.rules.with_raw_response.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.waiting_rooms.rules.with_streaming_response.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.waiting_rooms.rules.with_raw_response.edit(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.create(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.create(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.create(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.update(
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
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.update(
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
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.update(
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
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.update(
                "",
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[WaitingroomRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncSinglePage[WaitingroomRule], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.list(
            "699d98642c564d2e855e9661899b7252",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncSinglePage[WaitingroomRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.list(
                "699d98642c564d2e855e9661899b7252",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.list(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
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

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.waiting_rooms.rules.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
            description="allow all traffic from 10.20.30.40",
            enabled=True,
            position={"index": 0},
        )
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.waiting_rooms.rules.with_raw_response.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.waiting_rooms.rules.with_streaming_response.edit(
            "25756b2dfe6e378a06b033b670413757",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            waiting_room_id="699d98642c564d2e855e9661899b7252",
            action="bypass_waiting_room",
            expression="ip.src in {10.20.30.40}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleEditResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `waiting_room_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                "25756b2dfe6e378a06b033b670413757",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.waiting_rooms.rules.with_raw_response.edit(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                waiting_room_id="699d98642c564d2e855e9661899b7252",
                action="bypass_waiting_room",
                expression="ip.src in {10.20.30.40}",
            )
