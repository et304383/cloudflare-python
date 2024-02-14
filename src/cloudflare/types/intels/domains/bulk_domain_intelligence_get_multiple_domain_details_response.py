# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponse",
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponseItem",
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemAdditionalInformation",
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemApplication",
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedContentCategory",
    "BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedRiskType",
]


class BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemAdditionalInformation(BaseModel):
    suspected_malware_family: Optional[str] = None
    """Suspected DGA malware family."""


class BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemApplication(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedContentCategory(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedRiskType(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    super_category_id: Optional[int] = None


class BulkDomainIntelligenceGetMultipleDomainDetailsResponseItem(BaseModel):
    additional_information: Optional[
        BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemAdditionalInformation
    ] = None
    """Additional information related to the host name."""

    application: Optional[BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemApplication] = None
    """Application that the hostname belongs to."""

    content_categories: Optional[object] = None
    """Current content categories."""

    domain: Optional[str] = None

    inherited_content_categories: Optional[
        List[BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedContentCategory]
    ] = None

    inherited_from: Optional[str] = None
    """
    Domain from which `inherited_content_categories` and `inherited_risk_types` are
    inherited, if applicable.
    """

    inherited_risk_types: Optional[
        List[BulkDomainIntelligenceGetMultipleDomainDetailsResponseItemInheritedRiskType]
    ] = None

    popularity_rank: Optional[int] = None
    """
    Global Cloudflare 100k ranking for the last 30 days, if available for the
    hostname. The top ranked domain is 1, the lowest ranked domain is 100,000.
    """

    risk_score: Optional[float] = None
    """
    Hostname risk score, which is a value between 0 (lowest risk) to 1 (highest
    risk).
    """

    risk_types: Optional[object] = None


BulkDomainIntelligenceGetMultipleDomainDetailsResponse = List[
    BulkDomainIntelligenceGetMultipleDomainDetailsResponseItem
]