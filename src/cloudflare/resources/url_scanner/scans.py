# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.url_scanner import ScanCreateResponse, ScanGetResponse, ScanHarResponse

from typing import Type, Dict, List

from typing_extensions import Literal

from ..._response import (
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
from ...types.url_scanner import scan_create_params
from ...types.url_scanner import scan_screenshot_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Scans", "AsyncScans"]


class Scans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScansWithRawResponse:
        return ScansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScansWithStreamingResponse:
        return ScansWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        url: str,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanCreateResponse:
        """Submit a URL to scan.

        You can also set some options, like the visibility level
        and custom headers. Accounts are limited to 1 new scan every 10 seconds and 8000
        per month. If you need more, please reach out.

        Args:
          account_id: Account Id

          custom_headers: Set custom headers

          screenshots_resolutions: Take multiple screenshots targeting different device types

          visibility: The option `Public` means it will be included in listings like recent scans and
              search results. `Unlisted` means it will not be included in the aforementioned
              listings, users will need to have the scan's ID to access it. A a scan will be
              automatically marked as unlisted if it fails, if it contains potential PII or
              other sensitive material.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/urlscanner/scan",
            body=maybe_transform(
                {
                    "url": url,
                    "custom_headers": custom_headers,
                    "screenshots_resolutions": screenshots_resolutions,
                    "visibility": visibility,
                },
                scan_create_params.ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanCreateResponse], ResultWrapper[ScanCreateResponse]),
        )

    def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanGetResponse], ResultWrapper[ScanGetResponse]),
        )

    def har(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanHarResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/har",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanHarResponse], ResultWrapper[ScanHarResponse]),
        )

    def screenshot(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          resolution: Target device type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resolution": resolution}, scan_screenshot_params.ScanScreenshotParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncScans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScansWithRawResponse:
        return AsyncScansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScansWithStreamingResponse:
        return AsyncScansWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        url: str,
        custom_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        screenshots_resolutions: List[Literal["desktop", "mobile", "tablet"]] | NotGiven = NOT_GIVEN,
        visibility: Literal["Public", "Unlisted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanCreateResponse:
        """Submit a URL to scan.

        You can also set some options, like the visibility level
        and custom headers. Accounts are limited to 1 new scan every 10 seconds and 8000
        per month. If you need more, please reach out.

        Args:
          account_id: Account Id

          custom_headers: Set custom headers

          screenshots_resolutions: Take multiple screenshots targeting different device types

          visibility: The option `Public` means it will be included in listings like recent scans and
              search results. `Unlisted` means it will not be included in the aforementioned
              listings, users will need to have the scan's ID to access it. A a scan will be
              automatically marked as unlisted if it fails, if it contains potential PII or
              other sensitive material.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/urlscanner/scan",
            body=maybe_transform(
                {
                    "url": url,
                    "custom_headers": custom_headers,
                    "screenshots_resolutions": screenshots_resolutions,
                    "visibility": visibility,
                },
                scan_create_params.ScanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanCreateResponse], ResultWrapper[ScanCreateResponse]),
        )

    async def get(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanGetResponse:
        """
        Get URL scan by uuid

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanGetResponse], ResultWrapper[ScanGetResponse]),
        )

    async def har(
        self,
        scan_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScanHarResponse:
        """Get a URL scan's HAR file.

        See HAR spec at
        http://www.softwareishard.com/blog/har-12-spec/.

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/har",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ScanHarResponse], ResultWrapper[ScanHarResponse]),
        )

    async def screenshot(
        self,
        scan_id: str,
        *,
        account_id: str,
        resolution: Literal["desktop", "mobile", "tablet"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get scan's screenshot by resolution (desktop/mobile/tablet).

        Args:
          account_id: Account Id

          scan_id: Scan uuid

          resolution: Target device type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not scan_id:
            raise ValueError(f"Expected a non-empty value for `scan_id` but received {scan_id!r}")
        return await self._get(
            f"/accounts/{account_id}/urlscanner/scan/{scan_id}/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"resolution": resolution}, scan_screenshot_params.ScanScreenshotParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ScansWithRawResponse:
    def __init__(self, scans: Scans) -> None:
        self._scans = scans

        self.create = to_raw_response_wrapper(
            scans.create,
        )
        self.get = to_raw_response_wrapper(
            scans.get,
        )
        self.har = to_raw_response_wrapper(
            scans.har,
        )
        self.screenshot = to_custom_raw_response_wrapper(
            scans.screenshot,
            BinaryAPIResponse,
        )


class AsyncScansWithRawResponse:
    def __init__(self, scans: AsyncScans) -> None:
        self._scans = scans

        self.create = async_to_raw_response_wrapper(
            scans.create,
        )
        self.get = async_to_raw_response_wrapper(
            scans.get,
        )
        self.har = async_to_raw_response_wrapper(
            scans.har,
        )
        self.screenshot = async_to_custom_raw_response_wrapper(
            scans.screenshot,
            AsyncBinaryAPIResponse,
        )


class ScansWithStreamingResponse:
    def __init__(self, scans: Scans) -> None:
        self._scans = scans

        self.create = to_streamed_response_wrapper(
            scans.create,
        )
        self.get = to_streamed_response_wrapper(
            scans.get,
        )
        self.har = to_streamed_response_wrapper(
            scans.har,
        )
        self.screenshot = to_custom_streamed_response_wrapper(
            scans.screenshot,
            StreamedBinaryAPIResponse,
        )


class AsyncScansWithStreamingResponse:
    def __init__(self, scans: AsyncScans) -> None:
        self._scans = scans

        self.create = async_to_streamed_response_wrapper(
            scans.create,
        )
        self.get = async_to_streamed_response_wrapper(
            scans.get,
        )
        self.har = async_to_streamed_response_wrapper(
            scans.har,
        )
        self.screenshot = async_to_custom_streamed_response_wrapper(
            scans.screenshot,
            AsyncStreamedBinaryAPIResponse,
        )