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

variable "aws_lb_spacesapps2023_lambda_alb_dns_name" {
  type = string
}

variable "aws_lb_spacesapps2023_lambda_alb_zone_id" {
  type = string
}