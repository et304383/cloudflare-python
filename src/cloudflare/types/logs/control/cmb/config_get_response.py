# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["ConfigGetResponse"]


class ConfigGetResponse(BaseModel):
    regions: Optional[str] = None
    """Comma-separated list of regions."""