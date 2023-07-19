#!/usr/bin/env

import aws_cdk as cdk
from aws_cdk import Stack
# Import needed modules
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_autoscaling as autoscaling
from constructs import Construct


class Ec2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # EC2 instance types
        # https://aws.amazon.com/ec2/instance-types/
        instance_type_rhel = ec2.InstanceType("t2.micro")
        instance_type_ubuntu = ec2.InstanceType("t2.micro")

        # Security Group for EC2 instances
        # TODO: Review how this is set up
        security_group = ec2.SecurityGroup(self, "ec2-sg", vpc=vpc, allow_all_outbound=True)
        # TODO: Review how this rule and make it more secure. Use bastion host
        security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH from anywhere")

        # TODO: Attach public IP address to the instances.
        # TODO: Put proper names to the instances.
        # TODO: Create ssh key pairs for the instances.
        # TODO: Define volumes for the instances and sizes. and names.
        # TODO: Add names to security groups.
        # Auto Scaling Group for Ubuntu instances
        ubuntu_auto_scaling_group = autoscaling.AutoScalingGroup(self,
                                                                 "ubuntu-asg",
                                                                 vpc=vpc,
                                                                 instance_type=instance_type_ubuntu,
                                                                 # TODO: Create a proper AMI.
                                                                 machine_image=ec2.AmazonLinuxImage(),
                                                                 desired_capacity=1,
                                                                 min_capacity=1,
                                                                 max_capacity=3,
                                                                 # Todo: Add subnets properly
                                                                 vpc_subnets=ec2.SubnetSelection(
                                                                     subnet_type=ec2.SubnetType.PUBLIC),
                                                                 security_group=security_group
                                                                 )

        # Auto Scaling Group for RHEL instances
        # TODO: Review this setup
        rhel_auto_scaling_group = autoscaling.AutoScalingGroup(self,
                                                               "rhel-asg",
                                                               vpc=vpc,
                                                               instance_type=instance_type_rhel,
                                                               # TODO: Create RHEL AMI
                                                               machine_image=ec2.AmazonLinuxImage(),
                                                               desired_capacity=2,
                                                               min_capacity=2,
                                                               max_capacity=4,
                                                               vpc_subnets=ec2.SubnetSelection(
                                                                   subnet_type=ec2.SubnetType.PUBLIC),
                                                               security_group=security_group
                                                               )
