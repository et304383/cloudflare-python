# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.zaraz import WorkflowGetResponse

from typing import Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Workflow", "AsyncWorkflow"]


class Workflow(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowWithRawResponse:
        return WorkflowWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowWithStreamingResponse:
        return WorkflowWithStreamingResponse(self)

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowGetResponse:
        """
        Gets Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkflowGetResponse], ResultWrapper[WorkflowGetResponse]),
        )


class AsyncWorkflow(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowWithRawResponse:
        return AsyncWorkflowWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowWithStreamingResponse:
        return AsyncWorkflowWithStreamingResponse(self)

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowGetResponse:
        """
        Gets Zaraz workflow for a zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/workflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[WorkflowGetResponse], ResultWrapper[WorkflowGetResponse]),
        )


class WorkflowWithRawResponse:
    def __init__(self, workflow: Workflow) -> None:
        self._workflow = workflow

        self.get = to_raw_response_wrapper(
            workflow.get,
        )


class AsyncWorkflowWithRawResponse:
    def __init__(self, workflow: AsyncWorkflow) -> None:
        self._workflow = workflow

        self.get = async_to_raw_response_wrapper(
            workflow.get,
        )


class WorkflowWithStreamingResponse:
    def __init__(self, workflow: Workflow) -> None:
        self._workflow = workflow

        self.get = to_streamed_response_wrapper(
            workflow.get,
        )


class AsyncWorkflowWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflow) -> None:
        self._workflow = workflow

        self.get = async_to_streamed_response_wrapper(
            workflow.get,
        )