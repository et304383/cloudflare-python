# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.rules.lists import (
    ItemDeleteResponse,
    ItemGetResponse,
    ItemListsCreateListItemsResponse,
    ItemListsGetListItemsResponse,
    ItemListsUpdateAllListItemsResponse,
    item_delete_params,
    item_lists_create_list_items_params,
    item_lists_update_all_list_items_params,
)

from typing import Type, Optional, Iterable

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
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
from ....types.rules.lists import item_delete_params
from ....types.rules.lists import item_lists_create_list_items_params
from ....types.rules.lists import item_lists_get_list_items_params
from ....types.rules.lists import item_lists_update_all_list_items_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Items", "AsyncItems"]


class Items(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsWithRawResponse:
        return ItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsWithStreamingResponse:
        return ItemsWithStreamingResponse(self)

    def delete(
        self,
        list_id: str,
        *,
        account_id: str,
        items: Iterable[item_delete_params.Item] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemDeleteResponse]:
        """Removes one or more items from a list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._delete(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform({"items": items}, item_delete_params.ItemDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemDeleteResponse]], ResultWrapper[ItemDeleteResponse]),
        )

    def get(
        self,
        item_id: str,
        *,
        account_identifier: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemGetResponse]:
        """
        Fetches a list item in the list.

        Args:
          account_identifier: Identifier

          list_id: The unique ID of the list.

          item_id: The unique ID of the item in the List.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return cast(
            Optional[ItemGetResponse],
            self._get(
                f"/accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ItemGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def lists_create_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_lists_create_list_items_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsCreateListItemsResponse]:
        """Appends new items to the list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._post(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, item_lists_create_list_items_params.ItemListsCreateListItemsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ItemListsCreateListItemsResponse]], ResultWrapper[ItemListsCreateListItemsResponse]
            ),
        )

    def lists_get_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsGetListItemsResponse]:
        """
        Fetches all the items in the list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          cursor: The pagination cursor. An opaque string token indicating the position from which
              to continue when requesting the next/previous set of records. Cursor values are
              provided under `result_info.cursors` in the response. You should make no
              assumptions about a cursor's content or length.

          per_page: Amount of results to include in each paginated response. A non-negative 32 bit
              integer.

          search:
              A search query to filter returned items. Its meaning depends on the list type:
              IP addresses must start with the provided string, hostnames and bulk redirects
              must contain the string, and ASNs must match the string exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._get(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "search": search,
                    },
                    item_lists_get_list_items_params.ItemListsGetListItemsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemListsGetListItemsResponse]], ResultWrapper[ItemListsGetListItemsResponse]),
        )

    def lists_update_all_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_lists_update_all_list_items_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsUpdateAllListItemsResponse]:
        """
        Removes all existing items from the list and adds the provided items to the
        list.

        This operation is asynchronous. To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return self._put(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, item_lists_update_all_list_items_params.ItemListsUpdateAllListItemsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ItemListsUpdateAllListItemsResponse]], ResultWrapper[ItemListsUpdateAllListItemsResponse]
            ),
        )


class AsyncItems(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsWithRawResponse:
        return AsyncItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsWithStreamingResponse:
        return AsyncItemsWithStreamingResponse(self)

    async def delete(
        self,
        list_id: str,
        *,
        account_id: str,
        items: Iterable[item_delete_params.Item] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemDeleteResponse]:
        """Removes one or more items from a list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform({"items": items}, item_delete_params.ItemDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemDeleteResponse]], ResultWrapper[ItemDeleteResponse]),
        )

    async def get(
        self,
        item_id: str,
        *,
        account_identifier: str,
        list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemGetResponse]:
        """
        Fetches a list item in the list.

        Args:
          account_identifier: Identifier

          list_id: The unique ID of the list.

          item_id: The unique ID of the item in the List.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return cast(
            Optional[ItemGetResponse],
            await self._get(
                f"/accounts/{account_identifier}/rules/lists/{list_id}/items/{item_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ItemGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def lists_create_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_lists_create_list_items_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsCreateListItemsResponse]:
        """Appends new items to the list.

        This operation is asynchronous.

        To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._post(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, item_lists_create_list_items_params.ItemListsCreateListItemsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ItemListsCreateListItemsResponse]], ResultWrapper[ItemListsCreateListItemsResponse]
            ),
        )

    async def lists_get_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsGetListItemsResponse]:
        """
        Fetches all the items in the list.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          cursor: The pagination cursor. An opaque string token indicating the position from which
              to continue when requesting the next/previous set of records. Cursor values are
              provided under `result_info.cursors` in the response. You should make no
              assumptions about a cursor's content or length.

          per_page: Amount of results to include in each paginated response. A non-negative 32 bit
              integer.

          search:
              A search query to filter returned items. Its meaning depends on the list type:
              IP addresses must start with the provided string, hostnames and bulk redirects
              must contain the string, and ASNs must match the string exactly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._get(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                        "search": search,
                    },
                    item_lists_get_list_items_params.ItemListsGetListItemsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemListsGetListItemsResponse]], ResultWrapper[ItemListsGetListItemsResponse]),
        )

    async def lists_update_all_list_items(
        self,
        list_id: str,
        *,
        account_id: str,
        body: Iterable[item_lists_update_all_list_items_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ItemListsUpdateAllListItemsResponse]:
        """
        Removes all existing items from the list and adds the provided items to the
        list.

        This operation is asynchronous. To get current the operation status, invoke the
        [Get bulk operation status](/operations/lists-get-bulk-operation-status)
        endpoint with the returned `operation_id`.

        Args:
          account_id: Identifier

          list_id: The unique ID of the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not list_id:
            raise ValueError(f"Expected a non-empty value for `list_id` but received {list_id!r}")
        return await self._put(
            f"/accounts/{account_id}/rules/lists/{list_id}/items",
            body=maybe_transform(body, item_lists_update_all_list_items_params.ItemListsUpdateAllListItemsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ItemListsUpdateAllListItemsResponse]], ResultWrapper[ItemListsUpdateAllListItemsResponse]
            ),
        )


class ItemsWithRawResponse:
    def __init__(self, items: Items) -> None:
        self._items = items

        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.get = to_raw_response_wrapper(
            items.get,
        )
        self.lists_create_list_items = to_raw_response_wrapper(
            items.lists_create_list_items,
        )
        self.lists_get_list_items = to_raw_response_wrapper(
            items.lists_get_list_items,
        )
        self.lists_update_all_list_items = to_raw_response_wrapper(
            items.lists_update_all_list_items,
        )


class AsyncItemsWithRawResponse:
    def __init__(self, items: AsyncItems) -> None:
        self._items = items

        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.get = async_to_raw_response_wrapper(
            items.get,
        )
        self.lists_create_list_items = async_to_raw_response_wrapper(
            items.lists_create_list_items,
        )
        self.lists_get_list_items = async_to_raw_response_wrapper(
            items.lists_get_list_items,
        )
        self.lists_update_all_list_items = async_to_raw_response_wrapper(
            items.lists_update_all_list_items,
        )


class ItemsWithStreamingResponse:
    def __init__(self, items: Items) -> None:
        self._items = items

        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.get = to_streamed_response_wrapper(
            items.get,
        )
        self.lists_create_list_items = to_streamed_response_wrapper(
            items.lists_create_list_items,
        )
        self.lists_get_list_items = to_streamed_response_wrapper(
            items.lists_get_list_items,
        )
        self.lists_update_all_list_items = to_streamed_response_wrapper(
            items.lists_update_all_list_items,
        )


class AsyncItemsWithStreamingResponse:
    def __init__(self, items: AsyncItems) -> None:
        self._items = items

        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            items.get,
        )
        self.lists_create_list_items = async_to_streamed_response_wrapper(
            items.lists_create_list_items,
        )
        self.lists_get_list_items = async_to_streamed_response_wrapper(
            items.lists_get_list_items,
        )
        self.lists_update_all_list_items = async_to_streamed_response_wrapper(
            items.lists_update_all_list_items,
        )