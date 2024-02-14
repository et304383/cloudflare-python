# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers import (
    RouteUpdateResponse,
    RouteDeleteResponse,
    RouteGetResponse,
    RouteWorkerRoutesCreateRouteResponse,
    RouteWorkerRoutesListRoutesResponse,
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
from cloudflare.types.workers import route_update_params
from cloudflare.types.workers import route_worker_routes_create_route_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        route = client.workers.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        route = client.workers.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
            script="this-is_my_script-01",
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.routes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.routes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.routes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                pattern="example.net/*",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.workers.routes.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        route = client.workers.routes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.routes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.routes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.routes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.workers.routes.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        route = client.workers.routes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.routes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.routes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteGetResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.routes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.workers.routes.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_routes_create_route(self, client: Cloudflare) -> None:
        route = client.workers.routes.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_routes_create_route_with_all_params(self, client: Cloudflare) -> None:
        route = client.workers.routes.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
            script="this-is_my_script-01",
        )
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_routes_create_route(self, client: Cloudflare) -> None:
        response = client.workers.routes.with_raw_response.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_routes_create_route(self, client: Cloudflare) -> None:
        with client.workers.routes.with_streaming_response.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_routes_create_route(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.routes.with_raw_response.worker_routes_create_route(
                "",
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_routes_list_routes(self, client: Cloudflare) -> None:
        route = client.workers.routes.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_routes_list_routes(self, client: Cloudflare) -> None:
        response = client.workers.routes.with_raw_response.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_routes_list_routes(self, client: Cloudflare) -> None:
        with client.workers.routes.with_streaming_response.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_routes_list_routes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.routes.with_raw_response.worker_routes_list_routes(
                "",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
            script="this-is_my_script-01",
        )
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.routes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteUpdateResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.routes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteUpdateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.routes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                pattern="example.net/*",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.workers.routes.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.routes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteDeleteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.routes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteDeleteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.routes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.workers.routes.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.routes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteGetResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.routes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteGetResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.routes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.workers.routes.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_routes_create_route(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_routes_create_route_with_all_params(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
            script="this-is_my_script-01",
        )
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_routes_create_route(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.routes.with_raw_response.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_routes_create_route(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.routes.with_streaming_response.worker_routes_create_route(
            "023e105f4ecef8ad9ca31a8372d0c353",
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteWorkerRoutesCreateRouteResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_routes_create_route(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.routes.with_raw_response.worker_routes_create_route(
                "",
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        route = await async_client.workers.routes.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.routes.with_raw_response.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.routes.with_streaming_response.worker_routes_list_routes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteWorkerRoutesListRoutesResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_routes_list_routes(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.routes.with_raw_response.worker_routes_list_routes(
                "",
            )