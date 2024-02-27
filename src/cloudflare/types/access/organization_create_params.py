# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationCreateParams", "LoginDesign"]


class OrganizationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: Required[str]
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    auth_domain: Required[str]
    """The unique subdomain assigned to your Zero Trust organization."""

    name: Required[str]
    """The name of your Zero Trust organization."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate via WARP for any application in your
    organization. Application settings will take precedence over this value.
    """

    auto_redirect_to_identity: bool
    """
    When set to `true`, users skip the identity provider selection step during
    login.
    """

    is_ui_read_only: bool
    """Lock all settings as Read-Only in the Dashboard, regardless of user permission.

    Updates may only be made via the API or Terraform for this account when enabled.
    """

    login_design: LoginDesign

    session_duration: str
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    ui_read_only_toggle_reason: str
    """A description of the reason why the UI read only field is being toggled."""

    user_seat_expiration_inactive_time: str
    """The amount of time a user seat is inactive before it expires.

    When the user seat exceeds the set time of inactivity, the user is removed as an
    active seat and no longer counts against your Teams seat count. Must be in the
    format `300ms` or `2h45m`. Valid time units are: `ns`, `us` (or `µs`), `ms`,
    `s`, `m`, `h`.
    """

    warp_auth_session_duration: str
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `30m` or `2h45m`. Valid time units are: m, h.
    """


class LoginDesign(TypedDict, total=False):
    background_color: str
    """The background color on your login page."""

    footer_text: str
    """The text at the bottom of your login page."""

    header_text: str
    """The text at the top of your login page."""

    logo_path: str
    """The URL of the logo on your login page."""

    text_color: str
    """The text color on your login page."""