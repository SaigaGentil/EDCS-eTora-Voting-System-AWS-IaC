#!/usr/bin/env

# Import needed modules
import aws_cdk as cdk
import yaml
from aws_cdk import Stack
from glob import glob
from aws_cdk import aws_ec2 as ec2
from constructs import Construct


# Start the class
class NetworkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        # TODO: Add the VPC name to the context
        vpc_id = "main-vpc"
        # vpc_id = self.node.try_get_context("vpc_id")
        vpc = ec2.Vpc(self,
                      vpc_id,
                      cidr="10.0.0.0/16",
                      max_azs=2,
                      vpc_name=vpc_id,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                              # TODO: Add the public subnet name to the context
                              name="public-sg",
                              cidr_mask=24,
                              subnet_type=ec2.SubnetType.PUBLIC,
                              map_public_ip_on_launch=False
                          ),
                          ec2.SubnetConfiguration(
                              # TODO: Add the private subnet name to the context
                              name="private-sg",
                              cidr_mask=24,
                              subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                          ),
                          ec2.SubnetConfiguration(
                              # TODO: Add the isolated subnet name to the context
                              name="isolated-sg",
                              cidr_mask=28,
                              subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                          )
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

        # Public Network ACL to associate with the public subnets
        public_network_acl = ec2.NetworkAcl(self,
                                            "public-network-acl",
                                            vpc=vpc,
                                            network_acl_name="public-network-acl",
                                            subnet_selection=ec2.SubnetSelection(
                                                subnet_type=ec2.SubnetType.PUBLIC
                                            )
                                            )

        # Private Network ACL to associate with the private subnets
        private_network_acl = ec2.NetworkAcl(self,
                                             "private-network-acl",
                                             vpc=vpc,
                                             network_acl_name="private-network-acl",
                                             subnet_selection=ec2.SubnetSelection(
                                                 subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
                                             )
                                             )

        # Isolated Network ACL to associate with the isolated subnets
        isolated_network_acl = ec2.NetworkAcl(self,
                                              "isolated-network-acl",
                                              vpc=vpc,
                                              network_acl_name="isolated-network-acl",
                                              subnet_selection=ec2.SubnetSelection(
                                                  subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                                              )
                                              )

        # Function to add 'name' tag to the network ACLs
        def tag_network_acls(network_acl: ec2.NetworkAcl, tag_key: str, tag_value: str):
            cdk.Tags.of(network_acl).add(tag_key, tag_value)

        # Tag the network ACLs
        tag_network_acls(public_network_acl, "Name", "public-network-acl")
        tag_network_acls(private_network_acl, "Name", "private-network-acl")
        tag_network_acls(isolated_network_acl, "Name", "isolated-network-acl")

        # Look for all YAML rule configuration files. The path starts from the root of the project.
        nacl_files = glob(
            'network/config/network_acl_rules/*_active.yaml', recursive=True)
        # Iterate over the found files
        for nacl_file in nacl_files:
            # Open the public_nacl_rules file with mode 'r' for reading.
            with open(nacl_file, mode='r') as nacl_file_rules:
                # Load the file content into a dictionary.
                nacl_rules = yaml.load(nacl_file_rules, Loader=yaml.FullLoader)
                # Iterate over the elements of the dictionary.
                for nacl_rule in nacl_rules:
                    match nacl_rule['subnet']:
                        case 'public':
                            ec2.CfnNetworkAclEntry(self,
                                                   nacl_rule['id'],
                                                   network_acl_id=public_network_acl.network_acl_id,
                                                   protocol=nacl_rule['protocol'],
                                                   rule_action=nacl_rule['rule_action'],
                                                   rule_number=nacl_rule['rule_number'],
                                                   cidr_block=nacl_rule['cidr_block'],
                                                   egress=nacl_rule['egress'],
                                                   port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(
                                                       from_=nacl_rule['port_range']['from'],
                                                       to=nacl_rule['port_range']['to']
                                                   )
                                                   )
                        case 'private':
                            ec2.CfnNetworkAclEntry(self,
                                                   nacl_rule['id'],
                                                   network_acl_id=private_network_acl.network_acl_id,
                                                   protocol=nacl_rule['protocol'],
                                                   rule_action=nacl_rule['rule_action'],
                                                   rule_number=nacl_rule['rule_number'],
                                                   cidr_block=nacl_rule['cidr_block'],
                                                   egress=nacl_rule['egress'],
                                                   port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(
                                                       from_=nacl_rule['port_range']['from'],
                                                       to=nacl_rule['port_range']['to']
                                                   )
                                                   )
                        case 'isolated':
                            ec2.CfnNetworkAclEntry(self,
                                                   nacl_rule['id'],
                                                   network_acl_id=isolated_network_acl.network_acl_id,
                                                   protocol=nacl_rule['protocol'],
                                                   rule_action=nacl_rule['rule_action'],
                                                   rule_number=nacl_rule['rule_number'],
                                                   cidr_block=nacl_rule['cidr_block'],
                                                   egress=nacl_rule['egress'],
                                                   port_range=ec2.CfnNetworkAclEntry.PortRangeProperty(
                                                       from_=nacl_rule['port_range']['from'],
                                                       to=nacl_rule['port_range']['to']
                                                   )
                                                   )

