# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["TLSUpdateResponse"]


class TLSUpdateResponse(BaseModel):
    created_at: Optional[datetime] = None
    """This is the time the tls setting was originally created for this hostname."""

    hostname: Optional[str] = None
    """The hostname for which the tls settings are set."""

    status: Optional[str] = None
    """Deployment status for the given tls setting."""

    updated_at: Optional[datetime] = None
    """This is the time the tls setting was updated."""

    value: Union[float, str, List[str], None] = None
    """The tls setting value."""