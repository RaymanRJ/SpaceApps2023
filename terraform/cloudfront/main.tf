resource "aws_cloudfront_origin_access_control" "spaceapps2023_oac" {
  name                              = "${var.stack_name}-oac"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "spaceapps2023_distribution" {
  origin {
    domain_name              = var.s3_bucket_regional_domain_name
    origin_access_control_id = aws_cloudfront_origin_access_control.spaceapps2023_oac.id
    origin_id                = var.origin_id
  }

  aliases = ["${var.domain_name}", "www.${var.domain_name}"]
  enabled = true
  default_root_object      = "index.html"
  is_ipv6_enabled = true
  
  custom_error_response {
    error_caching_min_ttl = 10 
    error_code            = 403 
    response_code         = 403
    response_page_path    = "/index.html"
  }

  default_cache_behavior {
    allowed_methods = ["GET", "HEAD", "OPTIONS"]
    cached_methods  = ["GET", "HEAD", "OPTIONS"]
    target_origin_id = var.origin_id 
    viewer_protocol_policy = "redirect-to-https"

    forwarded_values {
      query_string = false
      headers      = ["Origin"]

      cookies {
        forward = "none"
      }
    }
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
      locations        = []
    }
  }

  viewer_certificate {
    acm_certificate_arn = var.acm_certificate_arn
    cloudfront_default_certificate = false
    minimum_protocol_version = "TLSv1.2_2021"
    ssl_support_method = "sni-only"
  }

}