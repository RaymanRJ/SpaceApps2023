output "spaceapps2023_certificate_arn" {
  value = aws_acm_certificate.spaceapps2023_certificate.arn
}

output "validation_options" {
  value = tolist(aws_acm_certificate.spaceapps2023_certificate.domain_validation_options)
}