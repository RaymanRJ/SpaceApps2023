resource "aws_ecr_repository" "spaceapps2023repo" {
  name                 = "${var.stack_name}repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
