# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.dlps import (
    PayloadLogDLPPayloadLogSettingsGetSettingsResponse,
    PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse,
)

from typing import Type, Optional

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
from ...types.dlps import payload_log_dlp_payload_log_settings_update_settings_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PayloadLogs", "AsyncPayloadLogs"]


class PayloadLogs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayloadLogsWithRawResponse:
        return PayloadLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayloadLogsWithStreamingResponse:
        return PayloadLogsWithStreamingResponse(self)

    def dlp_payload_log_settings_get_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogDLPPayloadLogSettingsGetSettingsResponse:
        """
        Gets the current DLP payload log settings for this account.

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
            f"/accounts/{account_id}/dlp/payload_log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PayloadLogDLPPayloadLogSettingsGetSettingsResponse],
                ResultWrapper[PayloadLogDLPPayloadLogSettingsGetSettingsResponse],
            ),
        )

    def dlp_payload_log_settings_update_settings(
        self,
        account_id: str,
        *,
        public_key: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse:
        """
        Updates the DLP payload log settings for this account.

        Args:
          account_id: Identifier

          public_key: The public key to use when encrypting extracted payloads, as a base64 string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/dlp/payload_log",
            body=maybe_transform(
                {"public_key": public_key},
                payload_log_dlp_payload_log_settings_update_settings_params.PayloadLogDLPPayloadLogSettingsUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse],
                ResultWrapper[PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse],
            ),
        )


class AsyncPayloadLogs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayloadLogsWithRawResponse:
        return AsyncPayloadLogsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayloadLogsWithStreamingResponse:
        return AsyncPayloadLogsWithStreamingResponse(self)

    async def dlp_payload_log_settings_get_settings(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogDLPPayloadLogSettingsGetSettingsResponse:
        """
        Gets the current DLP payload log settings for this account.

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
            f"/accounts/{account_id}/dlp/payload_log",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PayloadLogDLPPayloadLogSettingsGetSettingsResponse],
                ResultWrapper[PayloadLogDLPPayloadLogSettingsGetSettingsResponse],
            ),
        )

    async def dlp_payload_log_settings_update_settings(
        self,
        account_id: str,
        *,
        public_key: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse:
        """
        Updates the DLP payload log settings for this account.

        Args:
          account_id: Identifier

          public_key: The public key to use when encrypting extracted payloads, as a base64 string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/dlp/payload_log",
            body=maybe_transform(
                {"public_key": public_key},
                payload_log_dlp_payload_log_settings_update_settings_params.PayloadLogDLPPayloadLogSettingsUpdateSettingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse],
                ResultWrapper[PayloadLogDLPPayloadLogSettingsUpdateSettingsResponse],
            ),
        )


class PayloadLogsWithRawResponse:
    def __init__(self, payload_logs: PayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.dlp_payload_log_settings_get_settings = to_raw_response_wrapper(
            payload_logs.dlp_payload_log_settings_get_settings,
        )
        self.dlp_payload_log_settings_update_settings = to_raw_response_wrapper(
            payload_logs.dlp_payload_log_settings_update_settings,
        )


class AsyncPayloadLogsWithRawResponse:
    def __init__(self, payload_logs: AsyncPayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.dlp_payload_log_settings_get_settings = async_to_raw_response_wrapper(
            payload_logs.dlp_payload_log_settings_get_settings,
        )
        self.dlp_payload_log_settings_update_settings = async_to_raw_response_wrapper(
            payload_logs.dlp_payload_log_settings_update_settings,
        )


class PayloadLogsWithStreamingResponse:
    def __init__(self, payload_logs: PayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.dlp_payload_log_settings_get_settings = to_streamed_response_wrapper(
            payload_logs.dlp_payload_log_settings_get_settings,
        )
        self.dlp_payload_log_settings_update_settings = to_streamed_response_wrapper(
            payload_logs.dlp_payload_log_settings_update_settings,
        )


class AsyncPayloadLogsWithStreamingResponse:
    def __init__(self, payload_logs: AsyncPayloadLogs) -> None:
        self._payload_logs = payload_logs

        self.dlp_payload_log_settings_get_settings = async_to_streamed_response_wrapper(
            payload_logs.dlp_payload_log_settings_get_settings,
        )
        self.dlp_payload_log_settings_update_settings = async_to_streamed_response_wrapper(
            payload_logs.dlp_payload_log_settings_update_settings,
        )