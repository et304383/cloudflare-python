# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ItemCreateResponse"]


class ItemCreateResponse(BaseModel):
    operation_id: Optional[str] = None
    """The unique operation ID of the asynchronous action."""