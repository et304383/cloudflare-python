# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.firewalls.waf.packages import (
    RuleUpdateResponse,
    RuleGetResponse,
    RuleWAFRulesListWAFRulesResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewalls.waf.packages import rule_update_params
from cloudflare.types.firewalls.waf.packages import rule_waf_rules_list_waf_rules_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.firewalls.waf.packages.rules.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewalls.waf.packages.rules.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            mode="on",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.packages.rules.with_raw_response.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.waf.packages.rules.with_streaming_response.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.update(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.update(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.firewalls.waf.packages.rules.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.packages.rules.with_raw_response.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.waf.packages.rules.with_streaming_response.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.get(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.get(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_waf_rules_list_waf_rules(self, client: Cloudflare) -> None:
        rule = client.firewalls.waf.packages.rules.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_waf_rules_list_waf_rules_with_all_params(self, client: Cloudflare) -> None:
        rule = client.firewalls.waf.packages.rules.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            mode="CHL",
            order="priority",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_waf_rules_list_waf_rules(self, client: Cloudflare) -> None:
        response = client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_waf_rules_list_waf_rules(self, client: Cloudflare) -> None:
        with client.firewalls.waf.packages.rules.with_streaming_response.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_waf_rules_list_waf_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.waf.packages.rules.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.waf.packages.rules.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            mode="on",
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.packages.rules.with_raw_response.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.packages.rules.with_streaming_response.update(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.update(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.update(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.waf.packages.rules.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.packages.rules.with_raw_response.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.packages.rules.with_streaming_response.get(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            package_id="a25a9a7e9c00afc1fb2e0245519d725b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.get(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.get(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                package_id="a25a9a7e9c00afc1fb2e0245519d725b",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_waf_rules_list_waf_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.waf.packages.rules.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_waf_rules_list_waf_rules_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.firewalls.waf.packages.rules.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            match="any",
            mode="CHL",
            order="priority",
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_waf_rules_list_waf_rules(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_waf_rules_list_waf_rules(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.waf.packages.rules.with_streaming_response.waf_rules_list_waf_rules(
            "a25a9a7e9c00afc1fb2e0245519d725b",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleWAFRulesListWAFRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_waf_rules_list_waf_rules(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
                "a25a9a7e9c00afc1fb2e0245519d725b",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `package_id` but received ''"):
            await async_client.firewalls.waf.packages.rules.with_raw_response.waf_rules_list_waf_rules(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )