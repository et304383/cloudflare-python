# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.web3s import (
    HostnameUpdateResponse,
    HostnameDeleteResponse,
    HostnameGetResponse,
    HostnameWeb3HostnameCreateWeb3HostnameResponse,
    HostnameWeb3HostnameListWeb3HostnamesResponse,
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
from cloudflare.types.web3s import hostname_update_params
from cloudflare.types.web3s import hostname_web3_hostname_create_web3_hostname_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostnames:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my IPFS gateway.",
            dnslink="/ipns/onboarding.ipfs.cloudflare.com",
        )
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = response.parse()
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = response.parse()
            assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = response.parse()
        assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = response.parse()
            assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HostnameGetResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = response.parse()
        assert_matches_type(HostnameGetResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = response.parse()
            assert_matches_type(HostnameGetResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_create_web3_hostname(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        )
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_create_web3_hostname_with_all_params(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
            description="This is my IPFS gateway.",
            dnslink="/ipns/onboarding.ipfs.cloudflare.com",
        )
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_create_web3_hostname(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.with_raw_response.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = response.parse()
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_create_web3_hostname(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.with_streaming_response.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = response.parse()
            assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_create_web3_hostname(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.web3_hostname_create_web3_hostname(
                "",
                target="ipfs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_list_web3_hostnames(self, client: Cloudflare) -> None:
        hostname = client.web3s.hostnames.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_list_web3_hostnames(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.with_raw_response.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = response.parse()
        assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_list_web3_hostnames(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.with_streaming_response.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = response.parse()
            assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_list_web3_hostnames(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.with_raw_response.web3_hostname_list_web3_hostnames(
                "",
            )


class TestAsyncHostnames:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my IPFS gateway.",
            dnslink="/ipns/onboarding.ipfs.cloudflare.com",
        )
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = await response.parse()
        assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = await response.parse()
            assert_matches_type(HostnameUpdateResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = await response.parse()
        assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = await response.parse()
            assert_matches_type(Optional[HostnameDeleteResponse], hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HostnameGetResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = await response.parse()
        assert_matches_type(HostnameGetResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = await response.parse()
            assert_matches_type(HostnameGetResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_create_web3_hostname(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        )
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_create_web3_hostname_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        hostname = await async_client.web3s.hostnames.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
            description="This is my IPFS gateway.",
            dnslink="/ipns/onboarding.ipfs.cloudflare.com",
        )
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_create_web3_hostname(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.with_raw_response.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = await response.parse()
        assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_create_web3_hostname(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.with_streaming_response.web3_hostname_create_web3_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            target="ipfs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = await response.parse()
            assert_matches_type(HostnameWeb3HostnameCreateWeb3HostnameResponse, hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_create_web3_hostname(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.web3_hostname_create_web3_hostname(
                "",
                target="ipfs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_list_web3_hostnames(self, async_client: AsyncCloudflare) -> None:
        hostname = await async_client.web3s.hostnames.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_list_web3_hostnames(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.with_raw_response.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hostname = await response.parse()
        assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_list_web3_hostnames(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.with_streaming_response.web3_hostname_list_web3_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hostname = await response.parse()
            assert_matches_type(Optional[HostnameWeb3HostnameListWeb3HostnamesResponse], hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_list_web3_hostnames(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.with_raw_response.web3_hostname_list_web3_hostnames(
                "",
            )