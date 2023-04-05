terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.61.0"
    }
  }
}

provider "aws" {
    region = "{{REGION}}"
}

resource "aws_s3_bucket_lifecycle_configuration" "backups_lifecycle" {
  rule {
    id      = "expire-backups-after-30-day"
    status  = "Enabled"

    filter {
      prefix = "{{BACKUP-PATH}}"
    }

    expiration {
      days = 30
    }
  }

  bucket = "{{BUCKET-NAME}}"
}
