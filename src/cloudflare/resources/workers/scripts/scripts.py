# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .bindings import Bindings, AsyncBindings

from ...._compat import cached_property

from .schedules import Schedules, AsyncSchedules

from .tails import Tails, AsyncTails

from .usage_models import UsageModels, AsyncUsageModels

from ....types.workers import ScriptCreateResponse, ScriptUpdateResponse, ScriptListResponse, script_update_params

from typing import List, Type

from ...._types import FileTypes

from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.workers import script_update_params
from ....types.workers import script_delete_params
from .bindings import (
    Bindings,
    AsyncBindings,
    BindingsWithRawResponse,
    AsyncBindingsWithRawResponse,
    BindingsWithStreamingResponse,
    AsyncBindingsWithStreamingResponse,
)
from .schedules import (
    Schedules,
    AsyncSchedules,
    SchedulesWithRawResponse,
    AsyncSchedulesWithRawResponse,
    SchedulesWithStreamingResponse,
    AsyncSchedulesWithStreamingResponse,
)
from .tails import (
    Tails,
    AsyncTails,
    TailsWithRawResponse,
    AsyncTailsWithRawResponse,
    TailsWithStreamingResponse,
    AsyncTailsWithStreamingResponse,
)
from .usage_models import (
    UsageModels,
    AsyncUsageModels,
    UsageModelsWithRawResponse,
    AsyncUsageModelsWithRawResponse,
    UsageModelsWithStreamingResponse,
    AsyncUsageModelsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Scripts", "AsyncScripts"]


class Scripts(SyncAPIResource):
    @cached_property
    def bindings(self) -> Bindings:
        return Bindings(self._client)

    @cached_property
    def schedules(self) -> Schedules:
        return Schedules(self._client)

    @cached_property
    def tails(self) -> Tails:
        return Tails(self._client)

    @cached_property
    def usage_models(self) -> UsageModels:
        return UsageModels(self._client)

    @cached_property
    def with_raw_response(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self)

    def create(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptCreateResponse:
        """
        Upload a worker, or a new version of a worker.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ScriptCreateResponse,
            self._put(
                f"/zones/{zone_id}/workers/script",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ScriptCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id"])
    def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            body=maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "metadata": metadata,
                    "message": message,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptUpdateResponse], ResultWrapper[ScriptUpdateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptListResponse:
        """
        Fetch a list of uploaded workers.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptListResponse], ResultWrapper[ScriptListResponse]),
        )

    def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your worker.

        This call has no response body on a successful delete.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          force: If set to true, delete will not be stopped by associated service binding,
              durable object, or other binding. Any of these associated bindings/durable
              objects will be deleted along with the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Fetch raw script content for your worker.

        Note this is the original script
        content, not JSON encoded.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScripts(AsyncAPIResource):
    @cached_property
    def bindings(self) -> AsyncBindings:
        return AsyncBindings(self._client)

    @cached_property
    def schedules(self) -> AsyncSchedules:
        return AsyncSchedules(self._client)

    @cached_property
    def tails(self) -> AsyncTails:
        return AsyncTails(self._client)

    @cached_property
    def usage_models(self) -> AsyncUsageModels:
        return AsyncUsageModels(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self)

    async def create(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptCreateResponse:
        """
        Upload a worker, or a new version of a worker.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ScriptCreateResponse,
            await self._put(
                f"/zones/{zone_id}/workers/script",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ScriptCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          any_part_name: A module comprising a Worker script, often a javascript file. Multiple modules
              may be provided as separate named parts, but at least one module must be present
              and referenced in the metadata as `main_module` or `body_part` by part name.

          metadata: JSON encoded metadata about the uploaded parts and Worker configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        """
        Upload a worker module.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          rollback_to: Rollback to provided deployment based on deployment ID. Request body will only
              parse a "message" part. You can learn more about deployments
              [here](https://developers.cloudflare.com/workers/platform/deployments/).

          message: Rollback message to be associated with this deployment. Only parsed when query
              param `"rollback_to"` is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id"], ["account_id"])
    async def update(
        self,
        script_name: str,
        *,
        account_id: str,
        rollback_to: str | NotGiven = NOT_GIVEN,
        any_part_name: List[FileTypes] | NotGiven = NOT_GIVEN,
        metadata: script_update_params.Variant0Metadata | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            body=maybe_transform(
                {
                    "any_part_name": any_part_name,
                    "metadata": metadata,
                    "message": message,
                },
                script_update_params.ScriptUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"rollback_to": rollback_to}, script_update_params.ScriptUpdateParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptUpdateResponse], ResultWrapper[ScriptUpdateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScriptListResponse:
        """
        Fetch a list of uploaded workers.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScriptListResponse], ResultWrapper[ScriptListResponse]),
        )

    async def delete(
        self,
        script_name: str,
        *,
        account_id: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete your worker.

        This call has no response body on a successful delete.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          force: If set to true, delete will not be stopped by associated service binding,
              durable object, or other binding. Any of these associated bindings/durable
              objects will be deleted along with the script.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, script_delete_params.ScriptDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Fetch raw script content for your worker.

        Note this is the original script
        content, not JSON encoded.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScriptsWithRawResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.create = to_raw_response_wrapper(
            scripts.create,
        )
        self.update = to_raw_response_wrapper(
            scripts.update,
        )
        self.list = to_raw_response_wrapper(
            scripts.list,
        )
        self.delete = to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = to_custom_raw_response_wrapper(
            scripts.get,
            BinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> BindingsWithRawResponse:
        return BindingsWithRawResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> SchedulesWithRawResponse:
        return SchedulesWithRawResponse(self._scripts.schedules)

    @cached_property
    def tails(self) -> TailsWithRawResponse:
        return TailsWithRawResponse(self._scripts.tails)

    @cached_property
    def usage_models(self) -> UsageModelsWithRawResponse:
        return UsageModelsWithRawResponse(self._scripts.usage_models)


class AsyncScriptsWithRawResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.create = async_to_raw_response_wrapper(
            scripts.create,
        )
        self.update = async_to_raw_response_wrapper(
            scripts.update,
        )
        self.list = async_to_raw_response_wrapper(
            scripts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_custom_raw_response_wrapper(
            scripts.get,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> AsyncBindingsWithRawResponse:
        return AsyncBindingsWithRawResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> AsyncSchedulesWithRawResponse:
        return AsyncSchedulesWithRawResponse(self._scripts.schedules)

    @cached_property
    def tails(self) -> AsyncTailsWithRawResponse:
        return AsyncTailsWithRawResponse(self._scripts.tails)

    @cached_property
    def usage_models(self) -> AsyncUsageModelsWithRawResponse:
        return AsyncUsageModelsWithRawResponse(self._scripts.usage_models)


class ScriptsWithStreamingResponse:
    def __init__(self, scripts: Scripts) -> None:
        self._scripts = scripts

        self.create = to_streamed_response_wrapper(
            scripts.create,
        )
        self.update = to_streamed_response_wrapper(
            scripts.update,
        )
        self.list = to_streamed_response_wrapper(
            scripts.list,
        )
        self.delete = to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = to_custom_streamed_response_wrapper(
            scripts.get,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> BindingsWithStreamingResponse:
        return BindingsWithStreamingResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> SchedulesWithStreamingResponse:
        return SchedulesWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tails(self) -> TailsWithStreamingResponse:
        return TailsWithStreamingResponse(self._scripts.tails)

    @cached_property
    def usage_models(self) -> UsageModelsWithStreamingResponse:
        return UsageModelsWithStreamingResponse(self._scripts.usage_models)


class AsyncScriptsWithStreamingResponse:
    def __init__(self, scripts: AsyncScripts) -> None:
        self._scripts = scripts

        self.create = async_to_streamed_response_wrapper(
            scripts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            scripts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scripts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scripts.delete,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            scripts.get,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def bindings(self) -> AsyncBindingsWithStreamingResponse:
        return AsyncBindingsWithStreamingResponse(self._scripts.bindings)

    @cached_property
    def schedules(self) -> AsyncSchedulesWithStreamingResponse:
        return AsyncSchedulesWithStreamingResponse(self._scripts.schedules)

    @cached_property
    def tails(self) -> AsyncTailsWithStreamingResponse:
        return AsyncTailsWithStreamingResponse(self._scripts.tails)

    @cached_property
    def usage_models(self) -> AsyncUsageModelsWithStreamingResponse:
        return AsyncUsageModelsWithStreamingResponse(self._scripts.usage_models)