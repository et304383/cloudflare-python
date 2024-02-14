# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.vectorize import (
    IndexCreateResponse,
    IndexUpdateResponse,
    IndexListResponse,
    IndexDeleteResponse,
    IndexDeleteByIDsResponse,
    IndexGetResponse,
    IndexInsertResponse,
    IndexQueryResponse,
    IndexUpsertResponse,
    index_create_params,
)

from typing import Type, Optional, List, Iterable

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
from ...types.vectorize import index_create_params
from ...types.vectorize import index_update_params
from ...types.vectorize import index_delete_by_ids_params
from ...types.vectorize import index_get_by_ids_params
from ...types.vectorize import index_query_params
from ..._wrappers import ResultWrapper
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

__all__ = ["Indexes", "AsyncIndexes"]


class Indexes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndexesWithRawResponse:
        return IndexesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndexesWithStreamingResponse:
        return IndexesWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        config: index_create_params.Config,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexCreateResponse]:
        """
        Creates and returns a new Vectorize Index.

        Args:
          account_identifier: Identifier

          config: Specifies the type of configuration to use for the index.

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "description": description,
                },
                index_create_params.IndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexCreateResponse]], ResultWrapper[IndexCreateResponse]),
        )

    def update(
        self,
        index_name: str,
        *,
        account_identifier: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpdateResponse]:
        """
        Updates and returns the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._put(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
            body=maybe_transform({"description": description}, index_update_params.IndexUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpdateResponse]], ResultWrapper[IndexUpdateResponse]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexListResponse:
        """
        Returns a list of Vectorize Indexes

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/vectorize/indexes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndexListResponse], ResultWrapper[IndexListResponse]),
        )

    def delete(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteResponse]:
        """
        Deletes the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return cast(
            Optional[IndexDeleteResponse],
            self._delete(
                f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IndexDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete_by_ids(
        self,
        index_name: str,
        *,
        account_identifier: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteByIDsResponse]:
        """
        Delete a set of vectors from an index by their vector identifiers.

        Args:
          account_identifier: Identifier

          ids: A list of vector identifiers to delete from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/delete-by-ids",
            body=maybe_transform({"ids": ids}, index_delete_by_ids_params.IndexDeleteByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexDeleteByIDsResponse]], ResultWrapper[IndexDeleteByIDsResponse]),
        )

    def get(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexGetResponse]:
        """
        Returns the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._get(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexGetResponse]], ResultWrapper[IndexGetResponse]),
        )

    def get_by_ids(
        self,
        index_name: str,
        *,
        account_identifier: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get a set of vectors from an index by their vector identifiers.

        Args:
          account_identifier: Identifier

          ids: A list of vector identifiers to retrieve from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/get-by-ids",
            body=maybe_transform({"ids": ids}, index_get_by_ids_params.IndexGetByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def insert(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInsertResponse]:
        """
        Inserts vectors into the specified index and returns the count of the vectors
        successfully inserted.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/insert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInsertResponse]], ResultWrapper[IndexInsertResponse]),
        )

    def query(
        self,
        index_name: str,
        *,
        account_identifier: str,
        return_metadata: bool | NotGiven = NOT_GIVEN,
        return_values: bool | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexQueryResponse]:
        """
        Finds vectors closest to a given vector in an index.

        Args:
          account_identifier: Identifier

          return_metadata: Whether to return the metadata associated with the closest vectors.

          return_values: Whether to return the values associated with the closest vectors.

          top_k: The number of nearest neighbors to find.

          vector: The search vector that will be used to find the nearest neighbors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/query",
            body=maybe_transform(
                {
                    "return_metadata": return_metadata,
                    "return_values": return_values,
                    "top_k": top_k,
                    "vector": vector,
                },
                index_query_params.IndexQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexQueryResponse]], ResultWrapper[IndexQueryResponse]),
        )

    def upsert(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpsertResponse]:
        """
        Upserts vectors into the specified index, creating them if they do not exist and
        returns the count of values and ids successfully inserted.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/upsert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpsertResponse]], ResultWrapper[IndexUpsertResponse]),
        )


class AsyncIndexes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndexesWithRawResponse:
        return AsyncIndexesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndexesWithStreamingResponse:
        return AsyncIndexesWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        config: index_create_params.Config,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexCreateResponse]:
        """
        Creates and returns a new Vectorize Index.

        Args:
          account_identifier: Identifier

          config: Specifies the type of configuration to use for the index.

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "description": description,
                },
                index_create_params.IndexCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexCreateResponse]], ResultWrapper[IndexCreateResponse]),
        )

    async def update(
        self,
        index_name: str,
        *,
        account_identifier: str,
        description: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpdateResponse]:
        """
        Updates and returns the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          description: Specifies the description of the index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._put(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
            body=maybe_transform({"description": description}, index_update_params.IndexUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpdateResponse]], ResultWrapper[IndexUpdateResponse]),
        )

    async def list(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexListResponse:
        """
        Returns a list of Vectorize Indexes

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/vectorize/indexes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[IndexListResponse], ResultWrapper[IndexListResponse]),
        )

    async def delete(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteResponse]:
        """
        Deletes the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return cast(
            Optional[IndexDeleteResponse],
            await self._delete(
                f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IndexDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete_by_ids(
        self,
        index_name: str,
        *,
        account_identifier: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexDeleteByIDsResponse]:
        """
        Delete a set of vectors from an index by their vector identifiers.

        Args:
          account_identifier: Identifier

          ids: A list of vector identifiers to delete from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/delete-by-ids",
            body=maybe_transform({"ids": ids}, index_delete_by_ids_params.IndexDeleteByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexDeleteByIDsResponse]], ResultWrapper[IndexDeleteByIDsResponse]),
        )

    async def get(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexGetResponse]:
        """
        Returns the specified Vectorize Index.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._get(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexGetResponse]], ResultWrapper[IndexGetResponse]),
        )

    async def get_by_ids(
        self,
        index_name: str,
        *,
        account_identifier: str,
        ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get a set of vectors from an index by their vector identifiers.

        Args:
          account_identifier: Identifier

          ids: A list of vector identifiers to retrieve from the index indicated by the path.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/get-by-ids",
            body=maybe_transform({"ids": ids}, index_get_by_ids_params.IndexGetByIDsParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def insert(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexInsertResponse]:
        """
        Inserts vectors into the specified index and returns the count of the vectors
        successfully inserted.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/insert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexInsertResponse]], ResultWrapper[IndexInsertResponse]),
        )

    async def query(
        self,
        index_name: str,
        *,
        account_identifier: str,
        return_metadata: bool | NotGiven = NOT_GIVEN,
        return_values: bool | NotGiven = NOT_GIVEN,
        top_k: float | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexQueryResponse]:
        """
        Finds vectors closest to a given vector in an index.

        Args:
          account_identifier: Identifier

          return_metadata: Whether to return the metadata associated with the closest vectors.

          return_values: Whether to return the values associated with the closest vectors.

          top_k: The number of nearest neighbors to find.

          vector: The search vector that will be used to find the nearest neighbors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/query",
            body=maybe_transform(
                {
                    "return_metadata": return_metadata,
                    "return_values": return_values,
                    "top_k": top_k,
                    "vector": vector,
                },
                index_query_params.IndexQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexQueryResponse]], ResultWrapper[IndexQueryResponse]),
        )

    async def upsert(
        self,
        index_name: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IndexUpsertResponse]:
        """
        Upserts vectors into the specified index, creating them if they do not exist and
        returns the count of values and ids successfully inserted.

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not index_name:
            raise ValueError(f"Expected a non-empty value for `index_name` but received {index_name!r}")
        return await self._post(
            f"/accounts/{account_identifier}/vectorize/indexes/{index_name}/upsert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IndexUpsertResponse]], ResultWrapper[IndexUpsertResponse]),
        )


class IndexesWithRawResponse:
    def __init__(self, indexes: Indexes) -> None:
        self._indexes = indexes

        self.create = to_raw_response_wrapper(
            indexes.create,
        )
        self.update = to_raw_response_wrapper(
            indexes.update,
        )
        self.list = to_raw_response_wrapper(
            indexes.list,
        )
        self.delete = to_raw_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = to_raw_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = to_raw_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = to_raw_response_wrapper(
            indexes.get_by_ids,
        )
        self.insert = to_raw_response_wrapper(
            indexes.insert,
        )
        self.query = to_raw_response_wrapper(
            indexes.query,
        )
        self.upsert = to_raw_response_wrapper(
            indexes.upsert,
        )


class AsyncIndexesWithRawResponse:
    def __init__(self, indexes: AsyncIndexes) -> None:
        self._indexes = indexes

        self.create = async_to_raw_response_wrapper(
            indexes.create,
        )
        self.update = async_to_raw_response_wrapper(
            indexes.update,
        )
        self.list = async_to_raw_response_wrapper(
            indexes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = async_to_raw_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = async_to_raw_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = async_to_raw_response_wrapper(
            indexes.get_by_ids,
        )
        self.insert = async_to_raw_response_wrapper(
            indexes.insert,
        )
        self.query = async_to_raw_response_wrapper(
            indexes.query,
        )
        self.upsert = async_to_raw_response_wrapper(
            indexes.upsert,
        )


class IndexesWithStreamingResponse:
    def __init__(self, indexes: Indexes) -> None:
        self._indexes = indexes

        self.create = to_streamed_response_wrapper(
            indexes.create,
        )
        self.update = to_streamed_response_wrapper(
            indexes.update,
        )
        self.list = to_streamed_response_wrapper(
            indexes.list,
        )
        self.delete = to_streamed_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = to_streamed_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = to_streamed_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = to_streamed_response_wrapper(
            indexes.get_by_ids,
        )
        self.insert = to_streamed_response_wrapper(
            indexes.insert,
        )
        self.query = to_streamed_response_wrapper(
            indexes.query,
        )
        self.upsert = to_streamed_response_wrapper(
            indexes.upsert,
        )


class AsyncIndexesWithStreamingResponse:
    def __init__(self, indexes: AsyncIndexes) -> None:
        self._indexes = indexes

        self.create = async_to_streamed_response_wrapper(
            indexes.create,
        )
        self.update = async_to_streamed_response_wrapper(
            indexes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            indexes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            indexes.delete,
        )
        self.delete_by_ids = async_to_streamed_response_wrapper(
            indexes.delete_by_ids,
        )
        self.get = async_to_streamed_response_wrapper(
            indexes.get,
        )
        self.get_by_ids = async_to_streamed_response_wrapper(
            indexes.get_by_ids,
        )
        self.insert = async_to_streamed_response_wrapper(
            indexes.insert,
        )
        self.query = async_to_streamed_response_wrapper(
            indexes.query,
        )
        self.upsert = async_to_streamed_response_wrapper(
            indexes.upsert,
        )