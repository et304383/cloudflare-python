# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.devices.policies import (
    ExcludeDevicesGetSplitTunnelExcludeListResponse,
    ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
    ExcludeDevicesSetSplitTunnelExcludeListResponse,
    ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.devices.policies import exclude_devices_set_split_tunnel_exclude_list_params
from cloudflare.types.devices.policies import (
    exclude_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExcludes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_get_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        exclude = client.devices.policies.excludes.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_get_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        response = client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = response.parse()
        assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_get_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        with client.devices.policies.excludes.with_streaming_response.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = response.parse()
            assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        exclude = client.devices.policies.excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        response = client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = response.parse()
        assert_matches_type(
            Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with client.devices.policies.excludes.with_streaming_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = response.parse()
            assert_matches_type(
                Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
                exclude,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_set_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        exclude = client.devices.policies.excludes.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )
        assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_set_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        response = client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = response.parse()
        assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_set_split_tunnel_exclude_list(self, client: Cloudflare) -> None:
        with client.devices.policies.excludes.with_streaming_response.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = response.parse()
            assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        exclude = client.devices.policies.excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )
        assert_matches_type(
            Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        response = client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = response.parse()
        assert_matches_type(
            Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with client.devices.policies.excludes.with_streaming_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = response.parse()
            assert_matches_type(
                Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
                exclude,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                body=[
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                ],
            )


class TestAsyncExcludes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_get_split_tunnel_exclude_list(self, async_client: AsyncCloudflare) -> None:
        exclude = await async_client.devices.policies.excludes.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_get_split_tunnel_exclude_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = await response.parse()
        assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_get_split_tunnel_exclude_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.excludes.with_streaming_response.devices_get_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = await response.parse()
            assert_matches_type(Optional[ExcludeDevicesGetSplitTunnelExcludeListResponse], exclude, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        exclude = await async_client.devices.policies.excludes.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = await response.parse()
        assert_matches_type(
            Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.excludes.with_streaming_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = await response.parse()
            assert_matches_type(
                Optional[ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
                exclude,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.excludes.with_raw_response.devices_get_split_tunnel_exclude_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_set_split_tunnel_exclude_list(self, async_client: AsyncCloudflare) -> None:
        exclude = await async_client.devices.policies.excludes.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )
        assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_set_split_tunnel_exclude_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = await response.parse()
        assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_set_split_tunnel_exclude_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.excludes.with_streaming_response.devices_set_split_tunnel_exclude_list(
            "699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = await response.parse()
            assert_matches_type(Optional[ExcludeDevicesSetSplitTunnelExcludeListResponse], exclude, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        exclude = await async_client.devices.policies.excludes.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )
        assert_matches_type(
            Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        exclude = await response.parse()
        assert_matches_type(
            Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
            exclude,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.devices.policies.excludes.with_streaming_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            identifier="699d98642c564d2e855e9661899b7252",
            body=[
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
                {
                    "address": "192.0.2.0/24",
                    "description": "Exclude testing domains from the tunnel",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            exclude = await response.parse()
            assert_matches_type(
                Optional[ExcludeDevicesSetSplitTunnelExcludeListForADeviceSettingsPolicyResponse],
                exclude,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.devices.policies.excludes.with_raw_response.devices_set_split_tunnel_exclude_list_for_a_device_settings_policy(
                "",
                identifier="699d98642c564d2e855e9661899b7252",
                body=[
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                    {
                        "address": "192.0.2.0/24",
                        "description": "Exclude testing domains from the tunnel",
                    },
                ],
            )