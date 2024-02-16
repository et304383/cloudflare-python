# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AuditLogListResponse",
    "UnionMember0",
    "UnionMember0Result",
    "UnionMember0ResultAction",
    "UnionMember0ResultActor",
    "UnionMember0ResultOwner",
    "UnionMember0ResultResource",
    "Yq4V3hcHAPIResponseCommon",
    "Yq4V3hcHapiResponseCommonError",
    "Yq4V3hcHapiResponseCommonMessage",
]


class UnionMember0ResultAction(BaseModel):
    result: Optional[bool] = None
    """A boolean that indicates if the action attempted was successful."""

    type: Optional[str] = None
    """A short string that describes the action that was performed."""


class UnionMember0ResultActor(BaseModel):
    id: Optional[str] = None
    """The ID of the actor that performed the action.

    If a user performed the action, this will be their User ID.
    """

    email: Optional[str] = None
    """The email of the user that performed the action."""

    ip: Optional[str] = None
    """The IP address of the request that performed the action."""

    type: Optional[Literal["user", "admin", "Cloudflare"]] = None
    """The type of actor, whether a User, Cloudflare Admin, or an Automated System."""


class UnionMember0ResultOwner(BaseModel):
    id: Optional[str] = None
    """Identifier"""


class UnionMember0ResultResource(BaseModel):
    id: Optional[str] = None
    """An identifier for the resource that was affected by the action."""

    type: Optional[str] = None
    """A short string that describes the resource that was affected by the action."""


class UnionMember0Result(BaseModel):
    id: Optional[str] = None
    """A string that uniquely identifies the audit log."""

    action: Optional[UnionMember0ResultAction] = None

    actor: Optional[UnionMember0ResultActor] = None

    interface: Optional[str] = None
    """The source of the event."""

    metadata: Optional[object] = None
    """An object which can lend more context to the action being logged.

    This is a flexible value and varies between different actions.
    """

    new_value: Optional[str] = FieldInfo(alias="newValue", default=None)
    """The new value of the resource that was modified."""

    old_value: Optional[str] = FieldInfo(alias="oldValue", default=None)
    """The value of the resource before it was modified."""

    owner: Optional[UnionMember0ResultOwner] = None

    resource: Optional[UnionMember0ResultResource] = None

    when: Optional[datetime] = None
    """A UTC RFC3339 timestamp that specifies when the action being logged occured."""


class UnionMember0(BaseModel):
    errors: Optional[object] = None

    messages: Optional[List[object]] = None

    result: Optional[List[UnionMember0Result]] = None

    success: Optional[bool] = None


class Yq4V3hcHapiResponseCommonError(BaseModel):
    code: int

    message: str


class Yq4V3hcHapiResponseCommonMessage(BaseModel):
    code: int

    message: str


class Yq4V3hcHAPIResponseCommon(BaseModel):
    errors: List[Yq4V3hcHapiResponseCommonError]

    messages: List[Yq4V3hcHapiResponseCommonMessage]

    result: Union[object, List[object], str]

    success: Literal[True]
    """Whether the API call was successful"""


AuditLogListResponse = Union[UnionMember0, Yq4V3hcHAPIResponseCommon]