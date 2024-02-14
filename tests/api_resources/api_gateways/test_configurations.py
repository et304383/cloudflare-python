# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.api_gateways import (
    ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
    ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.api_gateways import (
    configuration_api_shield_settings_get_information_about_specific_configuration_properties_params,
)
from cloudflare.types.api_gateways import configuration_api_shield_settings_set_configuration_properties_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_settings_get_information_about_specific_configuration_properties(
        self, client: Cloudflare
    ) -> None:
        configuration = client.api_gateways.configurations.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_settings_get_information_about_specific_configuration_properties_with_all_params(
        self, client: Cloudflare
    ) -> None:
        configuration = client.api_gateways.configurations.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
            properties=["auth_id_characteristics"],
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_settings_get_information_about_specific_configuration_properties(
        self, client: Cloudflare
    ) -> None:
        response = client.api_gateways.configurations.with_raw_response.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_settings_get_information_about_specific_configuration_properties(
        self, client: Cloudflare
    ) -> None:
        with client.api_gateways.configurations.with_streaming_response.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_settings_get_information_about_specific_configuration_properties(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.configurations.with_raw_response.api_shield_settings_get_information_about_specific_configuration_properties(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_settings_set_configuration_properties(self, client: Cloudflare) -> None:
        configuration = client.api_gateways.configurations.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_api_shield_settings_set_configuration_properties_with_all_params(self, client: Cloudflare) -> None:
        configuration = client.api_gateways.configurations.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_api_shield_settings_set_configuration_properties(self, client: Cloudflare) -> None:
        response = (
            client.api_gateways.configurations.with_raw_response.api_shield_settings_set_configuration_properties(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_api_shield_settings_set_configuration_properties(self, client: Cloudflare) -> None:
        with client.api_gateways.configurations.with_streaming_response.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(
                ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_api_shield_settings_set_configuration_properties(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.api_gateways.configurations.with_raw_response.api_shield_settings_set_configuration_properties(
                "",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_settings_get_information_about_specific_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = await async_client.api_gateways.configurations.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_settings_get_information_about_specific_configuration_properties_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = await async_client.api_gateways.configurations.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
            properties=["auth_id_characteristics"],
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_settings_get_information_about_specific_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.configurations.with_raw_response.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
            configuration,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_settings_get_information_about_specific_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.configurations.with_streaming_response.api_shield_settings_get_information_about_specific_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                ConfigurationAPIShieldSettingsGetInformationAboutSpecificConfigurationPropertiesResponse,
                configuration,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_settings_get_information_about_specific_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.configurations.with_raw_response.api_shield_settings_get_information_about_specific_configuration_properties(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_settings_set_configuration_properties(self, async_client: AsyncCloudflare) -> None:
        configuration = await async_client.api_gateways.configurations.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_api_shield_settings_set_configuration_properties_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        configuration = await async_client.api_gateways.configurations.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
            auth_id_characteristics=[
                {
                    "name": "authorization",
                    "type": "header",
                }
            ],
        )
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_api_shield_settings_set_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.api_gateways.configurations.with_raw_response.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(
            ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_api_shield_settings_set_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.api_gateways.configurations.with_streaming_response.api_shield_settings_set_configuration_properties(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(
                ConfigurationAPIShieldSettingsSetConfigurationPropertiesResponse, configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_api_shield_settings_set_configuration_properties(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.api_gateways.configurations.with_raw_response.api_shield_settings_set_configuration_properties(
                "",
            )