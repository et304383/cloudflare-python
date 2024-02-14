# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = [
    "PcapMagicPcapCollectionCreatePcapRequestParams",
    "_7dRf5S6WPcapsRequestSimple",
    "_7dRf5S6WPcapsRequestSimpleFilterV1",
    "_7dRf5S6WPcapsRequestFull",
    "_7dRf5S6WPcapsRequestFullFilterV1",
]


class _7dRf5S6WPcapsRequestSimple(TypedDict, total=False):
    packet_limit: Required[float]
    """The limit of packets contained in a packet capture."""

    system: Required[Literal["magic-transit"]]
    """The system used to collect packet captures."""

    time_limit: Required[float]
    """The packet capture duration in seconds."""

    type: Required[Literal["simple", "full"]]
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """

    filter_v1: _7dRf5S6WPcapsRequestSimpleFilterV1
    """The packet capture filter. When this field is empty, all packets are captured."""


class _7dRf5S6WPcapsRequestSimpleFilterV1(TypedDict, total=False):
    destination_address: str
    """The destination IP address of the packet."""

    destination_port: float
    """The destination port of the packet."""

    protocol: float
    """The protocol number of the packet."""

    source_address: str
    """The source IP address of the packet."""

    source_port: float
    """The source port of the packet."""


class _7dRf5S6WPcapsRequestFull(TypedDict, total=False):
    colo_name: Required[str]
    """The name of the data center used for the packet capture.

    This can be a specific colo (ord02) or a multi-colo name (ORD). This field only
    applies to `full` packet captures.
    """

    destination_conf: Required[str]
    """The full URI for the bucket. This field only applies to `full` packet captures."""

    system: Required[Literal["magic-transit"]]
    """The system used to collect packet captures."""

    time_limit: Required[float]
    """The packet capture duration in seconds."""

    type: Required[Literal["simple", "full"]]
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """

    byte_limit: float
    """The maximum number of bytes to capture.

    This field only applies to `full` packet captures.
    """

    filter_v1: _7dRf5S6WPcapsRequestFullFilterV1
    """The packet capture filter. When this field is empty, all packets are captured."""

    packet_limit: float
    """The limit of packets contained in a packet capture."""


class _7dRf5S6WPcapsRequestFullFilterV1(TypedDict, total=False):
    destination_address: str
    """The destination IP address of the packet."""

    destination_port: float
    """The destination port of the packet."""

    protocol: float
    """The protocol number of the packet."""

    source_address: str
    """The source IP address of the packet."""

    source_port: float
    """The source port of the packet."""


PcapMagicPcapCollectionCreatePcapRequestParams = Union[_7dRf5S6WPcapsRequestSimple, _7dRf5S6WPcapsRequestFull]