variable "base_domain_name" {
  description  = "Base Domain Name"
}

variable "domain_name" {
  description = "Domain Name"
}

variable "validation_options" {
    description = ""
    type = list
}

variable "cloudfront_distribution_domain_name" {
  description = "CloudFront Distrribution Domain"
  type = string
}