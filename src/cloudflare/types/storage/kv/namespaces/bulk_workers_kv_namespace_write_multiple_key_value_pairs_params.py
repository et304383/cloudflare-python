# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ....._types import FileTypes
from ....._utils import PropertyInfo
from .....types import shared_params

__all__ = ["BulkWorkersKvNamespaceWriteMultipleKeyValuePairsParams", "Body"]


class BulkWorkersKvNamespaceWriteMultipleKeyValuePairsParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    base64: bool
    """Whether or not the server should base64 decode the value before storing it.

    Useful for writing values that wouldn't otherwise be valid JSON strings, such as
    images.
    """

    expiration: float
    """
    The time, measured in number of seconds since the UNIX epoch, at which the key
    should expire.
    """

    expiration_ttl: float
    """The number of seconds for which the key should be visible before it expires.

    At least 60.
    """

    key: str
    """A key's name.

    The name may be at most 512 bytes. All printable, non-whitespace characters are
    valid.
    """

    metadata: object
    """Arbitrary JSON that is associated with a key."""

    value: str
    """A UTF-8 encoded string to be stored, up to 25 MiB in length."""