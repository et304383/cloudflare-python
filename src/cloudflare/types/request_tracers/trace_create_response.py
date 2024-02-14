# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["TraceCreateResponse", "Trace", "TraceTrace"]


class TraceTrace(BaseModel):
    action: Optional[str] = None
    """If step type is rule, then action performed by this rule"""

    action_parameters: Optional[object] = None
    """If step type is rule, then action parameters of this rule as JSON"""

    description: Optional[str] = None
    """If step type is rule or ruleset, the description of this entity"""

    expression: Optional[str] = None
    """If step type is rule, then expression used to match for this rule"""

    kind: Optional[str] = None
    """If step type is ruleset, then kind of this ruleset"""

    matched: Optional[bool] = None
    """Whether tracing step affected tracing request/response"""

    name: Optional[str] = None
    """If step type is ruleset, then name of this ruleset"""

    step_name: Optional[str] = None
    """Tracing step identifying name"""

    trace: Optional[object] = None

    type: Optional[str] = None
    """Tracing step type"""


class Trace(BaseModel):
    action: Optional[str] = None
    """If step type is rule, then action performed by this rule"""

    action_parameters: Optional[object] = None
    """If step type is rule, then action parameters of this rule as JSON"""

    description: Optional[str] = None
    """If step type is rule or ruleset, the description of this entity"""

    expression: Optional[str] = None
    """If step type is rule, then expression used to match for this rule"""

    kind: Optional[str] = None
    """If step type is ruleset, then kind of this ruleset"""

    matched: Optional[bool] = None
    """Whether tracing step affected tracing request/response"""

    name: Optional[str] = None
    """If step type is ruleset, then name of this ruleset"""

    step_name: Optional[str] = None
    """Tracing step identifying name"""

    trace: Optional[List[TraceTrace]] = None

    type: Optional[str] = None
    """Tracing step type"""


class TraceCreateResponse(BaseModel):
    status_code: Optional[int] = None
    """HTTP Status code of zone response"""

    trace: Optional[List[Trace]] = None