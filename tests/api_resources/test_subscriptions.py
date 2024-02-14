# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionAccountSubscriptionsCreateSubscriptionResponse,
    SubscriptionAccountSubscriptionsListSubscriptionsResponse,
    SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse,
    SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse,
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
from cloudflare.types import subscription_update_params
from cloudflare.types import subscription_account_subscriptions_create_subscription_params
from cloudflare.types import subscription_zone_subscription_create_zone_subscription_params
from cloudflare.types import subscription_zone_subscription_update_zone_subscription_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.subscriptions.with_raw_response.update(
                "506e3185e9c882d175a2d0cb0093d9f2",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_identifier` but received ''"
        ):
            client.subscriptions.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.subscriptions.with_raw_response.delete(
                "506e3185e9c882d175a2d0cb0093d9f2",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_identifier` but received ''"
        ):
            client.subscriptions.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_subscriptions_create_subscription(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_subscriptions_create_subscription_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_subscriptions_create_subscription(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_subscriptions_create_subscription(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_subscriptions_create_subscription(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.subscriptions.with_raw_response.account_subscriptions_create_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_subscriptions_list_subscriptions(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_subscriptions_list_subscriptions(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(
            Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_subscriptions_list_subscriptions(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_subscriptions_list_subscriptions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.subscriptions.with_raw_response.account_subscriptions_list_subscriptions(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_subscription_create_zone_subscription(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_subscription_create_zone_subscription_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_subscription_create_zone_subscription(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_subscription_create_zone_subscription(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_subscription_create_zone_subscription(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.subscriptions.with_raw_response.zone_subscription_create_zone_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_subscription_update_zone_subscription(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_subscription_update_zone_subscription_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_subscription_update_zone_subscription(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_subscription_update_zone_subscription(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_subscription_update_zone_subscription(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.subscriptions.with_raw_response.zone_subscription_update_zone_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_subscription_zone_subscription_details(self, client: Cloudflare) -> None:
        subscription = client.subscriptions.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_subscription_zone_subscription_details(self, client: Cloudflare) -> None:
        response = client.subscriptions.with_raw_response.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_subscription_zone_subscription_details(self, client: Cloudflare) -> None:
        with client.subscriptions.with_streaming_response.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_subscription_zone_subscription_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.subscriptions.with_raw_response.zone_subscription_zone_subscription_details(
                "",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.subscriptions.with_streaming_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.update(
                "506e3185e9c882d175a2d0cb0093d9f2",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_identifier` but received ''"
        ):
            await async_client.subscriptions.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.delete(
                "506e3185e9c882d175a2d0cb0093d9f2",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_identifier` but received ''"
        ):
            await async_client.subscriptions.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_subscriptions_create_subscription(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_subscriptions_create_subscription_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        subscription = await async_client.subscriptions.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_subscriptions_create_subscription(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_subscriptions_create_subscription(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.subscriptions.with_streaming_response.account_subscriptions_create_subscription(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                SubscriptionAccountSubscriptionsCreateSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_subscriptions_create_subscription(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.account_subscriptions_create_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_subscriptions_list_subscriptions(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_subscriptions_list_subscriptions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(
            Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_subscriptions_list_subscriptions(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.subscriptions.with_streaming_response.account_subscriptions_list_subscriptions(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                Optional[SubscriptionAccountSubscriptionsListSubscriptionsResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_subscriptions_list_subscriptions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.account_subscriptions_list_subscriptions(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_subscription_create_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_subscription_create_zone_subscription_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        subscription = await async_client.subscriptions.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_subscription_create_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_subscription_create_zone_subscription(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.subscriptions.with_streaming_response.zone_subscription_create_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionCreateZoneSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_subscription_create_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.zone_subscription_create_zone_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_subscription_update_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_subscription_update_zone_subscription_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        subscription = await async_client.subscriptions.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_subscription_update_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.subscriptions.with_raw_response.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_subscription_update_zone_subscription(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.subscriptions.with_streaming_response.zone_subscription_update_zone_subscription(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionUpdateZoneSubscriptionResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_subscription_update_zone_subscription(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.zone_subscription_update_zone_subscription(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_subscription_zone_subscription_details(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.subscriptions.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_subscription_zone_subscription_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.subscriptions.with_raw_response.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(
            SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_subscription_zone_subscription_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.subscriptions.with_streaming_response.zone_subscription_zone_subscription_details(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                SubscriptionZoneSubscriptionZoneSubscriptionDetailsResponse, subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_subscription_zone_subscription_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.subscriptions.with_raw_response.zone_subscription_zone_subscription_details(
                "",
            )