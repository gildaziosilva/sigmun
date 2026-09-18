# SIGMUN Infrastructure - Terraform Backend Configuration

terraform {
  backend "s3" {
    bucket         = "sigmun-terraform-state"
    key            = "sigmun/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "sigmun-terraform-locks"
  }
}
