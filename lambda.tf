# Define the AWS provider and region
provider "aws" {
  region = "ap-southeast-1"
}

# Create an AWS Lambda function
resource "aws_lambda_function" "my_lambda_function" {
    filename = "deploy.zip"
    function_name = "generate_viz_devs"
    role = "${aws_iam_role.viz_devs.arn}"
    handler = "main.lambda_handler"
    runtime = "python3.10"
    source_code_hash = filebase64sha256("deploy.zip")
    layers = ["${aws_lambda_layer_version.viz_devs.arn}"]
}

# Create an IAM role for the Lambda function_name
resource "aws_iam_role" "viz_devs" {
    name = "viz_devs"
     assume_role_policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
            {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Effect": "Allow",
            "Sid": ""
            }
        ]
    })
}

# Attach the necessary IAM policy to the Lambda function's role
resource "aws_iam_role_policy_attachment" "viz_devs" {
    role = "${aws_iam_role.viz_devs.name}"
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Create a layer for the Lambda function
resource "aws_lambda_layer_version" "viz_devs" {
    filename = "python.zip"
    layer_name = "viz_package"
    compatible_runtimes = ["python3.10"]
    source_code_hash = filebase64sha256("python.zip")
}

# Create the API Gateway REST API
resource "aws_api_gateway_rest_api" "viz_devs_api" {
  name = "viz_devs"
}

# Create a resource for the API Gateway REST API
resource "aws_api_gateway_resource" "viz_devs_gateway" {
  rest_api_id = "${aws_api_gateway_rest_api.viz_devs_api.id}"
  parent_id   = "${aws_api_gateway_rest_api.viz_devs_api.root_resource_id}"
  path_part   = "viz_devs"
}

# Create a method for the API Gateway REST API resource
resource "aws_api_gateway_method" "generate_dot" {
    rest_api_id = "${aws_api_gateway_rest_api.viz_devs_api.id}"
    resource_id = "${aws_api_gateway_resource.viz_devs_gateway.id}"
    http_method = "GET"
    authorization = "NONE"
}

# Create an integration between API Gateway and Lambda
resource "aws_api_gateway_integration" "lambda_gateway_integration" {
    rest_api_id = "${aws_api_gateway_rest_api.viz_devs_api.id}"
    resource_id = "${aws_api_gateway_resource.viz_devs_gateway.id}"
    http_method = "${aws_api_gateway_method.generate_dot.http_method}"
    integration_http_method = "POST"
    type = "AWS_PROXY"
    uri = "${aws_lambda_function.my_lambda_function.invoke_arn}"
}
