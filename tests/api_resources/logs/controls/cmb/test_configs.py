# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.logs.controls.cmb import (
    ConfigDeleteResponse,
    ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse,
    ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logs.controls.cmb import config_put_accounts_account_identifier_logs_control_cmb_config_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        config = client.logs.controls.cmb.configs.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.logs.controls.cmb.configs.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.logs.controls.cmb.configs.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logs.controls.cmb.configs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        config = client.logs.controls.cmb.configs.get_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        response = (
            client.logs.controls.cmb.configs.with_raw_response.get_accounts_account_identifier_logs_control_cmb_config(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_accounts_account_identifier_logs_control_cmb_config(
        self, client: Cloudflare
    ) -> None:
        with client.logs.controls.cmb.configs.with_streaming_response.get_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logs.controls.cmb.configs.with_raw_response.get_accounts_account_identifier_logs_control_cmb_config(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_put_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        config = client.logs.controls.cmb.configs.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_put_accounts_account_identifier_logs_control_cmb_config_with_all_params(
        self, client: Cloudflare
    ) -> None:
        config = client.logs.controls.cmb.configs.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regions="eu",
        )
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_put_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        response = (
            client.logs.controls.cmb.configs.with_raw_response.put_accounts_account_identifier_logs_control_cmb_config(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_put_accounts_account_identifier_logs_control_cmb_config(
        self, client: Cloudflare
    ) -> None:
        with client.logs.controls.cmb.configs.with_streaming_response.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(
                Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_put_accounts_account_identifier_logs_control_cmb_config(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.logs.controls.cmb.configs.with_raw_response.put_accounts_account_identifier_logs_control_cmb_config(
                "",
            )


class TestAsyncConfigs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.logs.controls.cmb.configs.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.controls.cmb.configs.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.controls.cmb.configs.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Optional[ConfigDeleteResponse], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logs.controls.cmb.configs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.logs.controls.cmb.configs.get_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.logs.controls.cmb.configs.with_raw_response.get_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logs.controls.cmb.configs.with_streaming_response.get_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logs.controls.cmb.configs.with_raw_response.get_accounts_account_identifier_logs_control_cmb_config(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_put_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.logs.controls.cmb.configs.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_put_accounts_account_identifier_logs_control_cmb_config_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        config = await async_client.logs.controls.cmb.configs.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
            regions="eu",
        )
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_put_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.logs.controls.cmb.configs.with_raw_response.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(
            Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_put_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.logs.controls.cmb.configs.with_streaming_response.put_accounts_account_identifier_logs_control_cmb_config(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(
                Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse], config, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_put_accounts_account_identifier_logs_control_cmb_config(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.logs.controls.cmb.configs.with_raw_response.put_accounts_account_identifier_logs_control_cmb_config(
                "",
            )