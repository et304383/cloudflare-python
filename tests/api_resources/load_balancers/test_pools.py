# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.load_balancers import (
    PoolUpdateResponse,
    PoolDeleteResponse,
    PoolAccountLoadBalancerPoolsCreatePoolResponse,
    PoolAccountLoadBalancerPoolsListPoolsResponse,
    PoolAccountLoadBalancerPoolsPatchPoolsResponse,
    PoolGetResponse,
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
from cloudflare.types.load_balancers import pool_update_params
from cloudflare.types.load_balancers import pool_account_load_balancer_pools_create_pool_params
from cloudflare.types.load_balancers import pool_account_load_balancer_pools_list_pools_params
from cloudflare.types.load_balancers import pool_account_load_balancer_pools_patch_pools_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolUpdateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.update(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.delete(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_create_pool(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_create_pool_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_load_balancer_pools_create_pool(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_load_balancer_pools_create_pool(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_load_balancer_pools_create_pool(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.account_load_balancer_pools_create_pool(
                "",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_list_pools(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_list_pools_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
            monitor={},
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_load_balancer_pools_list_pools(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_load_balancer_pools_list_pools(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_load_balancer_pools_list_pools(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.account_load_balancer_pools_list_pools(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_patch_pools(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_patch_pools_with_all_params(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_email='""',
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_load_balancer_pools_patch_pools(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_load_balancer_pools_patch_pools(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_load_balancer_pools_patch_pools(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.account_load_balancer_pools_patch_pools(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pool = client.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.get(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.load_balancers.pools.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            check_regions=["WEU", "ENAM"],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolUpdateResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.update(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolUpdateResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.update(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolDeleteResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.delete(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolDeleteResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.delete(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_create_pool(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_create_pool_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
                {
                    "address": "0.0.0.0",
                    "enabled": True,
                    "header": {"host": ["example.com", "example.com", "example.com"]},
                    "name": "app-server-1",
                    "virtual_network_id": "a5624d4e-044a-4ff0-b3e1-e2465353d4b4",
                    "weight": 0.6,
                },
            ],
            description="Primary data center - Provider XYZ",
            enabled=False,
            latitude=0,
            load_shedding={
                "default_percent": 0,
                "default_policy": "random",
                "session_percent": 0,
                "session_policy": "hash",
            },
            longitude=0,
            minimum_origins=0,
            monitor={},
            notification_email="someone@example.com,sometwo@example.com",
            notification_filter={
                "origin": {
                    "disable": True,
                    "healthy": True,
                },
                "pool": {
                    "disable": True,
                    "healthy": False,
                },
            },
            origin_steering={"policy": "random"},
        )
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_load_balancer_pools_create_pool(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_load_balancer_pools_create_pool(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_create_pool(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="primary-dc-1",
            origins=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolAccountLoadBalancerPoolsCreatePoolResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_load_balancer_pools_create_pool(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_create_pool(
                "",
                name="primary-dc-1",
                origins=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_list_pools(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_list_pools_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
            monitor={},
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_load_balancer_pools_list_pools(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_load_balancer_pools_list_pools(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_list_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(Optional[PoolAccountLoadBalancerPoolsListPoolsResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_load_balancer_pools_list_pools(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_list_pools(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_patch_pools(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_patch_pools_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        pool = await async_client.load_balancers.pools.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_email='""',
        )
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_load_balancer_pools_patch_pools(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_load_balancer_pools_patch_pools(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.account_load_balancer_pools_patch_pools(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(Optional[PoolAccountLoadBalancerPoolsPatchPoolsResponse], pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_load_balancer_pools_patch_pools(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.account_load_balancer_pools_patch_pools(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pool = await async_client.load_balancers.pools.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.load_balancers.pools.with_raw_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pool = await response.parse()
        assert_matches_type(PoolGetResponse, pool, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.pools.with_streaming_response.get(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pool = await response.parse()
            assert_matches_type(PoolGetResponse, pool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.get(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.load_balancers.pools.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )