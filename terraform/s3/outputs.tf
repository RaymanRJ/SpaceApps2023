output "bucket_regional_domain_name" {
  value = aws_s3_bucket.spaceapps2023_bucket_frontend.bucket_regional_domain_name
}

output "s3_arn" {
  value = aws_s3_bucket.spaceapps2023_bucket_assets.arn
}

output "s3_asset_arn"{
  value = aws_s3_bucket.spaceapps2023_bucket_frontend.arn
}