# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "OutageListResponse",
    "Annotation",
    "AnnotationAsnsDetail",
    "AnnotationAsnsDetailLocations",
    "AnnotationLocationsDetail",
    "AnnotationOutage",
]


class AnnotationAsnsDetailLocations(BaseModel):
    code: str

    name: str


class AnnotationAsnsDetail(BaseModel):
    asn: str

    name: str

    locations: Optional[AnnotationAsnsDetailLocations] = None


class AnnotationLocationsDetail(BaseModel):
    code: str

    name: str


class AnnotationOutage(BaseModel):
    outage_cause: str = FieldInfo(alias="outageCause")

    outage_type: str = FieldInfo(alias="outageType")


class Annotation(BaseModel):
    id: str

    asns: List[int]

    asns_details: List[AnnotationAsnsDetail] = FieldInfo(alias="asnsDetails")

    data_source: str = FieldInfo(alias="dataSource")

    event_type: str = FieldInfo(alias="eventType")

    locations: List[str]

    locations_details: List[AnnotationLocationsDetail] = FieldInfo(alias="locationsDetails")

    outage: AnnotationOutage

    start_date: str = FieldInfo(alias="startDate")

    description: Optional[str] = None

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    scope: Optional[str] = None


class OutageListResponse(BaseModel):
    annotations: List[Annotation]