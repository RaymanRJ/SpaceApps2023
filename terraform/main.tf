provider "aws" {
    region = var.aws_region

    default_tags {
        tags = var.default_tags
    }
}

terraform {
  backend "s3" {
    key     = "space-apps-2023/terraform.tfstate"
  }
}

data "terraform_remote_state" "base_project" {
  backend = "s3"
  config = {
    bucket = var.base_project_state.bucket
    key    = "${var.base_project_state.key}/terraform.tfstate"
    region = var.base_project_state.region
  }
}

locals{
    base_domain_name = data.terraform_remote_state.base_project.outputs.domain_name
    domain_name = "${var.stack_name}.${local.base_domain_name}"
    origin_id = "S3Origin"
    logging_bucket = "${var.stack_name}-logging-bucket"
}

module "s3" {
  source = "./s3"
  stack_name = var.stack_name
  cloudfront_distribution_arn = module.cloudfront.cloudfront_distribution_arn
}

module "cloudfront" {
  source = "./cloudfront"
  domain_name = local.domain_name
  stack_name = var.stack_name
  s3_bucket_regional_domain_name = module.s3.bucket_regional_domain_name
  acm_certificate_arn = module.acm.spaceapps2023_certificate_arn
  origin_id = local.origin_id
}

module "acm" {
  source = "./acm"
  domain_name = local.domain_name
}

module "ecr" {
  source = "./ecr"
  stack_name = var.stack_name
}

module "route53" {
  source = "./route53"
  base_domain_name = local.base_domain_name
  domain_name = local.domain_name
  validation_options = module.acm.validation_options
  cloudfront_distribution_domain_name = module.cloudfront.cloudfront_distribution_domain_name
}

module "iam" {
  source = "./iam"
  stack_name = var.stack_name
  s3_arn = module.s3.s3_arn
  s3_asset_arn = module.s3.s3_asset_arn
  cloudfront_arn = module.cloudfront.cloudfront_distribution_arn
  cicd_actions_group_name = var.cicd_actions_group_name
}