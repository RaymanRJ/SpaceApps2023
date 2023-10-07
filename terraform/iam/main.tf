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
        var.cloudfront_arn
      ]
    }

    resources = [
      var.s3_arn,
      "${var.s3_arn}/*",
    ]
  }
}

resource "aws_iam_policy" "github_actions_policy" {
  name        = "${var.stack_name}-github-actions-policy"
  description = "GitHub Actions Policy for ${var.stack_name}"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid      = "VisualEditor0"
        Effect   = "Allow"
        Action   = ["s3:PutObject", "s3:ListBucket", "s3:GetObject", "cloudfront:CreateInvalidation"]
        Resource = [
          "${var.cloudfront_arn}",
          "${var.s3_arn}",
          "${var.s3_arn}/*",
          "${var.s3_asset_arn}",
          "${var.s3_asset_arn}/*"
        ]
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "ci_cd_policy_attachment" {
  name       = "Attach ${var.stack_name} GitHub Actions Policy to existing group"
  policy_arn = aws_iam_policy.github_actions_policy.arn
  groups     = [var.cicd_actions_group_name]
}