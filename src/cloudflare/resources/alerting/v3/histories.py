# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.alerting.v3 import HistoryListResponse, history_list_params

__all__ = ["Histories", "AsyncHistories"]


class Histories(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[HistoryListResponse]:
        """Gets a list of history records for notifications sent to an account.

        The records
        are displayed for last `x` number of days based on the zone plan (free = 30, pro
        = 30, biz = 30, ent = 90).

        Args:
          account_id: The account id

          before: Limit the returned results to history records older than the specified date.
              This must be a timestamp that conforms to RFC3339.

          page: Page number of paginated results.

          per_page: Number of items per page.

          since: Limit the returned results to history records newer than the specified date.
              This must be a timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/history",
            page=SyncV4PagePaginationArray[HistoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )


class AsyncHistories(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        since: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[HistoryListResponse, AsyncV4PagePaginationArray[HistoryListResponse]]:
        """Gets a list of history records for notifications sent to an account.

        The records
        are displayed for last `x` number of days based on the zone plan (free = 30, pro
        = 30, biz = 30, ent = 90).

        Args:
          account_id: The account id

          before: Limit the returned results to history records older than the specified date.
              This must be a timestamp that conforms to RFC3339.

          page: Page number of paginated results.

          per_page: Number of items per page.

          since: Limit the returned results to history records newer than the specified date.
              This must be a timestamp that conforms to RFC3339.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/alerting/v3/history",
            page=AsyncV4PagePaginationArray[HistoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "before": before,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            model=HistoryListResponse,
        )


class HistoriesWithRawResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.list = to_raw_response_wrapper(
            histories.list,
        )


class AsyncHistoriesWithRawResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.list = async_to_raw_response_wrapper(
            histories.list,
        )


class HistoriesWithStreamingResponse:
    def __init__(self, histories: Histories) -> None:
        self._histories = histories

        self.list = to_streamed_response_wrapper(
            histories.list,
        )


class AsyncHistoriesWithStreamingResponse:
    def __init__(self, histories: AsyncHistories) -> None:
        self._histories = histories

        self.list = async_to_streamed_response_wrapper(
            histories.list,
        )