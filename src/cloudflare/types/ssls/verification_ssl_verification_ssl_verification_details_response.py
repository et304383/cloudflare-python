# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "VerificationSSLVerificationSSLVerificationDetailsResponse",
    "VerificationSSLVerificationSSLVerificationDetailsResponseItem",
    "VerificationSSLVerificationSSLVerificationDetailsResponseItemVerificationInfo",
]


class VerificationSSLVerificationSSLVerificationDetailsResponseItemVerificationInfo(BaseModel):
    record_name: Optional[Literal["record_name", "http_url", "cname", "txt_name"]] = None
    """Name of CNAME record."""

    record_target: Optional[Literal["record_value", "http_body", "cname_target", "txt_value"]] = None
    """Target of CNAME record."""


class VerificationSSLVerificationSSLVerificationDetailsResponseItem(BaseModel):
    certificate_status: Literal[
        "initializing", "authorizing", "active", "expired", "issuing", "timing_out", "pending_deployment"
    ]
    """Current status of certificate."""

    brand_check: Optional[bool] = None
    """Certificate Authority is manually reviewing the order."""

    cert_pack_uuid: Optional[str] = None
    """Certificate Pack UUID."""

    signature: Optional[Literal["ECDSAWithSHA256", "SHA1WithRSA", "SHA256WithRSA"]] = None
    """Certificate's signature algorithm."""

    validation_method: Optional[Literal["http", "cname", "txt"]] = None
    """Validation method in use for a certificate pack order."""

    verification_info: Optional[VerificationSSLVerificationSSLVerificationDetailsResponseItemVerificationInfo] = None
    """Certificate's required verification information."""

    verification_status: Optional[bool] = None
    """
    Status of the required verification information, omitted if verification status
    is unknown.
    """

    verification_type: Optional[Literal["cname", "meta tag"]] = None
    """Method of verification."""


VerificationSSLVerificationSSLVerificationDetailsResponse = List[
    VerificationSSLVerificationSSLVerificationDetailsResponseItem
]