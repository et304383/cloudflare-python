# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    CertificateDeleteResponse,
    CertificateGetResponse,
    CertificateOriginCaCreateCertificateResponse,
    CertificateOriginCaListCertificatesResponse,
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
from cloudflare.types import certificate_origin_ca_create_certificate_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate = client.certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.certificates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate = client.certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateGetResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.certificates.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_origin_ca_create_certificate(self, client: Cloudflare) -> None:
        certificate = client.certificates.origin_ca_create_certificate()
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_origin_ca_create_certificate_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.certificates.origin_ca_create_certificate(
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICxzCCAa8CAQAwSDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lz\nY28xCzAJBgNVBAcTAkNBMRQwEgYDVQQDEwtleGFtcGxlLm5ldDCCASIwDQYJKoZI\nhvcNAQEBBQADggEPADCCAQoCggEBALxejtu4b+jPdFeFi6OUsye8TYJQBm3WfCvL\nHu5EvijMO/4Z2TImwASbwUF7Ir8OLgH+mGlQZeqyNvGoSOMEaZVXcYfpR1hlVak8\n4GGVr+04IGfOCqaBokaBFIwzclGZbzKmLGwIQioNxGfqFm6RGYGA3be2Je2iseBc\nN8GV1wYmvYE0RR+yWweJCTJ157exyRzu7sVxaEW9F87zBQLyOnwXc64rflXslRqi\ng7F7w5IaQYOl8yvmk/jEPCAha7fkiUfEpj4N12+oPRiMvleJF98chxjD4MH39c5I\nuOslULhrWunfh7GB1jwWNA9y44H0snrf+xvoy2TcHmxvma9Eln8CAwEAAaA6MDgG\nCSqGSIb3DQEJDjErMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5uZXSCD3d3dy5leGFt\ncGxlLm5ldDANBgkqhkiG9w0BAQsFAAOCAQEAcBaX6dOnI8ncARrI9ZSF2AJX+8mx\npTHY2+Y2C0VvrVDGMtbBRH8R9yMbqWtlxeeNGf//LeMkSKSFa4kbpdx226lfui8/\nauRDBTJGx2R1ccUxmLZXx4my0W5iIMxunu+kez+BDlu7bTT2io0uXMRHue4i6quH\nyc5ibxvbJMjR7dqbcanVE10/34oprzXQsJ/VmSuZNXtjbtSKDlmcpw6To/eeAJ+J\nhXykcUihvHyG4A1m2R6qpANBjnA0pHexfwM/SgfzvpbvUg0T1ubmer8BgTwCKIWs\ndcWYTthM51JIqRBfNqy4QcBnX+GY05yltEEswQI55wdiS3CjTTA67sdbcQ==\n-----END CERTIFICATE REQUEST-----",
            hostnames=["example.com", "*.example.com"],
            request_type="origin-rsa",
            requested_validity=5475,
        )
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_origin_ca_create_certificate(self, client: Cloudflare) -> None:
        response = client.certificates.with_raw_response.origin_ca_create_certificate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_origin_ca_create_certificate(self, client: Cloudflare) -> None:
        with client.certificates.with_streaming_response.origin_ca_create_certificate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_origin_ca_list_certificates(self, client: Cloudflare) -> None:
        certificate = client.certificates.origin_ca_list_certificates()
        assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_origin_ca_list_certificates(self, client: Cloudflare) -> None:
        response = client.certificates.with_raw_response.origin_ca_list_certificates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_origin_ca_list_certificates(self, client: Cloudflare) -> None:
        with client.certificates.with_streaming_response.origin_ca_list_certificates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.certificates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateGetResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.certificates.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_origin_ca_create_certificate(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.certificates.origin_ca_create_certificate()
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_origin_ca_create_certificate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.certificates.origin_ca_create_certificate(
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICxzCCAa8CAQAwSDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lz\nY28xCzAJBgNVBAcTAkNBMRQwEgYDVQQDEwtleGFtcGxlLm5ldDCCASIwDQYJKoZI\nhvcNAQEBBQADggEPADCCAQoCggEBALxejtu4b+jPdFeFi6OUsye8TYJQBm3WfCvL\nHu5EvijMO/4Z2TImwASbwUF7Ir8OLgH+mGlQZeqyNvGoSOMEaZVXcYfpR1hlVak8\n4GGVr+04IGfOCqaBokaBFIwzclGZbzKmLGwIQioNxGfqFm6RGYGA3be2Je2iseBc\nN8GV1wYmvYE0RR+yWweJCTJ157exyRzu7sVxaEW9F87zBQLyOnwXc64rflXslRqi\ng7F7w5IaQYOl8yvmk/jEPCAha7fkiUfEpj4N12+oPRiMvleJF98chxjD4MH39c5I\nuOslULhrWunfh7GB1jwWNA9y44H0snrf+xvoy2TcHmxvma9Eln8CAwEAAaA6MDgG\nCSqGSIb3DQEJDjErMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5uZXSCD3d3dy5leGFt\ncGxlLm5ldDANBgkqhkiG9w0BAQsFAAOCAQEAcBaX6dOnI8ncARrI9ZSF2AJX+8mx\npTHY2+Y2C0VvrVDGMtbBRH8R9yMbqWtlxeeNGf//LeMkSKSFa4kbpdx226lfui8/\nauRDBTJGx2R1ccUxmLZXx4my0W5iIMxunu+kez+BDlu7bTT2io0uXMRHue4i6quH\nyc5ibxvbJMjR7dqbcanVE10/34oprzXQsJ/VmSuZNXtjbtSKDlmcpw6To/eeAJ+J\nhXykcUihvHyG4A1m2R6qpANBjnA0pHexfwM/SgfzvpbvUg0T1ubmer8BgTwCKIWs\ndcWYTthM51JIqRBfNqy4QcBnX+GY05yltEEswQI55wdiS3CjTTA67sdbcQ==\n-----END CERTIFICATE REQUEST-----",
            hostnames=["example.com", "*.example.com"],
            request_type="origin-rsa",
            requested_validity=5475,
        )
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_origin_ca_create_certificate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificates.with_raw_response.origin_ca_create_certificate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_origin_ca_create_certificate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificates.with_streaming_response.origin_ca_create_certificate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateOriginCaCreateCertificateResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_origin_ca_list_certificates(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.certificates.origin_ca_list_certificates()
        assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_origin_ca_list_certificates(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.certificates.with_raw_response.origin_ca_list_certificates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_origin_ca_list_certificates(self, async_client: AsyncCloudflare) -> None:
        async with async_client.certificates.with_streaming_response.origin_ca_list_certificates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateOriginCaListCertificatesResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True