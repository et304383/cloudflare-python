# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ItemGetResponse", "ListsItemRedirect", "ListsItemHostname"]


class ListsItemRedirect(BaseModel):
    source_url: str

    target_url: str

    include_subdomains: Optional[bool] = None

    preserve_path_suffix: Optional[bool] = None

    preserve_query_string: Optional[bool] = None

    status_code: Optional[Literal[301, 302, 307, 308]] = None

    subpath_matching: Optional[bool] = None


class ListsItemHostname(BaseModel):
    url_hostname: str


ItemGetResponse = Union[str, ListsItemRedirect, ListsItemHostname, int, None]