# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    DNSRecordCreateResponse,
    DNSRecordUpdateResponse,
    DNSRecordListResponse,
    DNSRecordDeleteResponse,
    DNSRecordExportResponse,
    DNSRecordGetResponse,
    DNSRecordImportResponse,
    DNSRecordScanResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import dns_record_create_params
from cloudflare.types import dns_record_update_params
from cloudflare.types import dns_record_list_params
from cloudflare.types import dns_record_import_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDNSRecords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "string",
            },
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 8,
                "certificate": "string",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content={},
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "string",
            },
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 3,
                "digest": "string",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            type="DS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_9(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_9(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_10(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_10(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_11(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_11(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": "string",
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "string",
            },
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_11(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_11(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_12(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_12(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_12(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_12(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_13(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_13(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_13(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_13(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="example.com",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_14(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_14(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_14(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_14(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_15(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_15(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "name": "example.com",
                "port": 8806,
                "priority": 10,
                "proto": "_tcp",
                "service": "_sip",
                "target": "example.com",
                "weight": 5,
            },
            name="_sip._tcp.example.com",
            type="SRV",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_15(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_15(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_16(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_16(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 2,
                "fingerprint": "string",
                "type": 1,
            },
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_16(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_16(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_17(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_17(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_17(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_17(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_18(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_18(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_18(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_18(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_19(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_19(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_19(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_19(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                content="example text content",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_create_overload_20(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params_overload_20(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "content": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            type="URI",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_overload_20(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_overload_20(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "string",
            },
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 8,
                "certificate": "string",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_5(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_5(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content={},
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content={},
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_6(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "string",
            },
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_6(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_7(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 3,
                "digest": "string",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            type="DS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_7(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_8(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_8(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_9(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_9(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_9(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_10(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_10(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_10(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_11(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": "string",
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "string",
            },
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_11(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_11(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_12(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_12(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_12(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_12(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_13(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_13(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_13(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_13(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_13(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="example.com",
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="example.com",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_14(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_14(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_14(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_14(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_14(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_15(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_15(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "name": "example.com",
                "port": 8806,
                "priority": 10,
                "proto": "_tcp",
                "service": "_sip",
                "target": "example.com",
                "weight": 5,
            },
            name="_sip._tcp.example.com",
            type="SRV",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_15(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_15(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_15(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_16(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_16(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 2,
                "fingerprint": "string",
                "type": 1,
            },
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_16(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_16(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_16(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_17(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_17(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_17(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_17(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_17(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_18(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_18(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_18(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_18(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_18(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_19(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_19(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_19(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_19(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_19(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="example text content",
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="example text content",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update_overload_20(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params_overload_20(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "content": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            type="URI",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update_overload_20(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update_overload_20(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update_overload_20(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "present": "string",
                "absent": "string",
                "exact": "Hello, world",
                "contains": "ello, worl",
                "startswith": "Hello, w",
                "endswith": "o, world",
            },
            content="127.0.0.1",
            direction="asc",
            match="any",
            name="example.com",
            order="type",
            page=1,
            per_page=5,
            proxied=False,
            search="www.cloudflare.com",
            tag={
                "present": "important",
                "absent": "important",
                "exact": "greeting:Hello, world",
                "contains": "greeting:ello, worl",
                "startswith": "greeting:Hello, w",
                "endswith": "greeting:o, world",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(str, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(str, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.export(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            client.dns_records.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_import(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_import_with_all_params(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_import(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_import(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_import(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.import_(
                "",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_scan(self, client: Cloudflare) -> None:
        dns_record = client.dns_records.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_scan(self, client: Cloudflare) -> None:
        response = client.dns_records.with_raw_response.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = response.parse()
        assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_scan(self, client: Cloudflare) -> None:
        with client.dns_records.with_streaming_response.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = response.parse()
            assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_scan(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns_records.with_raw_response.scan(
                "",
            )


class TestAsyncDNSRecords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "string",
            },
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 8,
                "certificate": "string",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content={},
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "string",
            },
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 3,
                "digest": "string",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            type="DS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": "string",
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "string",
            },
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="example.com",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "name": "example.com",
                "port": 8806,
                "priority": 10,
                "proto": "_tcp",
                "service": "_sip",
                "target": "example.com",
                "weight": 5,
            },
            name="_sip._tcp.example.com",
            type="SRV",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 2,
                "fingerprint": "string",
                "type": 1,
            },
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                content="example text content",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "content": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            type="URI",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordCreateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.create(
                "",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="198.51.100.4",
            name="example.com",
            type="A",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="198.51.100.4",
                name="example.com",
                type="A",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="2400:cb00:2049::1",
            name="example.com",
            type="AAAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="2400:cb00:2049::1",
                name="example.com",
                type="AAAA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": 1,
                "tag": "issue",
                "value": "string",
            },
            name="example.com",
            type="CAA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CAA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="CAA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="CAA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 8,
                "certificate": "string",
                "key_tag": 1,
                "type": 9,
            },
            name="example.com",
            type="CERT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="CERT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="CERT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="CERT",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
            comment="Domain verification record",
            proxied=False,
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content={},
            name="example.com",
            type="CNAME",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content={},
                name="example.com",
                type="CNAME",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content={},
                name="example.com",
                type="CNAME",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 5,
                "flags": 1,
                "protocol": 3,
                "public_key": "string",
            },
            name="example.com",
            type="DNSKEY",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DNSKEY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="DNSKEY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="DNSKEY",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 3,
                "digest": "string",
                "digest_type": 1,
                "key_tag": 1,
            },
            name="example.com",
            type="DS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="DS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="DS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="DS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="HTTPS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="HTTPS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="HTTPS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="HTTPS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "altitude": 0,
                "lat_degrees": 37,
                "lat_direction": "N",
                "lat_minutes": 46,
                "lat_seconds": 46,
                "long_degrees": 122,
                "long_direction": "W",
                "long_minutes": 23,
                "long_seconds": 35,
                "precision_horz": 0,
                "precision_vert": 0,
                "size": 100,
            },
            name="example.com",
            type="LOC",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="LOC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="LOC",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="LOC",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="mx.example.com",
            name="example.com",
            priority=10,
            type="MX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="mx.example.com",
                name="example.com",
                priority=10,
                type="MX",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "flags": "string",
                "order": 100,
                "preference": 10,
                "regex": "string",
                "replacement": "string",
                "service": "string",
            },
            name="example.com",
            type="NAPTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="NAPTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="NAPTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="NAPTR",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="ns1.example.com",
            name="example.com",
            type="NS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="ns1.example.com",
                name="example.com",
                type="NS",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_13(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example.com",
            name="example.com",
            type="PTR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_13(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="example.com",
                name="example.com",
                type="PTR",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="example.com",
                name="example.com",
                type="PTR",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_14(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 0,
                "selector": 0,
                "usage": 3,
            },
            name="example.com",
            type="SMIMEA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SMIMEA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_14(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SMIMEA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SMIMEA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_15(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "name": "example.com",
                "port": 8806,
                "priority": 10,
                "proto": "_tcp",
                "service": "_sip",
                "target": "example.com",
                "weight": 5,
            },
            name="_sip._tcp.example.com",
            type="SRV",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="_sip._tcp.example.com",
            type="SRV",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_15(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="_sip._tcp.example.com",
                type="SRV",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_16(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "algorithm": 2,
                "fingerprint": "string",
                "type": 1,
            },
            name="example.com",
            type="SSHFP",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SSHFP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_16(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SSHFP",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SSHFP",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_17(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "priority": 1,
                "target": ".",
                "value": 'alpn="h3,h2" ipv4hint="127.0.0.1" ipv6hint="::1"',
            },
            name="example.com",
            type="SVCB",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="SVCB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_17(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="SVCB",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="SVCB",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_18(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "certificate": "string",
                "matching_type": 1,
                "selector": 0,
                "usage": 0,
            },
            name="example.com",
            type="TLSA",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            type="TLSA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_18(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                type="TLSA",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                type="TLSA",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_19(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            content="example text content",
            name="example.com",
            type="TXT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_19(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                content="example text content",
                name="example.com",
                type="TXT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                content="example text content",
                name="example.com",
                type="TXT",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params_overload_20(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={
                "content": "http://example.com/example.html",
                "weight": 20,
            },
            name="example.com",
            priority=10,
            type="URI",
            comment="Domain verification record",
            tags=["owner:dns-team", "owner:dns-team", "owner:dns-team"],
            ttl=3600,
        )
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            data={},
            name="example.com",
            priority=10,
            type="URI",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordUpdateResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update_overload_20(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                data={},
                name="example.com",
                priority=10,
                type="URI",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            comment={
                "present": "string",
                "absent": "string",
                "exact": "Hello, world",
                "contains": "ello, worl",
                "startswith": "Hello, w",
                "endswith": "o, world",
            },
            content="127.0.0.1",
            direction="asc",
            match="any",
            name="example.com",
            order="type",
            page=1,
            per_page=5,
            proxied=False,
            search="www.cloudflare.com",
            tag={
                "present": "important",
                "absent": "important",
                "exact": "greeting:Hello, world",
                "contains": "greeting:ello, worl",
                "startswith": "greeting:Hello, w",
                "endswith": "greeting:o, world",
            },
            tag_match="any",
            type="A",
        )
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(Optional[DNSRecordListResponse], dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(Optional[DNSRecordDeleteResponse], dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(str, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.export(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(str, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.export(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordGetResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dns_record_id` but received ''"):
            await async_client.dns_records.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_import(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
            proxied="true",
        )
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_import(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.import_(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="www.example.com. 300 IN  A 127.0.0.1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordImportResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_import(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.import_(
                "",
                file="www.example.com. 300 IN  A 127.0.0.1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_scan(self, async_client: AsyncCloudflare) -> None:
        dns_record = await async_client.dns_records.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_scan(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns_records.with_raw_response.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dns_record = await response.parse()
        assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_scan(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns_records.with_streaming_response.scan(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dns_record = await response.parse()
            assert_matches_type(DNSRecordScanResponse, dns_record, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_scan(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns_records.with_raw_response.scan(
                "",
            )