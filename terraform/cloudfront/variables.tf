variable "domain_name" {
  description = "Domain Name"
}

variable "stack_name" {
  description = "Stack Name"
}

variable "s3_bucket_regional_domain_name" {
  description = "The regional domain name of the S3 bucket"
  type        = string
}


variable "acm_certificate_arn" {
  description = "The arn of the ACM certificate"
  type = string
}

variable "origin_id" {
  description = "The origin Id of ..."
  type = string
}