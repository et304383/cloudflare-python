# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .zone_setting_image_resizing_param import ZoneSettingImageResizingParam

__all__ = ["ImageResizingEditParams"]


class ImageResizingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[ZoneSettingImageResizingParam]
    """
    Image Resizing provides on-demand resizing, conversion and optimisation for
    images served through Cloudflare's network. Refer to the
    [Image Resizing documentation](https://developers.cloudflare.com/images/) for
    more information.
    """
