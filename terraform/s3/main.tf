resource "aws_s3_bucket" "spaceapps2023_bucket_assets" {
  bucket = "${var.stack_name}-assets"
  force_destroy = true
}

resource "aws_s3_bucket" "spaceapps2023_bucket_frontend" {
  bucket = "${var.stack_name}-frontend"
  force_destroy = true
}

data "aws_iam_policy_document" "allow_access_from_cloudfront" {
  statement {
    principals {
      type = "Service"
      identifiers = ["cloudfront.amazonaws.com"]
    }

    actions = [
      "s3:GetObject"
    ]

    condition {
      test = "StringEquals"
      variable = "AWS:SourceArn"
      values = [
        var.cloudfront_distribution_arn
      ]
    }

    resources = [
      aws_s3_bucket.spaceapps2023_bucket_frontend.arn,
      "${aws_s3_bucket.spaceapps2023_bucket_frontend.arn}/*",
    ]
  }
}

resource "aws_s3_bucket_policy" "allow_access_from_another_account" {
  bucket = aws_s3_bucket.spaceapps2023_bucket_frontend.id
  policy = data.aws_iam_policy_document.allow_access_from_cloudfront.json
}