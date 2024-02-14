# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.alerting.v3s.destinations import (
    EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEligibles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, client: Cloudflare
    ) -> None:
        eligible = client.alerting.v3s.destinations.eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            eligible,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, client: Cloudflare
    ) -> None:
        response = client.alerting.v3s.destinations.eligibles.with_raw_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eligible = response.parse()
        assert_matches_type(
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            eligible,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, client: Cloudflare
    ) -> None:
        with client.alerting.v3s.destinations.eligibles.with_streaming_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eligible = response.parse()
            assert_matches_type(
                Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
                eligible,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.eligibles.with_raw_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
                "",
            )


class TestAsyncEligibles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, async_client: AsyncCloudflare
    ) -> None:
        eligible = await async_client.alerting.v3s.destinations.eligibles.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            eligible,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.alerting.v3s.destinations.eligibles.with_raw_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        eligible = await response.parse()
        assert_matches_type(
            Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
            eligible,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.alerting.v3s.destinations.eligibles.with_streaming_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            eligible = await response.parse()
            assert_matches_type(
                Optional[EligibleNotificationMechanismEligibilityGetDeliveryMechanismEligibilityResponse],
                eligible,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.eligibles.with_raw_response.notification_mechanism_eligibility_get_delivery_mechanism_eligibility(
                "",
            )