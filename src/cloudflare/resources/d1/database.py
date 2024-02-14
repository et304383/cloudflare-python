# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.d1 import DatabaseDeleteResponse, DatabaseGetResponse, DatabaseQueryResponse

from typing import Optional, Type, List

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
from ...types.d1 import database_query_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Database", "AsyncDatabase"]


class Database(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabaseWithRawResponse:
        return DatabaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabaseWithStreamingResponse:
        return DatabaseWithStreamingResponse(self)

    def delete(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatabaseDeleteResponse]:
        """
        Deletes the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return cast(
            Optional[DatabaseDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DatabaseDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseGetResponse:
        """
        Returns the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return self._get(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseGetResponse], ResultWrapper[DatabaseGetResponse]),
        )

    def query(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseQueryResponse:
        """
        Returns the query result.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return self._post(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}/query",
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
        )


class AsyncDatabase(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabaseWithRawResponse:
        return AsyncDatabaseWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabaseWithStreamingResponse:
        return AsyncDatabaseWithStreamingResponse(self)

    async def delete(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DatabaseDeleteResponse]:
        """
        Deletes the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return cast(
            Optional[DatabaseDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/d1/database/{database_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[DatabaseDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseGetResponse:
        """
        Returns the specified D1 database.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return await self._get(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseGetResponse], ResultWrapper[DatabaseGetResponse]),
        )

    async def query(
        self,
        database_identifier: str,
        *,
        account_identifier: str,
        sql: str,
        params: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseQueryResponse:
        """
        Returns the query result.

        Args:
          account_identifier: Account identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not database_identifier:
            raise ValueError(
                f"Expected a non-empty value for `database_identifier` but received {database_identifier!r}"
            )
        return await self._post(
            f"/accounts/{account_identifier}/d1/database/{database_identifier}/query",
            body=maybe_transform(
                {
                    "sql": sql,
                    "params": params,
                },
                database_query_params.DatabaseQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DatabaseQueryResponse], ResultWrapper[DatabaseQueryResponse]),
        )


class DatabaseWithRawResponse:
    def __init__(self, database: Database) -> None:
        self._database = database

        self.delete = to_raw_response_wrapper(
            database.delete,
        )
        self.get = to_raw_response_wrapper(
            database.get,
        )
        self.query = to_raw_response_wrapper(
            database.query,
        )


class AsyncDatabaseWithRawResponse:
    def __init__(self, database: AsyncDatabase) -> None:
        self._database = database

        self.delete = async_to_raw_response_wrapper(
            database.delete,
        )
        self.get = async_to_raw_response_wrapper(
            database.get,
        )
        self.query = async_to_raw_response_wrapper(
            database.query,
        )


class DatabaseWithStreamingResponse:
    def __init__(self, database: Database) -> None:
        self._database = database

        self.delete = to_streamed_response_wrapper(
            database.delete,
        )
        self.get = to_streamed_response_wrapper(
            database.get,
        )
        self.query = to_streamed_response_wrapper(
            database.query,
        )


class AsyncDatabaseWithStreamingResponse:
    def __init__(self, database: AsyncDatabase) -> None:
        self._database = database

        self.delete = async_to_streamed_response_wrapper(
            database.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            database.get,
        )
        self.query = async_to_streamed_response_wrapper(
            database.query,
        )