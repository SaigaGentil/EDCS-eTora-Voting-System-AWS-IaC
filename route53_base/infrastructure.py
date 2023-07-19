#!/usr/bin/python3

# Import needed modules
import aws_cdk as cdk
from aws_cdk import (
    aws_route53 as route53,
    aws_certificatemanager as certificate_manager,
    aws_route53_targets as targets,
    Stack
)
from constructs import Construct


class Route53BaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a hosted zone for the domain "helloskygroup.com"
        hosted_zone = route53.HostedZone(self,
                                         "helloskygroup-com-hosted-zone",
                                         zone_name="helloskygroup.com",
                                         comment="This hosted zone is used for helloskygroup.com domain and "
                                                 "subdomains."
                                         )
        self.hosted_zone = hosted_zone

        # TODO: Change the arn when the certificate is created.
        wildcard_cert_arn = "arn:aws:acm:eu-central-1:560995733478:certificate/f02d9d46-9dad-4d26-a972-f802aafbf4df"
        wildcard_cert = certificate_manager.Certificate.from_certificate_arn(
            self, "wildcard-cert", wildcard_cert_arn)
        self.wildcard_cert = wildcard_cert
