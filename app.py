#!/usr/bin/env python3

import aws_cdk as cdk

from network.infrastructure import NetworkStack
from route53_base.infrastructure import Route53BaseStack
from ec2.infrastructure import Ec2Stack

# Set account and region
# TODO: Define the account ID
env_eu_frankfurt = cdk.Environment(account='192152878086', region='eu-central-1')
env = env_eu_frankfurt

# TODO:Load the stacks

app = cdk.App()

# Define and run the route_53_base stack
route_53_base_stack = Route53BaseStack(app,
                                       "route-53-base-stack",
                                       description="This stack deploys the base DNS infrastructure. It creates a hosted zone and an SSL/TLS wildcard certificate for the domain.",
                                       env=env)

# Define and run the network stack
network_stack = NetworkStack(app,
                             "network-stack",
                             description="This stack deploys the network infrastructure. It creates a VPC, subnets, and a flow log.",
                             env=env)

# Define and run the ec2 stack
ec2_stack = Ec2Stack(app,
                     "ec2-stack",
                     description="This stack deploys the EC2 instances.",
                     env=env,
                     vpc=network_stack.vpc,
                     )

app.synth()
