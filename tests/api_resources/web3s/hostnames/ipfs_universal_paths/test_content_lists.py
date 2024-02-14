# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.web3s.hostnames.ipfs_universal_paths import (
    ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse,
    ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse,
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
from cloudflare.types.web3s.hostnames.ipfs_universal_paths import (
    content_list_web3_hostname_update_ipfs_universal_path_gateway_content_list_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_ipfs_universal_path_gateway_content_list_details(self, client: Cloudflare) -> None:
        content_list = client.web3s.hostnames.ipfs_universal_paths.content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, client: Cloudflare
    ) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = response.parse()
        assert_matches_type(
            ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, client: Cloudflare
    ) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = response.parse()
            assert_matches_type(
                ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse,
                content_list,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_update_ipfs_universal_path_gateway_content_list(self, client: Cloudflare) -> None:
        content_list = client.web3s.hostnames.ipfs_universal_paths.content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        )
        assert_matches_type(
            ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, client: Cloudflare
    ) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = response.parse()
        assert_matches_type(
            ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, client: Cloudflare
    ) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = response.parse()
            assert_matches_type(
                ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse,
                content_list,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                action="block",
                entries=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action="block",
                entries=[{}, {}, {}],
            )


class TestAsyncContentLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        content_list = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = await response.parse()
        assert_matches_type(
            ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = await response.parse()
            assert_matches_type(
                ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse,
                content_list,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_ipfs_universal_path_gateway_content_list_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_ipfs_universal_path_gateway_content_list_details(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        content_list = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        )
        assert_matches_type(
            ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = await response.parse()
        assert_matches_type(
            ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse, content_list, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = await response.parse()
            assert_matches_type(
                ContentListWeb3HostnameUpdateIpfsUniversalPathGatewayContentListResponse,
                content_list,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_update_ipfs_universal_path_gateway_content_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                action="block",
                entries=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.with_raw_response.web3_hostname_update_ipfs_universal_path_gateway_content_list(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                action="block",
                entries=[{}, {}, {}],
            )