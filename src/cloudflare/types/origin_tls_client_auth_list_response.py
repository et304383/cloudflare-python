# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OriginTLSClientAuthListResponse"]


class OriginTLSClientAuthListResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The zone's leaf certificate."""

    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""

    private_key: Optional[str] = None
    """The zone's private key."""
