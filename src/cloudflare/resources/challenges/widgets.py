# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.challenges import (
    WidgetCreateResponse,
    WidgetUpdateResponse,
    WidgetListResponse,
    WidgetDeleteResponse,
    WidgetGetResponse,
    WidgetRotateSecretResponse,
)

from typing import Type, Optional, List

from typing_extensions import Literal

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
from ...types.challenges import widget_create_params
from ...types.challenges import widget_update_params
from ...types.challenges import widget_list_params
from ...types.challenges import widget_rotate_secret_params
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

__all__ = ["Widgets", "AsyncWidgets"]


class Widgets(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WidgetsWithRawResponse:
        return WidgetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WidgetsWithStreamingResponse:
        return WidgetsWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        domains: List[str],
        mode: Literal["non-interactive", "invisible", "managed"],
        name: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "sitekey", "name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        bot_fight_mode: bool | NotGiven = NOT_GIVEN,
        clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"] | NotGiven = NOT_GIVEN,
        offlabel: bool | NotGiven = NOT_GIVEN,
        region: Literal["world"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetCreateResponse]:
        """
        Lists challenge widgets.

        Args:
          account_identifier: Identifier

          mode: Widget Mode

          name: Human readable widget name. Not unique. Cloudflare suggests that you set this to
              a meaningful string to make it easier to identify your widget, and where it is
              used.

          direction: Direction to order widgets.

          order: Field to order widgets by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
              challenges in response to malicious bots (ENT only).

          clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant
              challenge clearance, this setting can determine the clearance level to be set

          offlabel: Do not show any Cloudflare branding on the widget (ENT only).

          region: Region where this widget can be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/challenges/widgets",
            body=maybe_transform(
                {
                    "domains": domains,
                    "mode": mode,
                    "name": name,
                    "bot_fight_mode": bot_fight_mode,
                    "clearance_level": clearance_level,
                    "offlabel": offlabel,
                    "region": region,
                },
                widget_create_params.WidgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    widget_create_params.WidgetCreateParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetCreateResponse]], ResultWrapper[WidgetCreateResponse]),
        )

    def update(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        domains: List[str],
        mode: Literal["non-interactive", "invisible", "managed"],
        name: str,
        bot_fight_mode: bool | NotGiven = NOT_GIVEN,
        clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"] | NotGiven = NOT_GIVEN,
        offlabel: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetUpdateResponse]:
        """
        Update the configuration of a widget.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          mode: Widget Mode

          name: Human readable widget name. Not unique. Cloudflare suggests that you set this to
              a meaningful string to make it easier to identify your widget, and where it is
              used.

          bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
              challenges in response to malicious bots (ENT only).

          clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant
              challenge clearance, this setting can determine the clearance level to be set

          offlabel: Do not show any Cloudflare branding on the widget (ENT only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return self._put(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            body=maybe_transform(
                {
                    "domains": domains,
                    "mode": mode,
                    "name": name,
                    "bot_fight_mode": bot_fight_mode,
                    "clearance_level": clearance_level,
                    "offlabel": offlabel,
                },
                widget_update_params.WidgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetUpdateResponse]], ResultWrapper[WidgetUpdateResponse]),
        )

    def list(
        self,
        account_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "sitekey", "name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetListResponse]:
        """
        Lists all turnstile widgets of an account.

        Args:
          account_identifier: Identifier

          direction: Direction to order widgets.

          order: Field to order widgets by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/challenges/widgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    widget_list_params.WidgetListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetListResponse]], ResultWrapper[WidgetListResponse]),
        )

    def delete(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetDeleteResponse]:
        """
        Destroy a Turnstile Widget.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return self._delete(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetDeleteResponse]], ResultWrapper[WidgetDeleteResponse]),
        )

    def get(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetGetResponse]:
        """
        Show a single challenge widget configuration.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return self._get(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetGetResponse]], ResultWrapper[WidgetGetResponse]),
        )

    def rotate_secret(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        invalidate_immediately: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetRotateSecretResponse]:
        """Generate a new secret key for this widget.

        If `invalidate_immediately` is set to
        `false`, the previous secret remains valid for 2 hours.

        Note that secrets cannot be rotated again during the grace period.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          invalidate_immediately: If `invalidate_immediately` is set to `false`, the previous secret will remain
              valid for two hours. Otherwise, the secret is immediately invalidated, and
              requests using it will be rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return self._post(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}/rotate_secret",
            body=maybe_transform(
                {"invalidate_immediately": invalidate_immediately}, widget_rotate_secret_params.WidgetRotateSecretParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetRotateSecretResponse]], ResultWrapper[WidgetRotateSecretResponse]),
        )


class AsyncWidgets(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWidgetsWithRawResponse:
        return AsyncWidgetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWidgetsWithStreamingResponse:
        return AsyncWidgetsWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        domains: List[str],
        mode: Literal["non-interactive", "invisible", "managed"],
        name: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "sitekey", "name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        bot_fight_mode: bool | NotGiven = NOT_GIVEN,
        clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"] | NotGiven = NOT_GIVEN,
        offlabel: bool | NotGiven = NOT_GIVEN,
        region: Literal["world"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetCreateResponse]:
        """
        Lists challenge widgets.

        Args:
          account_identifier: Identifier

          mode: Widget Mode

          name: Human readable widget name. Not unique. Cloudflare suggests that you set this to
              a meaningful string to make it easier to identify your widget, and where it is
              used.

          direction: Direction to order widgets.

          order: Field to order widgets by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
              challenges in response to malicious bots (ENT only).

          clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant
              challenge clearance, this setting can determine the clearance level to be set

          offlabel: Do not show any Cloudflare branding on the widget (ENT only).

          region: Region where this widget can be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/challenges/widgets",
            body=maybe_transform(
                {
                    "domains": domains,
                    "mode": mode,
                    "name": name,
                    "bot_fight_mode": bot_fight_mode,
                    "clearance_level": clearance_level,
                    "offlabel": offlabel,
                    "region": region,
                },
                widget_create_params.WidgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    widget_create_params.WidgetCreateParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetCreateResponse]], ResultWrapper[WidgetCreateResponse]),
        )

    async def update(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        domains: List[str],
        mode: Literal["non-interactive", "invisible", "managed"],
        name: str,
        bot_fight_mode: bool | NotGiven = NOT_GIVEN,
        clearance_level: Literal["no_clearance", "jschallenge", "managed", "interactive"] | NotGiven = NOT_GIVEN,
        offlabel: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetUpdateResponse]:
        """
        Update the configuration of a widget.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          mode: Widget Mode

          name: Human readable widget name. Not unique. Cloudflare suggests that you set this to
              a meaningful string to make it easier to identify your widget, and where it is
              used.

          bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive
              challenges in response to malicious bots (ENT only).

          clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant
              challenge clearance, this setting can determine the clearance level to be set

          offlabel: Do not show any Cloudflare branding on the widget (ENT only).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return await self._put(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            body=maybe_transform(
                {
                    "domains": domains,
                    "mode": mode,
                    "name": name,
                    "bot_fight_mode": bot_fight_mode,
                    "clearance_level": clearance_level,
                    "offlabel": offlabel,
                },
                widget_update_params.WidgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetUpdateResponse]], ResultWrapper[WidgetUpdateResponse]),
        )

    async def list(
        self,
        account_identifier: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        order: Literal["id", "sitekey", "name", "created_on", "modified_on"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetListResponse]:
        """
        Lists all turnstile widgets of an account.

        Args:
          account_identifier: Identifier

          direction: Direction to order widgets.

          order: Field to order widgets by.

          page: Page number of paginated results.

          per_page: Number of items per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/challenges/widgets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    widget_list_params.WidgetListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetListResponse]], ResultWrapper[WidgetListResponse]),
        )

    async def delete(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetDeleteResponse]:
        """
        Destroy a Turnstile Widget.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return await self._delete(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetDeleteResponse]], ResultWrapper[WidgetDeleteResponse]),
        )

    async def get(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetGetResponse]:
        """
        Show a single challenge widget configuration.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return await self._get(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetGetResponse]], ResultWrapper[WidgetGetResponse]),
        )

    async def rotate_secret(
        self,
        sitekey: str,
        *,
        account_identifier: str,
        invalidate_immediately: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[WidgetRotateSecretResponse]:
        """Generate a new secret key for this widget.

        If `invalidate_immediately` is set to
        `false`, the previous secret remains valid for 2 hours.

        Note that secrets cannot be rotated again during the grace period.

        Args:
          account_identifier: Identifier

          sitekey: Widget item identifier tag.

          invalidate_immediately: If `invalidate_immediately` is set to `false`, the previous secret will remain
              valid for two hours. Otherwise, the secret is immediately invalidated, and
              requests using it will be rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not sitekey:
            raise ValueError(f"Expected a non-empty value for `sitekey` but received {sitekey!r}")
        return await self._post(
            f"/accounts/{account_identifier}/challenges/widgets/{sitekey}/rotate_secret",
            body=maybe_transform(
                {"invalidate_immediately": invalidate_immediately}, widget_rotate_secret_params.WidgetRotateSecretParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[WidgetRotateSecretResponse]], ResultWrapper[WidgetRotateSecretResponse]),
        )


class WidgetsWithRawResponse:
    def __init__(self, widgets: Widgets) -> None:
        self._widgets = widgets

        self.create = to_raw_response_wrapper(
            widgets.create,
        )
        self.update = to_raw_response_wrapper(
            widgets.update,
        )
        self.list = to_raw_response_wrapper(
            widgets.list,
        )
        self.delete = to_raw_response_wrapper(
            widgets.delete,
        )
        self.get = to_raw_response_wrapper(
            widgets.get,
        )
        self.rotate_secret = to_raw_response_wrapper(
            widgets.rotate_secret,
        )


class AsyncWidgetsWithRawResponse:
    def __init__(self, widgets: AsyncWidgets) -> None:
        self._widgets = widgets

        self.create = async_to_raw_response_wrapper(
            widgets.create,
        )
        self.update = async_to_raw_response_wrapper(
            widgets.update,
        )
        self.list = async_to_raw_response_wrapper(
            widgets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            widgets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            widgets.get,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            widgets.rotate_secret,
        )


class WidgetsWithStreamingResponse:
    def __init__(self, widgets: Widgets) -> None:
        self._widgets = widgets

        self.create = to_streamed_response_wrapper(
            widgets.create,
        )
        self.update = to_streamed_response_wrapper(
            widgets.update,
        )
        self.list = to_streamed_response_wrapper(
            widgets.list,
        )
        self.delete = to_streamed_response_wrapper(
            widgets.delete,
        )
        self.get = to_streamed_response_wrapper(
            widgets.get,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            widgets.rotate_secret,
        )


class AsyncWidgetsWithStreamingResponse:
    def __init__(self, widgets: AsyncWidgets) -> None:
        self._widgets = widgets

        self.create = async_to_streamed_response_wrapper(
            widgets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            widgets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            widgets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            widgets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            widgets.get,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            widgets.rotate_secret,
        )