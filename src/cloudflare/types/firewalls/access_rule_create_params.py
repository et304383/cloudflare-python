# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = [
    "AccessRuleCreateParams",
    "Configuration",
    "ConfigurationLegacyJhsIPConfiguration",
    "ConfigurationLegacyJhsIPV6Configuration",
    "ConfigurationLegacyJhsCidrConfiguration",
    "ConfigurationLegacyJhsAsnConfiguration",
    "ConfigurationLegacyJhsCountryConfiguration",
]


class AccessRuleCreateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    configuration: Required[Configuration]
    """The rule configuration."""

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""

    notes: str
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """


class ConfigurationLegacyJhsIPConfiguration(TypedDict, total=False):
    target: Literal["ip"]
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the rule.
    """

    value: str
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """


class ConfigurationLegacyJhsIPV6Configuration(TypedDict, total=False):
    target: Literal["ip6"]
    """The configuration target.

    You must set the target to `ip6` when specifying an IPv6 address in the rule.
    """

    value: str
    """The IPv6 address to match."""


class ConfigurationLegacyJhsCidrConfiguration(TypedDict, total=False):
    target: Literal["ip_range"]
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    rule.
    """

    value: str
    """The IP address range to match.

    You can only use prefix lengths `/16` and `/24` for IPv4 ranges, and prefix
    lengths `/32`, `/48`, and `/64` for IPv6 ranges.
    """


class ConfigurationLegacyJhsAsnConfiguration(TypedDict, total=False):
    target: Literal["asn"]
    """The configuration target.

    You must set the target to `asn` when specifying an Autonomous System Number
    (ASN) in the rule.
    """

    value: str
    """The AS number to match."""


class ConfigurationLegacyJhsCountryConfiguration(TypedDict, total=False):
    target: Literal["country"]
    """The configuration target.

    You must set the target to `country` when specifying a country code in the rule.
    """

    value: str
    """The two-letter ISO-3166-1 alpha-2 code to match.

    For more information, refer to
    [IP Access rules: Parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country).
    """


Configuration = Union[
    ConfigurationLegacyJhsIPConfiguration,
    ConfigurationLegacyJhsIPV6Configuration,
    ConfigurationLegacyJhsCidrConfiguration,
    ConfigurationLegacyJhsAsnConfiguration,
    ConfigurationLegacyJhsCountryConfiguration,
]