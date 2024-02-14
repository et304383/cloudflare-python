# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.logs.controls.cmb import (
    ConfigDeleteResponse,
    ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse,
    ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse,
)

from typing import Optional, Type

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.logs.controls.cmb import config_put_accounts_account_identifier_logs_control_cmb_config_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Configs", "AsyncConfigs"]


class Configs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self)

    def delete(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigDeleteResponse]:
        """
        Deletes CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[ConfigDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/logs/control/cmb/config",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get_accounts_account_identifier_logs_control_cmb_config(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse]:
        """
        Gets CMB config.

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
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse]],
                ResultWrapper[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse],
            ),
        )

    def put_accounts_account_identifier_logs_control_cmb_config(
        self,
        account_id: str,
        *,
        regions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse]:
        """
        Updates CMB config.

        Args:
          account_id: Identifier

          regions: Comma-separated list of regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=maybe_transform(
                {"regions": regions},
                config_put_accounts_account_identifier_logs_control_cmb_config_params.ConfigPutAccountsAccountIdentifierLogsControlCmbConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse]],
                ResultWrapper[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse],
            ),
        )


class AsyncConfigs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self)

    async def delete(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigDeleteResponse]:
        """
        Deletes CMB config.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[ConfigDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/logs/control/cmb/config",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ConfigDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get_accounts_account_identifier_logs_control_cmb_config(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse]:
        """
        Gets CMB config.

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
            f"/accounts/{account_id}/logs/control/cmb/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse]],
                ResultWrapper[ConfigGetAccountsAccountIdentifierLogsControlCmbConfigResponse],
            ),
        )

    async def put_accounts_account_identifier_logs_control_cmb_config(
        self,
        account_id: str,
        *,
        regions: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse]:
        """
        Updates CMB config.

        Args:
          account_id: Identifier

          regions: Comma-separated list of regions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/logs/control/cmb/config",
            body=maybe_transform(
                {"regions": regions},
                config_put_accounts_account_identifier_logs_control_cmb_config_params.ConfigPutAccountsAccountIdentifierLogsControlCmbConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse]],
                ResultWrapper[ConfigPutAccountsAccountIdentifierLogsControlCmbConfigResponse],
            ),
        )


class ConfigsWithRawResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.delete = to_raw_response_wrapper(
            configs.delete,
        )
        self.get_accounts_account_identifier_logs_control_cmb_config = to_raw_response_wrapper(
            configs.get_accounts_account_identifier_logs_control_cmb_config,
        )
        self.put_accounts_account_identifier_logs_control_cmb_config = to_raw_response_wrapper(
            configs.put_accounts_account_identifier_logs_control_cmb_config,
        )


class AsyncConfigsWithRawResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.delete = async_to_raw_response_wrapper(
            configs.delete,
        )
        self.get_accounts_account_identifier_logs_control_cmb_config = async_to_raw_response_wrapper(
            configs.get_accounts_account_identifier_logs_control_cmb_config,
        )
        self.put_accounts_account_identifier_logs_control_cmb_config = async_to_raw_response_wrapper(
            configs.put_accounts_account_identifier_logs_control_cmb_config,
        )


class ConfigsWithStreamingResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.delete = to_streamed_response_wrapper(
            configs.delete,
        )
        self.get_accounts_account_identifier_logs_control_cmb_config = to_streamed_response_wrapper(
            configs.get_accounts_account_identifier_logs_control_cmb_config,
        )
        self.put_accounts_account_identifier_logs_control_cmb_config = to_streamed_response_wrapper(
            configs.put_accounts_account_identifier_logs_control_cmb_config,
        )


class AsyncConfigsWithStreamingResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.delete = async_to_streamed_response_wrapper(
            configs.delete,
        )
        self.get_accounts_account_identifier_logs_control_cmb_config = async_to_streamed_response_wrapper(
            configs.get_accounts_account_identifier_logs_control_cmb_config,
        )
        self.put_accounts_account_identifier_logs_control_cmb_config = async_to_streamed_response_wrapper(
            configs.put_accounts_account_identifier_logs_control_cmb_config,
        )