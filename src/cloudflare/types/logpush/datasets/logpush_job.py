# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LogpushJob", "OutputOptions"]


class OutputOptions(BaseModel):
    batch_prefix: Optional[str] = None
    """String to be prepended before each batch."""

    batch_suffix: Optional[str] = None
    """String to be appended after each batch."""

    cve_2021_4428: Optional[bool] = FieldInfo(alias="CVE-2021-4428", default=None)
    """
    If set to true, will cause all occurrences of `${` in the generated files to be
    replaced with `x{`.
    """

    field_delimiter: Optional[str] = None
    """String to join fields. This field be ignored when `record_template` is set."""

    field_names: Optional[List[str]] = None
    """List of field names to be included in the Logpush output.

    For the moment, there is no option to add all fields at once, so you must
    specify all the fields names you are interested in.
    """

    output_type: Optional[Literal["ndjson", "csv"]] = None
    """Specifies the output type, such as `ndjson` or `csv`.

    This sets default values for the rest of the settings, depending on the chosen
    output type. Some formatting rules, like string quoting, are different between
    output types.
    """

    record_delimiter: Optional[str] = None
    """String to be inserted in-between the records as separator."""

    record_prefix: Optional[str] = None
    """String to be prepended before each record."""

    record_suffix: Optional[str] = None
    """String to be appended after each record."""

    record_template: Optional[str] = None
    """
    String to use as template for each record instead of the default comma-separated
    list. All fields used in the template must be present in `field_names` as well,
    otherwise they will end up as null. Format as a Go `text/template` without any
    standard functions, like conditionals, loops, sub-templates, etc.
    """

    sample_rate: Optional[float] = None
    """Floating number to specify sampling rate.

    Sampling is applied on top of filtering, and regardless of the current
    `sample_interval` of the data.
    """

    timestamp_format: Optional[Literal["unixnano", "unix", "rfc3339"]] = None
    """
    String to specify the format for timestamps, such as `unixnano`, `unix`, or
    `rfc3339`.
    """


class LogpushJob(BaseModel):
    id: Optional[int] = None
    """Unique id of the job."""

    dataset: Optional[str] = None
    """Name of the dataset."""

    destination_conf: Optional[str] = None
    """Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.

    Additional configuration parameters supported by the destination may be
    included.
    """

    enabled: Optional[bool] = None
    """Flag that indicates if the job is enabled."""

    error_message: Optional[datetime] = None
    """If not null, the job is currently failing.

    Failures are usually repetitive (example: no permissions to write to destination
    bucket). Only the last failure is recorded. On successful execution of a job the
    error_message and last_error are set to null.
    """

    frequency: Optional[Literal["high", "low"]] = None
    """The frequency at which Cloudflare sends batches of logs to your destination.

    Setting frequency to high sends your logs in larger quantities of smaller files.
    Setting frequency to low sends logs in smaller quantities of larger files.
    """

    last_complete: Optional[datetime] = None
    """Records the last time for which logs have been successfully pushed.

    If the last successful push was for logs range 2018-07-23T10:00:00Z to
    2018-07-23T10:01:00Z then the value of this field will be 2018-07-23T10:01:00Z.
    If the job has never run or has just been enabled and hasn't run yet then the
    field will be empty.
    """

    last_error: Optional[datetime] = None
    """Records the last time the job failed.

    If not null, the job is currently failing. If null, the job has either never
    failed or has run successfully at least once since last failure. See also the
    error_message field.
    """

    logpull_options: Optional[str] = None
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """

    name: Optional[str] = None
    """Optional human readable job name.

    Not unique. Cloudflare suggests that you set this to a meaningful string, like
    the domain name, to make it easier to identify your job.
    """

    output_options: Optional[OutputOptions] = None
    """The structured replacement for `logpull_options`.

    When including this field, the `logpull_option` field will be ignored.
    """
