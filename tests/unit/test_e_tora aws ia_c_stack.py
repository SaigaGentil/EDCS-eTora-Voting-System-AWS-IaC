import aws_cdk as core
import aws_cdk.assertions as assertions

from e_tora aws ia_c.e_tora aws ia_c_stack import EToraAwsIaCStack

# example tests. To run these tests, uncomment this file along with the example
# resource in e_tora aws ia_c/e_tora aws ia_c_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EToraAwsIaCStack(app, "e-tora-aws-ia-c")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
