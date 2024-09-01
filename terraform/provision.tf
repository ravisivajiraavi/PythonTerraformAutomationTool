terraform {

  backend "s3" {
    bucket = "ravi-terraform-state"
    key    = "global/s3/terraform.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.15.0"
    }
    random = {
      source = "hashicorp/random"
    }
  }

  required_version = "~> 1.9.2"
}