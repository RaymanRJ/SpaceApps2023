variable "aws_region" {
  description = "AWS region to deploy the resources"
  default     = "us-east-1"
}

variable "base_project_state" {
  description = "Name of the S3 bucket where the base project state is stored"
  type = object({
    bucket = string
    key    = string
    region = string
  })
}

variable "stack_name" {
  description = "Name of the stack"
}

variable "default_tags" {
  description = "Default tags for AWS resources"
  type        = map(string)
}

variable "cicd_actions_group_name" {
  description = "GitHub Actions Group Name for CICD"
  type = string
}