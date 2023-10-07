data "aws_route53_zone" "parent_zone" {
  name = "${var.base_domain_name}"
}

resource "aws_route53_zone" "spaceapps2023_zone" {
  name = var.domain_name
}

resource "aws_route53_record" "spaceapps2023_ns" {
  zone_id = data.aws_route53_zone.parent_zone.zone_id
  name    = var.domain_name
  type    = "NS"
  ttl     = "300"

  records = aws_route53_zone.spaceapps2023_zone.name_servers
}

resource "aws_route53_record" "spaceapps2023_record_to_www" {
  zone_id = aws_route53_zone.spaceapps2023_zone.zone_id
  name    = "www.${var.domain_name}"
  type    = "A"
  
  alias {
    name                   = var.cloudfront_distribution_domain_name
    zone_id                = "Z2FDTNDATAQYW2"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "spaceapps2023_record_to_cf" {
  zone_id = aws_route53_zone.spaceapps2023_zone.zone_id
  name    = var.domain_name
  type    = "A"
  
  alias {
    name                   = var.cloudfront_distribution_domain_name
    zone_id                = "Z2FDTNDATAQYW2"
    evaluate_target_health = false
  }
}

resource "aws_route53_record" "api_route" {
  zone_id = aws_route53_zone.spaceapps2023_zone.zone_id
  name    = "api.${var.domain_name}"
  type    = "A"

  alias {
    name                   = "dualstack.${var.aws_lb_spacesapps2023_lambda_alb_dns_name}"
    zone_id                = var.aws_lb_spacesapps2023_lambda_alb_zone_id
    evaluate_target_health = false
  }
}