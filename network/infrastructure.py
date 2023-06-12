#!/usr/bin/env

import aws_cdk as cdk
from aws_cdk import Stack
# Import needed modules
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


# Start the class
class NetworkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        # TODO: Add the VPC name to the context
        vpc_id = self.node.try_get_context("vpc_id")
        vpc = ec2.Vpc(self,
                      vpc_id,
                      cidr="10.0.0.0/16",
                      max_azs=2,
                      vpc_name=vpc_id,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                              # TODO: Add the public subnet name to the context
                              name="public-sg", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC,
                              map_public_ip_on_launch=False),
                          ec2.SubnetConfiguration(
                              # TODO: Add the private subnet name to the context
                              name="private-sg", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT),
                          ec2.SubnetConfiguration(
                              # TODO: Add the isolated subnet name to the context
                              name="isolated-sg", cidr_mask=28, subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)
                      ]
                      )
        # Create a flow log
        # TODO: Add the flow log name to the context
        vpc.add_flow_log("flow_log_debug")
        self.vpc = vpc

        # Define a function to tag subnets
        def tag_subnets(subnets: ec2.ISubnet, tag_key: str, tag_value: str):
            for subnet in subnets:
                cdk.Tags.of(subnet).add(tag_key, tag_value)

        # Tag the subnets
        tag_subnets(vpc.public_subnets, "Name", "public-sg")
        tag_subnets(vpc.private_subnets, "Name", "private-sg")
        tag_subnets(vpc.isolated_subnets, "Name", "isolated-sg")
