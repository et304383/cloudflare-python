# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse"]


class AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse(BaseModel):
    id: Optional[str] = None
    """Destination address identifier."""

    created: Optional[datetime] = None
    """The date and time the destination address has been created."""

    email: Optional[str] = None
    """The contact email address of the user."""

    modified: Optional[datetime] = None
    """The date and time the destination address was last modified."""

    tag: Optional[str] = None
    """Destination address tag.

    (Deprecated, replaced by destination address identifier)
    """

    verified: Optional[datetime] = None
    """The date and time the destination address has been verified.

    Null means not verified yet.
    """