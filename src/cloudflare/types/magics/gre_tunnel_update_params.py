# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["GreTunnelUpdateParams", "HealthCheck"]


class GreTunnelUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    cloudflare_gre_endpoint: Required[str]
    """The IP address assigned to the Cloudflare side of the GRE tunnel."""

    customer_gre_endpoint: Required[str]
    """The IP address assigned to the customer side of the GRE tunnel."""

    interface_address: Required[str]
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: Required[str]
    """The name of the tunnel.

    The name cannot contain spaces or special characters, must be 15 characters or
    less, and cannot share a name with another GRE tunnel.
    """

    description: str
    """An optional description of the GRE tunnel."""

    health_check: HealthCheck

    mtu: int
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: int
    """Time To Live (TTL) in number of hops of the GRE tunnel."""


class HealthCheck(TypedDict, total=False):
    direction: Literal["unidirectional", "bidirectional"]
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel.
    """

    enabled: bool
    """Determines whether to run healthchecks for a tunnel."""

    rate: Literal["low", "mid", "high"]
    """How frequent the health check is run. The default value is `mid`."""

    target: str
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`.
    """

    type: Literal["reply", "request"]
    """The type of healthcheck to run, reply or request. The default value is `reply`."""