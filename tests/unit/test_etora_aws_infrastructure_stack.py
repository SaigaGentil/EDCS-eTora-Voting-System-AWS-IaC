import aws_cdk as core
import aws_cdk.assertions as assertions

from etora_aws_infrastructure.etora_aws_infrastructure_stack import EtoraAwsInfrastructureStack

# example tests. To run these tests, uncomment this file along with the example
# resource in etora_aws_infrastructure/etora_aws_infrastructure_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EtoraAwsInfrastructureStack(app, "etora-aws-infrastructure")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
