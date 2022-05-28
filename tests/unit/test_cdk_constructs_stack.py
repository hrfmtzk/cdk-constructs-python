import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_constructs.cdk_constructs_stack import CdkConstructsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_constructs/cdk_constructs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkConstructsStack(app, "cdk-constructs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
