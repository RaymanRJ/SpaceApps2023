variable "stack_name" {
  description = "Name of the stack"
}

variable "cloudfront_distribution_arn" {
  description = "The ARN of the CloudFront distribution"
  type        = string
}