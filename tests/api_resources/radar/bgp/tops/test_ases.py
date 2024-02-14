# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.bgp.tops import AseListResponse, AsePrefixesResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.bgp.tops import ase_list_params
from cloudflare.types.radar.bgp.tops import ase_prefixes_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.tops.ases.list()
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.tops.ases.list(
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
            prefix=["string", "string", "string"],
            update_type=["ANNOUNCEMENT", "WITHDRAWAL"],
        )
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.bgp.tops.ases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = response.parse()
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.bgp.tops.ases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = response.parse()
            assert_matches_type(AseListResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_prefixes(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.tops.ases.prefixes()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_prefixes_with_all_params(self, client: Cloudflare) -> None:
        ase = client.radar.bgp.tops.ases.prefixes(
            country="NZ",
            format="JSON",
            limit=10,
        )
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_prefixes(self, client: Cloudflare) -> None:
        response = client.radar.bgp.tops.ases.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = response.parse()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_prefixes(self, client: Cloudflare) -> None:
        with client.radar.bgp.tops.ases.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = response.parse()
            assert_matches_type(AsePrefixesResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.tops.ases.list()
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.tops.ases.list(
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            name=["string", "string", "string"],
            prefix=["string", "string", "string"],
            update_type=["ANNOUNCEMENT", "WITHDRAWAL"],
        )
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.tops.ases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = await response.parse()
        assert_matches_type(AseListResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.tops.ases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = await response.parse()
            assert_matches_type(AseListResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_prefixes(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.tops.ases.prefixes()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_prefixes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ase = await async_client.radar.bgp.tops.ases.prefixes(
            country="NZ",
            format="JSON",
            limit=10,
        )
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.bgp.tops.ases.with_raw_response.prefixes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ase = await response.parse()
        assert_matches_type(AsePrefixesResponse, ase, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_prefixes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.bgp.tops.ases.with_streaming_response.prefixes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ase = await response.parse()
            assert_matches_type(AsePrefixesResponse, ase, path=["response"])

        assert cast(Any, response.is_closed) is True