# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .devices_fallback_domain_param import DevicesFallbackDomainParam

__all__ = ["FallbackDomainUpdateParams"]


class FallbackDomainUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[Iterable[DevicesFallbackDomainParam]]
