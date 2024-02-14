# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ......_compat import cached_property

from ......types.web3s.hostnames.ipfs_universal_paths.content_lists import (
    EntryUpdateResponse,
    EntryDeleteResponse,
    EntryGetResponse,
    EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse,
    EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse,
)

from typing import Type, Optional

from typing_extensions import Literal

from ......_response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ......_utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ......_types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ......types import shared_params
from ......types.web3s.hostnames.ipfs_universal_paths.content_lists import entry_update_params
from ......types.web3s.hostnames.ipfs_universal_paths.content_lists import (
    entry_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_params,
)
from ......_wrappers import ResultWrapper
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

__all__ = ["Entries", "AsyncEntries"]


class Entries(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntriesWithRawResponse:
        return EntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntriesWithStreamingResponse:
        return EntriesWithStreamingResponse(self)

    def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryUpdateResponse:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntryUpdateResponse], ResultWrapper[EntryUpdateResponse]),
        )

    def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryDeleteResponse]:
        """
        Delete IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryGetResponse:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntryGetResponse], ResultWrapper[EntryGetResponse]),
        )

    def web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_params.EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse],
                ResultWrapper[EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse],
            ),
        )

    def web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse]:
        """
        List IPFS Universal Path Gateway Content List Entries

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse]],
                ResultWrapper[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse],
            ),
        )


class AsyncEntries(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntriesWithRawResponse:
        return AsyncEntriesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntriesWithStreamingResponse:
        return AsyncEntriesWithStreamingResponse(self)

    async def update(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryUpdateResponse:
        """
        Edit IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._put(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_update_params.EntryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntryUpdateResponse], ResultWrapper[EntryUpdateResponse]),
        )

    async def delete(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryDeleteResponse]:
        """
        Delete IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._delete(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[EntryDeleteResponse]], ResultWrapper[EntryDeleteResponse]),
        )

    async def get(
        self,
        content_list_entry_identifier: str,
        *,
        zone_identifier: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryGetResponse:
        """
        IPFS Universal Path Gateway Content List Entry Details

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content_list_entry_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not content_list_entry_identifier:
            raise ValueError(
                f"Expected a non-empty value for `content_list_entry_identifier` but received {content_list_entry_identifier!r}"
            )
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[EntryGetResponse], ResultWrapper[EntryGetResponse]),
        )

    async def web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        content: str,
        type: Literal["cid", "content_path"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse:
        """
        Create IPFS Universal Path Gateway Content List Entry

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          content: CID or content path of content to block.

          type: Type of content list entry to block.

          description: An optional description of the content list entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            body=maybe_transform(
                {
                    "content": content,
                    "type": type,
                    "description": description,
                },
                entry_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_params.EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse],
                ResultWrapper[EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse],
            ),
        )

    async def web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self,
        identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse]:
        """
        List IPFS Universal Path Gateway Content List Entries

        Args:
          zone_identifier: Identifier

          identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse]],
                ResultWrapper[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse],
            ),
        )


class EntriesWithRawResponse:
    def __init__(self, entries: Entries) -> None:
        self._entries = entries

        self.update = to_raw_response_wrapper(
            entries.update,
        )
        self.delete = to_raw_response_wrapper(
            entries.delete,
        )
        self.get = to_raw_response_wrapper(
            entries.get,
        )
        self.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry = to_raw_response_wrapper(
            entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry,
        )
        self.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries = to_raw_response_wrapper(
            entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries,
        )


class AsyncEntriesWithRawResponse:
    def __init__(self, entries: AsyncEntries) -> None:
        self._entries = entries

        self.update = async_to_raw_response_wrapper(
            entries.update,
        )
        self.delete = async_to_raw_response_wrapper(
            entries.delete,
        )
        self.get = async_to_raw_response_wrapper(
            entries.get,
        )
        self.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry = async_to_raw_response_wrapper(
            entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry,
        )
        self.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries = async_to_raw_response_wrapper(
            entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries,
        )


class EntriesWithStreamingResponse:
    def __init__(self, entries: Entries) -> None:
        self._entries = entries

        self.update = to_streamed_response_wrapper(
            entries.update,
        )
        self.delete = to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = to_streamed_response_wrapper(
            entries.get,
        )
        self.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry = to_streamed_response_wrapper(
            entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry,
        )
        self.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries = to_streamed_response_wrapper(
            entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries,
        )


class AsyncEntriesWithStreamingResponse:
    def __init__(self, entries: AsyncEntries) -> None:
        self._entries = entries

        self.update = async_to_streamed_response_wrapper(
            entries.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            entries.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            entries.get,
        )
        self.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry = async_to_streamed_response_wrapper(
            entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry,
        )
        self.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries = async_to_streamed_response_wrapper(
            entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries,
        )