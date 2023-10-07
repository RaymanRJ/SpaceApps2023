output "iam_policy_document" {
    description = "The IAM policy document"
    value = data.aws_iam_policy_document.allow_access_from_cloudfront.json
}