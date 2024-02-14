# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.users.load_balancers.pools import ReferenceLoadBalancerPoolsListPoolReferencesResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_pools_list_pool_references(self, client: Cloudflare) -> None:
        reference = client.users.load_balancers.pools.references.load_balancer_pools_list_pool_references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(
            Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_pools_list_pool_references(self, client: Cloudflare) -> None:
        response = (
            client.users.load_balancers.pools.references.with_raw_response.load_balancer_pools_list_pool_references(
                "17b5962d775c646f3f9725cbc7a53df4",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(
            Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_pools_list_pool_references(self, client: Cloudflare) -> None:
        with client.users.load_balancers.pools.references.with_streaming_response.load_balancer_pools_list_pool_references(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(
                Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_load_balancer_pools_list_pool_references(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.load_balancers.pools.references.with_raw_response.load_balancer_pools_list_pool_references(
                "",
            )


class TestAsyncReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_pools_list_pool_references(self, async_client: AsyncCloudflare) -> None:
        reference = await async_client.users.load_balancers.pools.references.load_balancer_pools_list_pool_references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )
        assert_matches_type(
            Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_pools_list_pool_references(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.load_balancers.pools.references.with_raw_response.load_balancer_pools_list_pool_references(
            "17b5962d775c646f3f9725cbc7a53df4",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(
            Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_pools_list_pool_references(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancers.pools.references.with_streaming_response.load_balancer_pools_list_pool_references(
            "17b5962d775c646f3f9725cbc7a53df4",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(
                Optional[ReferenceLoadBalancerPoolsListPoolReferencesResponse], reference, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_load_balancer_pools_list_pool_references(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.load_balancers.pools.references.with_raw_response.load_balancer_pools_list_pool_references(
                "",
            )