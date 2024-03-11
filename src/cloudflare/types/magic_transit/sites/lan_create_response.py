# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = [
    "LanCreateResponse",
    "Lan",
    "LanNat",
    "LanRoutedSubnet",
    "LanRoutedSubnetNat",
    "LanStaticAddressing",
    "LanStaticAddressingDhcpRelay",
    "LanStaticAddressingDhcpServer",
]


class LanNat(BaseModel):
    static_prefix: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class LanRoutedSubnetNat(BaseModel):
    static_prefix: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class LanRoutedSubnet(BaseModel):
    next_hop: str
    """A valid IPv4 address."""

    prefix: str
    """A valid CIDR notation representing an IP range."""

    nat: Optional[LanRoutedSubnetNat] = None


class LanStaticAddressingDhcpRelay(BaseModel):
    server_addresses: Optional[List[str]] = None
    """List of DHCP server IPs."""


class LanStaticAddressingDhcpServer(BaseModel):
    dhcp_pool_end: Optional[str] = None
    """A valid IPv4 address."""

    dhcp_pool_start: Optional[str] = None
    """A valid IPv4 address."""

    dns_server: Optional[str] = None
    """A valid IPv4 address."""

    reservations: Optional[Dict[str, str]] = None
    """Mapping of MAC addresses to IP addresses"""


class LanStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: Optional[LanStaticAddressingDhcpRelay] = None

    dhcp_server: Optional[LanStaticAddressingDhcpServer] = None

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""

    virtual_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class Lan(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None

    ha_link: Optional[bool] = None
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    nat: Optional[LanNat] = None

    physport: Optional[int] = None

    routed_subnets: Optional[List[LanRoutedSubnet]] = None

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[LanStaticAddressing] = None
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""


class LanCreateResponse(BaseModel):
    lans: Optional[List[Lan]] = None