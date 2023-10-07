resource "aws_acm_certificate" "spaceapps2023_certificate" {
  domain_name       = var.domain_name
  validation_method = "DNS"
  subject_alternative_names = ["www.${var.domain_name}", "api.${var.domain_name}"]

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_acm_certificate_validation" "spaceapps2023_certificate_validation" {
  certificate_arn         = aws_acm_certificate.spaceapps2023_certificate.arn
  validation_record_fqdns = [for record in aws_acm_certificate.spaceapps2023_certificate.domain_validation_options : record.resource_record_name]
}