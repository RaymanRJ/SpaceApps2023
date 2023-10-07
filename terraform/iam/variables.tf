variable "stack_name" {
    description = "Stack Name"
    type = string
}

variable "s3_arn" {
    description = "The ARN of the S3 bucket"
    type = string
}

variable "s3_asset_arn" {
    description = "The ARN of the S3 bucket for assets"
    type = string
}

variable "cloudfront_arn" {
    description = "The ARN of the CloudFront distribution"
    type = string
}

variable "cicd_actions_group_name" {
    description = "The name of the IAM group for CICD actions"
    type = string
}